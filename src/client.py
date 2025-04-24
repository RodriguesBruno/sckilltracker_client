import asyncio
import logging
import subprocess
import uuid
from pathlib import Path
from random import randint
from typing import Callable, Optional
import httpx

from src.client_utls import generate_client_id
from src.logfile_monitor import LogFileMonitor
from src.models.models import (
    PlayerEvent,
    GameNotification,
    LogFileNotification,
    GameExecutableNotification, RecordingNotification
)
from src.msg_parser import (
    get_game_mode,
    get_log_date,
    get_victim_player_name,
    get_victim_zone,
    get_killed_by,
    get_using,
    get_damage,
    get_pilot_name,
    get_ship_name
)
from src.recordings_controller import RecordingsController
from src.statistics_controller import StatisticsController
from src.trigger_controller import TriggerController
from src.repository import Repository
from src.utils import get_date


SHIP_PREFIXES: list[str] = [
    "ORIG",
    "CRUS",
    "RSI",
    "AEGS",
    "VNCL",
    "DRAK",
    "ANVL",
    "BANU",
    "MISC",
    "CNOU",
    "XIAN",
    "GAMA",
    "TMBL",
    "ESPR",
    "KRIG",
    "GRIN",
    "XNAA",
	"MRAI"
]


def find_event_line(lines: list[str], keywords: list[str]) -> str | None:
    return next((line for line in lines if any(k in line for k in keywords)), None)

MAX_ENTRIES: int = 22

