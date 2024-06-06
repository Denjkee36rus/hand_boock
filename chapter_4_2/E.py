def to_string(*data, sep=' ', end='\n'):
    return sep.join(map(str, data))
print(to_string([7, 3, 1, "hello", (1, 2, 3)]))