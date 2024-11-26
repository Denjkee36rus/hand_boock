import sys


class StreamData:
    def create(self, fields, lst_values):
        length: int = len(fields)
        if length != len(lst_values):
            return False

        for i in range(length):
            self.__dict__[fields[i]] = lst_values[i]


        return True

    def __str__(self):
        if not self.__dict__:
            return 'None'

        return '; '.join(self.__dict__)


class StreamReader:
    FIELDS: tuple[str, ...] = ('id', 'title', 'pages')

    def readlines(self) -> tuple[StreamData, bool]:
        lst_in: list[str] = list(
            map(str.strip, sys.stdin.readlines())
        )
        sd = StreamData()
        res = sd.create(fields=self.FIELDS, lst_values=lst_in)
        return sd, res


if __name__ == '__main__':
    sr = StreamReader()
    obj, result = sr.readlines()

    print(obj)
    print(result)

"""
10
"Питон - основы мастерства"
512
"""
