# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
from random import randint

def get_polynomial(k:int)->str:
    i = 1
    res = str(randint(0, 101))
    while i <= k:
        a = randint(0, 101)
        if a != 0:
            if i == 1:
                res = f'{str(a)}*x + {res}'
            else:
                res = f'{str(a)}*x**{i} + {res}'
        i += 1
    res = res + ' = 0'
    return res

k = int(input('Введите cтепень: '))
st = get_polynomial(k)
with open ('file.txt','w') as my_file:
    my_file.write(f'k = {k} => {st} \n')
