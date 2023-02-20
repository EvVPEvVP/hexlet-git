1. #Проверяйте целочисленность операций деления (используйте подходящие операции деления).

def sum_of_numbers(a, b):
    sum = 0
    for i in range(a, b):
        if i % 2 == 0:
            sum += i / 2
        else:
            sum += i / 3
    return sum

With recommendations:

def sum_of_numbers(a: int, b: int) -> int:
    sum = 0
    for i in range(a, b):
        if i % 2 == 0:
            sum += i // 2
        else:
            sum += i // 3
    return sum

2. #Проверяйте возможное переполнение целых чисел.

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

With recommendations:

def factorial(n: int) -> int:
    result = 1
    for i in range(1, n+1):
        if result > sys.maxsize // i:
            raise OverflowError("Factorial overflow")
        result *= i
    return result

3. #Проверяйте на переполнение промежуточные результаты вычислений внутри выражений.

def calculate_total_price(quantity, price):
    total = quantity * price
    total += total * 0.05  # add 5% tax
    return total

With recommendations:

def calculate_total_price(quantity: int, price: float) -> float:
    total = quantity * price
    tax = total * 0.05  # calculate 5% tax
    if tax + total > sys.float_info.max:
        raise OverflowError("Overflow in calculation of total price")
    return total + tax
    
4. #Избегайте сложения и вычитания слишком разных по величине чисел.

def calculate_score(correct: int, total: int) -> float:
    return (correct / total) * 100.0
    
With recommendations:

def calculate_score(correct: int, total: int) -> float:
    if correct > 0 and total > 0 and correct / total < 0.01:
        raise ValueError("Ratio of correct to total answers is too small")
    return (correct / total) * 100.0
    
5. #Избегайте сравнений на равенство.

def get_greeting(name: str) -> str:
    if name == "Alice":
        return "Hello, Alice!"
    elif name == "Bob":
        return "Hello, Bob!"
    else:
        return "Hello, stranger."
        
With recommendations:

def get_greeting(name: str) -> str:
    greetings = {
        "Alice": "Hello, Alice!",
        "Bob": "Hello, Bob!"
    }
    if name in greetings:
        return greetings[name]
    else:
        return "Hello, stranger."

6. #Измените тип вещественной переменной на тип с большей точностью.

import math

def calculate_sqrt(x):
    return math.sqrt(x)

With recommendations:

import decimal

def calculate_sqrt(x):
    decimal_x = decimal.Decimal(x)
    sqrt_x = decimal_x.sqrt()
    return float(sqrt_x)
    
7. #Если вы используете числа с одинарной точностью, замените их числами с двойной точностью и т. д.

def calculate_sum():
    total = 0.0
    for i in range(10000000):
        total += 0.1
    return total

With recommendations:

def calculate_sum():
    total = 0.0
    for i in range(10000000):
        total += 0.1
    return round(total, 2)
    
8. #Измените в коде места, где используются значения с плавающей запятой, на целые значения, если это возможно.

def calculate_total_price(price_per_unit, quantity):
    total_price = price_per_unit * quantity
    tax_rate = 0.05
    tax_amount = total_price * tax_rate
    return total_price + tax_amount

With recommendations:

def calculate_total_price(price_per_unit, quantity):
    total_price = int(price_per_unit * quantity)
    tax_rate = 0.05
    tax_amount = int(total_price * tax_rate)
    return total_price + tax_amount

9. #Избегайте магических символов и строк -- используйте константы.

def calculate_area(shape, value1, value2):
    if shape == 'square':
        return value1 * value1
    elif shape == 'rectangle':
        return value1 * value2
    elif shape == 'triangle':
        return 0.5 * value1 * value2
    return None

With recommendations:

SHAPE_SQUARE = 'square'
SHAPE_RECTANGLE = 'rectangle'
SHAPE_TRIANGLE = 'triangle'

def calculate_area(shape, value1, value2):
    if shape == SHAPE_SQUARE:
        return value1 * value1
    elif shape == SHAPE_RECTANGLE:
        return value1 * value2
    elif shape == SHAPE_TRIANGLE:
        return 0.5 * value1 * value2
    return None

10. # используйте логические переменные для упрощения сложных условий

def can_vote(age, citizen, felony):
    if age >= 18 and citizen == "USA" and not felony:
        return True
    return False
        
With recommendations:

def can_vote(age, citizen, felony):
    is_of_voting_age = age >= 18
    is_us_citizen = citizen == "USA"
    has_no_felony = not felony
    
    if is_of_voting_age and is_us_citizen and has_no_felony:
        return True
    return False

11. # используйте логические переменные для упрощения сложных условий

if (user.is_admin and (user.has_permission or user.is_owner)) or (not user.is_admin and not user.is_guest):
    ...

With recommendations:

is_authorized = False

if user.is_admin:
    is_authorized = user.has_permission or user.is_owner
else:
    is_authorized = not user.is_guest

if is_authorized:
    ...
    
12. # используйте логические переменные для упрощения сложных условий

if (x > 0 and x < 10) or (y > 0 and y < 10):
    ...

With recommendations:

is_x_valid = x > 0 and x < 10
is_y_valid = y > 0 and y < 10

if is_x_valid or is_y_valid:
    ...

        
        
        
        
