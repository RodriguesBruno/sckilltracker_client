import logging
import uuid

from src.models.models import PlayerEvent, PlayerProfile
from src.msg_parser import (
    get_log_date,
    get_victim_name,
    get_victim_zone,
    get_killer_name,
    get_using,
    get_damage,
    get_ship_name,
    get_player_name,
    get_game_mode
)
from src.profile_manager import ProfileManager


def find_event_line(lines: list[str], keywords: list[str]) -> str | None:
    return next((line for line in lines if any(k in line for k in keywords)), None)


class EventManager:
    def __init__(self) -> None:
        self._profile_manager: ProfileManager = ProfileManager()
        self._event_lines: list[str] = []

        # self._pilot_name_keyword: str = '<OnClientConnected> Player'
        self._pilot_name_keyword: str = '<Legacy login response> [CIG-net] User Login Success - Handle['
        self._ship_name_keywords: list[str] = [
            '[VEHICLE SPAWN] CPlayerShipRespawnManager:',
            '<Jump Drive Requesting State Change>'
        ]
        self._game_mode_keywords: list[str] = ['> Loading screen for ', '> Mode[EA']
        self._player_event_keyword: str = "<Actor Death>"

        self._verbose_logging: bool = True
        self._debug_logging: bool = False

    @property
    def pilot_name_keyword(self) -> str:
        return self._pilot_name_keyword

    @property
    def ship_name_keywords(self) -> list[str]:
        return self._ship_name_keywords

    @property
    def game_mode_keywords(self) -> list[str]:
        return self._game_mode_keywords

    @property
    def verbose_logging(self) -> bool:
        return self._verbose_logging

    @verbose_logging.setter
    def verbose_logging(self, value: bool) -> None:
        self._verbose_logging = value
        logging.info(f"[EVENT MANAGER - Verbose Logging] {'Enabled' if value else 'Disabled'}")

    @property
    def debug_logging(self) -> bool:
        return self._debug_logging

    @debug_logging.setter
    def debug_logging(self, value: bool) -> None:
        logging.info(f'[EVENT MANAGER - Debug Logging] {"Enabled" if value else "Disabled"}')
        self._debug_logging = value

    def set_event_lines(self, lines: list[str]) -> None:
        self._event_lines = lines

    async def handle_pilot_name_event(self, new_lines: list[str], current_pilot_name: str) -> tuple[bool, PlayerProfile] | tuple[bool, None]:
        pilot_name_event: str | None = find_event_line(lines=new_lines, keywords=[self._pilot_name_keyword])

        if pilot_name_event:
            pilot_name: str = get_player_name(line=pilot_name_event.replace("\n", ""))

            if pilot_name != current_pilot_name:
                player_profile: PlayerProfile = await self._profile_manager.get_profile(name=pilot_name)

                return True, player_profile

        return False, None

    async def handle_ship_name_event(self, new_lines: list[str], current_ship_name: str) -> tuple[bool, str]:
        ship_name_event: str | None = find_event_line(lines=new_lines, keywords=self._ship_name_keywords)

        if ship_name_event:
            ship_name: str = get_ship_name(line=ship_name_event.replace("\n", ""))

            if ship_name != current_ship_name:
                return True, ship_name

        return False, '-'

    async def handle_game_mode_event(self, new_lines: list[str], current_game_mode: str) -> tuple[bool, str]:
        game_mode_event: str | None = find_event_line(lines=new_lines, keywords=self._game_mode_keywords)

        if game_mode_event:
            game_mode: str = get_game_mode(line=game_mode_event.replace("\n", ""))

            if game_mode != current_game_mode:
                return True, game_mode

        return False, '-'

    async def get_player_events(self, new_lines: list[str], game_mode: str, track_crash_deaths: bool) -> list[PlayerEvent]:
        player_events: list[PlayerEvent] = []
        for line in new_lines:
            if self._player_event_keyword in line:
                player_events.extend(
                    await self._get_player_event(
                        log_entry=line,
                        game_mode=game_mode,
                        track_crash_deaths=track_crash_deaths
                    )
                )

        return player_events

    async def _get_player_event(self, log_entry: str, game_mode: str, track_crash_deaths: bool) -> list[PlayerEvent]:
        date: str = get_log_date(line=log_entry)
        victim_name: str = get_victim_name(line=log_entry, track_crash_deaths=track_crash_deaths)
        victim_zone_name: str = get_victim_zone(line=log_entry)
        killer_name: str = get_killer_name(line=log_entry)
        using: str = get_using(line=log_entry)
        damage: str = get_damage(line=log_entry)

        victim_profile: PlayerProfile = await self._profile_manager.get_profile(name=victim_name)

        killer_profile: PlayerProfile = await self._profile_manager.get_profile(name=killer_name)

        if killer_name != 'npc' or victim_name != 'npc':
            return []

        elif game_mode == 'Elimination':
            ship_name = '-'
        else:
            ship_name = get_ship_name(log_entry)

        result: PlayerEvent = PlayerEvent(
            uuid=str(uuid.uuid4()),
            date=date,
            victim_profile=victim_profile,

            victim_zone_name=victim_zone_name,

            killer_profile=killer_profile,

            ship_name='-' if 'Suicide' in damage else ship_name,

            using='-' if 'Suicide' in damage else using,
            damage=damage,
            game_mode=game_mode
            )

        return [result]

