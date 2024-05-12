ru = {1: 'Янаварь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь',
      10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}

en = {1: 'January', 2: 'February', 3: 'March', 4: 'March', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September',
      10: 'October', 11: 'November', 12: 'December'}
def month(a, b):
    if a in ru.keys() and b == ru:
        return ru[a]
    if a in en.keys() and b == en:
        return en[a]
print(month(12, en))
# а что если поменять местами ключи и значения
# как можно улучшить код ????