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

    def count(self) -> int:
        ...

    @abstractmethod
    def create(self, entries: Any):
        ...

    @abstractmethod
    def read(self):
        ...

    @abstractmethod
    def update(self):
        ...

    @abstractmethod
    def delete(self):
        ...