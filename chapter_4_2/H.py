string = 'Яндекс использует Python во многих проектах'

print(sorted(string.split(), key=lambda x: (len(x), x.lower())))


# Пример с CodeChick

def snring(arg: str):
    return arg.upper()[::-1]


print(snring("hello world"))
