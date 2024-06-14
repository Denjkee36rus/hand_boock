data = []
even = []
odd = []

def enter_results(*args):
    global even, odd
    for item in args:
        if item % 2 == 0:
            even.append(item)
        else:
            odd.append(item)
    return even, odd

def get_sum():
    return round(sum(even), 2), round(sum(odd), 2)


def get_average():
    from functools import reduce
    average_even = reduce(lambda x, y: x + y, even) / len(even)
    average_odd = reduce(lambda x, y: x + y, odd) / len(odd)
    return round(average_even, 2), round(average_odd, 2)

enter_results(3.5, 2.14, 45.2, 37.99)
print(get_sum(), get_average())