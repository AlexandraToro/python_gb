# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
from random import randint


def multi_num(bingo: list):
    elements = list(
        map(int, input('Введите номера позиций через пробел (любые от 1 до n): ').split()))
    print(f'Номера позиций для умножения:{elements}')
    result = 1
    for j in elements:
        result *= bingo[j - 1]
    print(f'Итог: {result}')


n = int(input('Введите количество элементов n = '))
my_list = [randint(-n, n) for i in range(n)]
print(my_list)
multi_num(my_list)
