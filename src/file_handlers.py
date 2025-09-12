import json
import logging
from pathlib import Path
import shutil

def read_config(config_file: str) -> dict:
    with open(config_file, "r") as f:
        return json.load(f)

def write_config(config_file: str, data: dict) -> None:
    with open(config_file, 'w') as f:
        json.dump(data, f, indent=4)

def ensure_config(config_file: str, default_file: str) -> dict:
    path: Path = Path(config_file)

    if not path.exists():
        shutil.copy(default_file, config_file)
        logging.warning(f"Created missing config file from default: {default_file}")

    return read_config(config_file)