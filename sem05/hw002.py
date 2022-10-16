# Задача 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

def player_turn(name):
    x = int(input(f'{name}, введите количество конфет, которое возьмете от 1 до 28: '))
    while x < 1 or x > 28:
        x = int(input(f'{name}, введите корректное количество конфет: '))
    return x


def result_turn(name, x, count, candy):
    print(f'Ход>{count} Игрок>{name}, взял {x} конфет. На столе осталось {candy} конфет.')


user1 = input('Имя первого игрока: ')
user2 = input('Имя второго игрока: ')
candy = int(input('Количество конфет на столе: '))
flag = randint(0, 2)
if flag:
    print(f'Первый ходит {user1}')
else:
    print(f'Первый ходит {user2}')

count = 0

while candy > 28:
    if flag:
        x = player_turn(user1)
        count += 1
        candy -= x
        flag = False
        result_turn(user1, x, count, candy)
    else:
        x = player_turn(user2)
        count += 1
        candy -= x
        flag = True
        result_turn(user2, x, count, candy)

if flag:
    print(f'Выиграл {user1}')
else:
    print(f'Выиграл {user2}')

