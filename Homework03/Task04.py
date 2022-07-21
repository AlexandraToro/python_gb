# Напишите программу, которая будет преобразовывать десятичное число в двоичное.


def get_binary_neg_pos(x: int) -> str:     # с учетом знака числа
    s = ''
    if (x < 0):
        x *= -1
        a = '1'
    else:
        a = '0'
    while x > 0:
        s = str(x % 2) + s
        x = x//2
    s = a+s
    return s


def get_binary(x: int) -> str: 
    s = ''
    if (x < 0):
        x *= -1
    if (x < 0):
        x *= -1
    while x > 0:
        s = str(x % 2) + s
        x = x//2
    return s


x = int(input('Введите десятичное число для перевода в двоичную систему: '))
print(f"Unsigned: {x}-> "+get_binary(x))
print(f"Signed: {x}-> "+get_binary_neg_pos(x))
