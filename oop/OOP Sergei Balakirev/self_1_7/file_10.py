class AppStore:

    def __new__(cls, *args, **kwargs):
        # TODO: реализовать Singleton
        pass

    def __init__(self):
        self.__shop = []

    def add_application(self, app):
        self.__shop.append(app)

    def remove_application(self, app):
        self.__shop.remove(app)

    @staticmethod
    def block_application(app: 'Application'):
        app.blocked = True

    def total_apps(self):
        return len(self.__shop)

    def list_apps(self):
        print(self.__shop)


class Application:
    def __init__(self, name):
        self.name = name
        self.blocked = False


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
AppStore.block_application(app_youtube)
store.list_apps()
print(store.total_apps())

store_2 = AppStore()
google = Application("Google")
store_2.add_application(google)
print(store.total_apps())  # 2
store.remove_application(app_youtube)
store_2.remove_application(google)
