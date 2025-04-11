from datetime import datetime
import socket


def get_date() -> str:
    date_format: str = '%Y-%m-%d %H:%M:%S'
    return datetime.now().strftime(date_format)

def get_local_ip() -> str:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(('8.8.8.8', 80))
        result = s.getsockname()[0]

        return result
