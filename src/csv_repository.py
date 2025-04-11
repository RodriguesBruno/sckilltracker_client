import csv
import os

from src.repository import Repository


class CSVRepository(Repository):
    def __init__(self, file_name: str):
        self._file_name = file_name
        self._field_names: list[str] = ['date', 'victim_player_name', 'victim_zone_name', 'killed_by', 'ship_name', 'using', 'damage', 'game_mode']
        self._initialize()

    def _initialize(self):
        write_header = not os.path.exists(self._file_name) or os.stat(self._file_name).st_size == 0
        if write_header:
            with open(self._file_name, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self._field_names)
                writer.writeheader()

    @property
    def file_name(self) -> str:
        return self._file_name

    def create(self, entries: list[dict]):
        with open(self._file_name, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self._field_names)
            for e in entries:
                writer.writerow({key: e.get(key) for key in self._field_names})

    def read(self):
        with open(self._file_name, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row)
                # print(row['first_name'], row['last_name'])

    def update(self):
        pass

    def delete(self):
        pass