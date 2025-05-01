import csv
from pathlib import Path

from src.models.models import PlayerEvent


def transform_csv(old_csv_path: str, new_csv_path: str):
    # Define the new headers

    new_headers: list[str] = list(PlayerEvent.model_fields.keys())
    # new_headers = [
    #     'uuid',
    #     'date',
    #     'victim_player_name',
    #     'victim_player_icon_url',
    #     'victim_player_org',
    #     'victim_player_org_url',
    #     'victim_player_org_icon_url',
    #     'victim_player_enlisted_date',
    #
    #     'victim_zone_name',
    #
    #     'killed_by',
    #     'killed_by_player_icon_url',
    #     'killed_by_player_org',
    #     'killed_by_player_org_url',
    #     'killed_by_player_org_icon_url',
    #     'killed_by_player_enlisted_date',
    #
    #     'ship_name',
    #     'using',
    #     'damage',
    #     'game_mode',
    #     'client_enabled',
    #     'push_result_message',
    #     'push_result_is_success'
    # ]

    # Read the old CSV
    with open(old_csv_path, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        old_rows = list(reader)

    # Prepare new rows
    new_rows = []
    for old_row in old_rows:
        new_row = {}
        for header in new_headers:
            if header in old_row:
                new_row[header] = old_row[header]
            else:
                new_row[header] = '-'  # Fill new fields with '-'

        new_rows.append(new_row)

    # Write the new CSV
    with open(new_csv_path, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=new_headers)
        writer.writeheader()
        writer.writerows(new_rows)

    print(f"✅ Successfully created {new_csv_path}!")


old_csv_path = "../db/events.csv"
new_csv_path = "../db/events_new.csv"
transform_csv(old_csv_path, new_csv_path)