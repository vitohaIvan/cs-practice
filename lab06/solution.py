def count_items(values: list) -> dict:
    seen = {}
    for i in values:
        if i not in seen:
            seen[i] = 0
        seen[i] += 1
    return seen


