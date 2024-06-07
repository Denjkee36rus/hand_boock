en = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

ru = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декабрь'
}


def month(number: int, language: str = 'ru'):
    """
    Функция возвращает название заданного месяца.

    :param number: Номер месяца (от 1 до 12).
    :param language: Язык названия месяца. По умолчанию "ru".
    :return: Если номер месяца не найден "Такого месяца нет",
    иначе название месяца с заглавной буквы.
    """

    db: dict[int, str] = ru

    if language == 'en':
        db = en

    return db.get(number, 'Такого месяца нет')


print(month(3, 'en'))
print(month(3, 'ru'))
