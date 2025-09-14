import requests
import json
import logging
import shutil
import sys
import time
import os
from pathlib import Path
import psutil


LOG_FILE = Path(__file__).resolve().parent / "updater.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8", mode="w"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("updater")


REPO = "RodriguesBruno/sckilltracker_client"
CONFIG_PATH = Path(__file__).resolve().parent / "config" / "client_config.json"
EXE_NAME = "sckilltracker_client.exe"


def get_local_version() -> str:
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)["version"]


def get_latest_release():
    url = f"https://api.github.com/repos/{REPO}/releases/latest"
    resp = requests.get(url, timeout=10)
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
    local_version = get_local_version()
    latest_version, download_url, asset_name = get_latest_release()

    logger.info(f"Local version: {local_version}")
    logger.info(f"Latest version: {latest_version}")

    if latest_version > local_version:
        logger.info("New version available, preparing update...")

        exe_path = Path(__file__).resolve().parent / EXE_NAME

        kill_running_client(EXE_NAME)

        if exe_path.exists():
            backup = exe_path.with_name(f"{exe_path.stem}_{local_version}_old{exe_path.suffix}")
            logger.info(f"Renaming old exe to {backup.name}")
            shutil.move(str(exe_path), str(backup))

        download_file(download_url, exe_path)

        logger.info("Update complete. Restarting new version...")
        time.sleep(1)
        os.startfile(exe_path)
        sys.exit(0)
    else:
        logger.info("Already up to date. No update performed.")

if __name__ == "__main__":
    run_update()