#TRAY ICON
import threading
import pystray
from PIL import Image, ImageDraw
import ctypes
import os
##import signal
from pathlib import Path
#import sys
import psutil

#SLASH SCREEN
import tkinter as tk
from PIL import ImageTk, Image
import threading
import time


import webbrowser
from typing import Optional
import uvicorn
import asyncio
import multiprocessing
from multiprocessing import Manager
from contextlib import asynccontextmanager
import logging
from pathlib import Path
from fastapi import FastAPI, Request, WebSocketDisconnect, WebSocket, Form, status, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import ValidationError

from src.client import SCClient
from src.connection_manager import ConnectionManager
from src.enums import RequestedAction
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
from src.overlay_controller import OverlayController
from src.recordings_controller import RecordingsController
from src.statistics_controller import StatisticsController
from src.trigger_controller import TriggerController
from src.repository import Repository, RepositoryType
from src.repository_factory import RepositoryFactory
from src.settings_form import SettingsForm
from src.utils import get_local_ip, resource_path, setup_folders

sc_client: Optional[SCClient] = None
overlay_queue = None
position_value = None
color_value = None
font_size_value = None
overlay_enabled = None

overlay_on_suicide = None
overlay_on_own_death = None
overlay_on_pu = None
overlay_on_gun_rush = None
overlay_on_squadron_battle = None
overlay_on_arena_commander = None
overlay_on_classic_race = None
overlay_on_battle_royale = None
overlay_on_free_flight = None
overlay_on_pirate_swarm = None
overlay_on_vanduul_swarm = None
overlay_on_other = None


#SLASH SCREEN
def show_splash_screen(duration=2):
    def splash():
        splash_root = tk.Tk()
        splash_root.overrideredirect(True)
        splash_root.wm_attributes("-topmost", True)
        splash_root.attributes("-alpha", 0.0)  # Start fully transparent

        # Load splash image
        try:
            image = Image.open("static/splash.jpg")
            photo = ImageTk.PhotoImage(image)
            width, height = photo.width(), photo.height()
        except Exception:
            width, height = 400, 300
            photo = None

        # Center the window
        screen_width = splash_root.winfo_screenwidth()
        screen_height = splash_root.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        splash_root.geometry(f"{width}x{height}+{x}+{y}")

        # Transparent background color
        # splash_root.config(bg="white")
        # splash_root.wm_attributes("-transparentcolor", "white")

        if photo:
            canvas = tk.Canvas(splash_root, width=width, height=height, highlightthickness=0, bg="white")
            canvas.pack()
            canvas.create_image(0, 0, anchor="nw", image=photo)
            splash_root.image = photo
        else:
            tk.Label(splash_root, text="Loading...", font=("Helvetica", 18), bg="white").pack(expand=True)

        # Fade in
        def fade_in():
            for i in range(0, 21):
                splash_root.attributes("-alpha", i / 20)
                time.sleep(0.01)

        # Fade out
        def fade_out():
            for i in range(20, -1, -1):
                splash_root.attributes("-alpha", i / 20)
                time.sleep(0.01)

        def run_fade():
            fade_in()
            time.sleep(duration)
            fade_out()
            splash_root.destroy()

        threading.Thread(target=run_fade, daemon=True).start()
        splash_root.mainloop()

    threading.Thread(target=splash).start()

## sytem tray icon functions
def hide_console():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def show_console():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)

def load_tray_icon():
    icon_path = Path("static/sckticon.ico")  # Update the path as needed
    if not icon_path.exists():
        raise FileNotFoundError(f"Tray icon not found at: {icon_path}")
    return Image.open(icon_path)

def setup_system_tray(app_url: str):
    def on_open_ui(icon, item):
        webbrowser.open(app_url)

    def on_hide_console(icon, item):
        hide_console()

    def on_show_console(icon, item):
        show_console()

    def on_exit(icon, item):
        show_console()
        icon.stop()
        parent = psutil.Process(os.getpid())
        for child in parent.children(recursive=True):
            child.kill()
        parent.kill()

    icon = pystray.Icon("app")
    icon.icon = load_tray_icon()
    icon.menu = pystray.Menu(
        pystray.MenuItem("Open UI", on_open_ui),
        pystray.MenuItem("Hide Console", on_hide_console),
        pystray.MenuItem("Show Console", on_show_console),
        pystray.MenuItem("Exit", on_exit)
    )

    threading.Thread(target=icon.run, daemon=True).start()

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
            overlay_on_suicide,
            overlay_on_own_death,
            overlay_on_pu,
            overlay_on_gun_rush,
            overlay_on_squadron_battle,
            overlay_on_arena_commander,
            overlay_on_classic_race,
            overlay_on_battle_royale,
            overlay_on_free_flight,
            overlay_on_pirate_swarm,
            overlay_on_vanduul_swarm,
            overlay_on_other,
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
        "overlay": overlay_controller.get_config(),
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


