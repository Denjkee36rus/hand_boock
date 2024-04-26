# TODO: ДЗ
from collections import Counter
mans = int(input())
spisok = {}

spisok_2 = 0

for i in range(mans):
    names = input()
    spisok[names] = spisok.get(names, 0) + 1
for key, value in spisok.items():
    if value > 1:
        spisok_2 += value
if spisok_2 > 0:
    print(spisok_2)
else:
    print(0)









