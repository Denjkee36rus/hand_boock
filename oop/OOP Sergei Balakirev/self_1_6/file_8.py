TYPE_OS = 2 # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __new__(cls, *args, **kwargs):
        obg = None
        if TYPE_OS == 1:
            obg = super(Dialog, cls).__new__(DialogWindows)
        else:
            obg = super(Dialog, cls).__new__(DialogLinux)
        return obg

    def __init__(self, name):
        self.name = name


dlg = Dialog("name")
print(dlg)











