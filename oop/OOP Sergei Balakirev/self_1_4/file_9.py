import sys

lst_n: list[str] = list(map(str.strip, sys.stdin.readlines()))
class DataBase:
    lst_data: list[dict[str, str]] = []
    FIELDS: tuple[str, ...] = ('id', 'name', 'old', 'salary')


    def insert(self, data: list[str]) -> None:
        # TODO: Здесь нужно исправить добавление записей,
        #  в параметр data приходит следующий список:
        #  ['1 Sergey 35 120000', '2 Fedor 23 12000', '3 Ivan 13 1200'].
        #  Нужно улучшить решение.
        for item in data:
            item = item.split()
            self.lst_data.append(dict(zip(self.FIELDS, item)))

    def select(self, a, b):
        result = []
        for row in self.lst_data[a:b + 1]:
            result.append(' '.join(row.values()))
        print(*result, sep = '\n')







# if __name__ == '__main__':
#     # INFO: Здесь опечатались, метод readlines() должен быть
#     lst_n: list[str] = list(map(str.strip, sys.stdin.readlines()))
#     pass
    # print(lst_n)  # DEBUG

a = DataBase()
a.insert(lst_n)
a.select(0,7)


"""
1 Sergey 35 120000
2 Fedor 23 12000
3 Ivan 13 1200
"""