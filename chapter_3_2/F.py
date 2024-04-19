# TODO: ДЗ

count_mannyu = int(input())
count_ovsaynyu = int(input())

love_m = set()
love_o = set()

for i in range(count_mannyu + count_ovsaynyu):
    name = input()

    if name in love_m:
        love_o.add(name)
    else:
        love_m.add(name)

name_m_o = love_m ^ love_o

if len(name_m_o) == 0:
    print('Таких нет')
else:
    name_m_o = list(name_m_o)
    name_m_o.sort()
    print(*name_m_o, sep='\n')