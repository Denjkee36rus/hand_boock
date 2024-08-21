class SingletonFive:
    __count: int = 0

    def __new__(cls, *args, **kwargs):
        print(args, kwargs)
        _max_instance_count: int = 5
        if cls.__count < _max_instance_count:
            cls.__count += 1
            return super().__new__(cls)
        return f"Макимальное количество объектов {_max_instance_count}"

    def __init__(self, name: str, **kwargs):
        self.name = name


# Объект (экземпляр)
obj1 = SingletonFive("1")
obj2 = SingletonFive("2")
obj3 = SingletonFive("3")
obj4 = SingletonFive("4blabla", text="1234")
obj5 = SingletonFive("5")
obj6 = SingletonFive("6")

print(obj1)
print(obj2)
print(obj3)
print(obj4.name)
print(obj5)
print(obj6)
