
class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.gd = gd
        self.goods.append(self.gd)

    def remove(self, indx: int):
        del self.goods[indx]

    def get_list(self) -> list[str]:
        result = [f'{gd.name}:{gd.price}' for gd in self.goods]
        print(result)
        return result

class Table:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

class Notebook:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

class Cup:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

cart = Cart()

cart.add(TV('samsung', 20000))
cart.add(TV('LG', 20000))

cart.get_list()



