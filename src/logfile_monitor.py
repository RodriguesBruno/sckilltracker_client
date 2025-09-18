import logging

from src.utils import get_date


class LogFileMonitor:
    def __init__(self, config: dict) -> None:
        self._logfile_with_path: str = config.get('logfile_with_path')
        self._frequency: int = config.get('frequency')

        self._is_validated: bool = False
        self._last_read_date: str = 'Never'
        self._lines: int = 0
        self._file_position: int = 0

        self._verbose_logging: bool = True
        self._debug_logging: bool = False

    @property
    def logfile_with_path(self) -> str:
        return self._logfile_with_path

    @logfile_with_path.setter
    def logfile_with_path(self, value: str) -> None:
        self._logfile_with_path = value

    @property
    def lines(self) -> int:
        return self._lines

    @property
    def frequency(self) -> int:
        return self._frequency

    @frequency.setter
    def frequency(self, value: int) -> None:
        self._frequency = value

    @property
    def log_is_validated(self) -> bool:
        return self._is_validated

    @property
    def log_is_not_validated(self) -> bool:
        return not self._is_validated

    @log_is_validated.setter
    def log_is_validated(self, value: bool) -> None:
        self._is_validated = value

    @property
    def last_read_date(self) -> str:
        return self._last_read_date

    @property
    def verbose_logging(self) -> bool:
        return self._verbose_logging

    @verbose_logging.setter
    def verbose_logging(self, value: bool) -> None:
        self._verbose_logging = value
        logging.info(f"[LOGFILE MONITOR - Verbose Logging] {'Enabled' if value else 'Disabled'}")

    @property
    def debug_logging(self) -> bool:
        return self._debug_logging

    @debug_logging.setter
    def debug_logging(self, value: bool) -> None:
        logging.info(f'[LOGFILE MONITOR - Debug Logging] {"Enabled" if value else "Disabled"}')
        self._debug_logging = value

    def reset(self) -> None:
        self._is_validated = False
        self._file_position = 0

    def get_config(self) -> dict:
        return {
            "logfile_with_path": self._logfile_with_path,
            "frequency": self._frequency
        }

    async def validate_logfile(self, pilot_name_keyword: str, ship_name_keywords: list[str], game_mode_keywords: list[str]) ->  tuple[str, str, str]:
        logging.info(f"[LOGFILE MONITOR] Validating: {self._logfile_with_path}") and self._verbose_logging

        self._file_position: int = 0

        last_pilot_name_event_line = None
        last_ship_name_event_line = None
        last_game_mode_event_line = None

        try:
            with open(self._logfile_with_path, 'r') as file:
                lines: list[str] = file.readlines()
                total_lines: int = file.tell()

            if total_lines != self._file_position:
                self._file_position = total_lines

            for line in lines:
                if pilot_name_keyword in line:
                    last_pilot_name_event_line = line

                for word in ship_name_keywords:
                    if word in line:
                        last_ship_name_event_line = line

                for word in game_mode_keywords:
                    if word in line:
                        last_game_mode_event_line = line

            self._is_validated = True
            self._last_read_date = get_date()

            self._lines = len(lines)

            logging.info(f"[LOGFILE MONITOR] Validation Complete") and self._verbose_logging

        except Exception as _:
            self._file_position = 0
            logging.error(f"[LOGFILE MONITOR] Can't read Log File: {self._logfile_with_path}")

        finally:
            return last_pilot_name_event_line, last_ship_name_event_line, last_game_mode_event_line

    async def has_rolled_over(self) -> bool:
        with open(self._logfile_with_path, 'r') as file:
            file.readlines()
            total_lines: int = file.tell()

            if self._file_position > total_lines:
                logging.debug(f"[LOGFILE MONITOR] LOGFILE HAS ROLLED OVER") and self._debug_logging
                return True

            return False

    async def get_new_lines(self) -> list[str]:
        with open(self._logfile_with_path, 'r') as file:
            file.seek(self._file_position)

            new_lines: list[str] = file.readlines()
            self._file_position = file.tell()

            self._last_read_date = get_date()
            self._lines += len(new_lines)

            return new_lines
