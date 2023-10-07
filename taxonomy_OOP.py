class Vehicle:
    def __init__(self, name):
        self.name = name

    def start(self):
        pass

class GasolineEngineVehicle(Vehicle):
    def start(self):
        print(f"{self.name} starts with a gasoline engine")

class DieselEngineVehicle(Vehicle):
    def start(self):
        print(f"{self.name} starts with a diesel engine")

class ElectricEngineVehicle(Vehicle):
    def start(self):
        print(f"{self.name} starts with an electric engine")

car = GasolineEngineVehicle("Car")
truck = DieselEngineVehicle("Truck")
electric_car = ElectricEngineVehicle("Electric Car")

