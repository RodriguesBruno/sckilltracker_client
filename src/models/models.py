from pydantic import BaseModel, Field

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
