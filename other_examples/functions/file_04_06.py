# Позиционные и именованные аргументы.


# Позиционные
# def pizza_margarita(ingredients: list[str], size: int = 23) -> str:
#     print(f'\nГотово!\nИнгредиенты: {ingredients}\nРазмер: {size}')
#
#
# pizza_margarita(['abc'])


#

# first, *other = ['a', 'b', 'c', 'd']
#
# print(type(first), type(other))
# print(first, other)
#
#
# print(43, 324, 35, 56, 34, 7657,)


# ---------------------------

# def pizza_margarita(*ingredients, size: int = 23):
#     # print(f'\nГотово!\nИнгредиенты: {ingredients}\nРазмер: {size}')
#
#     for item in ingredients:
#         print(f'{item}')
#
#     data: list = list(ingredients)
#
#     print(type(ingredients), ingredients)
#
#
# pizza_margarita('соус', [True, False], 'сыр', 10, 'томаты', 43, 'колбаса', 'шампиньоны', size=27)
#
# first, *other = ('a', 'b', 'c', 'd')
# print(first, type(other))

# data_2 = ('a', 'b', [10, 20, 30], 'c', 'd')
# data_2[2][1] = 1000
# print(data_2)

# ---------------------------


# def simple_foo(*values, other: str | int = '*'):
#     result = []
#
#     if len(values) == 1:
#         size = values[0]
#
#         for i in range(size):
#             row = []
#             for j in range(size):
#                 row.append(other)
#             result.append(row)
#
#     else:
#         # width, height = values
#         width = values[0]
#         height = values[1]
#
#         for i in range(width):
#             row = []
#             for j in range(height):
#                 row.append(other)
#             result.append(row)
#
#
#     print(result)
#
#
# simple_foo(2, other=0)
# simple_foo(3, 3, other=9)


def all_types(*args):
    print(args)

    for item in args:
        if isinstance(item, (int, float)):
            print(f'Значение {item} числовое')
        elif isinstance(item, set):
            print(f'Значение {item} множество')
        elif isinstance(item, list):
            print(f'Значение {item} список')
        else:
            print(f'Значение {item} типа {type(item)}')


all_types(
    10,
    1.6489,
    'abc',
    [8, 5, 1, -3],
    ('a', 'b', 'c'),
    {1, 2, 3},
    {'login': 'admin', 'password': '1234'},
)
