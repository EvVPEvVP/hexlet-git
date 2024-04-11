#2.1 Класс слишком большой (нарушение SRP)

Вот пример плохо спроектированного класса в Python, который нарушает принцип единственной ответственности (SRP) и создает много инстансов:

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []
        self.notifications = []

    def place_order(self, order):
        self.orders.append(order)
        # Логика размещения заказа

    def send_notification(self, notification):
        self.notifications.append(notification)
        # Логика отправки уведомления

    def generate_report(self):
        # Логика генерации отчета по пользователю
        pass

Проблемы с этим классом:

Нарушение SRP: Класс `User` отвечает за слишком многое - хранение информации о пользователе, управление заказами, отправку уведомлений и генерацию отчетов. Это делает класс трудным для понимания, поддержки и модификации.

Как можно улучшить дизайн:

Разделить класс `User` на несколько классов с четкими обязанностями, следуя SRP. Например, выделить классы `Order`, `Notification` и `ReportGenerator`.

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Order:
    # Логика управления заказами

class Notification:
    # Логика управления уведомлениями

class ReportGenerator:
    # Логика генерации отчетов



#2.2. Класс слишком маленький или делает слишком мало.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

Проблемы с этим классом:

Класс `Rectangle` не предоставляет никакой дополнительной функциональности, кроме хранения ширины и высоты. Методы `get_width()` и `get_height()` просто возвращают значения атрибутов, что не добавляет никакой ценности.

Как можно улучшить дизайн:

Добавить в класс `Rectangle` методы, которые предоставляют полезную функциональность, связанную с прямоугольником. Например, методы для вычисления площади и периметра.

Пример улучшенного класса:

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)



#2.3. В классе есть метод, который выглядит более подходящим для другого класса.


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_payroll(self, employees):
        total_payroll = 0
        for employee in employees:
            total_payroll += employee.salary
        return total_payroll

Проблемы с этим классом:

Метод `calculate_payroll()` принимает список сотрудников и вычисляет общую сумму зарплат. Однако этот метод находится внутри класса `Employee`, что нарушает принцип единственной ответственности (SRP).
Класс `Employee` должен отвечать только за хранение и управление информацией, связанной с отдельным сотрудником, а не за вычисление общей суммы зарплат для списка сотрудников.

Как можно улучшить дизайн:

Вынести метод `calculate_payroll()` из класса `Employee` и поместить его в отдельный класс, который отвечает за операции, связанные с расчетом зарплаты. Например, класс `PayrollCalculator`.

Пример улучшенной структуры:

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class PayrollCalculator:
    @staticmethod
    def calculate_payroll(employees):
        total_payroll = 0
        for employee in employees:
            total_payroll += employee.salary
        return total_payroll



#2.4. Класс хранит данные, которые загоняются в него в множестве разных мест в программе.

class UserData:
    def __init__(self):
        self.data = {}

    def set_data(self, key, value):
        self.data[key] = value

    def get_data(self, key):
        return self.data.get(key)

# Использование класса в разных местах программы
user_data = UserData()

# В модуле авторизации
user_data.set_data("username", "john")
user_data.set_data("password", "secret")

# В модуле профиля пользователя
user_data.set_data("email", "john@example.com")
user_data.set_data("age", 30)

# В модуле настроек пользователя
user_data.set_data("theme", "dark")
user_data.set_data("language", "en")

Проблемы с этим классом:

Класс `UserData` используется как глобальное хранилище данных, к которому обращаются из разных частей программы. Это нарушает принципы инкапсуляции и модульности.

Как можно улучшить дизайн:

Разделить данные пользователя на отдельные классы с четкими обязанностями, такие как `UserCredentials`, `UserProfile`, `UserSettings`, и т.д.

Пример улучшенной структуры:

class UserCredentials:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserProfile:
    def __init__(self, email, age):
        self.email = email
        self.age = age

class UserSettings:
    def __init__(self, theme, language):
        self.theme = theme
        self.language = language


#2.5. Класс зависит от деталей реализации других классов.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.1


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def calculate_bonus(self):
        # Менеджер зависит от деталей реализации класса Employee
        employee_bonus = super().calculate_bonus()
        manager_bonus = self.salary * 0.2
        return employee_bonus + manager_bonus


