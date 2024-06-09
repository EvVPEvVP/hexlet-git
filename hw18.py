# Пример 1: Призрачное состояние

def swap(a, b):
    # Локальная переменная temp используется для обмена значениями
    temp = a
    a = b
    b = temp
    return a, b

x, y = 1, 2
x, y = swap(x, y)
print(x, y)  # Output: 2, 1

В этом примере переменная `temp` является призрачным состоянием, которое не отражено ни в сигнатуре функции, ни в её спецификации.

# Пример 2: Призрачное состояние


def calculate_sum(arr):
    total = 0
    for num in arr:
        # Локальная переменная temp для промежуточного хранения
        temp = num
        total += temp
    return total

print(calculate_sum([1, 2, 3, 4]))  # Output: 10

Здесь переменная `temp` добавляет ненужное состояние и может быть удалена без изменения логики.

# Пример 3: Призрачное состояние

def increment_elements(arr):
    result = []
    for i in range(len(arr)):
        # Локальная переменная для хранения промежуточного значения
        incremented_value = arr[i] + 1
        result.append(incremented_value)
    return result

print(increment_elements([1, 2, 3]))  # Output: [2, 3, 4]

Переменная `incremented_value` является призрачным состоянием и может быть исключена.

__________________________________________________________________________________________________

# Пример 1: Погрешность/неточность

def check_temperature(temp):
    # Новая спецификация: температура двигателя должна быть в диапазоне 50-100 градусов
    if 50 <= temp <= 100:
        return "Temperature is within the acceptable range."
    else:
        return "Temperature is out of the acceptable range."

# Старый код: погрешность сужает логику
def check_temperature_narrow(temp):
    if temp == 70:
        return "Temperature is within the acceptable range."
    else:
        return "Temperature is out of the acceptable range."

# Расширенная логика
print(check_temperature(70))  # Output: Temperature is within the acceptable range.
print(check_temperature_narrow(70))  # Output: Temperature is within the acceptable range.

В данном примере старая функция `check_temperature_narrow` слишком сужала диапазон.

# Пример 2: Погрешность/неточность

def validate_age(age):
    # Новая спецификация: возраст должен быть в диапазоне 0-150 лет
    if 0 <= age <= 150:
        return "Age is valid."
    else:
        return "Age is not valid."

# Старый код: погрешность сужает логику
def validate_age_narrow(age):
    if age == 30:
        return "Age is valid."
    else:
        return "Age is not valid."

# Расширенная логика
print(validate_age(30))  # Output: Age is valid.
print(validate_age_narrow(30))  # Output: Age is valid.
```
В данном примере старая функция `validate_age_narrow` ограничивала допустимый возраст до одного значения.

# Пример 3: Погрешность/неточность

def check_speed(speed):
    # Новая спецификация: скорость должна быть в диапазоне 0-200 км/ч
    if 0 <= speed <= 200:
        return "Speed is within the acceptable range."
    else:
        return "Speed is out of the acceptable range."

# Старый код: погрешность слишком сужает логику
def check_speed_narrow(speed):
    if speed == 100:
        return "Speed is within the acceptable range."
    else:
        return "Speed is out of the acceptable range."

# Расширенная логика
print(check_speed(100))  # Output: Speed is within the acceptable range.
print(check_speed_narrow(100))  # Output: Speed is within the acceptable range.

В данном примере старая функция `check_speed_narrow` ограничивала допустимую скорость до одного значения.


__________________________________________________________________________________________________


# интерфейс явно не должен быть проще реализации 


1. # Многослойные преобразования данных:
   В случае сложных ETL-процессов (Extract, Transform, Load), которые включают многослойные преобразования данных, упрощение интерфейса может привести к потере гибкости и контроля. 
   Например, если у нас есть сложная цепочка преобразований с несколькими этапами очистки данных, нормализации, агрегации и загрузки в различные хранилища данных, попытка упростить интерфейс может привести к невозможности управления каждым этапом отдельно.

    def complex_etl_process(data):
        # Extract
        extracted_data = extract_data(data)
        # Transform: Stage 1
        stage1_data = transform_stage1(extracted_data)
        # Transform: Stage 2
        stage2_data = transform_stage2(stage1_data)
        # Load
        load_data(stage2_data)

        return True

    # Более сложная реализация позволяет лучше контролировать каждый этап
    def extract_data(data):
        # extraction logic
        pass

    def transform_stage1(data):
        # stage 1 transformation logic
        pass

    def transform_stage2(data):
        # stage 2 transformation logic
        pass

    def load_data(data):
        # loading logic
        pass

2. # Сложные запросы к базе данных с параметризацией:
   При работе с базой данных часто требуется выполнять сложные запросы с множеством параметров и условий. 
   Упрощение интерфейса может привести к недостаточной гибкости для построения таких запросов. 

    from sqlalchemy import create_engine, MetaData, Table, select, and_

    engine = create_engine('sqlite:///example.db')
    metadata = MetaData()
    users = Table('users', metadata, autoload_with=engine)

    def get_users_with_conditions(age, country):
        query = select([users]).where(
            and_(
                users.c.age > age,
                users.c.country == country
            )
        )
        with engine.connect() as conn:
            result = conn.execute(query)
            return result.fetchall()


3. # Работа с базой данных:

import sqlite3

def execute_query(query, params):
    # Реализация сложная, интерфейс простой
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    cursor.execute(query, params)
    connection.commit()
    connection.close()

# Пример использования
execute_query("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))

Проблема: Простое имя функции и параметра не дают информации о структуре данных и типах, которые ожидаются.

Улучшение интерфейса с помощью типов данных:

from typing import Tuple, Any
import sqlite3

def execute_query(query: str, params: Tuple[Any, ...]) -> None:
    """
    Executes a SQL query with the given parameters.
    
    :param query: The SQL query to execute.
    :param params: A tuple of parameters to pass to the query.
    """
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    cursor.execute(query, params)
    connection.commit()
    connection.close()

execute_query("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
```
Использование аннотаций типов и документации улучшает понимание интерфейса функции.
