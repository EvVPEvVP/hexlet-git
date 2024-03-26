# 1. Уровень реализации 

Плохой код:

def process_data(data):
    result = []
    for i in range(len(data)):
        item = data[i]
        if item['type'] == 'A':
            if item['value'] > 10:
                result.append(item['value'] * 2)
        elif item['type'] == 'B':
            if item['value'] < 5:
                result.append(item['value'] ** 3)
        else:
            result.append(item['value'])
    
    total = 0
    for value in result:
        total += value
    
    average = total / len(result)
    
    return result, total, average

Проблемы:
1. Неинформативное имя функции `process_data` и переменных `data`, `item`, `i`.
2. Сложная вложенная логика с условными операторами.
3. Несколько ответственностей у функции: фильтрация, преобразование, вычисление суммы и среднего.
4. Неэффективное использование цикла `for` для вычисления суммы.
5. Отсутствие обработки случая, когда `result` пустой при вычислении среднего.

Улучшенный код:

def filter_and_transform_items(items):
    """
    Фильтрует и преобразует элементы в соответствии с заданными условиями.
    """
    transformed_values = []
    for item in items:
        if item['type'] == 'A' and item['value'] > 10:
            transformed_values.append(item['value'] * 2)
        elif item['type'] == 'B' and item['value'] < 5:
            transformed_values.append(item['value'] ** 3)
        else:
            transformed_values.append(item['value'])
    return transformed_values


def calculate_statistics(values):
    """
    Вычисляет сумму и среднее значение списка чисел.
    """
    if not values:
        raise ValueError("Список значений пустой.")
    
    total = sum(values)
    average = total / len(values)
    return total, average


def process_items(items):
    """
    Обрабатывает список элементов, фильтрует, преобразует и вычисляет статистику.
    """
    transformed_values = filter_and_transform_items(items)
    total, average = calculate_statistics(transformed_values)
    return transformed_values, total, average

Что было улучшено:
1. Функция `process_data` разделена на несколько функций с четкими обязанностями: `filter_and_transform_items`, `calculate_statistics`, `process_items`.
2. Имена функций и переменных более информативны и отражают их назначение.
3. Для вычисления суммы использована встроенная функция `sum()`, что более эффективно и читаемо.
4. Добавлена обработка случая, когда список значений пустой, с выбросом исключения `ValueError`.


# 1.1 Методы, которые используются только в тестах

Плохой код:

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def set_name(self, name):
        self.name = name
    
    def set_email(self, email):
        self.email = email

В этом примере класс `User` имеет методы `get_name()`, `get_email()`, `set_name()` и `set_email()`, которые используются только в тестах для получения и установки значений атрибутов `name` и `email`. 
Улучшенный код:

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

Что было улучшено:
1. Удалены методы `get_name()`, `get_email()`, `set_name()` и `set_email()`, которые использовались только в тестах.
2. Вместо этого атрибуты `name` и `email` доступны напрямую, без использования дополнительных методов.

Если требуется дополнительная логика при получении или установке значений атрибутов, можно использовать методы с более осмысленными названиями и функциональностью.

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def update_email(self, new_email):
        if '@' in new_email:
            self.email = new_email
        else:
            raise ValueError("Некорректный адрес электронной почты.")

# 1.2 Цепочки методов

Плохой код:

class Order:
    def __init__(self, items):
        self.items = items
    
    def calculate_total(self):
        return self.calculate_subtotal() + self.calculate_shipping() + self.calculate_tax()
    
    def calculate_subtotal(self):
        return sum(item.get_price() for item in self.items)
    
    def calculate_shipping(self):
        return self.calculate_shipping_weight() * 0.5
    
    def calculate_shipping_weight(self):
        return sum(item.get_weight() for item in self.items)
    
    def calculate_tax(self):
        return self.calculate_subtotal() * 0.13

В этом примере класс `Order` имеет метод `calculate_total()`, который вызывает другие методы (`calculate_subtotal()`, `calculate_shipping()`, `calculate_tax()`), которые в свою очередь вызывают другие методы (`get_price()`, `get_weight()`). Такая цепочка вызовов может быть сложной для понимания и отладки.

Улучшенный код:

class Item:
    def __init__(self, price, weight):
        self.price = price
        self.weight = weight


class Order:
    def __init__(self, items):
        self.items = items
    
    def calculate_total(self):
        subtotal = self.calculate_subtotal()
        shipping_weight = self.calculate_shipping_weight()
        shipping_cost = self.calculate_shipping_cost(shipping_weight)
        tax = self.calculate_tax(subtotal)
        return subtotal + shipping_cost + tax
    
    def calculate_subtotal(self):
        return sum(item.price for item in self.items)
    
    def calculate_shipping_weight(self):
        return sum(item.weight for item in self.items)
    
    def calculate_shipping_cost(self, weight):
        return weight * 0.5
    
    def calculate_tax(self, subtotal):
        return subtotal * 0.1

