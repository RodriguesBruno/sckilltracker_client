from typing import Any

from pydantic import BaseModel, Field

from src.repository import RepositoryType


class Organization(BaseModel):
    name: str = Field(default='-')
    url: str = Field(default='-')
    icon_url: str = Field(default='-')
    rank: str = Field(default='-')


class PlayerProfile(BaseModel):
    name: str = Field(default='-')
    icon_url: str = Field(default='-')
    enlisted_date: str = Field(default='-')
    location: str = Field(default='-')
    fluency: str = Field(default='-')
    org: Organization = Field(default=Organization())


class PlayerMonthStatistics(BaseModel):
    player_name: str
    month: str
    kills: int
    deaths: int
    suicides: int
    kdr: float = Field(default=0)


class PlayerEvent(BaseModel):
    uuid: str
    date: str
    victim_profile: PlayerProfile

    victim_zone_name: str

    killer_profile: PlayerProfile

    ship_name: str = Field(default='-')

    using: str
    damage: str
    game_mode: str = Field(default='-')

    client_enabled: bool = Field(default=False)
    push_result_message: str = Field(default='-')
    push_result_is_success: bool = Field(default=False)


class GameNotification(BaseModel):
    player_profile: PlayerProfile
    player_statistics: PlayerMonthStatistics

    ship_name: str
    game_mode: str


class LogFileNotification(BaseModel):
    logfile_frequency: int
    logfile_msg: str
    logfile_scanner_is_running: bool


class GameExecutableNotification(BaseModel):
    date: str
    game_is_running: bool
    msg: str


class RecordingNotification(BaseModel):
    recordings_qty: int
    latest_video_filename: str


class TopVictim(BaseModel):
    victim_name: str
    count: int


class TopVictimsTable(BaseModel):
    victim: str
    day: int
    week: int
    month: int
    all: int


class TopKiller(BaseModel):
    killer_name: str
    count: int


class TopKillersTable(BaseModel):
    killer: str
    day: int
    week: int
    month: int
    all: int


class KillsGameMode(BaseModel):
    game_mode: str
    count: int


class DamageTypeDistribution(BaseModel):
    damage: str
    count: int


class PilotMonthKills(BaseModel):
    month: str
    kills: int
    suicides: int
    deaths: int
    pilot: str


class StatisticsData(BaseModel):
    top_victims: list[TopVictim]
    top_victims_table: list[TopVictimsTable]
    top_killers: list[TopKiller]
    top_killers_table: list[TopKillersTable]
    kills_by_game_mode: list[KillsGameMode]
    damage_type_distribution: list[DamageTypeDistribution]
    player_month_statistics: PlayerMonthStatistics
    player_kills_deaths_by_period: dict[str, Any]


class Game(BaseModel):
    executable_name: str
    is_running: bool


class DB(BaseModel):
    type: RepositoryType
    records_qty: int


class ClientStatus(BaseModel):
    title: str
    startup_date: str
    game: Game
    db: DB


class ClientEnabledStatus(BaseModel):
    is_enabled: bool


class TriggerControllerStatus(BaseModel):
    enabled: bool
    selected_vendor: str


class LoggingStatus(BaseModel):
    is_verbose: bool


class OverlayStatus(BaseModel):
    is_enabled: bool


class RecordingsControllerStatus(BaseModel):
    path: str
    record_suicide: bool
    record_own_death: bool
    record_pu: bool
    record_gun_rush: bool
    record_squadron_battle: bool
    record_arena_commander: bool
    record_classic_race: bool
    record_battle_royale: bool
    record_free_flight: bool
    record_pirate_swarm: bool
    record_vanduul_swarm: bool
    record_other: bool


class PilotProfile(BaseModel):
    name: str
    org: str
    org_url: str
    enlisted_date: str
    location: str


class OverlayControllerStatus(BaseModel):
    on_suicide: bool
    on_own_death: bool
    on_pu: bool
    on_gun_rush: bool
    on_squadron_battle: bool
    on_arena_commander: bool
    on_classic_race: bool
    on_battle_royale: bool
    on_free_flight: bool
    on_pirate_swarm: bool
    ron_vanduul_swarm: bool
    on_other: bool
