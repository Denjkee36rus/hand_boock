from string import ascii_lowercase, digits

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper + digits
    def check_card_number(self, number: str):
        """Проверяет строку с номером карты и возвращает булево значение True."""
        string = number.split('-')
        if len(string) != 4:
            return False
        return all(item.isdigit() and len(item) == 4 for item in string)

    def check_name(self, name: str):
        """Проверяет строку с именем и фамилией и возвращает булево значение True."""
        string_name = name.split(' ')
        if len(string_name) != 2:
            return False
        return all(part.isalpha() and part.isupper() for part in string_name) # почему я не могу написать просто isupper , без isalpha???

a = CardCheck()
print(a.check_card_number("1234-5678-9012-3456"))  # Это должно вернуть True
print(a.check_name("SERGEI BALAKIRE"))  # Это должно вернуть True
print(a.check_name("Sergei Balakire"))  # Это должно вернуть False