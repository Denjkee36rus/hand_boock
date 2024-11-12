#
class Car:
    # атрибут, свойство, поле | класса
    WHEELS = 4

    # Переопределение метода
    def __new__(cls, *args, **kwargs):
        print("args", args)
        print("kwargs", kwargs)

        new_obj = super().__new__(cls)

        print(f"[__new__] ID объекта: {id(new_obj)}")

        return new_obj

    # Конструктор класс
    def __init__(self, color, car_body, brand, year):
        # атрибут, свойство, поле | объекта, экземпляра
        self.color = color
        self.car_body = car_body
        self.brand = brand
        self.year = year

        print(f"[__init__] ID объекта: {id(self)}")

    def info(self):
        print(
            f"Информация о машине:"
            f"\nНазвание: {self.brand}"
            f"\nЦвет: {self.color}"
            f"\nГод: {self.year}"
        )


# объект, экземпляр
bmw = Car(
    car_body='Седан',
    color='Зеленый',
    brand='BMW',
    year=2024
)
benz = Car('Черный', 'Хетчбэк', 'Benz', 2024)

# BMW
print(bmw.car_body)
# print(benz.car_body)

print(bmw.WHEELS)
# print(benz.WHEELS)

# print(bmw.brand)
# bmw.brand = 'Volga'
# print(bmw.brand)

bmw.feature = "Haha"
bmw.color = "asdkgjsaldgjlksfdjglsfdg"

print(bmw.__dict__)
print(benz.__dict__)

# bmw.info()
# benz.info()

#  args - неограниченное кол-во позиционных пар-ов
#  kwargs - неограниченное кол-во наименованных пар-ов
