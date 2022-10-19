# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности,
# список повторяемых и убрать дубликаты из заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

lst = [1, 2, 3, 5, 1, 5, 3, 10]
print(f'Оригинал {lst}')

def duble(lst):
    result = []
    for i in lst:
        if lst.count(i) < 2:
            result.append(i)
    return result

def repeat(lst):
    result = []
    for i in lst:
        if lst.count(i) > 1:
            result.append(i)
    return result

def unic(lst):
    result = []
    for i in range(len(lst)):
        result = [lst[i]]
        for j in range(i, len(lst)):
            if lst[j] > result[len(result) - 1]:
                result.append(lst[j])
        if len(result) != 1:
            break
    return result

print(f'Убрал дубликаты {duble(lst)}')
print(f'Уникальные {unic(lst)}')
print(f'Это сэт {set(lst)}')
print(f'Повторяемые {unic(repeat(lst))}')

