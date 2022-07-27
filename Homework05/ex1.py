# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

st1 = 'Привет, Мир! Мы очабв любим Пайтонабв! тебя!'

res = list(filter(lambda x: 'абв' not in x, st1.split()))
print(' '.join(res))

my_str = [word for word in st1.split() if 'абв' not in word]
print(' '.join(my_str))
