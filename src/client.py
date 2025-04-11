import asyncio
import logging
import subprocess
from typing import Callable

import httpx

from src.client_utls import generate_client_id
from src.logfile_monitor import LogFileMonitor
from src.models.models import (
    Notification,
    PushResult,
    PlayerEvent,
    GameNotification,
    LogFileNotification,
    ClientEvent,
    GameExecutableNotification
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

class SCClient:
    def __init__(self, config: dict, logfile_monitor: LogFileMonitor, repo: Repository, trigger_controller: TriggerController) -> None:
        self._version: str = config.get('version')
        self._enabled: bool = config.get('enabled')
        self._api_url: str = config.get('api_url')
        self._verbose_logging: bool = config.get('verbose_logging')

        self._logfile_monitor: LogFileMonitor = logfile_monitor
        self._repo: Repository = repo
        self._trigger_controller: TriggerController = trigger_controller

        self._startup_date: str = get_date()
        self._client_id: str = generate_client_id()

        self._game_mode: str = '-'
        self._ship_name: str = '-'
        self._pilot_name: str = '-'

        self._pilot_name_keyword: str = '<OnClientConnected> Player'
        self._ship_name_keywords: list[str] = ['[VEHICLE SPAWN] CPlayerShipRespawnManager:','<Jump Drive Requesting State Change>']
        self._game_mode_keywords: list[str] = ['<ContextEstablisherTaskFinished> establisher=', '<[EALobby] EALobbyChangeMode>']

        self._player_event_keyword: str = "<Actor Death>"

        self._current_date: str = ''

        self._notifications: list[Notification] = []

        self._game_is_running: bool = False
        self._game_is_running_last_checked: str = ''

        self._game_executable_name: str = 'starcitizen.exe'


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

            await asyncio.sleep(5)

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

    @property
    def notifications(self) -> list:
        return self._notifications

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
            "verbose_logging": self._verbose_logging
        }

    def _get_player_event(self, log_entry: str) -> PlayerEvent:
        date = get_log_date(log_entry)
        victim_player_name: str = get_victim_player_name(log_entry)
        victim_zone_name: str = get_victim_zone(log_entry)
        killed_by: str = get_killed_by(log_entry)

        if victim_player_name != self._pilot_name:
            ship_name: str = get_ship_name(log_entry)
        else:
            ship_name = '-'

        using: str = get_using(log_entry)
        damage: str = get_damage(log_entry)

        return PlayerEvent(
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
            logfile_msg: str = (f'Reading log file every: {self._logfile_monitor.frequency}s, '
                                f'Last time read: {self._logfile_monitor.last_read_date}')
        else:
            logfile_msg: str = F'LogFile Scanner stopped since game is not running'

        await broadcast(
            LogFileNotification(
                logfile_frequency=self._logfile_monitor.frequency,
                logfile_msg=logfile_msg,
                logfile_scanner_is_running = self._game_is_running
            ).model_dump()
        )

    async def _handle_game_mode_event(self, log_entry: str) -> None:
        game_mode: str = get_game_mode(log_entry)

        if game_mode != self._game_mode:
            self._game_mode = game_mode
            if self._verbose_logging:
                logging.debug(f"[CLIENT - GAME MODE EVENT] Game Mode: {self._game_mode}")

    async def _handle_ship_name_event(self, log_entry: str) -> None:
        ship_name: str = get_ship_name(log_entry)

        if ship_name != self._ship_name:
            self._ship_name = ship_name
            if self._verbose_logging:
                logging.debug(f"[CLIENT - SHIP NAME EVENT] Ship Name: {self._ship_name}")

    async def _handle_pilot_name_event(self, log_entry: str) -> None:
        pilot_name: str = get_pilot_name(log_entry)

        if pilot_name != self._pilot_name:
            self._pilot_name = pilot_name
            if self._verbose_logging:
                logging.debug(f"[CLIENT - PILOT NAME EVENT] Pilot Name: {self._pilot_name}")

    async def _handle_offline_mode(self, broadcast: Callable, player_events: list[PlayerEvent]) -> None:
        for player_event in player_events:

            notification: Notification = Notification(
                player_event=player_event,
                client_enabled=self._enabled,
                push_result=PushResult(message=f"Offline mode: {self._current_date}", is_success=False)
            )

            self._notifications.append(notification)

            await broadcast(notification.model_dump())

        if self._trigger_controller.is_enabled and player_events:
            self._trigger_controller.trigger_hotkey()

        self._repo.create([e.model_dump() for e in player_events])

    async def _handle_online_mode(self, broadcast: Callable, player_events: list[PlayerEvent]) -> None:
        async with httpx.AsyncClient() as client:
            for player_event in player_events:

                client_event: ClientEvent = ClientEvent(
                    client_id=self._client_id,
                    client_version=self._version,
                    player_event=player_event
                )

                message: str = ''
                is_success: bool = True

                try:
                    response = await client.post(self._api_url, json=client_event.model_dump())
                    logging.info(f"Status: {response.status_code}, Response: {response.text}")

                    message = f"Success: {self._current_date}"

                except httpx.RequestError as e:
                    logging.error(f"Request failed: {e}")

                    message = str(e)
                    is_success = False

                finally:
                    notification: Notification = Notification(
                        player_event=player_event,
                        client_enabled=self._enabled,
                        push_result=PushResult(message=message, is_success=is_success)
                    )
                    self._notifications.append(notification)

                    await broadcast(notification.model_dump())

            if self._trigger_controller.is_enabled and player_events:
                self._trigger_controller.trigger_hotkey()

            self._repo.create([e.model_dump() for e in player_events])

    async def validate_logfile(self) -> None:
        logging.info(f"[CLIENT] Requesting LogFile Validation")

        pilot_name_event, ship_name_event, game_mode_event,  = await self._logfile_monitor.validate_logfile(
            pilot_name_keyword=self._pilot_name_keyword,
            ship_name_keywords=self._ship_name_keywords,
            game_mode_keywords=self._game_mode_keywords
            )

        if pilot_name_event:
            await self._handle_pilot_name_event(pilot_name_event)

        if ship_name_event:
            await self._handle_ship_name_event(ship_name_event)

        if game_mode_event:
            await self._handle_game_mode_event(game_mode_event)

        logging.info(f"[CLIENT] Initialized:\n"
              f"    Pilot Name: {self._pilot_name}\n"
              f"    Ship Name: {self._ship_name}\n"
              f"    Game Mode: {self._game_mode}\n"
              f"*---------------------------------*")

    async def run(self, broadcast: Callable) -> None:
        asyncio.create_task(self._check_if_game_is_running(broadcast))

        while True:
            try:
                self._current_date: str = get_date()

                if not self._game_is_running:
                    await self._handle_logfile_notifications(broadcast)

                if self._logfile_monitor.log_is_validated and self._game_is_running:

                    new_lines: list[str] = await self._logfile_monitor.get_new_lines()

                    await self._handle_logfile_notifications(broadcast)

                    player_event_lines: list[str] = [line for line in new_lines if self._player_event_keyword in line]

                    broadcast_game_notification: bool = False

                    # PILOT NAME EVENT
                    pilot_name_event: str | None = next(
                        (line for line in new_lines if self._pilot_name_keyword in line), None)

                    if pilot_name_event:
                        await self._handle_pilot_name_event(pilot_name_event)
                        broadcast_game_notification = True

                    # SHIP NAME EVENT
                    ship_name_event = None
                    for line in new_lines:
                        for word in self._ship_name_keywords:
                            if word in line:
                                ship_name_event = line

                    if ship_name_event:
                        await self._handle_ship_name_event(ship_name_event)
                        broadcast_game_notification = True

                    # GAME MODE EVENT
                    game_mode_event = None
                    for line in new_lines:
                        for word in self._game_mode_keywords:
                            if word in line:
                                game_mode_event = line

                    if game_mode_event:
                        await self._handle_game_mode_event(game_mode_event)
                        broadcast_game_notification = True

                    if broadcast_game_notification:
                        logging.info(f"[CLIENT - UI NOTIFICATION] Pilot Name: {self._pilot_name}, Ship Name: {self._ship_name}, Game Mode: {self._game_mode}")

                        await broadcast(
                            GameNotification(
                                pilot_name=self._pilot_name,
                                ship_name=self._ship_name,
                                game_mode=self._game_mode
                            ).model_dump()
                        )

                    player_events: list[PlayerEvent] = [self._get_player_event(line) for line in player_event_lines]

                    if self.is_disabled:
                        await self._handle_offline_mode(broadcast, player_events)

                    if self.is_enabled:
                        await self._handle_online_mode(broadcast, player_events)

            except FileNotFoundError:
                logging.error(f"[CLIENT] LogFile not found: {self._logfile_monitor.logfile_with_path}")

            except Exception as e:
                logging.error(f"[CLIENT] Error reading file: {e}")

            await asyncio.sleep(self._logfile_monitor.frequency)

