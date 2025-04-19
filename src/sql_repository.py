import logging
import sqlite3

from src.repository import Repository


class SQLRepository(Repository):
    def __init__(self, path: str) -> None:
        self._db_path: str = path
        self._initialize()

    def _initialize(self):
        conn = sqlite3.connect(self._db_path)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS events (uuid TEXT PRIMARY KEY, date TEXT, victim_player_name TEXT, victim_zone_name TEXT, killed_by TEXT, ship_name TEXT, "using" TEXT, damage TEXT, game_mode TEXT)''')

        conn.commit()
        conn.close()

    @property
    def type(self) -> str:
        return 'sql'

    @property
    def count(self) -> int:
        conn = sqlite3.connect(self._db_path)
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM events")
        result = c.fetchone()[0]
        conn.close()
        return result

    def create(self, entries: list[dict]) -> None:

        logging.info(f"[SQL REPOSITORY] - CREATE")
        conn = sqlite3.connect(self._db_path)
        c = conn.cursor()

        for entry in entries:
            c.execute(
                'INSERT INTO events (uuid, date, victim_player_name, victim_zone_name, killed_by, ship_name, "using", damage, game_mode) VALUES (?, ?, ?, ? ,?, ?, ?, ?, ?)',
                (
                    entry.get('uuid'),
                    entry.get('date'),
                    entry.get('victim_player_name'),
                    entry.get('victim_zone_name'),
                    entry.get('killed_by'),
                    entry.get('ship_name'),
                    entry.get('using'),
                    entry.get('damage'),
                    entry.get('game_mode')
                    )
                )

        conn.commit()
        conn.close()

    def read(self) -> list[dict]:
        logging.info(f"[SQL REPOSITORY] - READ")

        conn = sqlite3.connect(self._db_path)
        c = conn.cursor()
        c.execute('SELECT date, victim_player_name, victim_zone_name, killed_by, ship_name, "using", damage, game_mode FROM events')
        results: list[dict] = [
            {
                "date": row[0],
                "victim_player_name": row[1],
                "victim_zone_name": row[2],
                "killed_by": row[3],
                "ship_name": row[4],
                "using": row[5],
                "damage": row[6],
                "game_mode": row[7]

            }
            for row in c.fetchall()
        ]

        conn.close()

        return results

    def update(self):
        pass

    def delete(self):
        pass