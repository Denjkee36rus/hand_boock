point_a = int(input())
point_b = int(input())
speed = int(input())

distance = abs(point_b - point_a)

delta_time = distance / speed
print(f'{delta_time:.2f}')
