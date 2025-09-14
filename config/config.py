import json
import sys
import logging
from pathlib import Path

from src.client import CLIENT_VERSION
from src.utils import resource_path

logging_config_file: str = resource_path('config/config_logging.json')
default_file = resource_path("config/config.default.json")

EXEC_DIR = Path(getattr(sys, "frozen", False) and sys.executable or __file__).resolve().parent

CONFIG_FILE: str = "config.json"


def read_logging_config() -> dict:
    with open(logging_config_file, "r") as f:
        return json.load(f)


def read_default_config() -> dict:
    with open(default_file, "r") as f:
        return json.load(f)


def read_config() -> dict:
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


def write_config(data: dict) -> None:
    with open(CONFIG_FILE, 'w') as f:
        json.dump(data, f, indent=4)


def ensure_config() -> dict:
    path: Path = Path(CONFIG_FILE)

    if not path.exists():
        config: dict = read_default_config()
        logging.warning(f"Created missing config file from default: {default_file}")
        config["client"]["version"] = CLIENT_VERSION
        write_config(data=config)

        return config

    return read_config()