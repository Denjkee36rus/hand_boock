# TODO: ДЗ
mans = int(input())

employees = {}
for i in range(mans):
    name = input()
    employees[name] = employees.get(name, 0) + 1
final_employees = []
for key, value in employees.items():
    if value > 1:
        final_employees.append((key, '-', value))
final_employees.sort()
if final_employees:
    for employee in final_employees: # Не совсем понимаю этот кусок мешали скобки.
        print(*employee, sep=' ')
else:
    print('Однофамильцев нет')







