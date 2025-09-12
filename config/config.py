import sys
from pathlib import Path
from src.utils import resource_path

logging_config_file: str = resource_path('config/config_logging.json')
client_config_file: str = resource_path('config/client_config.json')
default_file = resource_path("config/config.default.json")

EXEC_DIR = Path(getattr(sys, "frozen", False) and sys.executable or __file__).resolve().parent

config_file: str = str(EXEC_DIR / "config.json")