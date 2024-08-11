class Singleton:
    """Контроль над созданием экземпляров класса."""
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            print('Создается объект')
            cls.__instance = super().__new__(cls)
        # return 'Ошибка, нельзя создавать объекты абстрактного класса'
        print(f'Получаем объект {id(cls.__instance)}')
        return cls.__instance

    def __init__(self):
        pass


if __name__ == '__main__':
    sm = Singleton()
    sc = Singleton()
    pro = Singleton()
