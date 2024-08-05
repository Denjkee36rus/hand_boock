from copy import deepcopy


class Graph:
    def __init__(self, data: list[int]) -> None:

        # INFO: 1. Здесь нужно быть осторожнее,
        # в данном контексте задачи это будет работать.
        # Если передаваемый список содержит элементы ссылочного типа,
        # то лучше сделать глубокое копирование через deepcopy из модуля copy
        self.data = deepcopy(data)
        # self.data = data.copy()  # Создаем копию переданного списка
        self.is_show = True  # По умолчанию данные графика показаны

    # INFO: 2. Не забывайте про аннотации ко всем идентификаторам
    def get_data(self) -> str:
        return " ".join(map(str, self.data))

    def set_data(self, data):
        self.data = deepcopy(data)
        # self.data = data.copy()

    # INFO: 3. Нужно избавиться от дублирования кода,
    # у трех методов происходит почти одинаковые действия,
    # меняются только входные данные.
    def show_table(self):
        if self.is_show:
            print(self.get_data())
        else:
            print("Отображение данных закрыто")

    def show_graph(self):
        if self.is_show:
            print(f"Графическое отображение данных: {self.get_data()}")
        else:
            print("Отображение данных закрыто")

    def show_bar(self):
        if self.is_show:
            print(f'Столбчатая диаграмма: {self.get_data()}')
        else:
            print("Отображение данных закрыто")

    def set_show(self, fl_show: bool) -> None:
        self.is_show = fl_show


if __name__ == '__main__':
    # data_graph = [8, 11, 10, -32, 0, 7, 18]
    # 8 11 10 -32 0 7 18
    data_graph = list(map(int, input().split()))
    gr_1 = Graph(data_graph)
    gr_1.show_bar()
    gr_1.set_show(fl_show=False)
    gr_1.show_table()
