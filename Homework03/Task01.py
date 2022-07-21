# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции
from random import randint


def get_sum_odd(a: list) -> int:
    s = 0
    for i in range(len(a)):
        if i % 2 != 0:
            s += a[i]
    return s


my_list = [randint(0, 11) for i in range(1, 7)]
print(my_list)
print(get_sum_odd(my_list))
