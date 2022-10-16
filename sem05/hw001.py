# Задача 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

words = 'Удалим из текста все слова, содержащие "абв". Например: Автобус, автомобиль, вобла'
word = words.lower().split(' ')
print(word)
exclude = ('а' and 'в' and 'б')

for i in reversed(word):
    if exclude in i:
        print(i)
        word.remove(i)
print(word)

test = list(filter(lambda x: not exclude in x, word))
print(test)

# test = list(filter(lambda x: 'а' not in x or 'б' not in x or 'в' not in x, word))
# print(test)

# print(*filter(lambda x: not any(True if ch in x else False for ch in 'абв'), words.split()), sep=' ')
# Не работает с моим текстом

# print(*filter(lambda x: not set(x) >= (set('абв')), words.lower().split()), sep=' ') # issuperset
