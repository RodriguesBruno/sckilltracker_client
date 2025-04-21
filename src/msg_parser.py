import re

SHIP_PREFIXES: list[str] = [
    "ORIG",
    "CRUS",
    "RSI",
    "AEGS",
    "VNCL",
    "DRAK",
    "ANVL",
    "BANU",
    "MISC",
    "CNOU",
    "XIAN",
    "GAMA",
    "TMBL",
    "ESPR",
    "KRIG",
    "GRIN",
    "XNAA",
	"MRAI",
    "ARGO"
]

def get_log_date(line: str) -> str:
    match = re.search(r"<(?P<date>[\d:T-]*)[.\dZ]*>\s\[", line)
    return f'{match.group("date").replace("T", " ")} UTC' if match else '-'

def get_victim_player_name(line: str) -> str:
    if 'PU_Human_Enemy' and '_NPC_' in line:
        return 'npc'

    match = re.search(r"(?:_+?\w+?_PU_Advocacy_\d*)", line)
    if match:
        return 'npc'

    match = re.search(r"(?:_+?\w+?_pet_\d*)", line)
    if match:
        return 'npc'

    match = re.search(r"CActor::Kill:\s'(?P<player_name>[\w-]*)", line)
    return match.group('player_name') if match else '-'

def get_victim_zone(line: str) -> str:
    match = re.search(r"in\szone\s'(?P<zone>[a-zA-Z\d_-]*)'", line)
    if match:
        ship_name = match.group('zone')
        for prefix in SHIP_PREFIXES:
            if prefix in ship_name:
                ship_name = ship_name.replace('_', ' ').replace(prefix, '').replace('SCItem', '').strip(' ')
                return re.sub(r'\s\d+$', '', ship_name)

        ship_name = ship_name.replace('_', ' ').replace('-', '').replace('SCItem', '').replace('ObjectContainer', '').strip(' ')
        return re.sub(r'\s\d+$', '', ship_name)

    return '-'

def get_killed_by(line: str) -> str:
    if 'PU_Human_Enemy' and '_NPC_' in line:
        return 'npc'

    match = re.search(r"(?:_+?\w+?_PU_Advocacy_\d*)", line)
    if match:
        return 'npc'

    match = re.search(r"(?:_+?\w+?_pet_\d*)", line)
    if match:
        return 'npc'

    match = re.search(r"killed\sby\s'(?P<killed_by>[\w-]*)", line)
    return match.group('killed_by') if match else '-'

def get_using(line: str) -> str:
    if "with damage type 'Crash'" in line:
        return '-'

    match = re.search(r"using\s'(?P<using>[\w-]*)", line)
    if match:
        using_name = match.group('using')

        using_name = using_name.replace('_', ' ')
        return re.sub(r'\s\d+$', '', using_name)

    return '-'

def get_damage(line: str) -> str:
    match = re.search(r"damage\stype\s'(?P<damage>\w*)", line)
    if match:
        damage = match.group('damage')
        return re.sub(r'(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])', ' ', damage)

    return '-'

def get_game_mode(line: str) -> str:
    if 'Loading screen for Frontend_Main' in line:
        return '-'

    if "Starting 'Game" in line:
        return 'PU'

    match = re.search(r'screen\sfor\s[\w_]*\s:\s(?P<game_mode>[\w_]*)\sclosed', line)
    if match:
        game_mode = match.group('game_mode').replace('EA_', '')
        if game_mode == 'SC_Frontend':
            return 'PU'

        return re.sub(r'(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])', ' ', game_mode).replace('_', ' ')


    match = re.search(r'>\sMode\[EA_(?P<game_mode>[\w_]*)]', line)
    if match:
        game_mode = match.group('game_mode')
        if game_mode == 'FPSGunGame':
            return 'Gun Rush'

        return re.sub(r'(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])', ' ', game_mode).replace('_', ' ')

    return '-'

def get_ship_name(line: str) -> str:
    for prefix in SHIP_PREFIXES:
        if prefix in line:

            match = re.search(rf"in\szone\s'{prefix}_(?P<ship_name>[\w_]*)'\skilled", line)
            if not match:
                match = re.search(rf"{prefix}_(?P<ship_name>[\w_]*)\sin\szone\s", line)

            if not match:
                match = re.search(rf"{prefix}_(?P<ship_name>[\w_]*)\)\sby\splayer", line)

            if match:
                ship_name = match.group('ship_name')
                ship_name = ship_name.replace('_', ' ').replace(prefix, '').replace('SCItem', '').strip(' ')
                return re.sub(r'\s\d+$', '', ship_name)

    return '-'

def get_pilot_name(line: str) -> str:
    match = re.search(r"<OnClientConnected>\sPlayer\[(?P<pilot_name>\w*)]\s", line)
    return match.group('pilot_name') if match else '-'