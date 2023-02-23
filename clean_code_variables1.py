1.
Without recommendation:

def calculate_total_price(items, discount):
    total_price = 0
    discounted_price = 0
    final_price = 0

    for item in items:
        total_price += item.price

    if discount > 0:
        discounted_price = total_price * discount / 100
        final_price = total_price - discounted_price
    else:
        final_price = total_price

    return final_price

With recommendation:

def calculate_total_price(items, discount):
    # Initializing variables where they are used for the first time	
    total_price = sum([item.price for item in items])
    discounted_price = 0
    final_price = total_price if discount <= 0 else 0

    if discount > 0:
        discounted_price = total_price * discount / 100
        final_price = total_price - discounted_price

    return final_price

2.
Without recommendation:

def calculate_average(numbers):
    total = 0
    count = 0
    average = 0

    for number in numbers:
        total += number
        count += 1

    if count > 0:
        average = total / count

    return average

With recommendation:

def calculate_average(numbers):
    # Initializing variables where they are used for the first time
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0

    return average

3.
Without recommendation:

def calculate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    i = 2

    while i < n:
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
        i += 1

    return fibonacci_sequence
    
With recommendation:

def calculate_fibonacci(n):
    # Initializing variables where they are used for the first time
    if n < 2:
        fibonacci_sequence = [0, 1][:n]
    else:
        fibonacci_sequence = [0, 1]

    i = 2
    while i < n:
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
        i += 1

    return fibonacci_sequence
    
4.
Without recommendation:

