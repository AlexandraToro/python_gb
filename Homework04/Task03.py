# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint


my_list = [randint(1, 12) for i in range(12)]
lst = []
print(my_list)
for i in range(len(my_list)):
    count = 0
    j = 0
    while j < len(my_list):
        if my_list[i] == my_list[j] and i != j:
            count = 1
            break
        else:
            j += 1
    if count == 0:
        lst.append(my_list[i])
print(lst)
