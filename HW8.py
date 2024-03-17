# Example 1. 
# В этом примере Flyable и Swimmable являются миксинами. Duck и Penguin используют эти миксины, добавляя соответствующие методы. Swan наследуется от обоих миксинов.

class Flyable:
    def fly(self):
        print("I am flying!")

class Swimmable:
    def swim(self):
        print("I am swimming!")

class Duck:
    pass

class Penguin:
    pass

class Swan(Flyable, Swimmable):
    pass

duck = Duck()
duck.fly = Flyable().fly
duck.swim = Swimmable().swim

penguin = Penguin()
penguin.swim = Swimmable().swim

swan = Swan()

duck.fly()    # I am flying!
duck.swim()   # I am swimming! 
penguin.swim()# I am swimming!
swan.fly()    # I am flying!
swan.swim()   # I am swimming!


# Example 2.
# В этом примере мы определяем два миксина: Serializable и Loggable. Миксин Serializable предоставляет метод serialize(), который возвращает сериализованные данные объекта. Миксин Loggable предоставляет метод log(), который выводит сообщение в лог.


class Serializable:
    def serialize(self):
        return f"Serialized data: {self.__dict__}"

class Loggable:
    def log(self, message):
        print(f"Log: {message}")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person, Serializable, Loggable):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        self.log(f"{self.name} is studying")

class Teacher(Person, Serializable, Loggable):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        self.log(f"{self.name} is teaching {self.subject}")

student = Student("Alice", 20, "12345")
student.study()  # Output: Log: Alice is studying
print(student.serialize())  # Output: Serialized data: {'name': 'Alice', 'age': 20, 'student_id': '12345'}

teacher = Teacher("Bob", 35, "Math")
teacher.teach()  # Output: Log: Bob is teaching Math
print(teacher.serialize())  # Output: Serialized data: {'name': 'Bob', 'age': 35, 'subject': 'Math'}
