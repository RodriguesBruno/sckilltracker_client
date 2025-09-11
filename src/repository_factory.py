import logging

from src.csv_repository import CSVRepository
from src.repository import RepositoryType
from src.sql_repository import SQLRepository


class RepositoryFactory:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_repo(repository_type: RepositoryType):
        if repository_type == RepositoryType.CSV:
            logging.info(f"[REPOSITORY FACTORY] - CSV")
            path: str= "./db/events.csv"
            return CSVRepository(path=path)

        elif repository_type == RepositoryType.SQL:
            logging.info(f"[REPOSITORY FACTORY] - SQL")
            path: str = './db/events.db'
            return SQLRepository(path=path)

        return None
