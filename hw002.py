# Задача 1. Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр. 
# Пример:
# 6782 -> 23
# 0,56 -> 11

# num = float(input('Введите вещественное число: '))
# a = int(num)
# b = num - int(num)
# summa = 0
# while (a != 0):
#     summa += (a % 10)
#     a //= 10
# while (b != 0):
#     summa += int(b * 10)
#     b = round(b * 10 - int(b * 10), 4)
# print(f'Сумма цифр {summa}')


# Задача 2. Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)

# mult = 1
# result = [*(mult := int(mult * i) for i in range(1, int(input('Введите N: ')) + 1))]
# print(result)

# Решение-2
# lst = []
# for i in range(1, int(input('N: ')) + 1):
#     mult *= i
#     lst.append(result)
# print(lst)


# Задача 3. Задайте список из n чисел последовательности (1 + 1 / n) ** n 
# и выведите на экран их сумму.
# Пример:
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037

# num = int(input('Введите N: '))
# result = [*((1 + 1 / n)**n for n in range(1, num + 1))]
# print(f'{num} -> {sum(result)}')


# # Решение 2
# result = 0
# for n in range(1, int(input('Введите N: '))+1):
#     result += (1 + 1 / n)**n
# print(f'{n} -> {result}')


# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# from random import randint

# num = int(input('Введите N: '))
# lst = [randint(-num, num) for i in range(num)]
# print(lst)
# mult = 1
# with open('file.txt', 'r') as data:
#     for line in data:
#         for i in range(len(lst)):
#             if i == int(line.strip()):
#                 mult = mult * lst[i]
# print(mult)


# 5. Реализуйте алгоритм перемешивания списка.

# import random
# lst = [1, 2, 3, 4, 5]
# random.shuffle(lst)
# print('->', lst)
