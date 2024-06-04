# def make_list(length, value = 0):
#     result = []
#     for i in range(length):
#         result.append(value)
#     return result
# print(make_list(3, 1))

def make_list(length, value=0):
    return [value] * length


print(make_list(5,1))
