numbers = [1, 2, 3, 4, 5]

result = {x for x in numbers if round(x ** 0.5) ** 2 == x}
print(result)