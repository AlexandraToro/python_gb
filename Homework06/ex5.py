# Напишите программу, которая принимает на
# вход вещественное число и показывает сумму его цифр.

num = input('Введите любое вещественное число: ')
# 1 способ
lst = [i for i in num if (i != ',') if (i != '.')]
lst = list(map(int, lst))
print(sum(lst))

# 2 способ
f = lambda x: x != ',' or x != '.'
list1 = list(filter(f, lst))
print(sum(list1))

# + вариант использования enumerate с назначением стартового индекса
str = ['Яна', 'Маша', 'Игорь', 'Юля']
str = list(enumerate(str, 1))
print(str)
