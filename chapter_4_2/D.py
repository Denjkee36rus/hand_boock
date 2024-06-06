en = {	1:'Janauary',
		2:'February',
		3:'March',
		4:'April',
		5:'May',
		6:'June',
		7:'July',
		8:'August',
		9:'September',
		10:'October',
		11:'November',
		12:'December'		}

ru = {	1:'Январь',
		2:'Февраль',
		3:'Март',
		4:'Апрель',
		5:'Май',
		6:'Июнь',
		7:'Июль',
		8:'Август',
		9:'Сентябрь',
		10:'Октябрь',
		11:'Ноябрь',
		12:'Декабрь'		}
def month(number: int, language: str ='ru'):
    """функция month, которая возвращает название
     заданного месяца с заглавной буквы
     number: Номер месяца (от 1 до 12).
        language: Язык названия месяца (по умолчанию "ru").

    Возвращает:
        Название месяца с заглавной буквы
        или "Такого месяца нет", если номер месяца не найден
     """

    if number in ru.keys() and language == 'ru':
        return ru[number].title()
    elif number in en.keys() and language == 'en':
        return en[number].title()
    else:
        return 'Такого месяца нет'
print(month(3, 'en'))