@app.get("/client/{action}", response_model=ClientEnabledStatus)
async def control_client(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        sc_client.enable()
    else:
        sc_client.disable()
    
    config['client'] = sc_client.get_config()

    write_config(config_file=config_file, data=config)

    return ClientEnabledStatus(is_enabled=sc_client.is_enabled)


@app.get("/trigger_controller/{action}")
async def control_trigger_controller(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        trigger_controller.enable()
    else:
        trigger_controller.disable()
        
    config['trigger_controller'] = trigger_controller.get_config()
    
    write_config(config_file=config_file, data=config)

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
        
    config['recordings_controller'] = recordings_controller.get_config()

    write_config(config_file=config_file, data=config)
        
    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/own_death/{action}", response_model=RecordingsControllerStatus)
async def recordings_controller_on_own_death(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        recordings_controller.record_own_death_enable()
    else:
        recordings_controller.record_own_death_disable()
        
    config['recordings_controller'] = recordings_controller.get_config()

    write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())


@app.get("/recordings_controller/pu/{action}", response_model=RecordingsControllerStatus)
async def recordings_controller_on_pu(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        recordings_controller.record_pu_enable()
    else:
        recordings_controller.record_pu_disable()
        
    config['recordings_controller'] = recordings_controller.get_config()

    write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())

@app.get("/recordings_controller/gun_rush/{action}", response_model=RecordingsControllerStatus)
async def recordings_controller_on_gun_rush(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        recordings_controller.record_gun_rush_enable()
    else:
        recordings_controller.record_gun_rush_disable()
        
    config['recordings_controller'] = recordings_controller.get_config()

    write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())

@app.get("/recordings_controller/squadron_battle/{action}", response_model=RecordingsControllerStatus)
async def recordings_controller_on_squadron_battle(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        recordings_controller.record_squadron_battle_enable()
    else:
        recordings_controller.record_squadron_battle_disable()
        
    config['recordings_controller'] = recordings_controller.get_config()

    write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())

@app.get("/recordings_controller/arena_commander/{action}", response_model=RecordingsControllerStatus)
async def recordings_controller_on_arena_commander(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        recordings_controller.record_arena_commander_enable()
    else:
        recordings_controller.record_arena_commander_disable()
        
    config['recordings_controller'] = recordings_controller.get_config()

    write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())

@app.get("/recordings_controller/classic_race/{action}", response_model=RecordingsControllerStatus)
async def recordings_controller_on_classic_race(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        recordings_controller.record_classic_race_enable()
    else:
        recordings_controller.record_classic_race_disable()

    config['recordings_controller'] = recordings_controller.get_config()

    write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())

@app.get("/recordings_controller/battle_royale/{action}", response_model=RecordingsControllerStatus)
async def recordings_controller_on_battle_royale(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        recordings_controller.record_battle_royale_enable()
    else:
        recordings_controller.record_battle_royale_disable()

    config['recordings_controller'] = recordings_controller.get_config()

    write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())

@app.get("/recordings_controller/free_flight/{action}", response_model=RecordingsControllerStatus)
async def recordings_controller_on_free_flight(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        recordings_controller.record_free_flight_enable()
    else:
        recordings_controller.record_free_flight_disable()

    config['recordings_controller'] = recordings_controller.get_config()

    write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())

@app.get("/recordings_controller/pirate_swarm/{action}", response_model=RecordingsControllerStatus)
async def recordings_controller_on_pirate_swarm(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        recordings_controller.record_pirate_swarm_enable()
    else:
        recordings_controller.record_pirate_swarm_disable()

    config['recordings_controller'] = recordings_controller.get_config()

    write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())

@app.get("/recordings_controller/vanduul_swarm/{action}", response_model=RecordingsControllerStatus)
async def recordings_controller_on_vanduul_swarm(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        recordings_controller.record_vanduul_swarm_enable()
    else:
        recordings_controller.record_vanduul_swarm_disable()

    config['recordings_controller'] = recordings_controller.get_config()

    write_config(config_file=config_file, data=config)

    return RecordingsControllerStatus(**recordings_controller.get_config())

@app.get("/recordings_controller/other/{action}", response_model=RecordingsControllerStatus)
async def recordings_controller_other_enable(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        recordings_controller.record_other_enable()
    else:
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

@app.get("/overlay/{action}", response_model=OverlayStatus)
async def control_overlay(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_enabled.value = True
        overlay_controller.enabled = True
    else:
        overlay_enabled.value = False
        overlay_controller.enabled = False

    config['overlay'] = overlay_controller.get_config()

    write_config(config_file=config_file, data=config)

    return OverlayStatus(
        is_enabled=overlay_enabled.value
    )

@app.get("/overlay/suicide/{action}", response_model=OverlayStatus)
async def overlay_on_suicide(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_on_suicide.value = True
        overlay_controller.on_suicide = True
    else:
        overlay_on_suicide.value = False
        overlay_controller.on_suicide = False

    config['overlay'] = overlay_controller.get_config()

    write_config(config_file=config_file, data=config)

    return OverlayStatus(
        is_enabled=overlay_on_suicide.value
    )


@app.get("/overlay/own_death/{action}", response_model=OverlayStatus)
async def overlay_on_own_death(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_on_own_death.value = True
        overlay_controller.on_own_death = True
    else:
        overlay_on_own_death.value = False
        overlay_controller.on_own_death = False

    config['overlay'] = overlay_controller.get_config()

    write_config(config_file=config_file, data=config)

    return OverlayStatus(
        is_enabled=overlay_on_own_death.value
    )


@app.get("/overlay/pu/{action}", response_model=OverlayStatus)
async def overlay_on_pu(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_on_pu.value = True
        overlay_controller.on_pu = True
    else:
        overlay_on_pu.value = False
        overlay_controller.on_pu = False

    config['overlay'] = overlay_controller.get_config()

    write_config(config_file=config_file, data=config)

    return OverlayStatus(
        is_enabled=overlay_on_pu.value
    )

@app.get("/overlay/gun_rush/{action}", response_model=OverlayStatus)
async def overlay_on_gun_rush(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_on_gun_rush.value = True
        overlay_controller.on_gun_rush = True
    else:
        overlay_on_gun_rush.value = False
        overlay_controller.on_gun_rush = False

    config['overlay'] = overlay_controller.get_config()

    write_config(config_file=config_file, data=config)

    return OverlayStatus(
        is_enabled=overlay_on_gun_rush.value
    )


@app.get("/overlay/squadron_battle/{action}", response_model=OverlayStatus)
async def overlay_on_squadron_battle(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_on_squadron_battle.value = True
        overlay_controller.on_squadron_battle = True
    else:
        overlay_on_squadron_battle.value = False
        overlay_controller.on_squadron_battle = False

    config['overlay'] = overlay_controller.get_config()

    write_config(config_file=config_file, data=config)

    return OverlayStatus(
        is_enabled=overlay_on_squadron_battle.value
    )

@app.get("/overlay/arena_commander/{action}", response_model=OverlayStatus)
async def overlay_on_arena_commander(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_on_arena_commander.value = True
        overlay_controller.on_arena_commander = True
    else:
        overlay_on_arena_commander.value = False
        overlay_controller.on_arena_commander = False

    config['overlay'] = overlay_controller.get_config()

    write_config(config_file=config_file, data=config)

    return OverlayStatus(
        is_enabled=overlay_on_arena_commander.value
    )

@app.get("/overlay/classic_race/{action}", response_model=OverlayStatus)
async def overlay_on_classic_race(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_on_classic_race.value = True
        overlay_controller.on_classic_race = True
    else:
        overlay_on_classic_race.value = False
        overlay_controller.on_classic_race = False

    config['overlay'] = overlay_controller.get_config()

    write_config(config_file=config_file, data=config)

    return OverlayStatus(
        is_enabled=overlay_on_classic_race.value
    )

@app.get("/overlay/battle_royale/{action}", response_model=OverlayStatus)
async def overlay_on_battle_royale(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_on_battle_royale.value = True
        overlay_controller.on_battle_royale = True
    else:
        overlay_on_battle_royale.value = False
        overlay_controller.on_battle_royale = False

    config['overlay'] = overlay_controller.get_config()

    write_config(config_file=config_file, data=config)

    return OverlayStatus(
        is_enabled=overlay_on_battle_royale.value
    )

@app.get("/overlay/free_flight/{action}", response_model=OverlayStatus)
async def overlay_on_free_flight(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_on_free_flight.value = True
        overlay_controller.on_free_flight = True
    else:
        overlay_on_free_flight.value = False
        overlay_controller.on_free_flight = False

    config['overlay'] = overlay_controller.get_config()

    write_config(config_file=config_file, data=config)

    return OverlayStatus(
        is_enabled=overlay_on_free_flight.value
    )

@app.get("/overlay/free_flight/{action}", response_model=OverlayStatus)
async def overlay_on_free_flight(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_on_free_flight.value = True
        overlay_controller.on_free_flight = True
    else:
        overlay_on_free_flight.value = False
        overlay_controller.on_free_flight = False

    config['overlay'] = overlay_controller.get_config()

    write_config(config_file=config_file, data=config)

    return OverlayStatus(
        is_enabled=overlay_on_free_flight.value
    )

@app.get("/overlay/pirate_swarm/{action}", response_model=OverlayStatus)
async def overlay_on_pirate_swarm(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_on_pirate_swarm.value = True
        overlay_controller.on_pirate_swarm = True
    else:
        overlay_on_pirate_swarm.value = False
        overlay_controller.on_pirate_swarm = False

    config['overlay'] = overlay_controller.get_config()

    write_config(config_file=config_file, data=config)

    return OverlayStatus(
        is_enabled=overlay_on_pirate_swarm.value
    )

@app.get("/overlay/vanduul_swarm/{action}", response_model=OverlayStatus)
async def overlay_on_vanduul_swarm(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_on_vanduul_swarm.value = True
        overlay_controller.on_vanduul_swarm = True
    else:
        overlay_on_pirate_swarm.value = False
        overlay_controller.on_vanduul_swarm = False

    config['overlay'] = overlay_controller.get_config()

    write_config(config_file=config_file, data=config)

    return OverlayStatus(
        is_enabled=overlay_on_vanduul_swarm.value
    )

@app.get("/overlay/other/{action}", response_model=OverlayStatus)
async def overlay_on_other(action: RequestedAction):
    if action == RequestedAction.ENABLE:
        overlay_on_other.value = True
        overlay_controller.on_other = True
    else:
        overlay_on_other.value = False
        overlay_controller.on_other = False

    config['overlay'] = overlay_controller.get_config()

    write_config(config_file=config_file, data=config)

    return OverlayStatus(
        is_enabled=overlay_on_other.value
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
    enable_kill_sounds: str = Form("true"),
    kill_volume: str = Form("100")
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

    logfile_monitor.logfile_with_path = logfile
    logfile_monitor.frequency = int(frequency)

    await sc_client.validate_logfile()

    trigger_controller.set_overlay(gpu_vendor=gpu_vendor, hotkey=hotkey_combo)

    if not len(video_folder_path):
        video_folder_path = "."

    await recordings_controller.set_path(path=Path(video_folder_path))

    config["log_monitor"] = logfile_monitor.get_config()
    config["trigger_controller"] = trigger_controller.get_config()
    config["recordings_controller"] = recordings_controller.get_config()

    overlay_controller.position = overlay_position
    overlay_controller.font_color = overlay_font_color
    overlay_controller.font_size = overlay_font_size

    config["overlay"] = overlay_controller.get_config()

    # ✅ Handle kill sound toggle from dropdown
    config.setdefault("sound", {})
    config["sound"]["enable_kill_sounds"] = enable_kill_sounds.lower() == "true"

    try:
        volume_percent = float(kill_volume)
        volume_percent = max(0.0, min(100.0, volume_percent))  # clamp between 0–100
        config["sound"]["volume"] = round((volume_percent / 100), 4)  # precise float
    except (ValueError, TypeError):
        config["sound"]["volume"] = 1.0

    # ✅ Save updated config
    write_config(config_file=config_file, data=config)

    return RedirectResponse(url="/settings", status_code=303)


def main() -> None:
    # Hide console window on Windows
    hide_console() 

    global position_value, color_value, font_size_value, overlay_queue, sc_client, overlay_enabled, overlay_on_suicide, \
        overlay_on_own_death, overlay_on_pu, overlay_on_gun_rush, overlay_on_squadron_battle, \
        overlay_on_arena_commander, overlay_on_classic_race, overlay_on_battle_royale, overlay_on_free_flight, \
        overlay_on_pirate_swarm, overlay_on_vanduul_swarm, overlay_on_other


    manager = Manager()
    overlay_queue = manager.Queue()

    # position_value = manager.Value("u", config.get("overlay").get("position"))
    # color_value = manager.Value("u", config.get("overlay").get("font_color"))
    # font_size_value = manager.Value("u", config.get("overlay").get("font_size"))
    # overlay_enabled = manager.Value("b", config.get("overlay").get("enabled"))
    # overlay_on_suicide = manager.Value("b", config.get("overlay").get("on_suicide"))
    # overlay_on_own_death = manager.Value("b", config.get("overlay").get("on_own_death"))
    # overlay_on_pu = manager.Value("b", config.get("overlay").get("on_pu"))
    # overlay_on_gun_rush = manager.Value("b", config.get("overlay").get("on_gun_rush"))
    # overlay_on_squadron_battle = manager.Value("b", config.get("overlay").get("on_squadron_battle"))
    # overlay_on_arena_commander = manager.Value("b", config.get("overlay").get("on_arena_commander"))
    # overlay_on_classic_race= manager.Value("b", config.get("overlay").get("on_classic_race"))
    # overlay_on_battle_royale = manager.Value("b", config.get("overlay").get("on_battle_royale"))
    # overlay_on_free_flight = manager.Value("b", config.get("overlay").get("on_free_flight"))
    # overlay_on_pirate_swarm = manager.Value("b", config.get("overlay").get("on_pirate_swarm"))
    # overlay_on_vanduul_swarm = manager.Value("b", config.get("overlay").get("on_vanduul_swarm"))
    # overlay_on_other = manager.Value("b", config.get("overlay").get("on_other"))


    position_value = manager.Value("u", overlay_controller.position)
    color_value = manager.Value("u", overlay_controller.font_color)
    font_size_value = manager.Value("u", overlay_controller.font_size)
    overlay_enabled = manager.Value("b", overlay_controller.enabled)
    overlay_on_suicide = manager.Value("b", overlay_controller.on_suicide)
    overlay_on_own_death = manager.Value("b", overlay_controller.on_own_death)
    overlay_on_pu = manager.Value("b", overlay_controller.on_pu)
    overlay_on_gun_rush = manager.Value("b", overlay_controller.on_gun_rush)
    overlay_on_squadron_battle = manager.Value("b", overlay_controller.on_squadron_battle)
    overlay_on_arena_commander = manager.Value("b", overlay_controller.on_arena_commander)
    overlay_on_classic_race = manager.Value("b", overlay_controller.on_classic_race)
    overlay_on_battle_royale = manager.Value("b", overlay_controller.on_battle_royale)
    overlay_on_free_flight = manager.Value("b", overlay_controller.on_free_flight)
    overlay_on_pirate_swarm = manager.Value("b", overlay_controller.on_pirate_swarm)
    overlay_on_vanduul_swarm = manager.Value("b", overlay_controller.on_vanduul_swarm)
    overlay_on_other = manager.Value("b", overlay_controller.on_other)

    sc_client = SCClient(
        config=config.get('client'),
        logfile_monitor=logfile_monitor,
        repo=repo,
        statistics_controller=statistics_controller,
        trigger_controller=trigger_controller,
        recordings_controller=recordings_controller,
        overlay_controller=overlay_controller,
        overlay_queue=overlay_queue,
    )

    host: str = config.get("local_api").get("ip_address")
    port: int = config.get("local_api").get("port")

    cert_path: Path = Path("certs/cert.pem")
    key_path: Path = Path("certs/key.pem")

    hostname: str = "localhost" if host == "0.0.0.0" else host
    protoc: str = "https" if cert_path.exists() and key_path.exists() else "http"
    url: str = f"{protoc}://{hostname}:{port}"

 #systray gets custom url
    setup_system_tray(url)

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