# data_graph = list(map(int, input.split()))
class Graph:
    def __init__(self, data):
        self.data = data.copy()  # Создаем копию переданного списка
        self.is_show = True  # По умолчанию данные графика показаны

    def get_data(self):
        return " ".join(map(str, self.data))

    def set_data(self, data):
        self.data = data.copy()

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

    def set_show(self, fl_show):
        self.is_show = fl_show


data_graph = [8, 11, 10, -32, 0, 7, 18]

gr_1 = Graph(data_graph)

gr_1.show_bar()
gr_1.set_show(fl_show=False)
gr_1.show_table()


