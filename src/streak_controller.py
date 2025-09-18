
class StreakController:
    def __init__(self) -> None:
        self._kill_count: int = 0
        self._max_kill_level: int = 20

    @property
    def kill_count(self) -> int:
        return self._kill_count

    def increment_kill_streak(self) -> int:
        self._kill_count += 1
        level: int = min(self._kill_count, self._max_kill_level)

        return level

    def reset_kill_streak(self) -> None:
        self._kill_count = 0