import csv

from src.csv_repository import keys


def transform_csv(old_csv_path: str, new_csv_path: str):

    with open(old_csv_path, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        old_rows = list(reader)


    new_rows = []
    for old_row in old_rows:
        new_row = {}
        for header in keys:
            if header in old_row:
                new_row[header] = old_row[header]
            else:
                new_row[header] = '-'

        new_rows.append(new_row)

    with open(new_csv_path, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(new_rows)

    print(f"✅ Successfully created {new_csv_path}!")


old_csv_path = "../db/events.csv"
new_csv_path = "../db/events_new.csv"
transform_csv(old_csv_path, new_csv_path)