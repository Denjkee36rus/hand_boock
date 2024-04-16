count_mannyu = int(input())
count_ovsaynyu = int(input())

love_m = set()
love_o = set()

for i in range(count_mannyu):
    name_m = input()
    love_m.add(name_m)
for _ in range(count_ovsaynyu):
    name_o = input()
    love_o.add(name_o)

name_m_o = love_m & love_o

# if len(name_m_o) == 0:
if not name_m_o:
    print('Таких нет')
else:
    print(len(name_m_o))

# TODO: Аннотация типов
