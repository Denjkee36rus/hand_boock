#
class Car:
    # атрибут, свойство, поле | класса
    WHEELS = 4

    # Конструктор класс
    def __init__(self, color, car_body, brand, year):
        # атрибут, свойство, поле | объекта, экземпляра
        self.color = color
        self.car_body = car_body
        self.brand = brand
        self.year = year


    def info(self):
        print(
            f"Информация о машине:"
            f"\nНазвание: {self.brand}"
            f"\nЦвет: {self.color}"
            f"\nГод: {self.year}"
        )


# # объект, экземпляр
bmw = Car('Зеленый', 'Седан', 'BMW', 2024)
benz = Car('Черный', 'Хетчбэк', 'Benz', 2024)

# BMW
print(bmw.car_body)
# print(benz.car_body)

print(bmw.WHEELS)
# print(benz.WHEELS)

# print(bmw.brand)
# bmw.brand = 'Volga'
# print(bmw.brand)


print(bmw.__dict__)

bmw.info()
benz.info()
