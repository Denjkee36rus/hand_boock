def number_length(a):
    return len(str(abs(a)))


def number_length_2(a: int) -> int:
    if a < 0:
        a = abs(a)

    count: int = 0
    while a > 0:
        a //= 10
        count += 1

    return count or 1


print(number_length(-12345))
print(number_length_2(-12345))

print(number_length(0))
print(number_length_2(0))

print(number_length(123))
print(number_length_2(123))
