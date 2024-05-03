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

# Option 2
count: int = int(input())
today_dishes: set[str] = set()
for _ in range(count):
    dish: str = input()
    today_dishes.add(dish)

has_dishes: set[str] = set()
days: int = int(input())
for _ in range(days):
    curr_day_dish_count = int(input())
    for _ in range(curr_day_dish_count):
        dish: str = input()
        has_dishes.add(dish)

result: set[str] = today_dishes.difference(has_dishes)
# result: set[str] = today_dishes - has_dishes

print(*sorted(result) or 'Готовить нечего', sep='\n')
# if result:
#     print(*sorted(result), sep='\n')
# else:
#     print('Готовить нечего')
