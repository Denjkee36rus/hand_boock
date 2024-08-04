from pprint import pprint


class Translator:
    __new_dict: dict[str, list[str]] = {}

    def add(self, eng: str, rus: str) -> None:
        eng, rus = eng.lower(), rus.lower()
        value: list[str] = self.__new_dict.get(eng, [])
        if rus not in value:
            # current_data.append(rus)
            self.__new_dict[eng] = value + [rus]

    # --skip
    def add_extend(self, eng: str, rus: list[str]) -> None:
        eng = eng.lower()
        rus = [word.lower() for word in rus]
        value: list[str] = self.__new_dict.get(eng, [])

        diff: list[str] = list(set(rus).difference(value))
        self.__new_dict[eng] = value + diff

    def remove(self, eng: str) -> list[str]:
        return self.__new_dict.pop(eng.lower())

    def translate(self, eng: str) -> str:
        return ' '.join(self.__new_dict.get(eng.lower(), []))

    # --skip
    def get_all_words(self) -> None:
        pprint(self.__new_dict)


if __name__ == '__main__':
    a: Translator = Translator()
    a.add('tree', 'дерево')
    a.add('car', 'машина')
    a.add('car', 'автомобиль')
    a.add('leaf', 'лист')
    a.add('river', 'река')
    a.add('go', 'идти')
    a.add('go', 'ехать')
    a.add('go', 'ходить')
    a.add('milk', 'молоко')
    a.add_extend('go', ["abba", "abcd", "abba"])
    a.add_extend('go', ["def", "if", "for", "dEf", "DEf"])

    # ---------------------
    a.remove('car')
    print(a.translate('go'))
    a.get_all_words()