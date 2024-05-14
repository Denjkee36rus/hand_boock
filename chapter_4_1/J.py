def merge(data_1: tuple[int, ...],
          data_2: tuple[int, ...]) -> tuple[int, ...]:
    result: list[int] = []
    for left, right in zip(data_1, data_2):
        if left > right:
            result.extend([right, left])
        elif right > left:
            result.extend([left, right])
        else:
            result.extend([right, left])

    first_length = len(data_1)
    second_length = len(data_2)
    if first_length > second_length:
        result.extend(data_1[second_length:])
    elif second_length > first_length:
        result.extend(data_2[first_length:])

    return tuple(result)


print(merge((1, 2), (3, 4, 5)))
print(merge((7, 12), (1, 9, 50)))
print(merge((7, 12, 90), (1, 9)))
print(merge((7, 12, 90), (1, 9, 100)))
