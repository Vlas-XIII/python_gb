import UI
import view
from function import create_book, add_contact, reading, del_contact

def start():
    button = UI.menu()
    if button == '1':
        create_book()
        start()
    elif button == '2':
        view.show(add_contact())
        print('Контакт добавлен')
        start()
    elif button == '3':
        del_contact(reading())

        print('Контакт удален!')
        start()
    elif button == '4':
        view.show_book(reading())
        print('Вывели список!')
        start()
    elif button == '5':
        print('До новых встреч!')
