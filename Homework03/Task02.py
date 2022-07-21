# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import randint


def get_sum_pair(my_list: list) -> list:
    sec = []
    for i in range((len(my_list)+1)//2):
        sec.append(my_list[i]*my_list[len(my_list)-i-1])
    return sec


my_list = [randint(0, 11) for i in range(1, 6)]
print(my_list)
print(get_sum_pair(my_list))
