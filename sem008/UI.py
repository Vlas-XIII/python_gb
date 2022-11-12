from variables import *

def menu():
    chapter = '''Что делаем?
0 - Просмотр
1 - Добавить
2 - Удалить
3 - Сохранить
4 - Загрузить
5 - Выйти\n'''

    number = input(f'{chapter} Выбирай: ')
    return number


def get_user():
    user_list = [input(f'{values}: ') for values in headers[1:5]]
    return user_list


def del_user():
    x = input('Для удаления введите id -> ')
    return x

