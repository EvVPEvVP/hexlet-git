# Generalization

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        return f"Starting the {self.brand} {self.model} car"


class Bicycle(Vehicle):
    def start(self):
        return f"Pedaling the {self.brand} {self.model} bicycle"

# Specialization

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def calculate_salary(self):
        pass


class Developer(Employee):
    def __init__(self, name, employee_id, programming_language):
        super().__init__(name, employee_id)
        self.programming_language = programming_language

    def calculate_salary(self):
        base_salary = 100000
        return base_salary


class Manager(Employee):
    def __init__(self, name, employee_id, team_size):
        super().__init__(name, employee_id)
        self.team_size = team_size

    def calculate_salary(self):
        base_salary = 120000
        return base_salary + 2000 * self.team_size