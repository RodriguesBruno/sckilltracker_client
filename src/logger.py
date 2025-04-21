import logging.config
from logging import Logger

logger: Logger = logging.getLogger('app')

def setup_logging(config: dict) -> None:
    logging.config.dictConfig(config)
