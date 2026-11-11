import numpy as np

# Задание 1
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

print('Третий элемент:', hours[2])
print('Последний элемент:', hours[-1])
print('Индексы 2–5:', hours[2:6])
print('Каждый второй:', hours[::2])
print('В обратном порядке:', hours[::-1])


# Задание 3

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18]
])

print('Форма:', temperatures.shape)
print('Количество измерений:', temperatures.ndim)
print('Количество элементов:', temperatures.size)

print('Вторая строка, третий столбец:', temperatures[1, 2])
print('Первая строка:', temperatures[0])
print('Последний столбец:', temperatures[:, -1])

print('Первые две строки без первого столбца:')
print(temperatures[:2, 1:])

print('Центральный блок 2x2:')
print(temperatures[:2, 1:3])

# Задание 4

matrix = np.arange(1, 26).reshape(5, 5)

print('Исходная матрица:')
print(matrix)

a = matrix[:3, :]
print('Первые три строки:')
print(a)
print('Форма:', a.shape)

b = matrix[-2:, :]
print('Последние две строки:')
print(b)
print('Форма:', b.shape)

c = matrix[:, :2]
print('Первые два столбца:')
print(c)
print('Форма:', c.shape)

d = matrix[1:4, 2:5]
print('Строки 1-3, столбцы 2-4:')
print(d)
print('Форма:', d.shape)

e = matrix[-2:, -2:]
print('Правый нижний угол 2x2:')
print(e)
print('Форма:', e.shape)

# Задание 5

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1

print('Изменённый hours:', changed_hours)
print('Исходный hours:', hours)

changed_matrix = matrix.copy()

changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print('Изменённая матрица:')
print(changed_matrix)

print('Исходная матрица:')
print(matrix)

