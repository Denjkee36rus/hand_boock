data_graph = list(map(int, input.split()))
class Graph:
    def __init__(self, data):
        self.data = data.copy()  # Создаем копию переданного списка
        self.is_show = True  # По умолчанию данные графика показаны

    def set_data(self, data):
        self.data = data.copy()

    def show_table(self):
        if self.is_show:
            print(" ".join(map(str, self.data)))
        else:
            print("Отображение данных закрыто")

    def show_graph(self):
        result = " ".join(map(str, self.data))
        if self.is_show:
            print(f"Графическое отображение данных: {result}")
        else:
            print("Отображение данных закрыто")

    def show_bar(self):
        result = " ".join(map(str, self.data))
        if self.is_show:
            print(f'Столбчатая диаграмма: {result}')
        else:
            print("Отображение данных закрыто")

    def set_show(self, fl_show):
        self.is_show = fl_show



gr_1 = Graph(data_graph)

gr_1.show_bar()
gr_1.set_show(fl_show=False)
gr_1.show_table()


