import string

class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print_letters(self):
        print("Буквы алфавита:", self.letters)

    def letters_num(self):
        return len(self.letters)

# Создаем объект класса Alphabet
alphabet = Alphabet('Русский', 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

# Выводим буквы алфавита
alphabet.print_letters()

# Выводим количество букв в алфавите
print("Количество букв в алфавите:", alphabet.letters_num())


class EngAlphabet(Alphabet):
    __letters_num = 26  # Приватное статическое свойство, хранящее количество букв в алфавите
    def __init__(self):
        super().__init__("En", string.ascii_letters)
        self.lang = "En"
        self.letters = string.ascii_letters
    def is_en_letter(self, letter):
        if letter in string.ascii_uppercase:
            print("Символ является заглавной буквой английского  алфавита")
        else:
            print("Символ не является заглавной буквой английского  алфавита")

    def letters_num(self):
        return self.__letters_num



test_1 = EngAlphabet()
test_1.is_en_letter("В")
print()