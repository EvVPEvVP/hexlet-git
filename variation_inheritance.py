#type variation inheritance

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

circle = Circle(5)
print("Площадь круга:", circle.area())

rectangle = Rectangle(4, 6)
print("Площадь прямоугольника:", rectangle.area())


#Reification Inheritance

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
print("Собака говорит:", dog.speak())

cat = Cat()
print("Кошка говорит:", cat.speak())


#Structure Inheritance

class List:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

class Comparable:
    def compare(self, other):
        pass

class SortedList(List, Comparable):
    def compare(self, other):
        return sorted(self.items) == sorted(other.items)









