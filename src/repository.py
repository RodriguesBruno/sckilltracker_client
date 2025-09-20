from abc import ABC, abstractmethod
from enum import Enum
from typing import Any


class RepositoryType(Enum):
    CSV = 'csv'
    SQL = 'sql'


class Repository(ABC):

    @abstractmethod
    def type(self) -> RepositoryType:
        ...

    @abstractmethod
    def count(self) -> int:
        ...

    @abstractmethod
    def create(self, entries: Any) -> Any:
        ...

    @abstractmethod
    def read(self) -> list[dict[str, Any]]:
        ...

    @abstractmethod
    def update(self) -> None:
        ...

    @abstractmethod
    def delete(self) -> None:
        ...