class SalesManager(Manager):
    def __init__(self, name, salary, department, sales):
        super().__init__(name, salary, department)
        self.sales = sales

    def calculate_bonus(self):
        # SalesManager зависит от деталей реализации класса Manager
        manager_bonus = super().calculate_bonus()
        sales_bonus = self.sales * 0.05
        return manager_bonus + sales_bonus

В этом примере у нас есть базовый класс `Employee`, от которого наследуются классы `Manager` и `SalesManager`. Проблема заключается в том, что классы `Manager` и `SalesManager` зависят от деталей реализации своих родительских классов.

Для улучшения дизайна следует стремиться к уменьшению зависимости между классами. Каждый класс должен быть ответственен за свою собственную функциональность и не должен полагаться на детали реализации других классов.


#2.6. Приведение типов вниз по иерархии (родительские классы приводятся к дочерним).

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return "Meow"


class Dog(Animal):
    def make_sound(self):
        return "Woof"


def animal_sound(animal):
    if isinstance(animal, Cat):
        cat = Cat(animal.name)
        return cat.make_sound()
    elif isinstance(animal, Dog):
        dog = Dog(animal.name)
        return dog.make_sound()
    else:
        return "Unknown sound"

Проблема с этим подходом заключается в том, что функция `animal_sound` зависит от конкретных подклассов `Cat` и `Dog`. Если в будущем будут добавлены новые подклассы `Animal`, потребуется изменить функцию `animal_sound`, чтобы учесть эти новые подклассы.

Улучшенный пример:

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Unknown sound"


class Cat(Animal):
    def make_sound(self):
        return "Meow"


class Dog(Animal):
    def make_sound(self):
        return "Woof"


def animal_sound(animal):
    return animal.make_sound()

В улучшенном примере мы избавляемся от приведения типов вниз по иерархии. Функция `animal_sound` просто вызывает метод `make_sound` непосредственно на объекте `Animal`, не заботясь о конкретном подклассе.


#2.7. Когда создаётся класс-наследник для какого-то класса, приходится создавать классы-наследники и для некоторых других классов.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"


class Truck(Vehicle):
    def start_engine(self):
        return "Truck engine started"


class Engine:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def start(self):
        if isinstance(self.vehicle, Car):
            return "Car engine started"
        elif isinstance(self.vehicle, Truck):
            return "Truck engine started"
        else:
            return "Unknown engine"


class Transmission:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def shift_gear(self):
        if isinstance(self.vehicle, Car):
            return "Car gear shifted"
        elif isinstance(self.vehicle, Truck):
            return "Truck gear shifted"
        else:
            return "Unknown transmission"

В этом примере у нас есть базовый класс `Vehicle` и два подкласса `Car` и `Truck`. Классы `Engine` и `Transmission` зависят от конкретных классов `Car` и `Truck`, используя приведение типов с помощью `isinstance`.

Проблема заключается в том, что при добавлении нового класса-наследника `Vehicle`, например `Motorcycle`, нам придется создавать соответствующие классы-наследники для `Engine` и `Transmission`, чтобы обрабатывать специфику мотоцикла.

Улучшенный пример:

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"


class Truck(Vehicle):
    def start_engine(self):
        return "Truck engine started"


class Engine:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def start(self):
        return self.vehicle.start_engine()


class Transmission:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def shift_gear(self):
        return f"{self.vehicle.brand} gear shifted"

Класс `Engine` вызывает метод `start_engine()` непосредственно на объекте `vehicle`, не заботясь о конкретном типе транспортного средства. Каждый подкласс `Vehicle` переопределяет метод `start_engine()` в соответствии со своей спецификой.



#2.8. Дочерние классы не используют методы и атрибуты родительских классов, или переопределяют родительские методы.

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        return f"{self.name} is sleeping"


class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed

    def bark(self):
        return "Woof!"


class Cat(Animal):
    def __init__(self, name, color):
        self.color = color

    def eat(self):
        return "Cat is eating"

В этом примере у нас есть базовый класс `Animal` и два подкласса `Dog` и `Cat`. Однако дочерние классы не используют методы и атрибуты родительского класса должным образом.

