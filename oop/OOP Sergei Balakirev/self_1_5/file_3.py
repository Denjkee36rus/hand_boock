class Point:
    def __init__(self, x: int, y: int, color: str = 'black'):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self) -> str:
        return f'Point(x={self.x}, y={self.y}, color="{self.color}")'


if __name__ == '__main__':
    # points = [Point(i, i)for i in range(1, 1001, 2)]
    points: list[Point] = []
    for i in range(1, 1001, 2):
        if i == 3:
            point = Point(x=i, y=i, color='yellow')
        else:
            point = Point(x=i, y=i)

        # point = Point(x=i, y=i, color='yellow' if i == 3 else 'black')
        points.append(point)

    # points[1].color = 'yellow'
    print(*points, sep='\n')
