import sys
import asyncio
import logging
import uvicorn
import traceback
import webbrowser
import multiprocessing
from pathlib import Path
from typing import Optional
from multiprocessing import Manager
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, WebSocketDisconnect, WebSocket, Form, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError

from config.config import ensure_config, write_config, read_logging_config
from src.client import SCClient
from src.connection_manager import ConnectionManager
from src.enums import RequestedAction
from src.logfile_monitor import LogFileMonitor
from src.logger import setup_logging
from src.models.models import (
    StatisticsData,
    TopVictim,
    TopVictimsTable,
    TopKiller,
    TopKillersTable,
    KillsGameMode,
    DamageTypeDistribution,
    Game,
    DB,
    ClientStatus,
    TriggerControllerStatus,
    LoggingStatus,
    ClientEnabledStatus,
    RecordingsControllerStatus,
    OverlayStatus
)
from src.overlay import OverlayPosition, OverlayColor
from src.overlay_controller import OverlayController
from src.recordings_controller import RecordingsController
from src.repository import Repository, RepositoryType
from src.repository_factory import RepositoryFactory
from src.settings_form import SettingsForm
from src.sound_controller import SoundController
from src.splash_screen import show_splash_screen
from src.statistics_controller import StatisticsController
from src.system_tray import hide_system_tray_console, setup_system_tray
from src.trigger_controller import TriggerController
from src.utils import get_local_ip, resource_path, setup_folders


def log_exception(exc_type, exc_value, exc_tb):
    with open("sckilltracker_client_error.log", "w", encoding="utf-8") as f:
        traceback.print_exception(exc_type, exc_value, exc_tb, file=f)

sys.excepthook = log_exception

sc_client: Optional[SCClient] = None
position_value = None
color_value = None
font_size_value = None
overlay_queue = None

setup_folders()

config_logging: dict = read_logging_config()
setup_logging(config=config_logging)

config: dict = ensure_config()


@asynccontextmanager
async def lifespan(app: FastAPI):
    from src.overlay import run_overlay

    overlay_proc = multiprocessing.Process(
        target=run_overlay,
        args=(
            position_value,
            color_value,
            font_size_value,
            overlay_queue
        ),
    )
    overlay_proc.start()

    asyncio.create_task(sc_client.run(broadcast=connection_manager.broadcast))

    try:
        yield

    finally:
        overlay_proc.terminate()
        overlay_proc.join()


static_dir = resource_path("static")
templates_dir = resource_path("templates")

title: str = config.get('title')
recordings_path: Path = Path(config.get('recordings_controller').get('path'))

app: FastAPI = FastAPI(title=f"{title} API", openapi_url="/openapi.json", lifespan=lifespan)
app.mount("/static", StaticFiles(directory=static_dir), name="static")
templates = Jinja2Templates(directory=templates_dir)

connection_manager: ConnectionManager = ConnectionManager()

MAX_ENTRIES: int = 15

logfile_monitor: LogFileMonitor = LogFileMonitor(config=config.get('log_monitor'))

repo: Repository = RepositoryFactory().get_repo(
    repository_type=RepositoryType.SQL
    if config.get('db').get('type') == 'sql'
    else RepositoryType.CSV
)

statistics_controller: StatisticsController = StatisticsController()

trigger_controller: TriggerController = TriggerController(config=config.get('trigger_controller'))

recordings_controller: RecordingsController = RecordingsController(config=config.get('recordings_controller'))

overlay_controller: OverlayController = OverlayController(config=config.get('overlay'))

sound_controller: SoundController = SoundController(config=config.get('sound_controller'))

protocol: str = "wss" if (Path("certs/cert.pem").exists() and Path("certs/key.pem").exists()) else "ws"
ws_url: str = f'{protocol}://{get_local_ip()}:{config.get("local_api").get("port")}/ws'


def update_overlay_controller_config_and_save():
    config['overlay'] = overlay_controller.get_config()
    write_config(data=config)


def update_recordings_controller_config_and_save():
    config['recordings_controller'] = recordings_controller.get_config()
    write_config(data=config)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await connection_manager.connect(websocket=websocket)
    try:
        while True:
            _ = await websocket.receive_text()

    except WebSocketDisconnect:
        connection_manager.disconnect(websocket)

    except Exception as e:
        logging.warning(f"WebSocket error: {e}")


