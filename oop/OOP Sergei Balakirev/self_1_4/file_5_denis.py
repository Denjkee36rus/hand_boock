class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data: list[int]) -> None:
        self.data = data

    def draw(self) -> None:
        start, end = self.LIMIT_Y
        result: list[str] = [
            str(num) for num in self.data
            if num in range(start, end + 1)
        ]
        print(' '.join(result))


graph_1 = Graph()
graph_1.set_data([-5, 0, 1, 5, 11])
graph_1.draw()