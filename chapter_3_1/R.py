"""
0100011100
Берем символ смотрим следующий символ (справа):

Если следующий символ равен текущему, то увеличиваем счетчик
Иначе: выведем текущий элемент и его кол-во. Обнуляем.
"""



example = input()
temp_count = 1
for i in range(len(example) - 1):
    if example[i] == example[i + 1]:
        temp_count += 1
    else:
        print(example[i], temp_count)
        temp_count = 1
print(example[-1], temp_count)


# TODO: ДЗ
