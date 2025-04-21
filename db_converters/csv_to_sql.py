import csv
from typing import List, Dict

from src.sql_repository import SQLRepository


def import_csv_to_sql(csv_path: str, repo: SQLRepository):
    entries: List[Dict[str, str]] = []

    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            entries.append(row)

    repo.create(entries)

if __name__ == "__main__":
    path = ""
    repo: SQLRepository = SQLRepository(path=path)
    import_csv_to_sql('../events.csv', repo)
