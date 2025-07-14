import asyncio
import logging
import subprocess
from multiprocessing import Queue
from typing import Callable, Optional, Any
import httpx

from src.client_utils import generate_client_id
from src.csv_repository import player_event_to_csv_adapter, csv_to_player_event_adapter
from src.event_manager import EventManager
from src.logfile_monitor import LogFileMonitor
from src.models.models import (
    PlayerEvent,
    GameNotification,
    LogFileNotification,
    GameExecutableNotification,
    RecordingNotification,
    PlayerProfile,
    PlayerMonthStatistics
)
from src.overlay_controller import OverlayController

from src.recordings_controller import RecordingsController
from src.statistics_controller import StatisticsController
from src.trigger_controller import TriggerController
from src.repository import Repository, RepositoryType
from src.utils import get_date
from src.sound_player import SoundPlayer

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


class SCClient:
    def __init__(
            self,
            config: dict,
            logfile_monitor: LogFileMonitor,
            repo: Repository,
            statistics_controller: StatisticsController,
            trigger_controller: TriggerController,
            recordings_controller: RecordingsController,
            overlay_controller: OverlayController,
            overlay_queue: Optional[Queue] = None
    ) -> None:

        self._version: str = config.get('version')
        self._enabled: bool = config.get('enabled')
        self._api_url: str = config.get('api_url')
        self._verbose_logging: bool = config.get('verbose_logging')
        self._debug_logging: bool = False

        self._game_executable_name: str = config.get('game_executable_name')
        self._game_executable_check_frequency: int = config.get('game_executable_check_frequency')

        self._logfile_monitor: LogFileMonitor = logfile_monitor
        self._repo: Repository = repo
        self._statistics_controller: StatisticsController = statistics_controller
        self._trigger_controller: TriggerController = trigger_controller
        self._recordings_controller: RecordingsController = recordings_controller
        self._overlay_controller: OverlayController = overlay_controller
        self._overlay_queue = overlay_queue

        self._event_manager: EventManager = EventManager()

        self._startup_date: str = get_date()
        self._client_id: str = generate_client_id()

        self._game_mode: str = '-'
        self._ship_name: str = '-'

        self._player_profile: PlayerProfile = PlayerProfile()

        self._current_date: str = ''

        self._game_is_running: bool = False
        self._game_is_running_last_checked: str = ''


    async def _initialize_statistics_controller(self) -> None:
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

                player_statistics: PlayerMonthStatistics = self.statistics_for_pilot_this_month()

                game_notification: GameNotification = GameNotification(
                    player_profile=self._player_profile,
                    player_statistics=player_statistics,

                    ship_name=self._ship_name,
                    game_mode=self._game_mode
                )

                await broadcast(game_notification.model_dump())


                logging.debug(f"[CLIENT] {msg}") and self._debug_logging

            logging.info(
                f"[CLIENT - UI NOTIFICATION - GAME EXECUTABLE] is running: {self._game_is_running}, date: {date}") and self._verbose_logging

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
        return self._player_profile.name

    @property
    def pilot_org_name(self) -> str:
        return self._player_profile.org.name

    @property
    def pilot_icon_url(self) -> str:
        return self._player_profile.icon_url

    @property
    def pilot_org_icon_url(self) -> str:
        return self._player_profile.org.icon_url

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
            entries = self._repo.read()[-limit:]
        else:
            entries = self._repo.read()

        return [
                csv_to_player_event_adapter(entry)
                if self._repo.type == RepositoryType.CSV
                else entry
                for entry in entries
            ]

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
        logging.info(f"[CLIENT - Verbose Logging] Enabled")

    def verbose_logging_disable(self) -> None:
        self._verbose_logging = False
        logging.info(f"[CLIENT - Verbose Logging] Disabled")

    def debug_logging_enable(self) -> None:
        self._debug_logging = True
        logging.info(f"[CLIENT - Debug Logging] Enabled")

    def debug_logging_disable(self) -> None:
        self._debug_logging = False
        logging.info(f"[CLIENT - Debug Logging] Disabled")

    def logfile_monitor_verbose_logging_enable(self) -> None:
        self._logfile_monitor.verbose_logging = True

    def logfile_monitor_verbose_logging_disable(self) -> None:
        self._logfile_monitor.verbose_logging = False

    def logfile_monitor_debug_logging_enable(self) -> None:
        self._logfile_monitor.debug_logging = True

    def logfile_monitor_debug_logging_disable(self) -> None:
        self._logfile_monitor.debug_logging = False

    def get_config(self) -> dict:
        return {
            "version": self._version,
            "enabled": self._enabled,
            "api_url": self._api_url,
            "verbose_logging": self._verbose_logging,
            "game_executable_name": self._game_executable_name,
            "game_executable_check_frequency": self._game_executable_check_frequency
        }

    async def _handle_logfile_notifications(self, broadcast: Callable) -> None:
        if self._game_is_running:
            if self._logfile_monitor.log_is_validated:
                logfile_msg: str = (
                    f'Reading log file every: {self._logfile_monitor.frequency}s, '
                    f'Last time read: {self._logfile_monitor.last_read_date}, '
                    f'Number of Lines: {self._logfile_monitor.lines}'
                )
            else:
                logfile_msg: str = f'Can\'t read log file: {self._logfile_monitor.logfile_with_path}, Please check settings...'

        else:
            logfile_msg: str = f'LogFile Scanner stopped since game is not running'

        logfile_is_running: bool = False if not self._logfile_monitor.log_is_validated else self._game_is_running

        logging.info(f"[CLIENT - UI NOTIFICATION - LOGFILE SCANNER] is running: {logfile_is_running}") and self._verbose_logging

        await broadcast(
            LogFileNotification(
                logfile_frequency=self._logfile_monitor.frequency,
                logfile_msg=logfile_msg,
                logfile_scanner_is_running = logfile_is_running
            ).model_dump()
        )

    async def _handle_offline_mode(self, broadcast: Callable, player_events: list[PlayerEvent]) -> list[PlayerEvent]:

        for player_event in player_events:

            player_event.client_enabled = self._enabled
            player_event.push_result_message = f"Offline mode: {self._current_date}"
            player_event.push_result_is_success = False

            data = player_event.model_dump()
            await broadcast(data)


            if self._overlay_queue:
                must_display, reason = await self._overlay_controller.must_display_overlay(
                    player_name=self.pilot_name,
                    player_event=player_event
                )

                if must_display:
                    logging.info(f"[CLIENT - OVERLAY] Shown reason: {reason}") and self._verbose_logging

                    self._overlay_queue.put(data)

                else:
                    logging.info(f"[CLIENT - OVERLAY] Not Shown reason: {reason}") and self._verbose_logging

        return player_events

    async def _handle_online_mode(self, broadcast: Callable, player_events: list[PlayerEvent]):

        async with httpx.AsyncClient(verify=False) as client:
            for player_event in player_events:

                data: dict = {
                    "client_id": self._client_id,
                    "client_version": self._version,
                    "player_event": player_event.model_dump(
                        exclude={
                            "client_enabled",
                            "push_result_message",
                            "push_result_is_success"
                        }
                    )
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

                    data = player_event.model_dump()
                    await broadcast(data)

                    if self._overlay_queue and self._overlay_controller.must_display_overlay(
                        player_name=self.pilot_name,
                        player_event=player_event
                    ):
                        self._overlay_queue.put(data)

        return player_events

    async def recordings_video_files(self) -> list[str]:
        return self._recordings_controller.video_files()

    async def recordings_latest_videos(self, qty = 3) -> list[str]:
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
        logging.info(f"[CLIENT - REQUESTING LOGFILE VALIDATION]") and self._verbose_logging

        pilot_name_event, ship_name_event, game_mode_event = await self._logfile_monitor.validate_logfile(
            pilot_name_keyword=self._event_manager.pilot_name_keyword,
            ship_name_keywords=self._event_manager.ship_name_keywords,
            game_mode_keywords=self._event_manager.game_mode_keywords
            )

        if pilot_name_event:
            pilot_name_has_changed, player_profile = await self._event_manager.handle_pilot_name_event(
                new_lines=[pilot_name_event],
                current_pilot_name=self._player_profile.name
            )
            if pilot_name_has_changed:
                self._player_profile = player_profile

        if ship_name_event:
            ship_name_has_changed, ship_name = await self._event_manager.handle_ship_name_event(
                new_lines=[ship_name_event],
                current_ship_name=self._ship_name
            )
            if ship_name_has_changed:
                self._ship_name = ship_name

        if game_mode_event:
            game_mode_has_changed, game_mode = await self._event_manager.handle_game_mode_event(
                new_lines=[game_mode_event],
                current_game_mode=self._game_mode
            )
            if game_mode_has_changed:
                if game_mode == 'PU':
                    self._ship_name = '-'

                self._game_mode = game_mode

        logging.debug(f"[CLIENT] State:\n"
              f"    Pilot Name: {self._player_profile.name}\n"
              f"    Ship Name: {self._ship_name}\n"
              f"    Game Mode: {self._game_mode}\n"
              f"*---------------------------------*") and self._debug_logging

    async def run(self, broadcast: Callable) -> None:
        asyncio.create_task(self._recordings_controller.scan_video_files())
        asyncio.create_task(self._initialize_statistics_controller())
        asyncio.create_task(self._check_if_game_is_running(broadcast))

        while True:
            try:
                self._current_date: str = get_date()

                await self._handle_logfile_notifications(broadcast=broadcast)

                logfile_changed: bool = False
                if not self._logfile_monitor.log_is_validated:
                    await self.validate_logfile()
                    logfile_changed = True


                if self._logfile_monitor.log_is_validated and self._game_is_running:
                    logging.debug(f"[CLIENT - CHECKING FOR NEW EVENTS]") and self._debug_logging

                    if await self._logfile_monitor.has_rolled_over():
                        await self.validate_logfile()
                        logfile_changed = True

                    new_lines: list[str] = await self._logfile_monitor.get_new_lines()
                    self._event_manager.set_event_lines(lines=new_lines)

                    # [PILOT NAME EVENT]
                    pilot_name_changed, player_profile = await self._event_manager.handle_pilot_name_event(
                        new_lines=new_lines,
                        current_pilot_name=self._player_profile.name
                    )

                    if pilot_name_changed:
                        logging.debug(f"[CLIENT EVENT - PILOT NAME CHANGED] to {player_profile.name}") and self._debug_logging
                        self._player_profile = player_profile

                    # [SHIP NAME EVENT]
                    ship_name_changed, ship_name = await self._event_manager.handle_ship_name_event(
                        new_lines=new_lines,
                        current_ship_name=self._ship_name
                    )
                    if ship_name_changed:
                        logging.debug(f"[CLIENT EVENT - SHIP NAME CHANGED] to {ship_name}") and self._debug_logging
                        self._ship_name = ship_name

                    # [GAME MODE EVENT]
                    game_mode_changed, game_mode = await self._event_manager.handle_game_mode_event(
                        new_lines=new_lines,
                        current_game_mode=self._game_mode
                    )
                    if game_mode_changed:
                        logging.debug(f"[CLIENT EVENT - GAME MODE CHANGED] to {game_mode}") and self._debug_logging
                        self._game_mode = game_mode

                    # [PLAYER EVENTS]
                    player_events: list[PlayerEvent] = await self._event_manager.get_player_events(
                        new_lines=new_lines,
                        game_mode=self._game_mode
                    )

                    if player_events:
                        for player_event in player_events:
                            ##KILLSTREAKS
                                    # KILL EVENT
                            if (
                                player_event.killer_profile.name == self._player_profile.name and
                                player_event.victim_profile.name.lower() not in ["", "-", "npc"] and
                                player_event.victim_profile.name != self._player_profile.name
                            ):
                                SoundPlayer.increment_kill_streak()

                                if self._overlay_queue:
                                    self._overlay_queue.put({"kill_streak": SoundPlayer._kill_count})

                            # DEATH EVENT
                            elif (
                                player_event.victim_profile.name == self._player_profile.name and
                                player_event.killer_profile.name.lower() not in ["", "-", "npc"] and
                                player_event.killer_profile.name != self._player_profile.name
                            ):
                                SoundPlayer.reset_kill_streak()

                                if self._overlay_queue:
                                    self._overlay_queue.put({"kill_streak": 0})

                            if self._player_profile.name == player_event.killer_profile.name:
                                player_event.ship_name = self._ship_name

                            if self._player_profile.name == player_event.victim_profile.name:
                                self._ship_name = player_event.ship_name
                                player_event.ship_name = '-'
                                ship_name_changed = True


                            if self._trigger_controller.is_enabled:
                                must_record_video, reason = await self._recordings_controller.must_record_video(
                                    player_name=self._player_profile.name,
                                    player_event=player_event
                                )

                                if must_record_video:
                                    logging.info(f"[CLIENT EVENT - TRIGGERING VIDEO RECORDING] REASON: {reason}") and self._verbose_logging
                                    await self._trigger_controller.trigger_hotkey()

                                    video_filename: str = await self._recordings_controller.auto_rename_video(
                                        player_event=player_event
                                    )

                                    logging.info(
                                        f"[CLIENT - UI NOTIFICATION - RECORDING CONTROLLER] videos_qty: "
                                        f"{self._recordings_controller.video_files_quantity()}, "
                                        f"latest_video_filename: {video_filename}") and self._verbose_logging

                                    recording_notification: RecordingNotification = RecordingNotification(
                                        recordings_qty=self._recordings_controller.video_files_quantity(),
                                        latest_video_filename=video_filename
                                    )
                                    await broadcast(recording_notification.model_dump())

                                else:
                                    logging.info(f"[CLIENT EVENT - VIDEO RECORDING BYPASSED] REASON: {reason}") and self._verbose_logging

                        if self.is_enabled:
                            updated_player_events: list[PlayerEvent] = await self._handle_online_mode(broadcast, player_events)
                        else:
                            updated_player_events: list[PlayerEvent] = await self._handle_offline_mode(broadcast, player_events)

                        entries: list[dict] = [
                            player_event_to_csv_adapter(entry)
                            if self._repo.type == RepositoryType.CSV else entry
                            for entry in updated_player_events
                        ]

                        self._repo.create(entries)

                        self._statistics_controller.set_data(events=self._repo.read())

                        player_statistics: PlayerMonthStatistics = self.statistics_for_pilot_this_month()

                        logging.info(
                            f"[CLIENT - UI NOTIFICATION - GAME] Pilot Name: {self._player_profile.name}, "
                            f"Ship Name: {self._ship_name}, Game Mode: {self._game_mode}") and self._verbose_logging

                        game_notification: GameNotification = GameNotification(
                            player_profile = self._player_profile,
                            player_statistics = player_statistics,

                            ship_name=self._ship_name,
                            game_mode=self._game_mode
                        )

                        await broadcast(game_notification.model_dump())

                    if any((logfile_changed, pilot_name_changed, ship_name_changed, game_mode_changed)):
                        logging.info(
                            f"[CLIENT - UI NOTIFICATION - GAME] Pilot Name: {self._player_profile.name}, "
                            f"Ship Name: {self._ship_name}, "
                            f"Game Mode: {self._game_mode}"
                        ) and self._verbose_logging

                        player_statistics: PlayerMonthStatistics = self.statistics_for_pilot_this_month()

                        game_notification: GameNotification = GameNotification(
                            player_profile=self._player_profile,
                            player_statistics=player_statistics,

                            ship_name=self._ship_name,
                            game_mode=self._game_mode
                        )

                        await broadcast(game_notification.model_dump())


            except FileNotFoundError:
                logging.error(f"[CLIENT] LogFile not found: {self._logfile_monitor.logfile_with_path}")

            except Exception as e:
                logging.error(f"[CLIENT] Error reading file: {e}")

            await asyncio.sleep(self._logfile_monitor.frequency)


    # [STATISTICS METHODS]

    def statistics_top_victims(self, exclude_player: bool = True) -> list[dict]:
        if exclude_player:
            return self._statistics_controller.top_victims(exclude_player=self._player_profile.name)

        return self._statistics_controller.top_victims()

    def statistics_top_victims_table(self, exclude_player: bool = True) -> list[dict[str, int]]:
        if exclude_player:
            return self._statistics_controller.get_top_victims_table(exclude_player=self._player_profile.name)

        return self._statistics_controller.get_top_victims_table()

    def statistics_for_pilot_this_month(self, pilot_name: str = None) -> PlayerMonthStatistics:
        if not pilot_name:
            pilot_name = self._player_profile.name

        return self._statistics_controller.kills_for_player_this_month(player_name=pilot_name)

    def statistics_top_killers(self, exclude_player: bool = True) -> list[dict]:
        if exclude_player:
            return self._statistics_controller.top_killers(exclude_player=self._player_profile.name)

        return self._statistics_controller.top_killers()

    def statistics_top_killers_table(self,exclude_player: bool = True) -> list[dict[str, int]]:
        if exclude_player:
            return self._statistics_controller.get_top_killers_table(exclude_player=self._player_profile.name)

        return self._statistics_controller.get_top_killers_table()

    def statistics_kills_by_game_mode(self) -> list[dict[str, int]]:
        return self._statistics_controller.kills_by_game_mode()

    def statistics_damage_type_distribution(self) -> list[dict[str, int]]:
        return self._statistics_controller.damage_type_distribution()

    async def text_notification(self, broadcast: Callable) -> None:
        player_statistics: PlayerMonthStatistics = self.statistics_for_pilot_this_month()

        game_notification: GameNotification = GameNotification(
            player_profile=self._player_profile,
            player_statistics=player_statistics,

            ship_name=self._ship_name,
            game_mode=self._game_mode
        )

        await broadcast(game_notification.model_dump())