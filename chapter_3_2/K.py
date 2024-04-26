mans = int(input())

employees = {}
count = 0
for i in range(mans):
    name = input()
    employees[name] = employees.get(name, 0) + 1

for value in employees.values():
    if value > 1:
        count += value

print(count or 0)
