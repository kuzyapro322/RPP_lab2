# ==============================
# Пункт 3.13 — Работа со списками. Операции над списками в Python
# ==============================

# Импорты
# random — для пункта 3.13, чтобы заполнить список случайными целыми числами
import random

n = int(input("Введите количество элементов массива: "))

array = []
i = 0

while i < n:
    number = random.randint(1, 50)
    array.append(number)
    i += 1

print("Исходный массив:")
print(array)

repeat_indexes = []
i = 0

while i < len(array):
    j = 0
    is_repeated = False

    while j < len(array):
        if i != j and array[i] == array[j]:
            is_repeated = True
            break
        j += 1

    if is_repeated:
        repeat_indexes.append(i)

    i += 1

if len(repeat_indexes) == 0:
    print("Повторяющихся элементов нет")
else:
    print("Индексы повторяющихся элементов:")
    print(repeat_indexes)

i = 0

while i < len(array):
    if array[i] < 15:
        array[i] = array[i] * 2
    i += 1

print("Полученный массив:")
print(array)