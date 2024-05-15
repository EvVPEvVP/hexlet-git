
1. Валидация возраста пользователя:

# Было
def register_user(name, age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age < 18:
        raise ValueError("User must be at least 18 years old")
    # ...

# Стало
class Age(int):
    def __new__(cls, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        if value < 18:
            raise ValueError("User must be at least 18 years old")
        return super().__new__(cls, value)

def register_user(name, age: Age):
    # ...

Комментарий: Вместо проверок возраста внутри функции `register_user`, был создан специальный тип `Age`, который наследуется от `int` и выполняет валидацию при создании экземпляра. Теперь функция `register_user` принимает параметр `age` типа `Age`, и некорректные значения возраста будут отклонены на этапе создания объекта `Age`.

2. Проверка наличия ключа в словаре:

# Было
def get_user_email(user_dict):
    if "email" in user_dict:
        return user_dict["email"]
    else:
        return None

# Стало
from typing import Dict

def get_user_email(user_dict: Dict[str, str]) -> str:
    return user_dict["email"]

Комментарий: Вместо проверки наличия ключа "email" в словаре `user_dict`, был явно указан тип словаря `Dict[str, str]`, что гарантирует наличие ключа "email". Если ключ отсутствует, возникнет ошибка на этапе компиляции или выполнения, но это будет явной ошибкой, а не неявным возвратом `None`.

3. Проверка допустимых значений перечисления:

# Было
def set_user_status(status):
    if status not in ["active", "inactive", "suspended"]:
        raise ValueError("Invalid user status")
    # ...

# Стало
from enum import Enum

class UserStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

def set_user_status(status: UserStatus):
    # ...

Комментарий: Вместо проверки допустимых значений статуса пользователя в виде строк, мы создали перечисление `UserStatus` с предопределенными значениями. Теперь функция `set_user_status` принимает параметр типа `UserStatus`, и некорректные значения будут отклонены на этапе компиляции или выполнения.


4. Проверка диапазона значений:

# Было
def calculate_discount(total_amount, discount_percent):
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Invalid discount percentage")
    # ...

# Стало
from typing import NewType

Percentage = NewType("Percentage", int)

def is_valid_percentage(value: int) -> bool:
    return 0 <= value <= 100

def validate_percentage(value: int) -> Percentage:
    if not is_valid_percentage(value):
        raise ValueError("Invalid discount percentage")
    return Percentage(value)

def calculate_discount(total_amount, discount_percent: Percentage):
    # ...

Комментарий: Вместо проверки диапазона значений процента скидки внутри функции `calculate_discount`, был создан новый тип `Percentage` и функции `is_valid_percentage` и `validate_percentage`. Функция `is_valid_percentage` проверяет, находится ли значение в допустимом диапазоне (от 0 до 100), а функция `validate_percentage` выполняет валидацию и возвращает значение типа `Percentage`. Теперь функция `calculate_discount` принимает параметр типа `Percentage`, и некорректные значения будут отклонены на этапе вызова функции `validate_percentage`.

5. Проверка формата email:

# Было
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def send_email(email, subject, body):
    if not is_valid_email(email):
        raise ValueError("Invalid email address")
    # ...

# Стало
from typing import NewType
from email_validator import validate_email, EmailNotValidError

EmailAddress = NewType("EmailAddress", str)

def validate_email_address(value: str) -> EmailAddress:
    try:
        valid_email = validate_email(value).email
        return EmailAddress(valid_email)
    except EmailNotValidError:
        raise ValueError("Invalid email address")

def send_email(email: EmailAddress, subject, body):
    # ...

Комментарий: Вместо проверки формата email с помощью регулярного выражения внутри функции `send_email`, был создан новый тип `EmailAddress` и функция `validate_email_address`. Функция `validate_email_address` использует библиотеку `email_validator` для проверки корректности email и возвращает значение типа `EmailAddress`. Если email некорректный, возникает исключение `ValueError`. Теперь функция `send_email` принимает параметр типа `EmailAddress`, и некорректные email будут отклонены на этапе вызова функции `validate_email_address`.


