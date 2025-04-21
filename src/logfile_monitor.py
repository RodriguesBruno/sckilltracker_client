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

    @log_is_validated.setter
    def log_is_validated(self, value: bool) -> None:
        self._is_validated = value

    @property
    def last_read_date(self) -> str:
        return self._last_read_date

    def reset(self) -> None:
        self._is_validated = False
        self._file_position = 0

    def get_config(self) -> dict:
        return {
            "logfile_with_path": self._logfile_with_path,
            "frequency": self._frequency
        }

    async def validate_logfile(self, pilot_name_keyword: str, ship_name_keywords: list[str], game_mode_keywords: list[str]) ->  tuple[str, str, str]:
        logging.info(f"[LOGFILE MONITOR] Validating: {self._logfile_with_path}")

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

            logging.info(f"[LOGFILE MONITOR] Validation Complete")

        except Exception as _:
            self._file_position = 0
            logging.error(f"[LOGFILE MONITOR] Can't read Log File: {self._logfile_with_path}")

        finally:
            return last_pilot_name_event_line, last_ship_name_event_line, last_game_mode_event_line

    async def get_new_lines(self) -> list[str]:
        with open(self._logfile_with_path, 'r') as file:
            total_lines: int = file.tell()

            if self._file_position > total_lines:
                logging.info(f"[LOGFILE MONITOR] LOGFILE WAS RESET, RESETTING POSITION/LINES")
                self._file_position = 0
                self._lines = 0

            file.seek(self._file_position)

            new_lines: list[str] = file.readlines()
            self._file_position = file.tell()

            self._last_read_date = get_date()
            self._lines += len(new_lines)

            return new_lines
