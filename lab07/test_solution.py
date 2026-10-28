
from solution import *

# 1. reshape_rows
assert reshape_rows([1, 2, 3, 4, 5, 6], 3) == [
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0]
]

assert reshape_rows([1, 2, 3, 4], 2) == [
    [1.0, 2.0],
    [3.0, 4.0]
]

assert reshape_rows([1, 2, 3, 4, 5], 3) == []
assert reshape_rows([], 3) == []
assert reshape_rows([1, 2], 0) == []

print("1. reshape_rows: OK")


# 2. block
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

assert block(matrix, [0, 2], [1, 2]) == [
    [2.0, 3.0],
    [8.0, 9.0]
]

assert block(matrix, [2, 0], [2, 1]) == [
    [9.0, 8.0],
    [3.0, 2.0]
]

assert block(matrix, [1], [0, 2]) == [[4.0, 6.0]]
assert block(matrix, [], [0, 1]) == []
assert block(matrix, [0, 2], []) == [[], []]
assert block([], [], []) == []

print("2. block: OK")


# 3. column_means
assert column_means([[1, 2], [3, 4], [5, 6]]) == [3.0, 4.0]

assert column_means([[1, 2, 3]]) == [1.0, 2.0, 3.0]

assert column_means([[1], [2], [3]]) == [2.0]

assert column_means([[1], [2], [2]]) == [1.666667]

assert column_means([]) == []

print("3. column_means: OK")


# 4. column_range
assert column_range([[1, 2], [5, 7]], 1) == 5.0

assert column_range([[1, 2], [5, 7]], 0) == 4.0

assert column_range([[3, 4]], 1) == 0.0

assert column_range([[1.1], [2.23456789]], 0) == 1.134568

assert column_range([], 0) == 0.0

print("4. column_range: OK")

print("\nВсе 21 тест пройден!")

