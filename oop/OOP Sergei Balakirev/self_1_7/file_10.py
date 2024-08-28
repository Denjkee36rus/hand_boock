class AppStore:
    shop = []
    @classmethod
    def add_application(cls, app):
        cls.shop.append(app)

    @classmethod
    def remove_application(cls, app):
        cls.shop.pop(app)

    @classmethod
    def block_application(cls, app):
        app.blocked = True

    @classmethod
    def total_apps(cls):
        return len(cls.shop)

class Application:
    def __init__(self, name):
        self.name = name
        self.blocked = False

store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube) ### почему app_youtobe откуда он берется 
store.remove_application(app_youtube)