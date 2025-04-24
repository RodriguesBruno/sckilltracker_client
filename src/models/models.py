from pydantic import BaseModel, Field

from src.repository import RepositoryType


class PlayerEvent(BaseModel):
    uuid: str
    date: str
    victim_player_name: str
    victim_zone_name: str

    killed_by: str
    ship_name: str = Field(default='-')

    using: str
    damage: str
    game_mode: str = Field(default='-')

    client_enabled: bool = Field(default=False)
    push_result_message: str = Field(default='-')
    push_result_is_success: bool = Field(default=False)

class GameNotification(BaseModel):
    pilot_name: str
    month: str
    pilot_kills: int
    pilot_deaths: int
    pilot_suicides: int
    pilot_kdr: float = Field(default=0)

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
    victim_player_name: str
    count: int

class TopVictimsTable(BaseModel):
    victim: str
    day: int
    week: int
    month: int
    all: int

class TopKiller(BaseModel):
    killed_by: str
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
    pilot_month_kills: PilotMonthKills

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