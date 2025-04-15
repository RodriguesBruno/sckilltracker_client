from datetime import datetime
import socket
import os
import sys


def get_date() -> str:
    date_format: str = '%Y-%m-%d %H:%M:%S'
    return datetime.now().strftime(date_format)

def get_local_ip() -> str:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(('8.8.8.8', 80))
        result = s.getsockname()[0]

        return result

def resource_path(relative_path):
    try:
        return os.path.join(sys._MEIPASS, relative_path)

    except AttributeError:
        return os.path.abspath(relative_path)


def setup_folders():
    folders: list[str] = ['certs', 'db']

    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)