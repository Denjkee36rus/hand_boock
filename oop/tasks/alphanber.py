import string


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print('Буквы алфавита:', self.letters)

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num: int = 26  # Приватное статическое свойство, хранящее количество букв в алфавите

    def __init__(self):
        super().__init__('En', string.ascii_lowercase)

    def is_en_letter(self, letter: str) -> bool:
        return letter.lower() in self.letters

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example():
        return 'the quick brown fox jumped over the lazy dog'


# Создаем объект класса Alphabet
alphabet = Alphabet(
    'Русский',
    'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
)

# Выводим буквы алфавита
alphabet.print()

# Выводим количество букв в алфавите
print(
    'Количество букв в алфавите:',
    alphabet.letters_num()
)

english = EngAlphabet()
english.letters_num()
EngAlphabet.example()
english.example()

print(english.lang)
print(english.letters)
print(english.is_en_letter('g'))
