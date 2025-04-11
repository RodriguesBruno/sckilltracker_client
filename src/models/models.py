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