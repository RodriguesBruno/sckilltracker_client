import webbrowser
from typing import Optional

import uvicorn
import asyncio
import multiprocessing
from multiprocessing import Manager
from contextlib import asynccontextmanager
import logging
from pathlib import Path
from fastapi import FastAPI, Request, WebSocketDisconnect, WebSocket, Form, status, HTTPException, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import ValidationError

from src.client import SCClient
from src.connection_manager import ConnectionManager
from src.file_handlers import read_config, write_config
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
from src.recordings_controller import RecordingsController
from src.statistics_controller import StatisticsController
from src.trigger_controller import TriggerController
from src.repository import Repository, RepositoryType
from src.repository_factory import RepositoryFactory
from src.settings_form import SettingsForm
from src.utils import get_local_ip, resource_path, setup_folders

sc_client: Optional[SCClient] = None
position_value = None
color_value = None
font_size_value = None
overlay_queue = None
overlay_enabled_value = None

setup_folders()

config_logging: dict = read_config(config_file='./config_logging.json')
setup_logging(config=config_logging)

config_file: str = "./config.json"
config: dict = read_config(config_file=config_file)


@asynccontextmanager
async def lifespan(app: FastAPI):
    from src.overlay import run_overlay

    overlay_proc = multiprocessing.Process(
        target=run_overlay,
        args=(
            position_value,
            color_value,
            font_size_value,
            overlay_enabled,
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



protocol: str = "wss" if (Path("certs/cert.pem").exists() and Path("certs/key.pem").exists()) else "ws"
ws_url: str = f'{protocol}://{get_local_ip()}:{config.get("local_api").get("port")}/ws'


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
        "overlay_enabled": overlay_enabled.value,
        "verbose_logging": sc_client.is_verbose_logging,
        "player_month_statistics": sc_client.statistics_for_pilot_this_month(),
        "recordings_qty": await sc_client.recordings_video_files_quantity(),
        "latest_recordings": await sc_client.recordings_latest_videos(qty=1),
        "recording_controller": recordings_controller.get_config(),
        "ws_url": ws_url,
    })


@app.get("/statistics")
def statistics_page(request: Request):
    return templates.TemplateResponse("statistics.html", {
        "request": request,
        "title": title,
        "version": sc_client.version
    })


@app.get("/statistics/data", response_model=StatisticsData)
def statistics_data():
    return StatisticsData(
        top_victims=[TopVictim(**entry) for entry in sc_client.statistics_top_victims()],
        top_victims_table=[TopVictimsTable(**entry) for entry in sc_client.statistics_top_victims_table()],
        top_killers=[TopKiller(**entry) for entry in sc_client.statistics_top_killers()],
        top_killers_table=[TopKillersTable(**entry) for entry in sc_client.statistics_top_killers_table()],
        kills_by_game_mode=[KillsGameMode(**entry) for entry in sc_client.statistics_kills_by_game_mode()],
        damage_type_distribution=[DamageTypeDistribution(**entry) for entry in sc_client.statistics_damage_type_distribution()],
        player_month_statistics=sc_client.statistics_for_pilot_this_month()
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


@app.get("/client/enable", response_model=ClientEnabledStatus)
async def enable_client():
    if sc_client.is_disabled:
        sc_client.enable()
        config['client'] = sc_client.get_config()

        write_config(config_file=config_file, data=config)

    return ClientEnabledStatus(is_enabled=sc_client.is_enabled)


@app.get("/client/disable", response_model=ClientEnabledStatus)
async def disable_client():
    if sc_client.is_enabled:
        sc_client.disable()
        config['client'] = sc_client.get_config()

        write_config(config_file=config_file, data=config)

    return ClientEnabledStatus(is_enabled=sc_client.is_enabled)


@app.get("/trigger_controller/enable")
async def enable_trigger_controller():
    if trigger_controller.is_disabled:
        trigger_controller.enable()
        config['trigger_controller'] = trigger_controller.get_config()

        write_config(config_file=config_file, data=config)

    return TriggerControllerStatus(
        enabled=trigger_controller.is_enabled,
        selected_vendor=trigger_controller.selected_vendor
    )


@app.get("/trigger_controller/disable", response_model=TriggerControllerStatus)
async def trigger_controller_disable():
    if trigger_controller.is_enabled:
        trigger_controller.disable()
        config['trigger_controller'] = trigger_controller.get_config()

        write_config(config_file=config_file, data=config)

    return TriggerControllerStatus(
        enabled=trigger_controller.is_enabled,
        selected_vendor=trigger_controller.selected_vendor
    )


@app.get("/recordings_controller/suicide/enable", response_model=RecordingsControllerStatus)
async def recordings_controller_suicide_enable():
    if not recordings_controller.is_record_suicide:
        recordings_controller.record_suicide_enable()
        config['recordings_controller'] = recordings_controller.get_config()

        write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/suicide/disable", response_model=RecordingsControllerStatus)
async def recordings_controller_suicide_disable():
    if recordings_controller.is_record_suicide:
        recordings_controller.record_suicide_disable()
        config['recordings_controller'] = recordings_controller.get_config()

        write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())

