import sys


class DataBase:
    lst_data: list[dict[str, str]] = []
    FIELDS: tuple[str, ...] = ('id', 'name', 'old', 'salary')

    def select(self, a: int, b: int) -> list:
        return self.lst_data[a:b + 1]

    def insert(self, data: list[str]) -> None:
        # TODO: Здесь нужно исправить добавление записей,
        #  в параметр data приходит следующий список:
        #  ['1 Sergey 35 120000', '2 Fedor 23 12000', '3 Ivan 13 1200'].
        #  Нужно улучшить решение.

        self.lst_data.append(dict(zip(self.FIELDS, data)))


if __name__ == '__main__':
    # INFO: Здесь опечатались, метод readlines() должен быть
    lst_n: list[str] = list(map(str.strip, sys.stdin.readlines()))
    # print(lst_n)  # DEBUG

    a = DataBase()
    a.insert(lst_n)
    print(a.lst_data)

"""
1 Sergey 35 120000
2 Fedor 23 12000
3 Ivan 13 1200
"""
