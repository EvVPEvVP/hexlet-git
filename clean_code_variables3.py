1.

Example: Early Binding

def calculate_total(basket):
    DISCOUNT_RATE = 0.1
    total = 0
    for item in basket:
        if item["category"] == "books":
            total += item["price"] * 0.9
        else:
            total += item["price"]
    total *= (1 - DISCOUNT_RATE)
    print(f"The total cost is {total}")

basket = [
    {"name": "The Great Gatsby", "category": "books", "price": 10.99},
    {"name": "Red Bull Energy Drink", "category": "beverages", "price": 2.99},
    {"name": "Nike Running Shoes", "category": "apparel", "price": 59.99}
]
calculate_total(basket)



Example: Late Binding

def calculate_total(basket, discount_rate):
    total = 0
    for item in basket:
        if item["category"] == "books":
            total += item["price"] * 0.9
        else:
            total += item["price"]
    total *= (1 - discount_rate)
    print(f"The total cost is {total}")

basket = [
    {"name": "The Great Gatsby", "category": "books", "price": 10.99},
    {"name": "Red Bull Energy Drink", "category": "beverages", "price": 2.99},
    {"name": "Nike Running Shoes", "category": "apparel", "price": 59.99}
]
discount_rate = 0.1
calculate_total(basket, discount_rate)

Comment: 
Add the value of discount_rate as a parameter to the function calculate_total() instead of defining it within the function, making this an example of late binding. 


2.

Example: Early Binding

def get_employee_info(employee_id):
    TAX_RATE = 0.25
    employee = get_employee_by_id(employee_id)
    salary = employee["salary"]
    taxes = salary * TAX_RATE
    net_salary = salary - taxes
    print(f"Employee {employee['name']} with ID {employee_id} earns {salary}, pays {taxes} in taxes, and has a net salary of {net_salary}")

employee_id = 1234
get_employee_info(employee_id)



Example: Late Binding

def get_employee_info(employee_id, tax_rate):
    employee = get_employee_by_id(employee_id)
    salary = employee["salary"]
    taxes = salary * tax_rate
    net_salary = salary - taxes
    print(f"Employee {employee['name']} with ID {employee_id} earns {salary}, pays {taxes} in taxes, and has a net salary of {net_salary}")

employee_id = 1234
tax_rate = 0.25
get_employee_info(employee_id, tax_rate)

Comment: 
In this example, add the value of tax_rate as a parameter to the function get_employee_info() instead of defining it within the function, making this an example of late binding. 


3.

Example: Early Binding

SALES_TAX_RATE = 0.07

def calculate_price(item_price):
    price_with_tax = item_price * (1 + SALES_TAX_RATE)
    print(f"The price with tax is {price_with_tax}")

item_price = 9.99
calculate_price(item_price)



Example: Late Binding

import configparser

config = configparser.ConfigParser()
config.read("config.ini")
SALES_TAX_RATE = float(config["DEFAULT"]["SALES_TAX_RATE"])

def calculate_price(item_price):
    price_with_tax = item_price * (1 + SALES_TAX_RATE)
    print(f"The price with tax is {price_with_tax}")

item_price = 9.99
calculate_price(item_price)

Comment:
In this example, read the value of SALES_TAX_RATE from a configuration file using the configparser module. This allows us to change the value of SALES_TAX_RATE by editing the configuration file without modifying the code.



