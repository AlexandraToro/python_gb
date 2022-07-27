# Создайте программу для игры с конфетами человек против человека.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
from random import randint

mes = ['Возьмите от 1 до 28 конфет: ', 'Ваш ход: ', 'Итак, сколько конфет возьмете? ']


def get_candy() -> int:
    x = int(input(f'{mes[randint(0, 2)]}'))
    while x < 1 or x > 28:
        x = int(input(f'Повторите попытку, необходимо взять от 1 до 28 конфет: '))
    return x


print('Приветствуем вас в игре "Сладкоежки"'
      'На столе лежит 2021 конфета.'
      'За один ход можно забрать не более чем 28 конфет.'
      'Все конфеты достаются игроку сделавшему последний ход.')
candy = 2021
player = 1
count = 0
print('Выбор игры')
v = input('Для игры с друг против друга нажмите 1, для игры против бота нажмите 2: ')
if v == '1':
    print('Проведем жеребьевку: Первым ходит тот, у кого выпало большее число в рандомайзере')
    a = input('Нажмите пробел и Enter для получения первого числа: ')
    if a == ' ':
        print(randint(1, 1001))
    b = input('Нажмите пробел и Enter для получения второго числа: ')
    if b == ' ':
        print(randint(1, 1001))
    print('Игрок, получивший большее число ходит первым. Начинаем!')
    while candy > 0:
        count = get_candy()
        candy -= count
        print(f'Всего конфет: {candy}')
        player += 1
    if player % 2 == 1:
        winner = 2
    else:
        winner = 1
    print(f' Победил игрок номер {winner}')

if v == '2':
    s = input(' Выберите сложность игры: легкая - 1, сложная - 2: ')
    if s == '1':
        print(' Первый ход за вами!')
        while candy > 0:
            if player == 1:
                count = get_candy()
                player = 2
            else:
                count = randint(1, 29)
                player = 1
                print(f'Компьютер забрал {count} конфет{let(count)}')
            candy -= count
            print(f'Всего конфет: {candy}')
        if player == 2:
            print('Поздравляем вас с победой!!!')
        else:
            print('Проигрыш. Удачи в следующий раз')
    else:
        print(' Первый ход за компьютером!')
        while candy > 0:
            if player == 1:
                count = candy % 29
                print(f'Компьютер забрал {count} конфет{let(count)}')
                player = 2
            else:
                count = get_candy()
                player = 1
            candy -= count
            print(f'Всего конфет: {candy}')
        if player == 2:
            print('Проигрыш. Удачи в следующий раз.')
        else:
            print('Поздравляем вас с победой!!!')