Что было улучшено:
1. Введен класс `Item` для представления отдельных товаров в заказе. Каждый товар имеет свою цену (`price`) и вес (`weight`).
2. Метод `calculate_total()` разбит на несколько более мелких методов, каждый из которых выполняет определенную задачу.
3. Методы `calculate_subtotal()`, `calculate_shipping_weight()`, `calculate_shipping_cost()` и `calculate_tax()` теперь принимают необходимые параметры и возвращают результаты, а не вызывают другие методы напрямую.
4. Метод `calculate_total()` собирает результаты вызовов других методов и возвращает общую сумму заказа.


# 1.3. У метода слишком большой список параметров.

Плохой код:

class Car:
    def __init__(self, make, model, year, color, engine_type, transmission, num_doors, price, is_electric, has_sunroof, has_navigation, has_leather_seats):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.engine_type = engine_type
        self.transmission = transmission
        self.num_doors = num_doors
        self.price = price
        self.is_electric = is_electric
        self.has_sunroof = has_sunroof
        self.has_navigation = has_navigation
        self.has_leather_seats = has_leather_seats

В этом примере конструктор класса `Car` имеет слишком много параметров, что затрудняет его использование и понимание.

Улучшенный код:

class Engine:
    def __init__(self, engine_type, is_electric):
        self.engine_type = engine_type
        self.is_electric = is_electric


class Interior:
    def __init__(self, has_sunroof, has_navigation, has_leather_seats):
        self.has_sunroof = has_sunroof
        self.has_navigation = has_navigation
        self.has_leather_seats = has_leather_seats


class Car:
    def __init__(self, make, model, year, color, engine, transmission, num_doors, price, interior):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.engine = engine
        self.transmission = transmission
        self.num_doors = num_doors
        self.price = price
        self.interior = interior

Что было улучшено:
1. Введены классы `Engine` и `Interior`. Класс `Engine` содержит информацию о типе двигателя и является ли он электрическим. Класс `Interior` содержит информацию о наличии люка, навигации и кожаных сидений.
2. Конструктор класса `Car` теперь принимает объекты `Engine` и `Interior` вместо отдельных параметров для этих свойств.
3. Количество параметров в конструкторе класса `Car` уменьшилось, что делает его более читаемым и понятным.


# 1.4. Странные решения.

Плохой код:

class StringFormatter:
    def __init__(self, string):
        self.string = string
    
    def to_uppercase(self):
        return self.string.upper()
    
    def to_lowercase(self):
        return self.string.lower()
    
    def capitalize_first_letter(self):
        return self.string.capitalize()
    
    def capitalize_each_word(self):
        return ' '.join(word.capitalize() for word in self.string.split())
    
    def to_title_case(self):
        return self.string.title()

В этом примере класс `StringFormatter` имеет несколько методов для преобразования строки в разные стили: `to_uppercase()`, `to_lowercase()`, `capitalize_first_letter()`, `capitalize_each_word()` и `to_title_case()`. Хотя все эти методы решают проблему изменения регистра символов в строке, они создают несогласованность и дублирование кода.

Улучшенный код:

class StringFormatter:
    def __init__(self, string):
        self.string = string
    
    def format(self, style):
        if style == 'uppercase':
            return self.string.upper()
        elif style == 'lowercase':
            return self.string.lower()
        elif style == 'capitalize':
            return self.string.capitalize()
        elif style == 'title':
            return self.string.title()
        else:
            raise ValueError(f"Неизвестный стиль форматирования: {style}")

Что было улучшено:
1. Вместо нескольких методов для разных стилей форматирования введен один метод `format()`, который принимает параметр `style` для указания желаемого стиля.
2. Внутри метода `format()` используется условная логика для определения соответствующего стиля форматирования на основе значения параметра `style`.
3. Если передан неизвестный стиль форматирования, выбрасывается исключение `ValueError` с соответствующим сообщением об ошибке.

# 1.5. Чрезмерный результат.

Плохой код:

class User:
    def __init__(self, name, email, age, address):
        self.name = name
        self.email = email
        self.age = age
        self.address = address
    
    def get_user_info(self):
        return {
            'name': self.name,
            'email': self.email,
            'age': self.age,
            'address': self.address
        }

В этом примере класс `User` имеет метод `get_user_info()`, который возвращает словарь со всеми данными пользователя: именем, email, возрастом и адресом. Однако, если вызывающему компоненту нужно только имя и email пользователя, метод возвращает больше данных, чем необходимо.

Улучшенный код:

class User:
    def __init__(self, name, email, age, address):
        self.name = name
        self.email = email
        self.age = age
        self.address = address
    
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def get_age(self):
        return self.age
    
    def get_address(self):
        return self.address

Что было улучшено:
1. Вместо метода `get_user_info()`, который возвращает все данные пользователя, введены отдельные методы `get_name()`, `get_email()`, `get_age()` и `get_address()` для получения конкретных данных.
2. Каждый метод возвращает только один атрибут пользователя, предоставляя вызывающему компоненту возможность получить только необходимые данные.














