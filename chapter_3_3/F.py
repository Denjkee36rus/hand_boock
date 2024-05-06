text = 'Мама мыла раму!'
result = {letter: text.lower().count(letter) for letter in text.lower() if letter.isalpha()}
print(result)


