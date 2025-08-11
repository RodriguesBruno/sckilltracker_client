import asyncio
import logging
import msvcrt
import os
from pathlib import Path

from src.models.models import PlayerEvent


def file_is_locked(file_path: Path) -> bool:
    try:
        with open(file_path, 'r+b') as f:
            msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, 1)
            msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)
            return False

    except OSError:
        return True


class RecordingsController:
    def __init__(self, config: dict) -> None:
        self._path: Path = Path(config.get('path'))

        self._record_suicide: bool = config.get('record_suicide')
        self._record_own_death: bool = config.get('record_own_death')
        self._record_pu: bool = config.get('record_pu')
        self._record_gun_rush: bool = config.get('record_gun_rush')
        self._record_squadron_battle: bool = config.get('record_squadron_battle')
        self._record_arena_commander: bool = config.get('record_arena_commander')
        self._record_classic_race: bool = config.get('record_classic_race')
        self._record_battle_royale: bool = config.get('record_battle_royale')
        self._record_free_flight: bool = config.get('record_free_flight')
        self._record_pirate_swarm: bool = config.get('record_pirate_swarm')
        self._record_vanduul_swarm: bool = config.get('record_vanduul_swarm')
        self._record_other: bool = config.get('record_other')

        self._current_files: list[str] = []

    async def scan_video_files(self):
        video_files = sorted(
            [f for f in self._path.glob("*.mp4") if f.is_file()],
            key=lambda f: os.stat(f).st_ctime,
            reverse=True
        )

        self._current_files = [f.name for f in video_files]
        logging.info(f"[RECORDING CONTROLLER - SCAN VIDEO FILES] found {len(self._current_files)} files, path: '{self._path}'")

    @property
    def path(self) -> Path:
        return self._path

    async def set_path(self, path: Path) -> None:
        if self._path != path:
            self._path = path
            await self.scan_video_files()

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

        except FileNotFoundError:
            return []

        except Exception as e:
            logging.error(e)
            return []

    def video_files_quantity(self) -> int:
        return len(self._current_files)

    async def rename_video(self, old_name: str, new_name: str) -> None:
        logging.info(f"[RECORDING CONTROLLER - RENAME VIDEO]")
        try:
            old_path: Path = self._path / old_name
            new_path: Path = self._path / new_name

            if old_path.exists() and not new_path.exists():
                old_path.rename(new_path)

            self._current_files.remove(old_name)
            self._current_files.append(new_name)

            logging.info(f"[RECORDING CONTROLLER - RENAMED VIDEO] filename: {old_name}, new filename: {new_name}")

        except Exception as e:
            logging.error(f"[RECORDINGS CONTROLLER - RENAME VIDEO ERROR] {e}")

    async def must_record_video(self, player_name: str, player_event: PlayerEvent) -> tuple[bool, str]:
        is_self: bool = player_event.victim_profile.name == player_name

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
        logging.error(f"[RECORDINGS CONTROLLER - DELETE VIDEO]")
        try:
            file_path: Path = self._path / filename

            if file_path.exists():
                if file_is_locked(file_path=file_path):
                    logging.error(f"[RECORDINGS CONTROLLER - DELETE VIDEO ERROR] File is locked: {filename}")
                    return

                file_path.unlink()
                self._current_files.remove(filename)
                logging.info(f"[RECORDINGS CONTROLLER - DELETED VIDEO] Filename: {filename}")

        except Exception as e:
            logging.error(f"[RECORDINGS CONTROLLER - DELETE VIDEO ERROR] {e}")


    async def auto_rename_video(self, player_event: PlayerEvent) -> str:
        logging.info(f"[RECORDING CONTROLLER - AUTO RENAMING]")

        sleep_time = 0.5
        video_record_max_time: float = 6

        while video_record_max_time > 0:
            new_files: list[str] = sorted(
                [
                    f for f
                    in self._path.iterdir()
                    if f.is_file() and f.name not in self._current_files
                ],
                key=lambda f: f.stat().st_ctime,
                reverse=True
            )

            if new_files:
                await asyncio.sleep(3)
                file_name: str = new_files[0]
                old_file: Path = Path(self._path, file_name)

                if file_is_locked(file_path=old_file):
                    logging.warning(f"[RECORDING CONTROLLER - AUTO RENAMING] File is locked: {file_name}")
                    await asyncio.sleep(sleep_time)
                    video_record_max_time -= sleep_time
                    continue

                logging.info(f"[RECORDING CONTROLLER - AUTO RENAMING] File is unlocked: {file_name}, Proceeding with renaming...")

                new_name: str = (
                    f"{player_event.date.replace(':', '_')}_"
                    f"{player_event.victim_profile.name}_"
                    f"{player_event.victim_zone_name}_"
                    f"{player_event.killer_profile.name}_"
                    f"{player_event.ship_name}_"
                    f"{player_event.using}_"
                    f"{player_event.damage}_"
                    f"{player_event.game_mode}_"
                    f"{player_event.uuid[-6:]}"
                    f"{old_file.suffix}"
                )

                new_file: Path = old_file.with_name(new_name)

                try:
                    logging.info(f"[RECORDING CONTROLLER - AUTO RENAMING] filename: {file_name}, new filename: {new_name}")
                    old_file.rename(new_file)
                    self._current_files.append(new_name)

                    return new_name

                except Exception as e:
                    logging.error(
                        f"[RECORDING CONTROLLER - AUTO RENAMING ERROR] couldn't rename filename: {file_name} because {e}")

                    return str(file_name)

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
