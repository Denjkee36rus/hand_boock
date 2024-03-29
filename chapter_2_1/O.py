hours = int(input())
minutes = int(input())
delta_time = int(input())

total = (hours * 60) + minutes + delta_time

hours = total // 60 % 24
minutes = total % 60

print(f'{hours:0>2}:{minutes:0>2}')
