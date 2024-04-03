#1.

Было:


result = calculate_total(items) + calculate_tax(items) + calculate_shipping(items, user_address, shipping_method)

В этой строке происходит несколько вычислений: расчет общей стоимости товаров, расчет налога и расчет стоимости доставки. Каждое из этих вычислений имеет свою отдельную ответственность и зависит от разных параметров.

Стало:

subtotal = calculate_subtotal(items)
tax = calculate_tax(subtotal)
shipping_cost = calculate_shipping_cost(subtotal, user_address, shipping_method)
result = subtotal + tax + shipping_cost

Теперь каждое вычисление вынесено в отдельную строку с понятным названием переменной. Это улучшает читаемость кода и упрощает его модификацию.

#2.

Было:

result = [item for sublist in [[x.upper() for x in row if x.startswith('a')] for row in data if len(row) > 3] for item in sublist]

В этой строке происходит:

1. Фильтрация списка `data`, оставляя только строки длиной больше 3.
2. Для каждой строки выбираются только элементы, начинающиеся с 'a'.
3. Каждый выбранный элемент приводится к верхнему регистру.
4. Результаты из всех строк объединяются в один  список.

Стало:

def filter_rows(data):
    return [row for row in data if len(row) > 3]

def filter_elements(row):
    return [x for x in row if x.startswith('a')]

def uppercase_elements(row):
    return [x.upper() for x in row]

filtered_data = filter_rows(data)
filtered_elements = [filter_elements(row) for row in filtered_data]
result = [item for sublist in [uppercase_elements(row) for row in filtered_elements] for item in sublist]

Теперь каждая операция вынесена в отдельную функцию или строку


#3

Было:

def calculate_total_price(items):
    return sum(item['price'] * item['quantity'] * (1 - item['discount'] / 100) + item['shipping_cost'] for item in items if item['quantity'] > 0 and item['price'] > 0)

В этой функции происходит несколько операций:

1. Проверка, что количество (`quantity`) и цена (`price`) каждого товара больше нуля.
2. Расчет стоимости каждого товара с учетом скидки (`discount`) и стоимости доставки (`shipping_cost`).
3. Суммирование стоимостей всех товаров.

Стало:

def is_valid_item(item):
    return item['quantity'] > 0 and item['price'] > 0

def calculate_item_price(item):
    base_price = item['price'] * item['quantity']
    discount_amount = base_price * item['discount'] / 100
    return base_price - discount_amount + item['shipping_cost']

def calculate_total_price(items):
    valid_items = [item for item in items if is_valid_item(item)]
    item_prices = [calculate_item_price(item) for item in valid_items]
    return sum(item_prices)

Такое разделение улучшает читаемость и понятность кода. Каждая функция имеет свою отдельную ответственность, что соответствует принципу SRP.

#4

Было:

def send_email(user):
    subject = f"Hello, {user['name']}!"
    body = f"Dear {user['name']},\n\nYour account balance is {user['balance']}.\n\nBest regards,\nThe Team"
    return send_mail(user['email'], subject, body) if is_valid_email(user['email']) else False

В этой функции происходит:

1. Формирование темы письма.
2. Формирование тела письма.
3. Проверка валидности email адреса.
4. Отправка email письма.

Все эти операции происходят в одной функции, что нарушает принцип единственной ответственности (SRP).

Стало:

def generate_subject(user):
    return f"Hello, {user['name']}!"

def generate_body(user):
    return f"Dear {user['name']},\n\nYour account balance is {user['balance']}.\n\nBest regards,\nThe Team"

def is_valid_email(email):
    pass

def send_email(user):
    subject = generate_subject(user)
    body = generate_body(user)
    if is_valid_email(user['email']):
        return send_mail(user['email'], subject, body)
    else:
        return False

1. `generate_subject` - формирование темы письма.
2. `generate_body` - формирование тела письма.
3. `is_valid_email` - проверка валидности email адреса.
4. `send_email` - отправка email письма, использующая другие функции.


#5

Было:

def process_data(data):
    return [(x['name'], x['value'] * 1.2 if x['value'] > 100 else x['value'] * 1.1, x['date'].strftime('%Y-%m-%d')) for x in data if x['category'] == 'A' and x['date'] > datetime(2022, 1, 1)]

В этой функции происходит несколько операций:

1. Фильтрация данных по категории 'A' и дате больше 1 января 2022 года.
2. Для каждого элемента данных:
   - Выбирается имя ('name').
   - Значение ('value') умножается на 1.2, если оно больше 100, иначе на 1.1.
   - Дата ('date') форматируется в строку в формате 'YYYY-MM-DD'.
3. Результаты собираются в список кортежей.

Стало:

from datetime import datetime

def is_valid_item(item):
    return item['category'] == 'A' and item['date'] > datetime(2022, 1, 1)

def calculate_value(value):
    return value * 1.2 if value > 100 else value * 1.1

def format_date(date):
    return date.strftime('%Y-%m-%d')

def process_item(item):
    name = item['name']
    value = calculate_value(item['value'])
    date = format_date(item['date'])
    return (name, value, date)

def process_data(data):
    valid_items = [item for item in data if is_valid_item(item)]
    processed_items = [process_item(item) for item in valid_items]
    return processed_items

Теперь каждая операция вынесена в отдельную функцию:

1. `is_valid_item` - фильтрация элементов по категории и дате.
2. `calculate_value` - расчет нового значения в зависимости от исходного значения.
3. `format_date` - форматирование даты в строку.
4. `process_item` - обработка одного элемента данных, используя другие функции.
5. `process_data` - обработка всех данных, используя другие функции.








