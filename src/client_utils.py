import hashlib
import socket

def generate_client_id():
    hostname = socket.gethostname()
    mac = get_mac_address()
    raw = f"{hostname}-{mac}"

    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def get_mac_address() -> str:
    import uuid
    mac = uuid.getnode()
    return ':'.join(("%012X" % mac)[i:i + 2] for i in range(0, 12, 2))