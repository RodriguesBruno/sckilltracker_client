from typing import Any

from src.models.models import PlayerEvent


class OverlayController:
    def __init__(self, config: dict[str, Any]) -> None:
        self._enabled: bool = config.get('enabled', True)
        self._position: str = config.get('position', 'top-right')
        self._font_color: str = config.get('font_color', 'orange')
        self._font_size: str = config.get('font_size', '5')
        self._on_suicide: bool = config.get('on_suicide', True)
        self._on_own_death: bool = config.get('on_own_death', True)
        self._on_pu: bool = config.get('on_pu', True)
        self._on_gun_rush: bool = config.get('on_gun_rush', True)
        self._on_squadron_battle: bool = config.get('on_squadron_battle', True)
        self._on_arena_commander: bool = config.get('on_arena_commander', True)
        self._on_classic_race: bool = config.get('on_classic_race', True)
        self._on_battle_royale: bool = config.get('on_battle_royale', True)
        self._on_free_flight: bool = config.get('on_free_flight', True)
        self._on_pirate_swarm: bool = config.get('on_pirate_swarm', True)
        self._on_vanduul_swarm: bool = config.get('on_vanduul_swarm', True)
        self._on_other: bool = config.get('on_other', True)
        self._on_kill_streak: bool = config.get('on_kill_streak', True)


    @property
    def position(self) -> str:
        return self._position

    @position.setter
    def position(self, value: str) -> None:
        self._position = value

    @property
    def font_color(self) -> str:
        return self._font_color

    @font_color.setter
    def font_color(self, value: str) -> None:
        self._font_color = value

    @property
    def font_size(self) -> str:
        return self._font_size

    @font_size.setter
    def font_size(self, value: str) -> None:
        self._font_size = value

    @property
    def is_enabled(self) -> bool:
        return self._enabled

    def enable(self) -> None:
        self._enabled = True

    def disable(self) -> None:
        self._enabled = False

    @property
    def on_suicide(self) -> bool:
        return self._on_suicide

    def on_suicide_enable(self) -> None:
        self._on_suicide = True

    def on_suicide_disable(self) -> None:
        self._on_suicide = False

    @property
    def on_own_death(self) -> bool:
        return self._on_own_death

    def on_own_death_enable(self) -> None:
        self._on_own_death = True

    def on_own_death_disable(self) -> None:
        self._on_own_death = False

    @property
    def on_pu(self) -> bool:
        return self._on_pu

    def on_pu_enable(self) -> None:
        self._on_pu = True

    def on_pu_disable(self) -> None:
        self._on_pu = False

    @property
    def on_gun_rush(self) -> bool:
        return self._on_gun_rush

    def on_gun_rush_enable(self) -> None:
        self._on_gun_rush = True

    def on_gun_rush_disable(self) -> None:
        self._on_gun_rush = False

    @property
    def on_squadron_battle(self) -> bool:
        return self._on_squadron_battle

    def on_squadron_battle_enable(self) -> None:
        self._on_squadron_battle = True

    def on_squadron_battle_disable(self) -> None:
        self._on_squadron_battle = False

    @property
    def on_arena_commander(self) -> bool:
        return self._on_arena_commander

    def on_arena_commander_enable(self) -> None:
        self._on_arena_commander = True

    def on_arena_commander_disable(self) -> None:
        self._on_arena_commander = False

    @property
    def on_classic_race(self) -> bool:
        return self._on_classic_race

    def on_classic_race_enable(self) -> None:
        self._on_classic_race = True

    def on_classic_race_disable(self) -> None:
        self._on_classic_race = False

    @property
    def on_battle_royale(self) -> bool:
        return self._on_battle_royale

    def on_battle_royale_enable(self) -> None:
        self._on_battle_royale = True

    def on_battle_royale_disable(self) -> None:
        self._on_battle_royale = False

    @property
    def on_free_flight(self) -> bool:
        return self._on_free_flight

    def on_free_flight_enable(self) -> None:
        self._on_free_flight = True

    def on_free_flight_disable(self) -> None:
        self._on_free_flight = False

    @property
    def on_pirate_swarm(self) -> bool:
        return self._on_pirate_swarm

    def on_pirate_swarm_enable(self) -> None:
        self._on_pirate_swarm = True

    def on_pirate_swarm_disable(self) -> None:
        self._on_pirate_swarm = False

    @property
    def on_vanduul_swarm(self) -> bool:
        return self._on_vanduul_swarm

    def on_vanduul_swarm_enable(self) -> None:
        self._on_vanduul_swarm = True

    def on_vanduul_swarm_disable(self) -> None:
        self._on_vanduul_swarm = False

    @property
    def on_other(self) -> bool:
        return self._on_other

    def on_other_enable(self) -> None:
        self._on_other = True

    def on_other_disable(self) -> None:
        self._on_other = False

    @property
    def on_kill_streak(self) -> bool:
        return self._on_kill_streak

    @on_kill_streak.setter
    def on_kill_streak(self, value: bool) -> None:
        self._on_kill_streak = value

    async def must_display_overlay(self, player_name: str, player_event: PlayerEvent) -> tuple[bool, str]:
        is_self: bool = player_event.victim_profile.name == player_name

        if is_self:
            if player_event.damage == 'Suicide' and self._on_suicide:
                return True, 'Suicide Death is enabled'

            if player_event.damage == 'Suicide' and not self._on_suicide:
                return False, 'Suicide Death is disabled'

            if self._on_own_death:
                return True, 'Own Death is enabled'

            return False, 'Own Death is disabled'

        game_mode_flags: dict[str, Any] = {
            'PU': self._on_pu,
            'Gun Rush': self._on_gun_rush,
            'Squadron Battle': self._on_squadron_battle,
            'Arena Commander': self._on_arena_commander,
            'Classic Race': self._on_classic_race,
            'Battle Royale': self._on_battle_royale,
            'Free Flight': self._on_free_flight,
            'Pirate Swarm': self._on_pirate_swarm,
            'Vanduul Swarm': self._on_vanduul_swarm,
        }

        if game_mode_flags.get(player_event.game_mode):
            return True, f"{player_event.game_mode} is enabled"

        if player_event.game_mode not in game_mode_flags and self._on_other:
            return True, f"Other modes is enabled"

        return False, f'{player_event.game_mode} is disabled'

    def get_config(self) -> dict[str, Any]:
        return {
            "enabled": self._enabled,
            "position": self._position,
            "font_color": self._font_color,
            "font_size": self._font_size,
            "on_suicide": self._on_suicide,
            "on_own_death": self._on_own_death,
            "on_pu": self._on_pu,
            "on_gun_rush": self._on_gun_rush,
            "on_squadron_battle": self._on_squadron_battle,
            "on_arena_commander": self._on_arena_commander,
            "on_classic_race": self._on_classic_race,
            "on_battle_royale": self._on_battle_royale,
            "on_free_flight": self._on_free_flight,
            "on_pirate_swarm": self._on_pirate_swarm,
            "on_vanduul_swarm": self._on_vanduul_swarm,
            "on_other": self._on_other,
            "on_kill_streak": self._on_kill_streak
        }
