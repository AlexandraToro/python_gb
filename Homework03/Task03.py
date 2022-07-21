# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов

from random import uniform


def get_fractional_part(my_list: list) -> list:
    s = []
    for i in my_list:
        s.append(round(i-int(i), 2))
    return s


def minimal(my_list: list) -> float:
    min = my_list[0]
    for i in my_list:
        if i < min:
            min = i
    return min


def maximal(my_list: list) -> float:
    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
    return max


my_list = [round(uniform(1.1, 5.5), 2) for i in range(1, 10)]
print(my_list)
res = get_fractional_part(my_list)
print(res)
print(round(maximal(res)-minimal(res), 2))
