# Create General
class General:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"класс General с именем {self.name}")

# Create Any
class Any:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"класс Any с именем {self.name}")

# Create NoneClass как потомка всех классов
class NoneClass(General, Any):
    def __init__(self):
        super().__init__("None")

    def print_info(self):
        print("Я класс None (Void)")

general_obj = General("Объект класса General")
any_obj = Any("Объект класса Any")
none_obj = NoneClass()

objects = [general_obj, any_obj, none_obj]

for obj in objects:
    obj.print_info()