@app.get("/recordings_controller/own_death/enable", response_model=RecordingsControllerStatus)
async def recordings_controller_own_death_enable():
    if not recordings_controller.is_record_own_death:
        recordings_controller.record_own_death_enable()
        config['recordings_controller'] = recordings_controller.get_config()

        write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/own_death/disable", response_model=RecordingsControllerStatus)
async def recordings_controller_own_death_disable():
    if recordings_controller.is_record_own_death:
        recordings_controller.record_own_death_disable()
        config['recordings_controller'] = recordings_controller.get_config()

        write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/pu/enable", response_model=RecordingsControllerStatus)
async def recordings_controller_pu_enable():
    if not recordings_controller.is_record_pu:
        recordings_controller.record_pu_enable()
        config['recordings_controller'] = recordings_controller.get_config()

        write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/pu/disable", response_model=RecordingsControllerStatus)
async def recordings_controller_pu_disable():
    if recordings_controller.is_record_pu:
        recordings_controller.record_pu_disable()
        config['recordings_controller'] = recordings_controller.get_config()

        write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/gun_rush/enable", response_model=RecordingsControllerStatus)
async def recordings_controller_gun_rush_enable():
    if not recordings_controller.is_record_gun_rush:
        recordings_controller.record_gun_rush_enable()
        config['recordings_controller'] = recordings_controller.get_config()

        write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/gun_rush/disable", response_model=RecordingsControllerStatus)
async def recordings_controller_gun_rush_disable():
    if recordings_controller.is_record_gun_rush:
        recordings_controller.record_gun_rush_disable()
        config['recordings_controller'] = recordings_controller.get_config()

        write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/squadron_battle/enable", response_model=RecordingsControllerStatus)
async def recordings_controller_squadron_battle_enable():
    if not recordings_controller.is_record_squadron_battle:
        recordings_controller.record_squadron_battle_enable()
        config['recordings_controller'] = recordings_controller.get_config()

        write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/squadron_battle/disable", response_model=RecordingsControllerStatus)
async def recordings_controller_squadron_battle_disable():
    if recordings_controller.is_record_squadron_battle:
        recordings_controller.record_squadron_battle_disable()
        config['recordings_controller'] = recordings_controller.get_config()

        write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/arena_commander/enable", response_model=RecordingsControllerStatus)
async def recordings_controller_arena_commander_enable():
    if not recordings_controller.is_record_arena_commander:
        recordings_controller.record_arena_commander_enable()
        config['recordings_controller'] = recordings_controller.get_config()

        write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/arena_commander/disable", response_model=RecordingsControllerStatus)
async def recordings_controller_arena_commander_disable():
    if recordings_controller.is_record_arena_commander:
        recordings_controller.record_arena_commander_disable()
        config['recordings_controller'] = recordings_controller.get_config()

        write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/classic_race/enable", response_model=RecordingsControllerStatus)
async def recordings_controller_classic_race_enable():
    if not recordings_controller.is_record_classic_race:
        recordings_controller.record_classic_race_enable()
        config['recordings_controller'] = recordings_controller.get_config()

        write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/classic_race/disable", response_model=RecordingsControllerStatus)
async def recordings_controller_classic_race_disable():
    if recordings_controller.is_record_classic_race:
        recordings_controller.record_classic_race_disable()
        config['recordings_controller'] = recordings_controller.get_config()

        write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/battle_royale/enable", response_model=RecordingsControllerStatus)
async def recordings_controller_battle_royale_enable():
    if not recordings_controller.is_record_battle_royale:
        recordings_controller.record_battle_royale_enable()
        config['recordings_controller'] = recordings_controller.get_config()

        write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/battle_royale/disable", response_model=RecordingsControllerStatus)
