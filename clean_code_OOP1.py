1.
class Person:
    def __init__(self, name, age, is_employee):
        self.name = name
        self.age = age
        self.is_employee = is_employee

class PersonFactory:
    def create_person(name, age, is_employee=False):
        return Person(name, age, is_employee)

employee = PersonFactory.create_person('Alice', 25, True)
non_employee = PersonFactory.create_person('Bob', 30)

2.

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.make} {self.model}"

    def create_car(cls, make_model):
        make, model = make_model.split(" ")
        return cls(make, model)

car1 = Car("Ford", "Mustang")
car2 = Car.create_car("Toyota Camry")

3.

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} barks!")

class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"{self.name} meows!")

class AnimalFactory:
    def create_animal(animal_type, name):
        if animal_type == "dog":
            return Dog(name)
        elif animal_type == "cat":
            return Cat(name)
        else:
            raise ValueError(f"Invalid animal type: {animal_type}")

dog = AnimalFactory.create_animal("dog", "Fido")
cat = AnimalFactory.create_animal("cat", "Fluffy")

dog.bark()
cat.meow()
