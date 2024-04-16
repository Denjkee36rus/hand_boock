string_1: str = input()
string_2: str = input()

s_intersection = set(string_1) & set(string_2)

# print(*s_intersection, sep='')
print(''.join(s_intersection))
