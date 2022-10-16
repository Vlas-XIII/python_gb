# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def encoding(txt):

    count = 1
    result = ''
    for i in range(len(txt) - 1):
        if txt[i] == txt[i + 1]:
            count += 1
        else:
            result = result + str(count) + txt[i]
            count = 1
    result = result + str(count) + txt[-1]

    return result


def decoding(string: str):

    decode_string = ''
    i = 0
    while len(string[i: i + 2]) == 2:
        num, char = string[i: i + 2]
        decode_string += char * int(num)
        i += 2

    return decode_string


text = 'AAAAAvvvv1111   ___ggglk'
print(f"Текст после кодировки: {encoding(text)}")
print(f"Текст после дешифровки: {decoding(encoding(text))}")