class SCClient:
    def __init__(
            self,
            config: dict,
            logfile_monitor: LogFileMonitor,
            repo: Repository,
            statistics_controller: StatisticsController,
            trigger_controller: TriggerController,
            recordings_controller: RecordingsController
    ) -> None:

        self._version: str = config.get('version')
        self._enabled: bool = config.get('enabled')
        self._api_url: str = config.get('api_url')
        self._verbose_logging: bool = config.get('verbose_logging')

        self._game_executable_name: str = config.get('game_executable_name')
        self._game_executable_check_frequency: int = config.get('game_executable_check_frequency')

        self._logfile_monitor: LogFileMonitor = logfile_monitor
        self._repo: Repository = repo
        self._statistics_controller: StatisticsController = statistics_controller
        self._trigger_controller: TriggerController = trigger_controller
        self._recordings_controller: RecordingsController = recordings_controller

        self._startup_date: str = get_date()
        self._client_id: str = generate_client_id()

        self._game_mode: str = '-'
        self._ship_name: str = '-'
        self._pilot_name: str = '-'

        self._pilot_name_keyword: str = '<OnClientConnected> Player'
        self._ship_name_keywords: list[str] = ['[VEHICLE SPAWN] CPlayerShipRespawnManager:', '<Jump Drive Requesting State Change>']
        self._game_mode_keywords: list[str] = ['> Loading screen for ', '> Mode[EA']

        self._player_event_keyword: str = "<Actor Death>"

        self._current_date: str = ''

        self._game_is_running: bool = False
        self._game_is_running_last_checked: str = ''


    async def _initialize_statistics_controller(self):
        self._statistics_controller.set_data(events=self._repo.read())

    async def _check_if_game_is_running(self, broadcast: Callable) -> None:

        while True:
            result = subprocess.run(
                ['tasklist', '/FI', f"IMAGENAME eq {self._game_executable_name}"],
                     capture_output=True,
                     text=True
            )

            date: str = get_date()

            game_is_running: bool = True if self._game_executable_name in result.stdout.lower() else False

            msg: str = f"{self._game_executable_name} is{'' if game_is_running else ' not'} running, checked: {date}"

            if game_is_running != self._game_is_running:
                self._game_is_running = game_is_running

                if not self._game_is_running:
                    self._game_mode = '-'
                    self._ship_name = '-'

                pilot_month_kills: dict = self.statistics_kills_this_month_for_pilot()

                game_notification: GameNotification = GameNotification(
                    pilot_name=self._pilot_name,
                    month=pilot_month_kills.get('month'),
                    pilot_kills=pilot_month_kills.get('kills'),
                    pilot_deaths=pilot_month_kills.get('deaths'),
                    pilot_suicides=pilot_month_kills.get('suicides'),
                    ship_name=self._ship_name,
                    game_mode=self._game_mode,
                )

                await broadcast(game_notification.model_dump())

                if self._verbose_logging:
                    logging.debug(f"[CLIENT] {msg}")

            await broadcast(
                GameExecutableNotification(
                    date=date,
                    game_is_running=self._game_is_running,
                    msg=msg
                ).model_dump()
            )

            self._game_is_running_last_checked = date

            await asyncio.sleep(self._game_executable_check_frequency)

    @property
    def game_executable_name(self) -> str:
        return self._game_executable_name

    @property
    def game_is_running(self) -> bool:
        return self._game_is_running

    @property
    def game_is_running_last_checked(self) -> str:
        return self._game_is_running_last_checked

    @property
    def pilot_name(self) -> str:
        return self._pilot_name

    @property
    def ship_name(self) -> str:
        return self._ship_name

    @property
    def game_mode(self) -> str:
        return self._game_mode

    def enable(self) -> None:
        self._enabled = True

    @property
    def is_enabled(self) -> bool:
        return self._enabled

    def disable(self) -> None:
        self._enabled = False

    @property
    def is_disabled(self) -> bool:
        return not self._enabled

    @property
    def api_url(self) -> str:
        return self._api_url

    @api_url.setter
    def api_url(self, value: str) -> None:
        self._api_url = value

    def player_events(self, limit: Optional[int] = None) -> list[PlayerEvent]:
        if limit:
            res = self._repo.read()[-limit:]
            return res
        else:
            return self._repo.read()

    @property
    def startup_date(self) -> str:
        return self._startup_date

    @property
    def version(self) -> str:
        return self._version

    @property
    def is_verbose_logging(self) -> bool:
        return self._verbose_logging

    def verbose_logging_enable(self) -> None:
        self._verbose_logging = True
        logging.debug(f"[CLIENT] Verbose Logging Enabled")

    def verbose_logging_disable(self) -> None:
        self._verbose_logging = False
        logging.debug(f"[CLIENT] Verbose Logging Disabled")

    def get_config(self) -> dict:
        return {
            "version": self._version,
            "enabled": self._enabled,
            "api_url": self._api_url,
            "verbose_logging": self._verbose_logging,
            "game_executable_name": self._game_executable_name,
            "game_executable_check_frequency": self._game_executable_check_frequency
        }

    def _get_player_event(self, log_entry: str) -> PlayerEvent | None:
        date = get_log_date(log_entry)
        victim_player_name: str = get_victim_player_name(log_entry)
        victim_zone_name: str = get_victim_zone(log_entry)
        killed_by: str = get_killed_by(log_entry)
        using: str = get_using(log_entry)
        damage: str = get_damage(log_entry)

        if killed_by == 'npc' or victim_player_name == 'npc':
            return None

        if self._verbose_logging:
            logging.debug(f"[CLIENT - PLAYER EVENT LOG] {log_entry}")

        if killed_by == self._pilot_name:
            ship_name = self._ship_name

        elif self._game_mode == 'Elimination':
            ship_name = '-'
        else:
            ship_name: str = get_ship_name(log_entry)

        return PlayerEvent(
            uuid=str(uuid.uuid4()),
            date=date,
            victim_player_name=victim_player_name,
            victim_zone_name=victim_zone_name,
            killed_by=killed_by,
            ship_name='-' if 'Suicide' in damage else ship_name,
            using='-' if 'Suicide' in damage else using,
            damage=damage,
            game_mode=self._game_mode
            )

    async def _handle_logfile_notifications(self, broadcast: Callable) -> None:
        if self._game_is_running:
            if self._logfile_monitor.log_is_validated:
                logfile_msg: str = (f'Reading log file every: {self._logfile_monitor.frequency}s, '
                                    f'Last time read: {self._logfile_monitor.last_read_date}, '
                                    f'Number of Lines: {self._logfile_monitor.lines}')
            else:
                logfile_msg: str = f'Can\'t read log file: {self._logfile_monitor.logfile_with_path}, Please check settings...'

        else:
            logfile_msg: str = f'LogFile Scanner stopped since game is not running'

        await broadcast(
            LogFileNotification(
                logfile_frequency=self._logfile_monitor.frequency,
                logfile_msg=logfile_msg,
                logfile_scanner_is_running = False if not self._logfile_monitor.log_is_validated else self._game_is_running
            ).model_dump()
        )

    async def _handle_game_mode_event(self, log_entry: str) -> bool:
        if self._verbose_logging:
            logging.debug(f'[CLIENT - GAME MODE EVENT LOG] {log_entry}')

        game_mode: str = get_game_mode(log_entry)

        if game_mode != self._game_mode:
            if game_mode == 'PU':
                self._ship_name = '-'

                if self._verbose_logging:
                    logging.debug(f'[CLIENT - GAME MODE EVENT] SHIP NAME RESET BECAUSE GAME MODE CHANGED FROM {self._game_mode} TO PU')

            self._game_mode = game_mode
            if self._verbose_logging:
                logging.debug(f"[CLIENT - GAME MODE EVENT] Game Mode: {self._game_mode}")

            return True

        return False

    async def _handle_ship_name_event(self, log_entry: str) -> bool:
        if self._verbose_logging:
            logging.debug(f'[CLIENT - SHIP NAME EVENT LOG] {log_entry}')

        ship_name: str = get_ship_name(log_entry)

        if ship_name != self._ship_name:
            self._ship_name = ship_name
            if self._verbose_logging:
                logging.debug(f"[CLIENT - SHIP NAME EVENT] Ship Name: {self._ship_name}")

            return True

        return False

    async def _handle_pilot_name_event(self, log_entry: str) -> bool:
        if self._verbose_logging:
            logging.debug(f'[CLIENT - PILOT NAME EVENT LOG] {log_entry}')

        pilot_name: str = get_pilot_name(log_entry)

        if pilot_name != self._pilot_name:
            self._pilot_name = pilot_name

            if self._verbose_logging:
                logging.debug(f"[CLIENT - PILOT NAME EVENT] Pilot Name: {self._pilot_name}")

            return True

        return False

    async def _handle_offline_mode(self, broadcast: Callable, player_events: list[PlayerEvent]) -> list[PlayerEvent]:

        for player_event in player_events:

            player_event.client_enabled = self._enabled
            player_event.push_result_message = f"Offline mode: {self._current_date}"
            player_event.push_result_is_success = False

            await broadcast(player_event.model_dump())

        return player_events

    async def _handle_online_mode(self, broadcast: Callable, player_events: list[PlayerEvent]) -> list[PlayerEvent]:

        async with httpx.AsyncClient(verify=False) as client:
            for player_event in player_events:

                data: dict = {
                    "client_id": self._client_id,
                    "client_version": self._version,
                    "player_event": player_event.model_dump(exclude={"client_enabled", "push_result_message", "push_result_is_success"})
                }

                message: str = ''
                is_success: bool = True

                try:
                    response = await client.post(self._api_url, json=data)
                    logging.info(f"Status: {response.status_code}, Response: {response.text}")

                    message = f"Success: {self._current_date}"

                except httpx.RequestError as e:
                    logging.error(f"Request failed: {e}")

                    message = str(e)
                    is_success = False

                finally:
                    player_event.client_enabled=self._enabled
                    player_event.push_result_message=message
                    player_event.push_result_is_success=is_success

                    await broadcast(player_event.model_dump())

        return player_events

    async def recordings_trigger(self, broadcast: Callable):

        player_event: PlayerEvent = PlayerEvent(
            uuid = str(uuid.uuid4()),
            date = "2025-04-22 11:14:06 UTC",
            victim_player_name = "CBCORP",
            victim_zone_name = "Stanton",
            killed_by = "Cellin",
            ship_name = "Dicks",
            using = "gmni lmg ballistic 01 green red01",
            damage = "Bullet",
            game_mode = "FPS Gun Game",
            client_enabled = True,
            push_result_message = "Oh yes",
            push_result_is_success = True
        )
        await self._trigger_controller.trigger_hotkey()
        video_filename = await self._recordings_controller.auto_rename_video(player_event=player_event)

        recording_notification: RecordingNotification = RecordingNotification(
            recordings_qty=self._recordings_controller.video_files_quantity(),
            latest_recording=video_filename
        )
        await broadcast(recording_notification.model_dump())

    async def recordings_video_files(self) -> list[str]:
        return self._recordings_controller.video_files()

    async def recordings_latest_videos(self, qty = 3):
        return self._recordings_controller.latest_videos(qty=qty)

    async def recordings_rename_video(self, old_name: str, new_name: str) -> None:
        return await self._recordings_controller.rename_video(old_name=old_name, new_name=new_name)

    async def recordings_delete_video(self, filename: str) -> None:
        return await self._recordings_controller.delete_video(filename=filename)

    async def recordings_scan_video_files(self) -> None:
        return await self._recordings_controller.scan_video_files()

    async def recordings_video_files_quantity(self) -> int:
        return self._recordings_controller.video_files_quantity()

    async def validate_logfile(self) -> None:
        logging.info(f"[CLIENT - REQUESTING LOGFILE VALIDATION]")

        pilot_name_event, ship_name_event, game_mode_event = await self._logfile_monitor.validate_logfile(
            pilot_name_keyword=self._pilot_name_keyword,
            ship_name_keywords=self._ship_name_keywords,
            game_mode_keywords=self._game_mode_keywords
            )

        if pilot_name_event:
            await self._handle_pilot_name_event(log_entry=pilot_name_event.replace("\n", ""))

        if ship_name_event:
            await self._handle_ship_name_event(log_entry=ship_name_event.replace("\n", ""))

        if game_mode_event:
            await self._handle_game_mode_event(log_entry=game_mode_event.replace("\n", ""))

        if self._verbose_logging:
            logging.debug(f"[CLIENT] State:\n"
                  f"    Pilot Name: {self._pilot_name}\n"
                  f"    Ship Name: {self._ship_name}\n"
                  f"    Game Mode: {self._game_mode}\n"
                  f"*---------------------------------*")

    async def run(self, broadcast: Callable) -> None:
        asyncio.create_task(self._recordings_controller.scan_video_files())
        asyncio.create_task(self._initialize_statistics_controller())
        asyncio.create_task(self._check_if_game_is_running(broadcast))

        while True:
            try:
                self._current_date: str = get_date()

                await self._handle_logfile_notifications(broadcast)

                if not self._logfile_monitor.log_is_validated:
                    await self.validate_logfile()

                if self._logfile_monitor.log_is_validated and self._game_is_running:
                    if self._verbose_logging:
                        logging.debug(f"[CLIENT - CHECKING FOR NEW EVENTS]")

                    if await self._logfile_monitor.has_rolled_over():
                        await self.validate_logfile()

                    new_lines: list[str] = await self._logfile_monitor.get_new_lines()

                    # [PILOT NAME EVENT]
                    pilot_name_changed: bool = False


                    pilot_name_event: str | None = find_event_line(lines=new_lines, keywords=[self._pilot_name_keyword])

                    if pilot_name_event:
                        pilot_name_changed = await self._handle_pilot_name_event(
                            log_entry=pilot_name_event.replace("\n", "")
                        )

                    # [SHIP NAME EVENT]
                    ship_name_changed: bool = False

                    ship_name_event: str | None = find_event_line(lines=new_lines, keywords=self._ship_name_keywords)

                    if ship_name_event:
                        ship_name_changed: bool = await self._handle_ship_name_event(
                            log_entry=ship_name_event.replace("\n", "")
                        )

                    # [GAME MODE EVENT]
                    game_mode_changed: bool = False

                    game_mode_event: str | None = find_event_line(lines=new_lines, keywords=self._game_mode_keywords)

                    if game_mode_event:
                        game_mode_changed = await self._handle_game_mode_event(
                            log_entry=game_mode_event.replace("\n", "")
                        )

                    # [PLAYER EVENTS]
                    player_events: list[PlayerEvent] = [
                        self._get_player_event(log_entry=line)
                        for line in new_lines
                        if self._player_event_keyword in line
                    ]

                    player_events = list(filter(lambda x: x is not None, player_events))

                    if player_events:
                        for player_event in player_events:
                            if self._trigger_controller.is_enabled:
                                must_record_video, reason = await self._recordings_controller.must_record_video(player_name=self._pilot_name, player_event=player_event)

                                if must_record_video:
                                    logging.info(f"[CLIENT EVENT] TRIGGERING VIDEO RECORDING REASON: {reason}")
                                    await self._trigger_controller.trigger_hotkey()

                                    video_filename: str = await self._recordings_controller.auto_rename_video(player_event=player_event)

                                    recording_notification: RecordingNotification = RecordingNotification(
                                        recordings_qty=self._recordings_controller.video_files_quantity(),
                                        latest_recording=video_filename
                                    )
                                    await broadcast(recording_notification.model_dump())

                                else:
                                    logging.info(f"[CLIENT EVENT] VIDEO RECORDING BYPASSED REASON: {reason}")

                        if self.is_enabled:
                            updated_player_events: list[PlayerEvent] = await self._handle_online_mode(broadcast, player_events)
                        else:
                            updated_player_events: list[PlayerEvent] = await self._handle_offline_mode(broadcast, player_events)

                        self._repo.create([e.model_dump() for e in updated_player_events])

                        self._statistics_controller.set_data(events=self._repo.read())

                        pilot_month_kills: dict = self.statistics_kills_this_month_for_pilot()

                        game_notification: GameNotification = GameNotification(
                            pilot_name=self._pilot_name,
                            month=pilot_month_kills.get('month'),
                            pilot_kills=pilot_month_kills.get('kills'),
                            pilot_deaths=pilot_month_kills.get('deaths'),
                            pilot_suicides=pilot_month_kills.get('suicides'),
                            pilot_kdr=pilot_month_kills.get('kdr'),

                            ship_name=self._ship_name,
                            game_mode=self._game_mode,
                        )

                        await broadcast(game_notification.model_dump())

                    if any((pilot_name_changed, ship_name_changed, game_mode_changed)):
                        logging.info(
                            f"[CLIENT - UI NOTIFICATION] Pilot Name: {self._pilot_name}, Ship Name: {self._ship_name}, Game Mode: {self._game_mode}")



            except FileNotFoundError:
                logging.error(f"[CLIENT] LogFile not found: {self._logfile_monitor.logfile_with_path}")

            except Exception as e:
                logging.error(f"[CLIENT] Error reading file: {e}")

            await asyncio.sleep(self._logfile_monitor.frequency)

    # [STATISTICS METHODS]

    def statistics_top_victims(self) -> list[dict]:
        return self._statistics_controller.top_victims()

    def statistics_top_victims_table(self) -> list[dict[str, int]]:
        return self._statistics_controller.get_top_victims_table()

    def statistics_kills_this_month_for_pilot(self, pilot_name: str = None) -> dict[str, None | int | str]:
        if not pilot_name:
            pilot_name = self._pilot_name

        return self._statistics_controller.kills_this_month_for_pilot(pilot_name=pilot_name)

    def statistics_top_killers(self) -> list[dict]:
        return self._statistics_controller.top_killers()

    def statistics_top_killers_table(self) -> list[dict[str, int]]:
        return self._statistics_controller.get_top_killers_table()

    def statistics_kills_by_game_mode(self) -> list[dict[str, int]]:
        return self._statistics_controller.kills_by_game_mode()

    def statistics_damage_type_distribution(self) -> list[dict[str, int]]:
        return self._statistics_controller.damage_type_distribution()

    async def text_notification(self, broadcast: Callable) -> None:
        pilot_month_kills: dict = self.statistics_kills_this_month_for_pilot()

        kills = randint(0, 1000)

        game_notification: GameNotification = GameNotification(
            pilot_name=self._pilot_name,
            pilot_kills=kills,
            month=pilot_month_kills.get('month'),
            ship_name=self._ship_name,
            game_mode=self._game_mode,
        )

        await broadcast(game_notification.model_dump())
