from abc import ABC, abstractmethod
from enum import Enum
from typing import Any


class RepositoryType(Enum):
    CSV = 'csv'

class Repository(ABC):

    @abstractmethod
    def create(self, entry: Any):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass