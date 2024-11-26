class Car:
    WHEELS: int = 4

    def __init__(self, model_name: str, color: str, year: int) -> None:
        self.model = model_name
        self.color = color
        self.year = year


car_1 = Car("model 1", "gray", year=2077)
car_2 = Car("model 2", "green", 1977)
car_3 = Car("model 1", "gray", 2077)

print(car_1.__dict__)
print(car_2.__dict__)
print(car_3.__dict__)


class CarUp:
    def set_model(self, name: str) -> None:
        self.model = name


car_up_1 = CarUp()
car_up_2 = CarUp()
car_up_3 = CarUp()

car_up_1.set_model("RR")

print(car_up_1.__dict__)
print(car_up_2.__dict__)
print(car_up_3.__dict__)
