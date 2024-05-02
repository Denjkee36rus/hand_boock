# TODO: ДЗ

count_dishes = int(input())
spisok_dishes = {}
for _ in range(count_dishes):
    name_dishes = input()
    spisok_dishes[name_dishes] = 0

count_day = int(input())

for _ in range(count_day):
    count_dishes_2 = int(input())
    for d in range(count_dishes_2):
        meet = input()
        spisok_dishes[meet] = spisok_dishes.get(meet, 0) + 1
final_spisok = []
for key, value in spisok_dishes.items():
    if value == 0:
        final_spisok.append(key)
final_spisok.sort()
if final_spisok:
    print(*final_spisok, sep='\n')
else:
    print('Готовить нечего')











