import asyncio
import logging
import os
from pathlib import Path

from src.models.models import PlayerEvent


class RecordingsController:
    def __init__(self, path: Path) -> None:
        self._path: Path = path
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

    @path.setter
    def path(self, path: Path) -> None:
        self._path = path

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
        old_path: Path = self._path / old_name
        new_path: Path = self._path / new_name

        if old_path.exists() and not new_path.exists():
            old_path.rename(new_path)

        self._current_files.remove(old_name)
        self._current_files.append(new_name)

    async def delete_video(self, filename: str) -> None:
        file_path: Path = self._path / filename

        if file_path.exists():
            file_path.unlink()

        self._current_files.remove(filename)

    async def auto_rename_video(self, player_event: PlayerEvent) -> str:

        while True:
            new_files: list[str] = [f.name for f in self._path.iterdir() if f.is_file() and f.name not in self._current_files]

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

                logging.info(f"[RECORDING CONTROLLER RENAMING FILE] filename: {file_name}, new filename: {new_name}")

                old_file.rename(new_file)
                self._current_files.append(new_name)

                return file_name

            await asyncio.sleep(0.1)

    def get_config(self) -> dict:
        return {
            "path": str(self._path)
        }