@app.get("/notification")
async def notification():
    return await sc_client.text_notification(broadcast=connection_manager.broadcast)


@app.get("/videos/static/{filename}")
async def serve_video(filename: str):
    video_path: Path = recordings_controller.path / filename

    if video_path.exists():
        return FileResponse(video_path)
    else:
        raise HTTPException(status_code=404, detail="File not found")


@app.get("/")
async def index_page(request: Request):
    player_events = reversed(sc_client.player_events())

    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": title,
        "version": sc_client.version,
        "client_enabled": sc_client.is_enabled,
        "game_is_running": sc_client.game_is_running,
        "game_is_running_last_checked": sc_client.game_is_running_last_checked,
        "pilot_name": sc_client.pilot_name,
        "pilot_icon_url": sc_client.pilot_icon_url,
        "pilot_org_name": sc_client.pilot_org_name,
        "pilot_org_icon_url": sc_client.pilot_org_icon_url,
        "ship_name": sc_client.ship_name,
        "game_mode": sc_client.game_mode,
        "player_events": player_events,
        "startup_date": sc_client.startup_date,
        "logfile_date": logfile_monitor.last_read_date,
        "max_entries": MAX_ENTRIES,
        "logfile_frequency": logfile_monitor.frequency,
        "trigger_controller_enabled": trigger_controller.is_enabled,
        "overlay": overlay_controller.get_config(),
        "verbose_logging": sc_client.is_verbose_logging,
        "track_crash_deaths": sc_client.track_crash_deaths,
        "player_month_statistics": sc_client.statistics_for_pilot_this_month(),
        "recordings_qty": sc_client.recordings_video_files_quantity(),
        "latest_recordings": sc_client.recordings_latest_videos(qty=1),
        "recording_controller": recordings_controller.get_config(),
        "ws_url": ws_url
    })


@app.get("/statistics")
def statistics_page(request: Request):
    return templates.TemplateResponse("statistics.html", {
        "request": request,
        "title": title,
        "version": sc_client.version
    })


@app.get("/global")
def global_page(request: Request):
    return templates.TemplateResponse("global.html", {
        "request": request,
        "title": title,
        "version": sc_client.version
    })


@app.get("/statistics/timeline")
def statistics_timeline(period: str = "month"):
    try:
        player_name: str = sc_client.pilot_name
        return JSONResponse({"series": statistics_controller.kills_deaths_timeline(player_name, period=period)})

    except Exception:
        return JSONResponse({"series": []})


@app.get("/statistics/ships")
def statistics_ships():
    try:
        player_name: str = sc_client.pilot_name

        return JSONResponse(
            {
                "most_killed_ships": statistics_controller.killer_ships_used(player_name=player_name),
                "most_dead_ships": statistics_controller.deaths_by_zone(player_name=player_name)
            }
        )

    except Exception:
        return JSONResponse({"most_killed_ships": [], "most_dead_ships": []})


@app.get("/statistics/orgs")
def statistics_orgs():
    try:
        player_name: str = sc_client.pilot_name

        return JSONResponse(
            {
                "top_victim_orgs": statistics_controller.top_victim_orgs(player_name),
                "top_killer_orgs": statistics_controller.top_killer_orgs(player_name)
            }
        )

    except Exception:
        return JSONResponse({"top_victim_orgs": [], "top_killer_orgs": []})


@app.get("/statistics/data", response_model=StatisticsData)
def statistics_data():
    damage_type_distribution: list[DamageTypeDistribution] = [
        DamageTypeDistribution(**entry)
        for entry in
        sc_client.statistics_damage_type_distribution()
    ]

    return StatisticsData(
        top_victims=[TopVictim(**entry) for entry in sc_client.statistics_top_victims()],
        top_victims_table=[TopVictimsTable(**entry) for entry in sc_client.statistics_top_victims_table()],
        top_killers=[TopKiller(**entry) for entry in sc_client.statistics_top_killers()],
        top_killers_table=[TopKillersTable(**entry) for entry in sc_client.statistics_top_killers_table()],
        kills_by_game_mode=[KillsGameMode(**entry) for entry in sc_client.statistics_kills_by_game_mode()],
        damage_type_distribution=damage_type_distribution,
        player_month_statistics=sc_client.statistics_for_pilot_this_month(),
        player_kills_deaths_by_period=sc_client.statistics_kills_deaths_by_period()
    )