def calculate_median(numbers):
    numbers.sort()
    length = len(numbers)
    median = 0

    if length % 2 == 0:
        median = (numbers[length//2 - 1] + numbers[length//2]) / 2
    else:
        median = numbers[length//2]

    return median

With recommendation:

def calculate_median(numbers):
    # Initializing variables where they are used for the first time
    numbers_sorted = sorted(numbers)
    length = len(numbers_sorted)
    median = (numbers_sorted[length//2] + numbers_sorted[(length-1)//2]) / 2 if length % 2 == 0 else numbers_sorted[length//2]

    return median

5.
Without recommendation:

def process_data(data):
    total_sum = 0
    num_valid_entries = 0

    for entry in data:
        if is_valid(entry):
            total_sum += entry
            num_valid_entries += 1
    
    if num_valid_entries > 0:
        average = total_sum / num_valid_entries
    else:
        average = 0

    return average
    
With recommendation:

def process_data(data):
    total_sum = 0
    num_valid_entries = 0

    for entry in data:
        if is_valid(entry):
            total_sum += entry
            num_valid_entries += 1
    
    if num_valid_entries > 0:
        average = total_sum / num_valid_entries
    else:
        average = 0

    # Assigning "invalid" values to the variables
    total_sum = None
    num_valid_entries = None

    return average

6.
Without recommendation:

def find_largest_number(numbers):
    largest_number = None

    for number in numbers:
        if largest_number is None or number > largest_number:
            largest_number = number

    return largest_number

With recommendation:

def find_largest_number(numbers):
    largest_number = None

    for number in numbers:
        if largest_number is None or number > largest_number:
            largest_number = number

    # Assigning "invalid" values to the variables
    numbers = None

    return largest_number

7.
Without recommendation:

def calculate_average_grade(grades):
    total = 0
    count = 0

    for grade in grades:
        total += grade
        count += 1

    if count > 0:
        average = total / count
    else:
        average = 0

    return average

With recommendation:

def calculate_average_grade(grades):
    total = 0
    count = 0

    for grade in grades:
        total += grade
        count += 1

    if count > 0:
        average = total / count
    else:
        average = 0

    # Assigning "invalid" values to the variables
    grades = None
    total = None
    count = None

    return average

8.

Without recommendation:
def divide_numbers(a, b):
    # Initializing variables when they are declared
    quotient = 0

    # Dividing the numbers
    if b != 0:
        quotient = a / b

    # Returning the quotient
    return quotient
    
    
With recommendation: 
def divide_numbers(a, b):
    quotient = 0

    if b != 0:
        quotient = a / b

    # Assigning error values to the variables
    if quotient == 0:
        quotient = -1

    return quotient
    
9.

Without recommendation:
def find_largest_number(numbers):
    largest_number = None

    for number in numbers:
        if largest_number is None or number > largest_number:
            largest_number = number

    return largest_number

With recommendation:
def find_largest_number(numbers):
    largest_number = None

    for number in numbers:
        if largest_number is None or number > largest_number:
            largest_number = number

    # Assigning error values to the variables
    if largest_number is None:
        largest_number = -1

    return largest_number

10.

Without recommendation:
def calculate_salary(hours_worked, hourly_rate):
    salary = 0

    if hours_worked > 0 and hourly_rate > 0:
        salary = hours_worked * hourly_rate

    return salary    

With recommendation:
def calculate_salary(hours_worked, hourly_rate):
    salary = 0

    if hours_worked > 0 and hourly_rate > 0:
        salary = hours_worked * hourly_rate

    # Assigning error values to the variables
    if salary == 0:
        salary = -1

    return salary
    
11.

Without recommendation:
def find_average(numbers):
    total = 0
    count = 0

    for number in numbers:
        total += number
        count += 1

    if count > 0:
        average = total / count
    else:
        average = 0

    return average

With recommendation:
def find_average(numbers):
    total = 0
    count = 0

    for number in numbers:
        total += number
        count += 1

    if count > 0:
        average = total / count
    else:
        average = -1

    # Assigning error values to the variables
    if average == 0:
        average = "***ERROR***"

    return average

12.

Without recommendation:
def calculate_total_price(prices, tax_rate):
    subtotal = 0
    total_price = 0

    for price in prices:
        subtotal += price

    total_price = subtotal * (1 + tax_rate)

    return total_price
    
With recommendation:
def calculate_total_price(prices, tax_rate):
    subtotal = 0
    total_price = 0

    for price in prices:
        subtotal += price

    # Adding debugging statements to check variable validity
    assert subtotal >= 0, "Invalid subtotal: {}".format(subtotal)

    total_price = subtotal * (1 + tax_rate)

    # Adding debugging statements to check variable validity
    assert total_price >= 0, "Invalid total price: {}".format(total_price)

    return total_price

13.

Without recommendation:
def calculate_discounted_price(total_price, discount):
    discounted_price = 0

    discounted_price = total_price * discount / 100

    return discounted_price

With recommendation:
def calculate_discounted_price(total_price, discount):
    discounted_price = total_price * discount / 100

    # Adding debugging statements to check variable validity
    assert discounted_price >= 0, "Invalid discounted price: {}".format(discounted_price)

    return discounted_price

14.

Without recommendation:
def calculate_percentage(total_marks, obtained_marks):
    percentage = 0
    percentage = (obtained_marks / total_marks) * 100

    return percentage
    
With recommendation:   
def calculate_percentage(total_marks, obtained_marks):
    percentage = 0

    # Checking if the total marks are zero
    if total_marks == 0:
        print("Warning: Total marks cannot be zero")
        return None

    percentage = (obtained_marks / total_marks) * 100

    # Checking if the percentage is invalid
    if percentage < 0 or percentage > 100:
        print("Warning: Invalid percentage value")
        return None

    return percentage

15.

Without recommendation:
def calculate_discounted_price(total_price, discount):
    discounted_price = 0
    discounted_price = total_price * discount / 100

    return discounted_price
    
With recommendation:
def calculate_discounted_price(total_price, discount):
    discounted_price = 0

    # Checking the validity of the total price and discount
    assert total_price >= 0, "Total price cannot be negative"
    assert 0 <= discount <= 100, "Discount value is invalid"

    discounted_price = total_price * discount / 100

    # Checking the validity of the discounted price
    assert discounted_price >= 0, "Discounted price cannot be negative"

    return discounted_price

    








