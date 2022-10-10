# Задача 5 Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
import os

dir = 'files'
txt_files = [file for file in os.listdir(dir) if file.endswith('.txt')]
result = {}
for txt_file in txt_files:
    with open(f'{dir}\\{txt_file}', encoding='utf-8') as f:
        polynom = filter(lambda x: x not in ('+', '=', '0'), f.read().split())

    for term in polynom:
        if 'x^' in term:
            coeff, degree = map(lambda x: int(x) if x else 1, term.split('x^'))
            result[degree] = result.get(degree, 0) + coeff
        elif 'x' in term:
            coeff, _ = map(lambda x: int(x) if x else 1, term.split('x'))
            result[1] = result.get(1, 0) + coeff
        else:
            result[0] = result.get(0, 0) + int(term)

result = sorted(result.items(), reverse=True)
# print(result)
terms = []
for degree, coeff in result:
    coeff = coeff if degree == 0 else '' if coeff == 1 else coeff
    degree = 'x' if degree == 1 else '' if degree == 0 else f'x^{degree}'
    temp = f'{coeff}{degree}'

    terms.append(temp)

sum_polynom = ' + '.join(terms) + ' = 0'
print(sum_polynom)