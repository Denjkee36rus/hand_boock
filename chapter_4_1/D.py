RU = {1: 'Янаварь',
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
      12: 'Декабрь'}

EN = {1: 'January',
      2: 'February',
      3: 'March',
      4: 'March',
      5: 'May',
      6: 'June',
      7: 'July',
      8: 'August',
      9: 'September',
      10: 'October',
      11: 'November',
      12: 'December'}


def month(num, lang):
    global RU, EN
    data = RU if lang == 'ru' else EN

    # if lang == 'ru':
    #     data = RU
    # else:
    #     data = EN

    return data[num]


print(month(12, "en"))
print(month(1, "ru"))


# Option 2
def month(day: int, language: str):
    languages = {
        'en': {
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
            12: 'December',
        },

        'ru': {
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
            12: 'Декабрь',
        },
    }
    if language == 'en':
        return languages[language].get(day)
    elif language == 'ru':
        return languages[language].get(day)

    return 'Unknown'
