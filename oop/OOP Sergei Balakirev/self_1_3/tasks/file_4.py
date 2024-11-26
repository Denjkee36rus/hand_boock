class DataBase:
    pk = 1
    title = 'Классы и объекты'
    author = 'Сергей Балакирев'
    views = 14356
    price = 1024

DataBase.price = 2048
print(DataBase.price)

DataBase.inflaton = 100

print(DataBase.__dict__)