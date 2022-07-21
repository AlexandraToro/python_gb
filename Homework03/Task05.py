# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

x = int(input('Введите любое положительное число: '))


def fibonacci(n):
    if (n == 0):
        return 0
    elif(n == 1 or n == 2):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def negafibonacci(n):
    if (n == 0):
        return 0
    elif (n == -1):
        return 1
    else:
        return (negafibonacci(n+2)-negafibonacci(n+1))


for i in range(-x, 0):
    print(negafibonacci(i), end=' ')

for i in range(x+1):
    print(fibonacci(i), end=' ')
