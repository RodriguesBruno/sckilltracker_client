from pydantic import BaseModel, Field

class PlayerEvent(BaseModel):
    date: str
    victim_player_name: str
    victim_zone_name: str

    killed_by: str
    ship_name: str = Field(default='-')

    using: str
    damage: str
    game_mode: str = Field(default='-')

class ClientEvent(BaseModel):
    client_id: str
    client_version: str
    player_event: PlayerEvent

class ClientConfig(BaseModel):
    enabled: bool
    api_url: str

class LogMonitorConfig(BaseModel):
    logfile_with_path: str
    frequency: int

class PushResult(BaseModel):
    is_success: bool = Field(default=True)
    message: str = Field(default='')

class Notification(BaseModel):
    player_event: PlayerEvent
    client_enabled: bool
    push_result: PushResult

class GameNotification(BaseModel):
    pilot_name: str
    pilot_kills: int
    month: str
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
    pilot: str


class StatisticsResult(BaseModel):
    top_victims: list[TopVictim]
    top_victims_table: list[TopVictimsTable]
    top_killers: list[TopKiller]
    top_killers_table: list[TopKillersTable]
    kills_by_game_mode: list[KillsGameMode]
    damage_type_distribution: list[DamageTypeDistribution]
    pilot_month_kills: PilotMonthKills