async def recordings_controller_battle_royale_disable():
    if recordings_controller.is_record_battle_royale:
        recordings_controller.record_battle_royale_disable()
        config['recordings_controller'] = recordings_controller.get_config()

        write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/free_flight/enable", response_model=RecordingsControllerStatus)
async def recordings_controller_free_flight_enable():
    if not recordings_controller.is_record_free_flight:
        recordings_controller.record_free_flight_enable()
        config['recordings_controller'] = recordings_controller.get_config()

        write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/free_flight/disable", response_model=RecordingsControllerStatus)
async def recordings_controller_free_flight_disable():
    if recordings_controller.is_record_free_flight:
        recordings_controller.record_free_flight_disable()
        config['recordings_controller'] = recordings_controller.get_config()

        write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/pirate_swarm/enable", response_model=RecordingsControllerStatus)
async def recordings_controller_pirate_swarm_enable():
    if not recordings_controller.is_record_pirate_swarm:
        recordings_controller.record_pirate_swarm_enable()
        config['recordings_controller'] = recordings_controller.get_config()

        write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/pirate_swarm/disable", response_model=RecordingsControllerStatus)
async def recordings_controller_pirate_swarm_disable():
    if recordings_controller.is_record_pirate_swarm:
        recordings_controller.record_pirate_swarm_disable()
        config['recordings_controller'] = recordings_controller.get_config()

        write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/vanduul_swarm/enable", response_model=RecordingsControllerStatus)
async def recordings_controller_vanduul_swarm_enable():
    if not recordings_controller.is_record_vanduul_swarm:
        recordings_controller.record_vanduul_swarm_enable()
        config['recordings_controller'] = recordings_controller.get_config()

        write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/vanduul_swarm/disable", response_model=RecordingsControllerStatus)
async def recordings_controller_vanduul_swarm_disable():
    if recordings_controller.is_record_vanduul_swarm:
        recordings_controller.record_vanduul_swarm_disable()
        config['recordings_controller'] = recordings_controller.get_config()

        write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/other/enable", response_model=RecordingsControllerStatus)
async def recordings_controller_other_enable():
    if not recordings_controller.is_record_other:
        recordings_controller.record_other_enable()
        config['recordings_controller'] = recordings_controller.get_config()

        write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/other/disable", response_model=RecordingsControllerStatus)
async def recordings_controller_other_disable():
    if recordings_controller.is_record_other:
        recordings_controller.record_other_disable()
        config['recordings_controller'] = recordings_controller.get_config()

        write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings")
async def recordings_page(request: Request):
    return templates.TemplateResponse("recordings.html", {
        "request": request,
        "title": title,
        "version": sc_client.version,
        "video_files": await sc_client.recordings_video_files()
    })


@app.post("/recordings_controller/rename_video")
async def rename_video(old_name: str = Form(...), new_name: str = Form(...)):
    if not '.mp4' in new_name:
        new_name = f"{new_name}.mp4"

    await sc_client.recordings_rename_video(old_name=old_name, new_name=new_name)

    return RedirectResponse(url="/recordings", status_code=303)


@app.post("/recordings_controller/delete_video")
async def delete_video(filename: str = Form(...)):
    await sc_client.recordings_delete_video(filename=filename)

    return RedirectResponse(url="/recordings", status_code=303)


@app.get("/overlay/enable", response_model=OverlayStatus)
async def enable_overlay():
    if not overlay_enabled.value:
        overlay_enabled.value = True
        config['overlay']['enabled'] = True

        write_config(config_file=config_file, data=config)

    return OverlayStatus(
        is_enabled=overlay_enabled.value
    )


@app.get("/overlay/disable", response_model=OverlayStatus)
async def disable_overlay():
    if overlay_enabled.value:
        overlay_enabled.value = False
        config['overlay']['enabled'] = False

        write_config(config_file=config_file, data=config)

    return OverlayStatus(
        is_enabled=overlay_enabled.value
    )


@app.get("/verbose_logging/enable", response_model=LoggingStatus)
async def enable_verbose_logging():
    if not sc_client.is_verbose_logging:
        sc_client.verbose_logging_enable()
        config['client'] = sc_client.get_config()

        write_config(config_file=config_file, data=config)

    return LoggingStatus(
        is_verbose=sc_client.is_verbose_logging
    )


