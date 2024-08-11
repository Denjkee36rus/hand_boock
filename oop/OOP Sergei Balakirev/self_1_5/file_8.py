class Cart:
    def __init__(self):
        self.goods: list['Good'] = []

    def add(self, gd: 'Good'):
        self.goods.append(gd)

    def remove(self, indx: int):
        # TODO: Что если список товаров пуст?
        del self.goods[indx]

    def get_list(self) -> list[str]:
        result = [f'{gd.name}: {gd.price}' for gd in self.goods]
        return result


class Good:
    """Базовый класс для товаров."""

    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class Table(Good):
    pass


class TV(Good):
    pass


class Notebook(Good):
    pass


class Cup(Good):
    pass


if __name__ == '__main__':
    cart = Cart()

    cart.add(TV('samsung', 20000))
    cart.add(TV('LG', 20000))

    print(cart.get_list())
