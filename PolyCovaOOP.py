# Polymorphism


class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Gav!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

animal_sound(dog) 
animal_sound(cat) 



# Covariant

from typing import List

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159265359 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def calculate_area(shapes: List[Shape]):
    total_area = 0
    for shape in shapes:
        total_area += shape.area()
    return total_area

shapes = [Circle(5), Rectangle(4, 6)]

total = calculate_area(shapes)
print("Total area:", total)

