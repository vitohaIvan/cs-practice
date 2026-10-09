def winner(names: list[str], scores: list[float]) -> str:
    best = 0
    for i in range(len(scores)):
        if scores[i] > scores[best]:
            best = i
    return names[best]

def average(scores: list[float]) -> float:
    if len(scores) == 0:
        return 0.0
    tot = 0
    for i in scores:
        tot += i
    return round(tot / len(scores), 2)

def above_average(names: list[str],scores: list[float]) -> list[str]:
    answ = []
    av = average(scores)
    for i in range(len(scores)):
        if scores[i] > av:
            answ += [names[i]]
    return answ

def ranking(names: list[str], scores: list[float]) -> list[str]:
    seen = {}
    for i in range(len(names)):
        seen[names[i]] = scores[i]
    return sorted(seen,key=seen.get, reverse=1)
print(average([1,2,3]))
