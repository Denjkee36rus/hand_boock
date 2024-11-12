def intern():
    print('Салфетки')


intern()
intern()
intern()


def admin_hosts(name: str | None = None):
    if name is None:
        print('Приветствую Вас!')
    else:
        print(f'Здравствуйте, {name}!')

    # return None


admin_hosts()
admin_hosts('Alex')
admin_hosts('Sara')


# int a; null
#
# []
# 0
# ''
# a: int | None = None
# print(a)
# a = 10
# print(a)


def two_sum(a: int | float, b: int) -> int | float:
    return a + b


print(two_sum(10, 15))

my_var: int | float = two_sum(5, 19)
