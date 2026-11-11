import numpy as np

# задание 1
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3, dtype=int)

print('hours:', hours)
print('shape:', hours.shape)
print('ndim:', hours.ndim)
print('size:', hours.size)
print('dtype:', hours.dtype)

print('line:', line)
print('zeros:', zeros)
print('unknown_table:\n', unknown_table)
print('identity:\n', identity)

# Задание 2

print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Индексы 2–5:", hours[2:6])
print("Каждый второй:", hours[::2])
print("В обратном порядке:", hours[::-1])