class Graph:
    # Статическое свойство класса
    LIMIT_Y: list[int, int] = [0, 10]

    def set_data(self, data: list[int]) -> None:
        # Динамическое свойство объекта
        self.data = data

    def draw(self) -> None:
        start, end = self.LIMIT_Y
        result: list[str] = [
            str(num) for num in self.data
            if num in range(start, end + 1)
        ]
        print(' '.join(result))


if __name__ == '__main__':
    graph_1 = Graph()
    graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
    graph_1.draw()
