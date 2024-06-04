def make_matrix(*width, value = 0):
    result = []
    for i in width:
        result.append(value)
        return result * value




print(make_matrix((4, 2), 1))