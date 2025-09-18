import json
import sys
import logging
from pathlib import Path
from typing import Dict, Any, Tuple

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


def merge_defaults(default_config: Dict[str, Any], user_config: Dict[str, Any]) -> Tuple[Dict[str, Any], bool]:
    """
    Recursively merge `default_config` into `user_config`.

    Returns:
        (updated_user_config, changed)
        - updated_user_config: the merged config (same dict as user_config, updated in place)
        - changed: True if user_config was modified
    """
    changed = False

    for key, value in default_config.items():
        if key not in user_config:
            user_config[key] = value
            changed = True  # new key added

        elif isinstance(value, dict) and isinstance(user_config[key], dict):
            _, sub_changed = merge_defaults(value, user_config[key])
            if sub_changed:
                changed = True
        # else → keep user_config[key] as-is

    return user_config, changed

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

    default_config: dict = read_default_config()
    user_config: dict = read_config()

    merged_config, changed = merge_defaults(default_config=default_config, user_config=user_config)
    if changed:
        write_config(data=merged_config)

    return merged_config
