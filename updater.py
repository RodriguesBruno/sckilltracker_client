import traceback
import requests
import json
import logging
import shutil
import sys
import time
import os
import psutil
from pathlib import Path
from requests import Response


def log_exception(exc_type, exc_value, exc_tb):
    with open("sckilltracker_updater_error.log", "w", encoding="utf-8") as f:
        traceback.print_exception(exc_type, exc_value, exc_tb, file=f)

sys.excepthook = log_exception

LOG_FILE: Path = Path(__file__).resolve().parent / "updater.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8", mode="w"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("updater")

EXEC_DIR = Path(getattr(sys, "frozen", False) and sys.executable or __file__).resolve().parent

CONFIG_PATH: str = str(EXEC_DIR / "config.json")

REPO = "RodriguesBruno/sckilltracker_client"
EXE_NAME = "sckilltracker_client.exe"

def get_local_version() -> dict:
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def update_local_config(data: dict) -> None:
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def get_latest_release() -> tuple[str, str ,str]:
    url: str = f"https://api.github.com/repos/{REPO}/releases/latest"
    resp: Response = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    tag = data["tag_name"].lstrip("v")

    asset = next((a for a in data["assets"] if a["name"].endswith(".exe")), None)
    if not asset:
        raise RuntimeError("No Windows .exe asset found in release")

    return tag, asset["browser_download_url"], asset["name"]


def download_file(url: str, dest: Path) -> None:
    logger.info(f"Downloading: {url}")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    logger.info(f"Downloaded to {dest}")


def kill_running_client(exe_name: str) -> bool:
    logger.info(f"Checking if {exe_name} is running...")
    for proc in psutil.process_iter(["pid", "name"]):
        try:
            if proc.info["name"].lower() == exe_name.lower():
                logger.info(f"Found running client (PID {proc.pid}), terminating...")
                proc.terminate()
                try:
                    proc.wait(timeout=10)
                    logger.info("Client terminated successfully.")

                except psutil.TimeoutExpired:
                    logger.warning("Client did not exit in time, killing forcefully.")
                    proc.kill()

                return True

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    logger.info("No running client found.")

    return False


def run_update():
    try:
        config: dict = get_local_version()
        local_version: str = config.get('client').get('version')
        latest_version, download_url, asset_name = get_latest_release()

        logger.info(f"Local version: {local_version}")
        logger.info(f"Latest version: {latest_version}")

        if latest_version > local_version:
            logger.info("New version available, preparing update...")

            exe_path: Path = Path(__file__).resolve().parent / EXE_NAME

            kill_running_client(exe_name=EXE_NAME)

            if exe_path.exists():
                backup = exe_path.with_name(f"{exe_path.stem}_{local_version}_old{exe_path.suffix}")
                logger.info(f"Renaming old exe to {backup.name}")
                shutil.move(str(exe_path), str(backup))

            download_file(url=download_url, dest=exe_path)

            config['client']['version'] = latest_version
            update_local_config(data=config)

            logger.info("Update complete. Restarting new version...")

            time.sleep(1)
            os.startfile(exe_path)
            sys.exit(0)
        else:
            logger.info("Already up to date. No update performed.")

    except Exception as e:
        logging.error(f"There was an error with updater: {e}")

if __name__ == "__main__":
    run_update()