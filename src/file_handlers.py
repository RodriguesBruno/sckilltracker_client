import json

def read_config(config_file: str) -> dict:
    with open(config_file, "r") as f:
        return json.load(f)

def write_config(config_file: str, data: dict) -> None:
    with open(config_file, 'w') as f:
        json.dump(data, f, indent=4)
