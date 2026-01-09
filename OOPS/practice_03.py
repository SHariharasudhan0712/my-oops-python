class Data:
    def __init__(self):
        self.name='Hari'
        self.__p='abc'
    def show(self): print(self.__p)

d=Data();print(d.name);d.show()