import csv

values = []
rejected = 0
with open("readings.csv", newline="", encoding="utf-8") as stream:
    for row in csv.DictReader(stream):
        try:
            value = int(row["value"])
        except ValueError:
            rejected += 1
            continue
        values.append(value)
print(len(values), sum(values), min(values), max(values), rejected)
