class Factory:
    @staticmethod
    def build_sequence():
        return []
    @staticmethod
    def build_number(string):
        return int(string)


class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence() # не совсем пойму строчку кода
        for sub in string.split(","):
            item = factory.build_number(sub) # тоже лучше объснить
            seq.append(item)
        return seq


res = Loader.parse_format("4, 5, -6", Factory)

print(*res)

print(Loader.parse_format('1,2,5', Factory))

