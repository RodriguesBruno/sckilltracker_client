import logging
import threading
from pathlib import Path
import pygame

from src.utils import resource_path


class SoundController:
    pygame.mixer.init()

    def __init__(self, config: dict) -> None:
        self._path: Path = Path(config.get('path'))
        self._kill_sounds_enabled: bool = config.get('kill_sounds').get('enabled')
        self._volume: float = config.get('volume')

    @property
    def kill_sounds_enabled(self) -> bool:
        return self._kill_sounds_enabled

    @kill_sounds_enabled.setter
    def kill_sounds_enabled(self, value: bool) -> None:
        self._kill_sounds_enabled = value

    @property
    def volume(self) -> float:
        return self._volume

    @volume.setter
    def volume(self, value: float) -> None:
        volume_percent = max(0.0, min(100.0, value))
        rounded_value = round((volume_percent / 100), 4)

        if rounded_value < 0.0 or rounded_value > 1.0:
            rounded_value = 1.0

        self._volume = rounded_value

    def play_sound(self, path: str) -> None:
        if not self._kill_sounds_enabled:
            return  # 🔇 Sounds disabled

        def _play() -> None:
            try:
                sound = pygame.mixer.Sound(path)
                sound.set_volume(self._volume)
                sound.play()

            except Exception as e:
                logging.error(f"Sound error: {e}")

        threading.Thread(target=_play, daemon=True).start()

    def play_streak_sound(self, level: int) -> None:
        path: str = resource_path(str(self._path / f"kill{level}.mp3"))
        self.play_sound(path=path)

    def get_config(self) -> dict:
        return {
            "path": str(self._path),
            "kill_sounds": {
                "enabled": self._kill_sounds_enabled
            },
            "volume": self._volume
        }