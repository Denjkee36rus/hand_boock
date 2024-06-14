result = filter(lambda x: sum(map(int, str(x))) % 2 == 0, (32, 64, 128, 256, 512))

print(*list(result))

# Пользовательские функции
# Встроенные функции map, zip, sorted, filter
# Импортируемые функции reduce, cmp_to_key
