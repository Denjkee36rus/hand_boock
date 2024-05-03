mans: int = int(input())

employees: dict[str, int] = {}
for i in range(mans):
    name: str = input()
    employees[name] = employees.get(name, 0) + 1

final_employees = []
final_employees_2 = []
for key, value in employees.items():
    if value > 1:
        res = f'{key} - {value}'
        final_employees.append((res))
        final_employees_2.append((key, '-', value))

final_employees.sort()
# print(final_employees)
# print(final_employees_2)

if final_employees:
    # Option 1
    # print(*final_employees, sep='\n')

    # Optino 2
    for item in final_employees:
        print(item)

    # Optin 3
    print('\n'.join(final_employees))

else:
    print('Однофамильцев нет')


def custom_join(sequence: list[str] | tuple[str] | set[str] | str,
                separator):
    result = ''
    for i in range(len(sequence)):
        if type(sequence[i]) != str:
            raise ValueError(
                f'Ожидается str получено {type(sequence[i])}'
            )

        result += sequence[i]
        if i != len(sequence) - 1:
            result += separator

    return result


data: list[str] = ['Иванов - 2', 'Петров - 3']
data_2: list[int] = [2, 10, 3]

print(custom_join(data, '\n'))
print(custom_join(data_2, '\n'))
