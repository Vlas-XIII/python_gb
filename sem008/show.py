

def show(data):
    # print(type(data))
    for row in data:
        print(row)


def welcome():
    line = 'Добро пожаловать!'
    decor = len(line) * '-'
    print(decor, line, decor, sep='\n', end='\n\n')


def mes_export():
    line = 'Данные экспортированны'
    decor = len(line) * '-'
    print(decor, line, decor, sep='\n', end='\n\n')


def mes_import():
    line = 'Данные импортированны'
    decor = len(line) * '-'
    print(decor, line, decor, sep='\n', end='\n\n')