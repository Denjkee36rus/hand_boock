def make_matrix(*width, value=0):
    if len(width) == 2:
        value = width[1]

    if isinstance(width[0], int):
        _width = _height = width[0]
    else:
        _width, _height = width[0]

    result = []
    for _ in range(_height):
        row = []
        for _ in range(_width):
            row.append(value)
        result.append(row)
    return result


print(make_matrix(3))
print(make_matrix( (4, 2), 7 ))
print(make_matrix( (4, 2)))
