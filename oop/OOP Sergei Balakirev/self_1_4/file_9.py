import sys

lst_n = list(map(str.strip, sys.stdin.readline()))


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        self.lst_data.append(dict(zip(self.FIELDS, data)))


a = DataBase()
a.insert(lst_n)
print(a.lst_data)