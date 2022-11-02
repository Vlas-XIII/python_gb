import json
import csv

BD = []

# with open('phone_book.csv', 'r', encoding='utf-8') as file:
#     counter = len(file.readlines())

def create_book():
    """Создание файла"""
    # with open('book.json', 'w') as fson:
    #     json.dump(BD, fson, indent=2)

    with open('phone_book.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(('ID', 'lastname', 'name', 'phone'))

def add_contact():
    """Принимаем данные и собираем вместе"""
    # global counter
    global BD
    with open('phone_book.csv', 'r', encoding='utf-8') as file:
        counter = len(file.readlines())
    counter += 1
    lastname = input('фамилия: ')
    name = input('имя: ')
    phone = input('телефон: ')
    headers = ['ID', 'lastname', 'name', 'phone']
    result = [str(counter), lastname, name, phone]
    json_result = dict(zip(headers, result))

    # with open ('book.json', 'r+') as fson:
    #     BD = json.load(fson)
    #     BD.append(json_result)
    #     print(BD)
    #     json.dumps(BD, ensure_ascii=False)

    with open('phone_book.csv', 'a', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(result)

        # counter, lastname, name, phone
    return json_result


def reading():
    """Чтение файла"""
    with open('phone_book.csv', 'r', encoding='utf-8') as file:
        data = csv.reader(file, delimiter=',')
        test = list(data)
        # print(test)
    return test


def del_contact(data):
    """Удаляем строку"""
    ids = int(input('Введите id для удаления: '))
    data.pop(ids)
    # print(test)
    return data

