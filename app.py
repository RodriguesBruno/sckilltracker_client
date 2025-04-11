import os
import sys
import uvicorn
import asyncio
from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI, Request, WebSocketDisconnect, WebSocket, Form, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import ValidationError

from src.client import SCClient
from src.connection_manager import ConnectionManager
from src.file_handlers import read_config, write_config
from src.logfile_monitor import LogFileMonitor
from src.recording_statistics import RecordingStatistics
from src.trigger_controller import TriggerController
from src.repository import Repository, RepositoryType
from src.repository_factory import RepositoryFactory
from src.settings_form import SettingsForm
from src.utils import get_local_ip

logging.basicConfig(
    level=logging.DEBUG,  # or DEBUG if you want verbose output
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

config_file: str = "./config.json"
config: dict = read_config(config_file=config_file)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await client.validate_logfile()
    asyncio.create_task(client.run(broadcast=connection_manager.broadcast))
    yield

def resource_path(relative_path):
    try:
        return os.path.join(sys._MEIPASS, relative_path)
    except AttributeError:
        return os.path.abspath(relative_path)

static_dir = resource_path("static")
templates_dir = resource_path("templates")

title: str = config.get('title')

app: FastAPI = FastAPI(title=f"{title} API", openapi_url="/openapi.json", lifespan=lifespan)
app.mount("/static", StaticFiles(directory=static_dir), name="static")
templates = Jinja2Templates(directory=templates_dir)

connection_manager: ConnectionManager = ConnectionManager()

MAX_ENTRIES: int = 22

logfile_monitor: LogFileMonitor = LogFileMonitor(config=config.get('log_monitor'))

repo: Repository = RepositoryFactory().get_repo(RepositoryType.CSV)

recording_statistics: RecordingStatistics = RecordingStatistics(csv_path='./events.csv')

trigger_controller: TriggerController = TriggerController(config=config.get('trigger_controller'))

client: SCClient = SCClient(
    config=config.get('client'),
    logfile_monitor=logfile_monitor,
    repo=repo,
    trigger_controller=trigger_controller
)

ws_url: str = f'ws://{get_local_ip()}:{config.get("local_api").get("port")}/ws'


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await connection_manager.connect(websocket=websocket)
    try:
        while True:
            _ = await websocket.receive_text()

    except WebSocketDisconnect:
        connection_manager.disconnect(websocket)

@app.get("/")
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": title,
        "version": client.version,
        "client_enabled": client.is_enabled,
        "game_is_running": client.game_is_running,
        "game_is_running_last_checked": client.game_is_running_last_checked,
        "pilot_name": client.pilot_name,
        "ship_name": client.ship_name,
        "game_mode": client.game_mode,
        "notifications": client.notifications[:MAX_ENTRIES],
        "startup_date": client.startup_date,
        "logfile_date": logfile_monitor.last_read_date,
        "max_entries": MAX_ENTRIES,
        "logfile_frequency": logfile_monitor.frequency,
        "trigger_controller_enabled": trigger_controller.is_enabled,
        "verbose_logging": client.is_verbose_logging,
        "ws_url": ws_url,

    })

@app.get("/stats")
def stats(request: Request):
    top_victims = recording_statistics.top_victims()
    top_killers = recording_statistics.top_killers()

    kills_by_mode = recording_statistics.kills_by_game_mode()
    damage_distribution = recording_statistics.damage_type_distribution()

    top_victims_chart: str = recording_statistics.get_top_victims_chart_html()
    top_killers_chart: str = recording_statistics.get_top_killers_chart_html()
    game_mode_chart: str = recording_statistics.get_game_mode_pie_chart_html()
    damage_chart : str = recording_statistics.get_damage_type_distribution_chart_html()

    return templates.TemplateResponse("stats.html", {
        "request": request,
        "title": title,
        "top_victims": top_victims,
        "top_killers": top_killers,
        "kills_by_mode": kills_by_mode,
        "damage_distribution": damage_distribution,
        "top_victims_chart": top_victims_chart,
        "top_killers_chart": top_killers_chart,
        "game_mode_chart": game_mode_chart,
        "damage_chart": damage_chart
    })

@app.get("/status")
async def get_status():
    return  {
        "title": title,
        "startup_date": client.startup_date,
        "notifications": client.notifications
    }

@app.get("/client/enable")
async def enable_client():
    if client.is_disabled:
        client.enable()
        config['client'] = client.get_config()

        write_config(config_file=config_file, data=config)

    return  {
        "client_enabled": client.is_enabled
    }

@app.get("/client/disable")
async def disable_client():
    if client.is_enabled:
        client.disable()
        config['client'] = client.get_config()

        write_config(config_file=config_file, data=config)

    return {
        "client_enabled": client.is_enabled
    }

@app.get("/trigger_controller/enable")
async def enable_trigger_controller():
    if trigger_controller.is_disabled:
        trigger_controller.enable()
        config['trigger_controller'] = trigger_controller.get_config()

        write_config(config_file=config_file, data=config)

    return  {
        "trigger_controller": trigger_controller.is_enabled
    }

@app.get("/trigger_controller/disable")
async def disable_trigger_controller():
    if trigger_controller.is_enabled:
        trigger_controller.disable()
        config['trigger_controller'] = trigger_controller.get_config()

        write_config(config_file=config_file, data=config)

    return {
        "trigger_controller": trigger_controller.is_enabled
    }

@app.get("/verbose_logging/enable")
async def enable_verbose_logging():
    if not client.is_verbose_logging:
        client.verbose_logging_enable()
        config['client'] = client.get_config()

        write_config(config_file=config_file, data=config)

    return  {
        "verbose_logging": client.is_verbose_logging
    }

@app.get("/verbose_logging/disable")
async def disable_verbose_logging():
    if client.is_verbose_logging:
        client.verbose_logging_disable()
        config['client'] = client.get_config()

        write_config(config_file=config_file, data=config)

    return {
        "verbose_logging": client.is_verbose_logging
    }



@app.get("/settings")
async def get_settings(request: Request):
    return templates.TemplateResponse("settings.html", {
        "request": request,
        "title": title,
        "config": config
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
        hotkey_combo: str = Form(None)
    ):

    try:
        form_data = SettingsForm(
            local_api_ip_address=local_api_ip_address,
            local_api_port=local_api_port,
            api_url=api_url,
            logfile=logfile,
            frequency=frequency
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
                        "version": client.version,
                        "enabled": client.is_enabled,
                        "api_url": api_url
                    },
                    "log_monitor": {
                        "logfile_with_path": logfile,
                        "frequency": frequency,
                    },
                    "trigger_controller": trigger_controller.get_config(),
                    "version": config.get('version'),
                },
                "errors": e.errors(),
            },
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    client.api_url = str(form_data.api_url)

    if form_data.logfile != logfile_monitor.logfile_with_path:
        logfile_monitor.log_is_validated = False
        logfile_monitor.logfile_with_path = form_data.logfile

        await client.validate_logfile()

    logfile_monitor.frequency = int(form_data.frequency)

    trigger_controller.set_overlay(gpu_vendor=gpu_vendor, hotkey=hotkey_combo)

    config['local_api']['port'] = int(form_data.local_api_port)
    config['client'] = client.get_config()
    config['log_monitor'] = logfile_monitor.get_config()
    config['trigger_controller'] = trigger_controller.get_config()

    write_config(config_file=config_file, data=config)

    return RedirectResponse(url="/settings", status_code=303)


def main() -> None:
    uvicorn.run(
        app=app,
        host=config.get("local_api").get("ip_address"),
        port=config.get("local_api").get("port")
    )

if __name__ == "__main__":
    main()