@app.get("/verbose_logging/disable", response_model=LoggingStatus)
async def disable_verbose_logging():
    if sc_client.is_verbose_logging:
        sc_client.verbose_logging_disable()
        config['client'] = sc_client.get_config()

        write_config(config_file=config_file, data=config)

    return LoggingStatus(
        is_verbose=sc_client.is_verbose_logging
    )


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
async def set_settings(
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
        overlay_font_size: str = Form(...)
    ):

    try:
        form_data = SettingsForm(
            local_api_ip_address=local_api_ip_address,
            local_api_port=local_api_port,
            api_url=api_url,
            logfile=logfile,
            frequency=frequency,
            overlay_position=overlay_position,
            overlay_font_color=overlay_font_color,
            overlay_font_size=overlay_font_size
        )

    except ValidationError as e:
        return templates.TemplateResponse(
            "settings.html",
            {
                "request": request,
                "config": {
                    "local_api": {
                        "ip_address": local_api_ip_address,
                        "port": local_api_port,
                    },
                    "client": {
                        "version": sc_client.version,
                        "enabled": sc_client.is_enabled,
                        "api_url": api_url
                    },
                    "log_monitor": {
                        "logfile_with_path": logfile,
                        "frequency": frequency,
                    },
                    "trigger_controller": trigger_controller.get_config(),
                    "recordings_controller": {
                        "path": recordings_controller.path
                    }
                },
                "errors": e.errors(),
            },
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    sc_client.api_url = str(form_data.api_url)

    if form_data.logfile != logfile_monitor.logfile_with_path:
        logfile_monitor.logfile_with_path = form_data.logfile
        logfile_monitor.reset()

        await sc_client.validate_logfile()


    logfile_monitor.frequency = int(form_data.frequency)

    trigger_controller.set_overlay(gpu_vendor=gpu_vendor, hotkey=hotkey_combo)

    if not len(video_folder_path):
        video_folder_path = "."

    await recordings_controller.set_path(path=Path(video_folder_path))

    config['local_api']['port'] = int(form_data.local_api_port)
    config['client'] = sc_client.get_config()
    config['log_monitor'] = logfile_monitor.get_config()
    config['trigger_controller'] = trigger_controller.get_config()
    config['recordings_controller'] = recordings_controller.get_config()

    config['overlay']['position'] = overlay_position
    position_value.value = overlay_position

    config['overlay']['font_color'] = overlay_font_color
    color_value.value = overlay_font_color

    config['overlay']['font_size'] = overlay_font_size
    font_size_value.value = str(overlay_font_size)


    write_config(config_file=config_file, data=config)

    return RedirectResponse(url="/settings", status_code=303)


@app.post("/overlay/position")
async def set_overlay_position(position: OverlayPosition = Query(...)):
    config['overlay']['position'] = position.value

    position_value.value = position.value
    write_config(config_file=config_file, data=config)

    return {
        "position": position.value
    }


@app.post("/overlay/color")
async def set_overlay_color(color: OverlayColor = Query(...)):
    config['overlay']['font_color'] = color.value

    color_value.value = color.value
    write_config(config_file=config_file, data=config)

    return {
        "font_color": color.value
    }


@app.post("/overlay/font_size")
async def set_overlay_font_size(font_size: int = Query(..., ge=5, le=30)):
    config['overlay']['font_size'] = font_size

    font_size_value.value = str(font_size)
    write_config(config_file=config_file, data=config)

    return {
        "font_size": font_size
    }


def main() -> None:
    global position_value, color_value, font_size_value, overlay_queue, sc_client, overlay_enabled

    manager = Manager()
    overlay_queue = manager.Queue()

    position_value = manager.Value("u", config.get("overlay").get("position"))
    color_value = manager.Value("u", config.get("overlay").get("font_color"))
    font_size_value = manager.Value("u", config.get("overlay").get("font_size"))
    overlay_enabled = manager.Value("b", config.get("overlay").get("enabled"))

    sc_client = SCClient(
        config=config.get('client'),
        logfile_monitor=logfile_monitor,
        repo=repo,
        statistics_controller=statistics_controller,
        trigger_controller=trigger_controller,
        recordings_controller=recordings_controller,
        overlay_queue=overlay_queue,
    )

    host: str = config.get("local_api").get("ip_address")
    port: int = config.get("local_api").get("port")

    cert_path: Path = Path("certs/cert.pem")
    key_path: Path = Path("certs/key.pem")

    hostname: str = "localhost" if host == "0.0.0.0" else host
    protoc: str = "https" if cert_path.exists() and key_path.exists() else "http"
    url: str = f"{protoc}://{hostname}:{port}"

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
