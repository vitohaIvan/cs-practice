def read_rows(stat: list[str]) -> list[dict]:
    rows = []
    header = []

    for l in stat:
        l = l.strip()  
        if l == '':
            continue
        part = l.split(',')
        if header == []:
            header = part
            continue
        if len(part) != len(header):
            continue
        
        row = {}
        for i in range(len(header)):
            row[header[i].strip()] = part[i].strip()
        rows += [row]
    return rows

def count_types(rows: list[dict]) -> dict:
    answ = {}

    for r in rows:
        type = r['тип']
        
        if type not in answ:
            answ[type] = 0
        answ[type] += 1
    return answ

def total_minutes(rows: list[dict], kind: str) -> float:
    total = 0.0 
    for r in rows:
        if r['тип'] == kind:
            try:
                minutes = float(row["минуты"].replace(",", "."))
                total += minutes
            except ValueError:
                continue
    return round(total,1)

