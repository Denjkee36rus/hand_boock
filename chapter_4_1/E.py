def split_numbers(a):
    my_string = []
    for diggit in str(a).split(' '):
        my_string.append(int(diggit))
    return tuple(my_string)


def split_numbers_2(line: str) -> tuple[int, ...]:
    return tuple(
        int(num) for num in line.split()
    )


print(split_numbers('1 -2 3 -4 5'))
print(split_numbers_2('1 -2 3 -4 5'))

print(split_numbers('1'))
print(split_numbers_2('1'))

# Кортеж с одним элементом
nums: tuple[int] = (10,)
