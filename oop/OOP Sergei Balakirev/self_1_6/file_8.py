TYPE_OS: int = 2


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    __classes: dict = {
        1: DialogWindows,
        2: DialogLinux
    }

    def __new__(cls, *args, **kwargs):
        if TYPE_OS not in cls.__classes:
            raise ValueError(f"Некорректные данные для класса {TYPE_OS}")

        obj = super().__new__(cls.__classes.get(TYPE_OS, Dialog))
        first, *_ = args
        obj.name = first
        return obj


dlg = Dialog("One")
TYPE_OS = 1
dlg2 = Dialog("Two")
dlg3 = Dialog("Three")
# TYPE_OS = 3
# dlg4 = Dialog("Four")
print(dlg)
print(dlg2.name)
print(dlg3.name)
# print(dlg4.name)
