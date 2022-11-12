import os
import json
import sqlite3
from variables import *


def create_db():
    try:
        sqlite_connection = sqlite3.connect(name_db)
        cursor = sqlite_connection.cursor()

        cursor.execute(table_users)
        sqlite_connection.commit()

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе функции: create_db с SQLite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()



def user_insert(data):
    try:
        sqlite_connection = sqlite3.connect(name_db)
        cursor = sqlite_connection.cursor()

        cursor.execute(insert_user, data)
        sqlite_connection.commit()

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе функции: user_insert с SQLite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()



def user_insert_list(data):
    try:
        sqlite_connection = sqlite3.connect(name_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        cursor.executemany(insert_user, data)
        sqlite_connection.commit()
        print("Пользовател внесен")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе функции: user_insert с SQLite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def view_db():
    try:
        sqlite_connection = sqlite3.connect(name_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        cursor.execute(view_all)
        result = cursor.fetchall()
        # print(len(result))
        # print(type(result))



        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе функции: view_db с SQLite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()


    return result


def delete_record(data):
    try:
        sqlite_connection = sqlite3.connect(name_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        cursor.execute(sql_delete_query, data)
        sqlite_connection.commit()
        print("Запись успешно удалена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")



def save(data):
    res = {user[0]: dict(zip(headers[1:5], user[1:5])) for user in data}
    with open('book.json', 'w', encoding='utf-8') as fson:
        json.dump(res, fson, ensure_ascii=False, indent=4)
        # for i in BD[0:]:
        #     json.dump(i, fson, ensure_ascii=False, indent=4)


def load():
    # data = [json.loads(line) for line in open('book.json', 'r', encoding='utf-8')]
    # print(data)
    res = []
    with open('book.json', 'r', encoding='utf-8') as fson:
        text = json.load(fson)
        # print(text)
        for value in text.values():
            result = (value["Фамилия"], value["Имя"], value["Телефон"], value["email"])
            res.append(result)
            # print(result)
            # for elem in value.values():
            #     print(elem)
    return res

