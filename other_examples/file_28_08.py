class Factory:
    @staticmethod
    def build_sequence():
        return []

    @staticmethod
    def build_number(string):
        return int(string)


def parse_format(arg_string: str, factory):
    """Парсит строку.
    :param arg_string: Строка состоящая из числовых символов.
    :param factory: Класс фабрика.
    :return:
    """
    seq = factory.build_sequence()
    for sub in arg_string.split(","):
        item = arg_string.build_number(sub)
        seq.append(item)
    return seq


parse_format("1, 2, 3", Factory)


def sort(arr: list):
    arr.count("5")
