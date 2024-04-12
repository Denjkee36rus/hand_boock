petya_speed = int(input())
vasay_speed = int(input())
tolay_speed = int(input())
if petya_speed > vasay_speed and petya_speed > tolay_speed:
    print('Петя')
elif vasay_speed > petya_speed and vasay_speed > tolay_speed:
    print('Вася')
else:
    print('Толя')