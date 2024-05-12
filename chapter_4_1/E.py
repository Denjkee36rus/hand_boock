def split_numbers(a):
    my_string = []
    for diggit in str(a).split(' '):
        my_string.append(int(diggit))
    return tuple(my_string)
print(split_numbers('1 -2 3 -4 5'))


