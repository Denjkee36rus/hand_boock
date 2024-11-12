class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            new_obj = super().__new__(cls)
            cls.__instance = new_obj

        return cls.__instance


magic = Singleton()
copy_1 = Singleton()
copy_2 = Singleton()
copy_3 = Singleton()
copy_4 = Singleton()

print(id(magic))
print(id(copy_1))
print(id(copy_2))
print(id(copy_3))
print(id(copy_4))
