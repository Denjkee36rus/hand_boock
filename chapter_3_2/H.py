data = {}

for _ in range(int(input())):
    # line = input().split()  # Иванов манная овсяная
    # name = line[0]
    # other = line[1:]
    name, *other = input().split()
    data[name] = other

query = input()

result = []
for key, value in data.items():
    if query in value:
        result.append(key)

if result:
    result.sort()
    print(*result, sep='\n')
else:
    print('Таких нет')
