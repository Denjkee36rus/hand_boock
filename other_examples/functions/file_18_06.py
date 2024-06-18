# Функции высшего порядка


# def example_1(*args):
#     print(args, type(args))
#
#
# def example_2(name):
#     print(f"Название товара: {name}", type(name))
#
#
# def example_3(foo):
#     foo("Привет, Мир!")
#     # print("Привет, Мир!")
#
#
# def custom_print(*args):
#     print(args)
#
#
# example_1(1, 2, 3)
# example_2("Машина")
# example_3(foo=custom_print)

# ----------------------------

# items = ["abba", "cacathh", "gfg", "fd"]
# print(max(items, key=len))


# def custom_map(func, data):
#     result = []
#     for item in data:
#         item = func(item)
#         result.append(item)
#     return result
#
#
# print(list(map(int, ["1", "2", "3"])))
# print(custom_map(int, ["1", "2", "3"]))

# ----------------------------

# Декораторы
def get_info(func):
    def inner(*args, **kwargs):
        print(f"Вызываем {func.__name__}")
        print(func(*args, **kwargs))
        print(f"Функция {func.__name__} заканчивает работу")

    return inner


# @example_1
# @example_2
# @example_3
@get_info
def generate_range(num):
    result = [i for i in range(num)]
    return result


@get_info
def custom_map(func, data):
    result = []
    for item in data:
        item = func(item)
        result.append(item)
    return result


generate_range(10)
custom_map(int, ["1", "2", "3"])

# https://ru.hexlet.io/courses/python-functions/lessons/decorators/theory_unit
# https://habr.com/ru/companies/otus/articles/727590/


# ----------------------------
# ----------------------------
# ----------------------------
