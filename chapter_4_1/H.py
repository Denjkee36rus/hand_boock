def is_palindrome(data: int | str | tuple | list) -> bool:
    """Определяет палиндром или нет.

    Принимает натуральное число, строку, кортеж или список,
    а возвращает логическое значение: True — если передан
    палиндром, а в противном случае — False.

    :param data: Входные данные, натуральное число, строку, кортеж или список.
    :return: Булевое значение.
    """
    # if type(data) == int:
    # if type(data) == str:
    if isinstance(data, (int, str)):
        return str(data) == str(data)[::-1]
    return data == data[::-1]


print(is_palindrome(123))  # False
print(is_palindrome([1, 2, 1, 2, 1]))  # True
print(is_palindrome('1221'))  # True
print(is_palindrome((1, 2, 1, 2, 1)))  # True