Проблемы:
- Класс `Dog` не вызывает конструктор родительского класса `__init__` и не устанавливает атрибут `name`. Вместо этого он определяет свой собственный атрибут `breed`.
- Класс `Cat` также не вызывает конструктор родительского класса и не устанавливает атрибут `name`. Вместо этого он определяет свой собственный атрибут `color`.
- Класс `Cat` переопределяет метод `eat`, но не вызывает реализацию родительского класса с помощью `super().eat()`.

Улучшенный пример:

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        return f"{self.name} is sleeping"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        return "Woof!"


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def eat(self):
        return f"{super().eat()} (Cat-specific eating)"

В улучшенном примере дочерние классы `Dog` и `Cat` правильно используют методы и атрибуты родительского класса:

- Дочерние классы правильно используют методы и атрибуты родительского класса, обеспечивая согласованность и правильное поведение.
- Переопределение методов в дочерних классах осуществляется с учетом поведения родительского класса, используя `super()` для вызова реализации родительского класса.


#3.1. Одна модификация требует внесения изменений в несколько классов.

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_user_info(self):
        return f"Name: {self.name}, Email: {self.email}"


class Order:
    def __init__(self, user, items):
        self.user = user
        self.items = items

    def get_order_info(self):
        user_info = self.user.get_user_info()
        items_info = ", ".join(self.items)
        return f"User: {user_info}, Items: {items_info}"


class Payment:
    def __init__(self, user, amount):
        self.user = user
        self.amount = amount

    def process_payment(self):
        user_info = self.user.get_user_info()
        return f"Payment processed for {user_info}, Amount: {self.amount}"

В этом примере у нас есть классы `User`, `Order` и `Payment`. Каждый класс имеет свои методы, которые используют информацию о пользователе.

Проблема заключается в том, что если нам нужно изменить формат или структуру информации о пользователе (например, добавить новое поле), мы должны внести изменения во все классы, которые используют эту информацию (`Order` и `Payment`).

Улучшенный пример:

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_user_info(self):
        return f"Name: {self.name}, Email: {self.email}"


class Order:
    def __init__(self, user, items):
        self.user = user
        self.items = items

    def get_order_info(self):
        items_info = ", ".join(self.items)
        return f"User: {self.user.get_user_info()}, Items: {items_info}"


class Payment:
    def __init__(self, user, amount):
        self.user = user
        self.amount = amount

    def process_payment(self):
        return f"Payment processed for {self.user.get_user_info()}, Amount: {self.amount}"

В улучшенном примере мы по-прежнему имеем классы `User`, `Order` и `Payment`, но теперь они используют метод `get_user_info()` класса `User` для получения информации о пользователе.


#3.2. Использование сложных паттернов проектирования там, где можно использовать более простой и незамысловатый дизайн.

использование паттерна Абстрактная Фабрика:

from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class WindowsButton(Button):
    def render(self):
        return "Rendering a Windows button"

class MacButton(Button):
    def render(self):
        return "Rendering a Mac button"

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

def client_code(factory):
    button = factory.create_button()
    print(button.render())

if __name__ == "__main__":
    windows_factory = WindowsFactory()
    client_code(windows_factory)

    mac_factory = MacFactory()
    client_code(mac_factory)

В этом примере используется паттерн Абстрактная Фабрика для создания кнопок в зависимости от операционной системы (Windows или Mac).

Улучшенный пример (простой подход):

class Button:
    def __init__(self, os):
        self.os = os

    def render(self):
        if self.os == "Windows":
            return "Rendering a Windows button"
        elif self.os == "Mac":
            return "Rendering a Mac button"
        else:
            return "Rendering a default button"

def client_code(os):
    button = Button(os)
    print(button.render())

if __name__ == "__main__":
    client_code("Windows")
    client_code("Mac")

В улучшенном примере мы используем более простой подход без применения паттерна Абстрактная Фабрика. Вместо этого мы создаем класс `Button`, который принимает параметр `os` в своем конструкторе. Метод `render()` проверяет значение `os` и возвращает соответствующий результат рендеринга кнопки.












