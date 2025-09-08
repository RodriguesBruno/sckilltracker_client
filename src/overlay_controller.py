from src.models.models import PlayerEvent


class OverlayController:
    def __init__(self, config: dict) -> None:
        self._position: str = config.get('position')
        self._font_color: str = config.get('font_color')
        self._font_size: str = config.get('font_size')
        self._enabled: bool = config.get('enabled')
        self._on_suicide: bool = config.get('on_suicide')
        self._on_own_death: bool = config.get('on_own_death')
        self._on_pu: bool = config.get('on_pu')
        self._on_gun_rush: bool = config.get('on_gun_rush')
        self._on_squadron_battle: bool = config.get('on_squadron_battle')
        self._on_arena_commander: bool = config.get('on_arena_commander')
        self._on_classic_race: bool = config.get('on_classic_race')
        self._on_battle_royale: bool = config.get('on_battle_royale')
        self._on_free_flight: bool = config.get('on_free_flight')
        self._on_pirate_swarm: bool = config.get('on_pirate_swarm')
        self._on_vanduul_swarm: bool = config.get('on_vanduul_swarm')
        self._on_other: bool = config.get('on_other')


    @property
    def position(self) -> str:
        return self._position

    @position.setter
    def position(self, value) -> None:
        self._position = value

    @property
    def font_color(self) -> str:
        return self._font_color

    @font_color.setter
    def font_color(self, value) -> None:
        self._font_color = value

    @property
    def font_size(self) -> str:
        return self._font_size

    @font_size.setter
    def font_size(self, value) -> None:
        self._font_size = value

    @property
    def enabled(self) -> bool:
        return self._enabled

    @enabled.setter
    def enabled(self, value) -> None:
        self._enabled = value

    @property
    def on_suicide(self) -> bool:
        return self._on_suicide

    @on_suicide.setter
    def on_suicide(self, value) -> None:
        self._on_suicide = value

    @property
    def on_own_death(self) -> bool:
        return self._on_own_death

    @on_own_death.setter
    def on_own_death(self, value) -> None:
        self._on_own_death = value

    @property
    def on_pu(self) -> bool:
        return self._on_pu

    @on_pu.setter
    def on_pu(self, value) -> None:
        self._on_pu = value

    @property
    def on_gun_rush(self) -> bool:
        return self._on_gun_rush

    @on_gun_rush.setter
    def on_gun_rush(self, value) -> None:
        self._on_gun_rush = value

    @property
    def on_squadron_battle(self) -> bool:
        return self._on_squadron_battle

    @on_squadron_battle.setter
    def on_squadron_battle(self, value) -> None:
        self._on_squadron_battle = value

    @property
    def on_arena_commander(self) -> bool:
        return self._on_arena_commander

    @on_arena_commander.setter
    def on_arena_commander(self, value) -> None:
        self._on_arena_commander = value

    @property
    def on_classic_race(self) -> bool:
        return self._on_classic_race

    @on_classic_race.setter
    def on_classic_race(self, value) -> None:
        self._on_classic_race = value

    @property
    def on_battle_royale(self) -> bool:
        return self._on_battle_royale

    @on_battle_royale.setter
    def on_battle_royale(self, value) -> None:
        self._on_battle_royale = value

    @property
    def on_free_flight(self) -> bool:
        return self._on_free_flight

    @on_free_flight.setter
    def on_free_flight(self, value) -> None:
        self._on_free_flight = value

    @property
    def on_pirate_swarm(self) -> bool:
        return self._on_pirate_swarm

    @on_pirate_swarm.setter
    def on_pirate_swarm(self, value) -> None:
        self._on_pirate_swarm = value

    @property
    def on_vanduul_swarm(self) -> bool:
        return self._on_vanduul_swarm

    @on_vanduul_swarm.setter
    def on_vanduul_swarm(self, value) -> None:
        self._on_vanduul_swarm = value

    @property
    def on_other(self) -> bool:
        return self._on_other

    @on_other.setter
    def on_other(self, value) -> None:
        self._on_other = value

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

        game_mode_flags: dict = {
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

    def get_config(self) -> dict:
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
            "on_other": self._on_other
        }