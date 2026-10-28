import numpy as np
def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if (width <= 0) or (len(values) % width != 0):
        return []
    arr = np.asarray(values, dtype=float)
    result = arr.reshape(len(values) // width, width)
    return result.tolist()

def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    arr = np.asarray(matrix, dtype=float)

    if arr.size == 0 or not rows:
        return []
    if not columns:
        return [[] for _ in rows]
    result = arr[np.ix_(rows,columns)]
    return result.tolist()

def column_means(matrix: list[list[float]]) -> list[float]:
    arr = np.asarray(matrix, dtype=float)

    if arr.size == 0:
        return []
    result = arr.mean(axis=0)
    return result.round(6).tolist()

def column_range(matrix: list[list[float]], column: int) -> float:
    arr = np.asarray(matrix, dtype=float)

    if arr.size == 0:
        return 0.0
    col = arr.T[column] 
    m_min = min(col)
    m_max = max(col)
    return round(float(m_max - m_min), 6)



