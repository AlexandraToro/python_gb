# Реализуйте алгоритм перемешивания списка.
from random import randint


def mix_list(our_list: list):
    for i in range(len(our_list)):
        r = randint(0, len(our_list) - 1)
        our_list[i], our_list[r] = our_list[r], our_list[i]
    print(our_list)


new_list = [randint(1, 100) for i in range(10)]
print(new_list)
mix_list(new_list)

