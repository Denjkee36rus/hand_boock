# def merge(x, b):
#     spisok = []
#     for i in x:
#         spisok.append(i)
#     for j in b:
#         spisok.append(j)
#     return tuple(sorted(spisok))
#
# print(merge((7, 12), (1, 9, 50)))
# ''.join(sorted(list(x))).join(list(b))


def merge(x, b):
    return ','.join(map(str, sorted(x))) + ','.join(map(str, sorted(b)))

print(merge((7, 12), (1, 9, 50)))

