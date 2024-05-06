numbers = [3, 1, 2, 3, 2, 2, 1]

result = ' - '.join(set([str(diggit) for diggit in numbers]))
print(result)