from tablestats import *

filename = input()

with open(filename, encoding="utf-8") as file:
    rows = read_rows(file)

counts = count_types(rows)
print(len(rows))
print(len(counts))
print(total_minutes(rows, "ошибка"))

with open("summary.csv", "w", encoding="utf-8") as file:
    file.write(to_csv(counts))
