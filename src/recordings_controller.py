import asyncio
import logging
import os
from pathlib import Path

from src.models.models import PlayerEvent


class RecordingsController:
    def __init__(self, config: dict) -> None:
        self._path: Path = Path(config.get('path'))

        self._record_suicide = config.get('record_suicide')
        self._record_own_death = config.get('record_own_death')
        self._record_pu = config.get('record_pu')
        self._record_gun_rush = config.get('record_gun_rush')
        self._record_squadron_battle = config.get('record_squadron_battle')
        self._record_arena_commander = config.get('record_arena_commander')
        self._record_classic_race = config.get('record_classic_race')
        self._record_battle_royale = config.get('record_battle_royale')
        self._record_free_flight = config.get('record_free_flight')
        self._record_pirate_swarm = config.get('record_pirate_swarm')
        self._record_vanduul_swarm = config.get('record_vanduul_swarm')
        self._record_other = config.get('record_other')

        self._current_files: list[str] = []

    async def scan_video_files(self):
        video_files = sorted(
            [f for f in self._path.glob("*.mp4") if f.is_file()],
            key=lambda f: os.stat(f).st_ctime,
            reverse=True
        )

        self._current_files = [f.name for f in video_files]
        logging.info(f"[RECORDING CONTROLLER SCANNING VIDEO FILES] found {len(self._current_files)} files, path: '{self._path}'")

    @property
    def path(self) -> str:
        return str(self._path)

    @property
    def is_record_suicide(self) -> bool:
        return self._record_suicide

    def record_suicide_enable(self) -> None:
        self._record_suicide = True

    def record_suicide_disable(self) -> None:
        self._record_suicide = False

    @property
    def is_record_own_death(self) -> bool:
        return self._record_own_death

    def record_own_death_enable(self) -> None:
        self._record_own_death = True

    def record_own_death_disable(self) -> None:
        self._record_own_death = False

    @property
    def is_record_pu(self) -> bool:
        return self._record_pu

    def record_pu_enable(self) -> None:
        self._record_pu = True

    def record_pu_disable(self) -> None:
        self._record_pu = False

    @property
    def is_record_gun_rush(self) -> bool:
        return self._record_gun_rush

    def record_gun_rush_enable(self) -> None:
        self._record_gun_rush = True

    def record_gun_rush_disable(self) -> None:
        self._record_gun_rush = False

    @property
    def is_record_squadron_battle(self) -> bool:
        return self._record_squadron_battle

    def record_squadron_battle_enable(self) -> None:
        self._record_squadron_battle = True

    def record_squadron_battle_disable(self) -> None:
        self._record_squadron_battle = False

    @property
    def is_record_arena_commander(self) -> bool:
        return self._record_arena_commander

    def record_arena_commander_enable(self) -> None:
        self._record_arena_commander = True

    def record_arena_commander_disable(self) -> None:
        self._record_arena_commander = False

    @property
    def is_record_classic_race(self) -> bool:
        return self._record_classic_race

    def record_classic_race_enable(self) -> None:
        self._record_classic_race = True

    def record_classic_race_disable(self) -> None:
        self._record_classic_race = False

    @property
    def is_record_battle_royale(self) -> bool:
        return self._record_battle_royale

    def record_battle_royale_enable(self) -> None:
        self._record_battle_royale = True

    def record_battle_royale_disable(self) -> None:
        self._record_battle_royale = False

    @property
    def is_record_free_flight(self) -> bool:
        return self._record_free_flight

    def record_free_flight_enable(self) -> None:
        self._record_free_flight = True

    def record_free_flight_disable(self) -> None:
        self._record_free_flight = False

    @property
    def is_record_pirate_swarm(self) -> bool:
        return self._record_pirate_swarm

    def record_pirate_swarm_enable(self) -> None:
        self._record_pirate_swarm = True

    def record_pirate_swarm_disable(self) -> None:
        self._record_pirate_swarm = False

    @property
    def is_record_vanduul_swarm(self) -> bool:
        return self._record_vanduul_swarm

    def record_vanduul_swarm_enable(self) -> None:
        self._record_vanduul_swarm = True

    def record_vanduul_swarm_disable(self) -> None:
        self._record_vanduul_swarm = False

    @property
    def is_record_other(self) -> bool:
        return self._record_other

    def record_other_enable(self) -> None:
        self._record_other = True

    def record_other_disable(self) -> None:
        self._record_other = False

    async def set_path(self, path: Path) -> None:
        if self._path != path:
            self._path = path
            await self.scan_video_files()

    def video_files(self) -> list[str]:
        return sorted(
            self._current_files,
            key=lambda name: os.stat(self._path / name).st_ctime,
            reverse=True
        )

    def latest_videos(self, qty: int) -> list[str]:
        try:
            return self.video_files()[:qty]

        except IndexError:
            return []

    def video_files_quantity(self) -> int:
        return len(self._current_files)

    async def rename_video(self, old_name: str, new_name: str) -> None:
        try:
            old_path: Path = self._path / old_name
            new_path: Path = self._path / new_name

            if old_path.exists() and not new_path.exists():
                old_path.rename(new_path)

            self._current_files.remove(old_name)
            self._current_files.append(new_name)

        except Exception as e:
            logging.error(f"[RECORDINGS CONTROLLER ERROR RENAME VIDEO] {e}")

    async def must_record_video_old(self, player_name: str, player_event: PlayerEvent) -> bool:
        if player_event.victim_player_name == player_name and player_event.damage == 'Suicide' and self._record_suicide:
            return True

        if player_event.victim_player_name == player_name and self._record_own_death:
            return True

        if player_event.game_mode == 'PU' and self._record_pu:
            return True

        if player_event.game_mode == 'Gun Rush' and self._record_gun_rush:
            return True

        if player_event.game_mode == 'Squadron Battle' and self._record_squadron_battle:
            return True

        if player_event.game_mode == 'Arena Commander' and self._record_arena_commander:
            return True

        if player_event.game_mode == 'Classic Race' and self._record_classic_race:
            return True

        if player_event.game_mode == 'Battle Royale' and self._record_battle_royale:
            return True

        if player_event.game_mode == 'Free Flight' and self._record_free_flight:
            return True

        if player_event.game_mode == 'Pirate Swarm' and self._record_pirate_swarm:
            return True

        if player_event.game_mode == 'Vanduul Swarm' and self._record_vanduul_swarm:
            return True

        game_modes: list[str] = ['PU', 'Gun Rush', 'Squadron Battle', 'Arena Commander', 'Classic Race', 'Battle Royale', 'Free Flight', 'Pirate Swarm']

        if player_event.game_mode not in game_modes and self._record_other:
            return True

        return False

    async def must_record_video(self, player_name: str, player_event: PlayerEvent) -> tuple[bool, str]:
        is_self: bool = player_event.victim_player_name == player_name

        if is_self:
            if player_event.damage == 'Suicide' and self._record_suicide:
                return True, 'Suicide Death is enabled'

            if player_event.damage == 'Suicide' and not self._record_suicide:
                return False, 'Suicide Death is disabled'

            if self._record_own_death:
                return True, 'Own Death is enabled'

            return False, 'Own Death is disabled'

        game_mode_flags: dict = {
            'PU': self._record_pu,
            'Gun Rush': self._record_gun_rush,
            'Squadron Battle': self._record_squadron_battle,
            'Arena Commander': self._record_arena_commander,
            'Classic Race': self._record_classic_race,
            'Battle Royale': self._record_battle_royale,
            'Free Flight': self._record_free_flight,
            'Pirate Swarm': self._record_pirate_swarm,
            'Vanduul Swarm': self._record_vanduul_swarm,
        }

        if game_mode_flags.get(player_event.game_mode):
            return True, f"{player_event.game_mode} is enabled"

        if player_event.game_mode not in game_mode_flags and self._record_other:
            return True, f"Other modes is enabled"

        return False, f'{player_event.game_mode} is disabled'

    async def delete_video(self, filename: str) -> None:
        try:
            file_path: Path = self._path / filename

            if file_path.exists():
                file_path.unlink()

            self._current_files.remove(filename)

        except Exception as e:
            logging.error(f"[RECORDINGS CONTROLLER ERROR DELETE VIDEO] {e}")

    async def auto_rename_video(self, player_event: PlayerEvent) -> str:
        logging.info(f"[RECORDING CONTROLLER AUTO RENAMING]")

        sleep_time = 0.1
        video_record_max_time: float = 4

        while video_record_max_time > 0:
            new_files: list[str] = sorted(
                [f for f in self._path.iterdir() if f.is_file() and f.name not in self._current_files],
                key=lambda f: f.stat().st_ctime,
                reverse=True
            )

            if new_files:
                file_name: str = new_files[0]

                old_file: Path = Path(self._path, file_name)

                new_name: str = (
                    f"{player_event.date.replace(':', '_')}_"
                    f"{player_event.victim_player_name}_"
                    f"{player_event.victim_zone_name}_"
                    f"{player_event.killed_by}_"
                    f"{player_event.ship_name}_"
                    f"{player_event.using}_"
                    f"{player_event.damage}_"
                    f"{player_event.game_mode}_"
                    f"{player_event.uuid[-12:]}"
                    f"{old_file.suffix}"
                )

                new_file: Path = old_file.with_name(new_name)

                try:
                    logging.info(f"[RECORDING CONTROLLER RENAMING FILE] filename: {file_name}, new filename: {new_name}")
                    old_file.rename(new_file)
                    self._current_files.append(new_name)

                    return new_name

                except Exception as e:
                    logging.error(
                        f"[RECORDING CONTROLLER RENAMING FILE - ERROR] couldn't rename filename: {file_name} because {e}")

                    return file_name

            await asyncio.sleep(sleep_time)
            video_record_max_time -= sleep_time

        return ''

    def get_config(self) -> dict:
        return {
            "path": str(self._path),
            "record_suicide": self._record_suicide,
            "record_own_death": self._record_own_death,
            "record_pu": self._record_pu,
            "record_gun_rush": self._record_gun_rush,
            "record_squadron_battle": self._record_squadron_battle,
            "record_arena_commander": self._record_arena_commander,
            "record_classic_race": self._record_classic_race,
            "record_battle_royale": self._record_battle_royale,
            "record_free_flight": self._record_free_flight,
            "record_pirate_swarm": self._record_pirate_swarm,
            "record_vanduul_swarm": self._record_vanduul_swarm,
            "record_other": self._record_other
        }
