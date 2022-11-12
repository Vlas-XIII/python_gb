import UI
from show import show, welcome, mes_export, mes_import
from function import create_db, user_insert, view_db, delete_record, user_insert_list, save, load

def start():
    welcome()
    create_db()
    flag = True
    while flag:
        button = UI.menu()
        match button:
            case '0':
                """Просмотр файла"""
                show(view_db())
            case '1':
                """Добавить запись"""
                user_insert(UI.get_user())
            case '2':
                """Удалить запись"""
                delete_record(UI.del_user())
            case '3':
                """Сохранить"""
                save(view_db())
                mes_export()

            case '4':
                """Загрузить"""
                user_insert_list(load())
                mes_import()

            case '5':
                print('До новых встреч!')
                flag = False

            case _:
                print('Попробуй снова')