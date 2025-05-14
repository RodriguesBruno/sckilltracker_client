import csv
import os

from src.models.models import PlayerEvent, PlayerProfile, Organization
from src.repository import Repository, RepositoryType

keys: list[str] = [
    "uuid",
    "date",
    "victim_name",
    "victim_name_icon_url",
    "victim_org",
    "victim_org_rank",
    "victim_org_url",
    "victim_org_icon_url",
    "victim_enlisted_date",
    "victim_fluency",

    "victim_location",


    "victim_zone_name",

    "killer_name",
    "killer_name_icon_url",
    "killer_org",
    "killer_org_rank",
    "killer_org_url",
    "killer_org_icon_url",
    "killer_enlisted_date",
    "killer_location",
    "killer_fluency",

    "ship_name",
    "using",
    "damage",
    "game_mode",
    "client_enabled",
    "push_result_message",
    "push_result_is_success"
]

def player_event_to_csv_adapter(event: PlayerEvent) -> dict:
    return {
        "uuid": event.uuid,
        "date": event.date,
        "victim_name": event.victim_profile.name,
        "victim_name_icon_url": event.victim_profile.icon_url,
        "victim_org": event.victim_profile.org.name,
        "victim_org_rank": event.victim_profile.org.rank,
        "victim_org_url": event.victim_profile.org.url,
        "victim_org_icon_url": event.victim_profile.org.icon_url,
        "victim_enlisted_date": event.victim_profile.enlisted_date,
        "victim_location": event.victim_profile.location,
        "victim_fluency": event.victim_profile.fluency,

        "victim_zone_name": event.victim_zone_name,

        "killer_name": event.killer_profile.name,
        "killer_name_icon_url": event.killer_profile.icon_url,
        "killer_org": event.killer_profile.org.name,
        "killer_org_rank": event.killer_profile.org.rank,
        "killer_org_url": event.killer_profile.org.url,
        "killer_org_icon_url": event.killer_profile.org.icon_url,
        "killer_enlisted_date": event.killer_profile.enlisted_date,
        "killer_location": event.killer_profile.location,
        "killer_fluency": event.killer_profile.fluency,

        "ship_name": event.ship_name,
        "using": event.using,
        "damage": event.damage,
        "game_mode": event.game_mode,
        "client_enabled": event.client_enabled,
        "push_result_message": event.push_result_message,
        "push_result_is_success": event.push_result_is_success
    }

def csv_to_player_event_adapter(entry: dict) -> PlayerEvent:
    return PlayerEvent(
        uuid=entry["uuid"],
        date=entry["date"],
        victim_profile=PlayerProfile(
            name=entry["victim_name"],
            icon_url=entry["victim_name_icon_url"],
            enlisted_date=entry["victim_enlisted_date"],
            location=entry["victim_location"],
            fluency=entry["victim_fluency"],
            org=Organization(
                name=entry["victim_org"],
                url=entry["victim_org_url"],
                icon_url=entry["victim_org_icon_url"],
                rank=entry["victim_org_rank"]
            ),
        ),

        victim_zone_name=entry["victim_zone_name"],

        killer_profile=PlayerProfile(
            name=entry["killer_name"],
            icon_url=entry["killer_name_icon_url"],
            enlisted_date=entry["killer_enlisted_date"],
            location=entry["killer_location"],
            fluency=entry["killer_fluency"],
            org = Organization(
                name=entry["killer_org"],
                url=entry["killer_org_url"],
                icon_url=entry["killer_org_icon_url"],
                rank=entry["killer_org_rank"]
            ),
        ),
        ship_name=entry["ship_name"],
        using=entry["using"],
        damage=entry["damage"],
        game_mode=entry["game_mode"],
        client_enabled=entry["client_enabled"],
        push_result_message=entry["push_result_message"],
        push_result_is_success=entry["push_result_is_success"]
    )


class CSVRepository(Repository):
    def __init__(self, path: str) -> None:
        self._file_name: str = path
        self._key_names: list[str] = keys
        self._encoding: str = 'utf-8'
        self._initialize()


    def _initialize(self) -> None:
        write_header = not os.path.exists(self._file_name) or os.stat(self._file_name).st_size == 0
        if write_header:
            with open(self._file_name, 'w', newline='', encoding=self._encoding) as f:
                writer = csv.DictWriter(f, fieldnames=self._key_names)
                writer.writeheader()

    @property
    def type(self) -> RepositoryType:
        return RepositoryType.CSV

    @property
    def count(self) -> int:
        with open(self._file_name, newline='', encoding=self._encoding) as f:
            reader = csv.DictReader(f)
            return sum(1 for _ in reader)

    @property
    def file_name(self) -> str:
        return self._file_name

    def create(self, entries: list[dict]):
        with open(self._file_name, 'a', newline='', encoding=self._encoding) as f:
            writer = csv.DictWriter(f, fieldnames=self._key_names)
            for e in entries:
                writer.writerow({key: e.get(key) for key in self._key_names})

    def read(self) -> list[dict]:
        with open(self._file_name, newline='', encoding=self._encoding) as f:
            reader = csv.DictReader(f)

            result = []

            for row in reader:
                parsed_row = {}
                for key in self._key_names:
                    value = row[key]
                    if key in ("client_enabled", "push_result_is_success"):
                        parsed_row[key] = value.strip().lower() == "true"
                    else:
                        parsed_row[key] = value

                result.append(parsed_row)

            return result

    def update(self):
        pass

    def delete(self):
        pass