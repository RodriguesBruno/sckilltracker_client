import threading

import pygame

from src.file_handlers import read_config

pygame.mixer.init()

class SoundPlayer:
    _kill_count = 0
    _max_kill_level = 30

    @staticmethod
    def play_sound(path: str):
        config = read_config("config.json")
        if not config.get("sound", {}).get("enable_kill_sounds", True):
            return  # 🔇 Sounds disabled
        
        volume = config.get("sound", {}).get("volume", 1.0)

        def _play():
            try:
                sound = pygame.mixer.Sound(path)
                sound.set_volume(volume)
                sound.play()
            except Exception as e:
                print(f"Sound error: {e}")

        threading.Thread(target=_play, daemon=True).start()

    @staticmethod
    def increment_kill_streak():
        SoundPlayer._kill_count += 1
        SoundPlayer._play_streak_sound()

    @staticmethod
    def reset_kill_streak():
        SoundPlayer._kill_count = 0

    @staticmethod
    def _play_streak_sound():
        level = min(SoundPlayer._kill_count, SoundPlayer._max_kill_level)
        SoundPlayer.play_sound(f"static/sounds/kill{level}.mp3")