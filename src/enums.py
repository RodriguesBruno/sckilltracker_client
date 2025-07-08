from enum import Enum


class RequestedAction(str, Enum):
    ENABLE = 'enable'
    DISABLE = 'disable'