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

