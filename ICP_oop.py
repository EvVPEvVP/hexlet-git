# Inheritance

# Определяем базовый класс Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # Этот метод будет переопределён в дочерних классах

# Класс Dog наследует от Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} говорит 'Гав!'"

# Класс Cat также наследует от Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} говорит 'Мяу!'"


# Compositiion

# Создаем класс Engine, который представляет двигатель
class Engine:
    def start(self):
        print("Двигатель запущен")

    def stop(self):
        print("Двигатель остановлен")

# Создаем класс Car, который использует композицию с классом Engine
class Car:
    def __init__(self):
        self.engine = Engine()  # Создаем экземпляр класса Engine

    def start(self):
        print("Машина начала движение")
        self.engine.start()  # Используем функциональность Engine

    def stop(self):
        print("Машина остановилась")
        self.engine.stop()  # Используем функциональность Engine


# Polymorphism

# Создаем базовый класс Shape
class Shape:
    def calculate_area(self):
        pass  # Этот метод будет переопределен в дочерних классах

# Класс Circle наследует от Shape и реализует свой метод calculate_area
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius * self.radius

# Класс Rectangle также наследует от Shape и реализует свой метод calculate_area
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# Функция для вычисления площади любой фигуры (полиморфизм)
def print_area(shape):
    area = shape.calculate_area()
    print(f"Площадь фигуры: {area}")