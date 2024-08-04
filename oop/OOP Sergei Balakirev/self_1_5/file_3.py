class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


# points = [Point(1, 1)for i in range(1, 100 + 1)]
points = []
for i in range(1, 1001):
    x = 2 * i - 1
    y = 2 * i - 1
    if i == 2:
        color = 'yellow'
    else:
        color = 'black'
    point = Point(x, y, color)
    points.append(point)


print(points)






