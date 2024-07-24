import sys

lst_n = list(map(str.strip, sys.stdin.readline()))


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        self.lst_data.insert(data)

    def select(self, a, b):
        pass
