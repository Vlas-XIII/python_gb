# Задача 4. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = 2
coeff = [randint(0, 100) for i in range(k + 1)]

print(coeff)
result = []

for coef in coeff:
    if coef:
        coef = coef if k == 0 else '' if coef == 1 else coef
        degree = 'x' if k == 1 else '' if k == 0 else f'x^{k}'
        temp = f'{coef}{degree}'
        result.append(temp)

    k -= 1
polynom = ' + '.join(result) + ' = 0'
print(polynom)

with open('polynom.txt', 'w', encoding='utf-8') as file:
    file.write(polynom)
