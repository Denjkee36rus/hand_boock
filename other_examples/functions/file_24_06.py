# Рекурсия
import sys


# for i in range(1, 6):
#     print(f'Число {i}')


def say_hello(name):
    result = [10]
    print(f'Привет, {name}!')


def get_range(n):
    # Базовый случай
    if n <= 0:
        return 1
    # print(n)
    return get_range(n - 1)


def fact(num):
    # Базовый случай
    if num <= 1:
        return num
    return num * fact(num - 1)


# Через цикл
num = 6
prod = 1
for i in range(1, num + 1):
    prod *= i
print(prod)

data: str = input('Введите что-нибудь: ')

data_from_std: list[str] = sys.stdin.readlines()

print(data)
print(data_from_std)

if __name__ == '__main__':
    # say_hello('Max')
    # say_hello('Max')
    # say_hello('Max')
    # say_hello('Max')
    # ------------------------
    # get_range(5)
    # ------------------------
    print(fact(6))
    # ------------------------
