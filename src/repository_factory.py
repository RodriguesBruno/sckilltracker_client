from src.csv_repository import CSVRepository
from src.repository import RepositoryType


class RepositoryFactory:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_repo(repository_type: RepositoryType):
        if repository_type == RepositoryType.CSV:
            file_name: str= "events.csv"
            return CSVRepository(file_name=file_name)