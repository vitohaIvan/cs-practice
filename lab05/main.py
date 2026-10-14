from tablestats import read_rows 

with open("events.csv", encoding="utf-8") as file:
    rows = read_rows(file)

for row in rows:
    print(row)

print("Количество записей:", len(rows))