@app.get("/status", response_model=ClientStatus)
async def get_status():
    return ClientStatus(
        title=title,
        startup_date=sc_client.startup_date,
        game=Game(
            executable_name=sc_client.game_executable_name,
            is_running=sc_client.game_is_running
        ),
        db=DB(
            type=repo.type,
            records_qty=repo.count
        )
    )


@app.get("/client/{action}", response_model=ClientEnabledStatus)
async def control_client(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        sc_client.enable()
    else:
        sc_client.disable()
    
    config['client'] = sc_client.get_config()
    write_config(data=config)
    return ClientEnabledStatus(is_enabled=sc_client.is_enabled)


@app.get("/trigger_controller/{action}")
async def control_trigger_controller(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        trigger_controller.enable()
    else:
        trigger_controller.disable()
        
    config['trigger_controller'] = trigger_controller.get_config()
    write_config(data=config)
    return TriggerControllerStatus(
        enabled=trigger_controller.is_enabled,
        selected_vendor=trigger_controller.selected_vendor
    )

@app.get("/recordings_controller/suicide/{action}", response_model=RecordingsControllerStatus)
async def recordings_controller_on_suicide(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        recordings_controller.record_suicide_enable()
    else:
        recordings_controller.record_suicide_disable()
        
    update_recordings_controller_config_and_save()
    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/own_death/{action}", response_model=RecordingsControllerStatus)
async def recordings_controller_on_own_death(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        recordings_controller.record_own_death_enable()
    else:
        recordings_controller.record_own_death_disable()
        
    update_recordings_controller_config_and_save()
    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/pu/{action}", response_model=RecordingsControllerStatus)
async def recordings_controller_on_pu(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        recordings_controller.record_pu_enable()
    else:
        recordings_controller.record_pu_disable()
        
    update_recordings_controller_config_and_save()
    return RecordingsControllerStatus(**recordings_controller.get_config())

@app.get("/recordings_controller/gun_rush/{action}", response_model=RecordingsControllerStatus)
async def recordings_controller_on_gun_rush(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        recordings_controller.record_gun_rush_enable()
    else:
        recordings_controller.record_gun_rush_disable()
        
    update_recordings_controller_config_and_save()
    return RecordingsControllerStatus(**recordings_controller.get_config())

@app.get("/recordings_controller/squadron_battle/{action}", response_model=RecordingsControllerStatus)
async def recordings_controller_on_squadron_battle(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        recordings_controller.record_squadron_battle_enable()
    else:
        recordings_controller.record_squadron_battle_disable()
        
    update_recordings_controller_config_and_save()
    return RecordingsControllerStatus(**recordings_controller.get_config())

@app.get("/recordings_controller/arena_commander/{action}", response_model=RecordingsControllerStatus)
async def recordings_controller_on_arena_commander(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        recordings_controller.record_arena_commander_enable()
    else:
        recordings_controller.record_arena_commander_disable()
        
    update_recordings_controller_config_and_save()
    return RecordingsControllerStatus(**recordings_controller.get_config())

@app.get("/recordings_controller/classic_race/{action}", response_model=RecordingsControllerStatus)
async def recordings_controller_on_classic_race(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        recordings_controller.record_classic_race_enable()
    else:
        recordings_controller.record_classic_race_disable()

    update_recordings_controller_config_and_save()
    return RecordingsControllerStatus(**recordings_controller.get_config())

@app.get("/recordings_controller/battle_royale/{action}", response_model=RecordingsControllerStatus)
async def recordings_controller_on_battle_royale(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        recordings_controller.record_battle_royale_enable()
    else:
        recordings_controller.record_battle_royale_disable()

    update_recordings_controller_config_and_save()
    return RecordingsControllerStatus(**recordings_controller.get_config())

@app.get("/recordings_controller/free_flight/{action}", response_model=RecordingsControllerStatus)
async def recordings_controller_on_free_flight(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        recordings_controller.record_free_flight_enable()
    else:
        recordings_controller.record_free_flight_disable()

    update_recordings_controller_config_and_save()
    return RecordingsControllerStatus(**recordings_controller.get_config())

@app.get("/recordings_controller/pirate_swarm/{action}", response_model=RecordingsControllerStatus)
async def recordings_controller_on_pirate_swarm(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        recordings_controller.record_pirate_swarm_enable()
    else:
        recordings_controller.record_pirate_swarm_disable()

    update_recordings_controller_config_and_save()
    return RecordingsControllerStatus(**recordings_controller.get_config())

@app.get("/recordings_controller/vanduul_swarm/{action}", response_model=RecordingsControllerStatus)
async def recordings_controller_on_vanduul_swarm(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        recordings_controller.record_vanduul_swarm_enable()
    else:
        recordings_controller.record_vanduul_swarm_disable()

    update_recordings_controller_config_and_save()
    return RecordingsControllerStatus(**recordings_controller.get_config())

@app.get("/recordings_controller/other/{action}", response_model=RecordingsControllerStatus)
async def recordings_controller_other_enable(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        recordings_controller.record_other_enable()
    else:
        recordings_controller.record_other_disable()

    update_recordings_controller_config_and_save()
    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings")
async def recordings_page(request: Request):
    return templates.TemplateResponse("recordings.html", {
        "request": request,
        "title": title,
        "version": sc_client.version,
        "video_files": sc_client.recordings_video_files()
    })


@app.post("/recordings_controller/rename_video")
async def rename_video(old_name: str = Form(...), new_name: str = Form(...)):
    if not '.mp4' in new_name:
        new_name = f"{new_name}.mp4"

    sc_client.recordings_rename_video(old_name=old_name, new_name=new_name)

    return RedirectResponse(url="/recordings", status_code=303)


@app.post("/recordings_controller/delete_video")
async def delete_video(filename: str = Form(...)):
    sc_client.recordings_delete_video(filename=filename)

    return RedirectResponse(url="/recordings", status_code=303)

@app.get("/overlay/{action}", response_model=OverlayStatus)
async def control_overlay(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_controller.enable()
    else:
        overlay_controller.disable()

    update_overlay_controller_config_and_save()
    return OverlayStatus(is_enabled=overlay_controller.is_enabled)

@app.get("/overlay/suicide/{action}", response_model=OverlayStatus)
async def overlay_on_suicide(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_controller.on_suicide_enable()
    else:
        overlay_controller.on_suicide_disable()

    update_overlay_controller_config_and_save()
    return OverlayStatus(is_enabled=overlay_controller.on_suicide)


@app.get("/overlay/own_death/{action}", response_model=OverlayStatus)
async def overlay_on_own_death(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_controller.on_own_death_enable()
    else:
        overlay_controller.on_own_death_disable()

    update_overlay_controller_config_and_save()
    return OverlayStatus(is_enabled=overlay_controller.on_own_death)


@app.get("/overlay/pu/{action}", response_model=OverlayStatus)
async def overlay_on_pu(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_controller.on_pu_enable()
    else:
        overlay_controller.on_pu_disable()

    update_overlay_controller_config_and_save()
    return OverlayStatus(is_enabled=overlay_controller.on_pu)

@app.get("/overlay/gun_rush/{action}", response_model=OverlayStatus)
async def overlay_on_gun_rush(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_controller.on_gun_rush_enable()
    else:
        overlay_controller.on_gun_rush_disable()

    update_overlay_controller_config_and_save()
    return OverlayStatus(is_enabled=overlay_controller.on_gun_rush)


@app.get("/overlay/squadron_battle/{action}", response_model=OverlayStatus)
async def overlay_on_squadron_battle(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_controller.on_squadron_battle_enable()
    else:
        overlay_controller.on_squadron_battle_disable()

    update_overlay_controller_config_and_save()
    return OverlayStatus(is_enabled=overlay_controller.on_squadron_battle)

@app.get("/overlay/arena_commander/{action}", response_model=OverlayStatus)
async def overlay_on_arena_commander(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_controller.on_arena_commander_enable()
    else:
        overlay_controller.on_arena_commander_disable()

    update_overlay_controller_config_and_save()
    return OverlayStatus(is_enabled=overlay_controller.on_arena_commander)

@app.get("/overlay/classic_race/{action}", response_model=OverlayStatus)
async def overlay_on_classic_race(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_controller.on_classic_race_enable()
    else:
        overlay_controller.on_classic_race_disable()

    update_overlay_controller_config_and_save()
    return OverlayStatus(is_enabled=overlay_controller.on_classic_race)

@app.get("/overlay/battle_royale/{action}", response_model=OverlayStatus)
async def overlay_on_battle_royale(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_controller.on_battle_royale_enable()
    else:
        overlay_controller.on_battle_royale_disable()

    update_overlay_controller_config_and_save()
    return OverlayStatus(is_enabled=overlay_controller.on_battle_royale)

@app.get("/overlay/free_flight/{action}", response_model=OverlayStatus)
async def overlay_on_free_flight(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_controller.on_free_flight_enable()
    else:
        overlay_controller.on_free_flight_disable()

    update_overlay_controller_config_and_save()
    return OverlayStatus(is_enabled=overlay_controller.on_free_flight)

@app.get("/overlay/pirate_swarm/{action}", response_model=OverlayStatus)
async def overlay_on_pirate_swarm(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_controller.on_pirate_swarm_enable()
    else:
        overlay_controller.on_pirate_swarm_disable()

    update_overlay_controller_config_and_save()
    return OverlayStatus(is_enabled=overlay_controller.on_pirate_swarm)

@app.get("/overlay/vanduul_swarm/{action}", response_model=OverlayStatus)
async def overlay_on_vanduul_swarm(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_controller.on_vanduul_swarm_enable()
    else:
        overlay_controller.on_vanduul_swarm_disable()

    update_overlay_controller_config_and_save()
    return OverlayStatus(is_enabled=overlay_controller.on_vanduul_swarm)

@app.get("/overlay/other/{action}", response_model=OverlayStatus)
async def overlay_on_other(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_controller.on_other_enable()
    else:
        overlay_controller.on_other_disable()

    update_overlay_controller_config_and_save()
    return OverlayStatus(is_enabled=overlay_controller.on_other)

@app.get("/verbose_logging/enable", response_model=LoggingStatus)
async def enable_verbose_logging():
    if not sc_client.is_verbose_logging:
        sc_client.verbose_logging_enable()
        config['client'] = sc_client.get_config()

        write_config(data=config)

    return LoggingStatus(is_verbose=sc_client.is_verbose_logging)


@app.get("/verbose_logging/disable", response_model=LoggingStatus)
async def disable_verbose_logging():
    if sc_client.is_verbose_logging:
        sc_client.verbose_logging_disable()
        config['client'] = sc_client.get_config()

        write_config(data=config)

    return LoggingStatus(is_verbose=sc_client.is_verbose_logging)

@app.get("/crash_tracking/{action}")
async def toggle_crash_tracking(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        sc_client.enable_track_crash_deaths()
    else:
        sc_client.disable_track_crash_deaths()

    config['client'] = sc_client.get_config()
    write_config(data=config)
    return JSONResponse({"track_crash_deaths": sc_client.track_crash_deaths})

@app.get("/settings")
async def settings_page(request: Request):
    return templates.TemplateResponse("settings.html", {
        "request": request,
        "title": title,
        "version": sc_client.version,
        "config": config,
        "overlay_positions": [entry.value for entry in OverlayPosition],
        "overlay_font_colors": [entry.value for entry in OverlayColor],
        "overlay_font_sizes": list(range(5, 31))

    })

@app.post("/settings")
async def update_settings(
    request: Request,
    local_api_ip_address: str = Form(...),
    local_api_port: str = Form(...),
    api_url: str = Form(...),
    logfile: str = Form(...),
    frequency: str = Form(...),
    gpu_vendor: str = Form(...),
    hotkey_combo: str = Form(None),
    video_folder_path: str = Form(...),
    overlay_position: str = Form(...),
    overlay_font_color: str = Form(...),
    overlay_font_size: str = Form(...),
    overlay_kill_streak: bool = Form(...),
    enable_kill_sounds: bool = Form(...),
    volume: float = Form(...),
    rename_files: bool = Form(...),
    trigger_delay: int = Form(...),

):
    try:
        form_data = SettingsForm(
            local_api_ip_address=local_api_ip_address,
            local_api_port=int(local_api_port),
            api_url=api_url,
            logfile=logfile,
            frequency=int(frequency),
            overlay_position=overlay_position,
            overlay_font_color=overlay_font_color,
            overlay_font_size=int(overlay_font_size),
            trigger_delay=int(trigger_delay)
        )

    except ValidationError as e:
        return templates.TemplateResponse(
            "settings.html",
            {
                "request": request,
                "config": config,
                "errors": e.errors(),
                "overlay_positions": [entry.value for entry in OverlayPosition],
                "overlay_font_colors": [entry.value for entry in OverlayColor],
                "overlay_font_sizes": list(range(5, 31)),
            },
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    # Update all config fields
    config["local_api"]["ip_address"] = local_api_ip_address
    config["local_api"]["port"] = int(local_api_port)
    config["client"]["api_url"] = api_url
    sc_client.api_url = api_url

    # Log Monitor settings
    logfile_monitor.logfile_with_path = logfile
    logfile_monitor.frequency = int(frequency)
    await sc_client.validate_logfile()
    config["log_monitor"] = logfile_monitor.get_config()

    # Recordings Controller settings
    await recordings_controller.set_path(path=video_folder_path)
    recordings_controller.rename_files = rename_files
    config["recordings_controller"] = recordings_controller.get_config()

    # Trigger Controller settings
    trigger_controller.set_overlay(gpu_vendor=gpu_vendor, hotkey=hotkey_combo)
    trigger_controller.set_delay(seconds=trigger_delay)
    config["trigger_controller"] = trigger_controller.get_config()

    # Overlay Controller settings
    overlay_controller.position = overlay_position
    overlay_controller.font_color = overlay_font_color
    overlay_controller.font_size = overlay_font_size
    overlay_controller.on_kill_streak = overlay_kill_streak
    config["overlay"] = overlay_controller.get_config()

    # Sound Controller settings
    sound_controller.kill_sounds_enabled = enable_kill_sounds
    sound_controller.volume = volume
    config["sound_controller"] = sound_controller.get_config()

    # ✅ Save updated config
    write_config(data=config)

    return RedirectResponse(url="/settings", status_code=303)


def main() -> None:
    hide_system_tray_console()

    global position_value, color_value, font_size_value, overlay_queue, sc_client

    manager = Manager()
    overlay_queue = manager.Queue()

    # Initialize once from overlay_controller (single source of truth)
    position_value = manager.Value("u", overlay_controller.position)
    color_value = manager.Value("u", overlay_controller.font_color)
    font_size_value = manager.Value("u", overlay_controller.font_size)

    sc_client = SCClient(
        config=config.get('client'),
        logfile_monitor=logfile_monitor,
        repo=repo,
        statistics_controller=statistics_controller,
        trigger_controller=trigger_controller,
        recordings_controller=recordings_controller,
        overlay_controller=overlay_controller,
        sound_controller=sound_controller,
        overlay_queue=overlay_queue
    )

    host: str = config.get("local_api").get("ip_address")
    port: int = config.get("local_api").get("port")

    cert_path: Path = Path("certs/cert.pem")
    key_path: Path = Path("certs/key.pem")

    hostname: str = "localhost" if host == "0.0.0.0" else host
    protoc: str = "https" if cert_path.exists() and key_path.exists() else "http"
    url: str = f"{protoc}://{hostname}:{port}"

    setup_system_tray(app_url=url)

    show_splash_screen(duration=3)
    webbrowser.open(url)

    if not cert_path.exists() or not key_path.exists():
        logging.info("⚠️ Certificate files not found. HTTPS will not be enabled.")
        uvicorn.run(app=app, host=host, port=port)

    else:
        logging.info("✅ Starting API with HTTPS")
        uvicorn.run(
            app=app,
            host=host,
            port=port,
            ssl_certfile=str(cert_path),
            ssl_keyfile=str(key_path)
        )

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()