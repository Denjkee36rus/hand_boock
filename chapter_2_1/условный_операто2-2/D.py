petya_speed = int(input())
vasay_speed = int(input())
tolay_speed = int(input())
if tolay_speed < vasay_speed < petya_speed:
    print(f'1. Петя', f'2. Вася', f'3. Толя', sep='\n')
elif tolay_speed > vasay_speed > petya_speed:
    print(f'1. Толя', f'2. Вася', f'3. Петя', sep='\n')
