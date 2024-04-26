from pprint import pprint

s = """А — A
Б — B
В — V
Г — G
Д — D
Е — E
Ё — E
Ж — ZH
З — Z
И — I
Й — I
К — K
Л — L
М — M
Н — N
О — O
П — P
Р — R
С — S
Т — T
У — U
Ф — F
Х — KH
Ц — TC
Ч — CH
Ш — SH
Щ — SHCH
Ы — Y
Э — E
Ю — IU
Я — IA"""

rows = s.split('\n')

letters = {}
for row in rows:
    key, value = row.split(' — ')

    letters[key] = value

# pprint(letters)

# Solve

data = {
    'Ё': 'E',
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ж': 'ZH',
    'З': 'Z',
    'И': 'I',
    'Й': 'I',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'KH',
    'Ц': 'TC',
    'Ч': 'CH',
    'Ш': 'SH',
    'Щ': 'SHCH',
    'Ы': 'Y',
    'Э': 'E',
    'Ю': 'IU',
    'Я': 'IA'
}

text = input()

translit = ''
for char in text:
    if char.isalpha():
        if char.isupper():
            translit += data.get(char, '').capitalize()
        else:
            translit += data.get(char.upper(), '').lower()
    else:
        translit += char

print(translit)
