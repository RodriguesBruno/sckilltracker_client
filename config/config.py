from src.utils import resource_path

logging_config_file: str = resource_path('config/config_logging.json')
client_config_file: str = resource_path('config/client_config.json')
default_file = resource_path("config/config.default.json")
config_file: str = resource_path("config.json")