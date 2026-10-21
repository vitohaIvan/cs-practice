def count_items(values: list) -> dict:
    seen = {}
    for i in values:
        if i not in seen:
            seen[i] = 0
        seen[i] += 1
    return seen

def unique_sorted(values: list) -> list:
    return sorted(set(values))

def common(first: list, second: list) -> list:
    result = []
    for i in first:
        if i in second and i not in result:
            result += [i]
    return sorted(result)

def only_in_first(first: list, second: list) -> list:
    return sorted(set(first) - set(second))
