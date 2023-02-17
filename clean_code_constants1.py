1.
def calculate_area(radius):
    return 3.14 * radius**2

# PI is constant
PI = 3.14
def calculate_area(radius):
    return PI * radius**2
    
2.
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# add the constanst
FAHRENHEIT_OFFSET = 32
FAHRENHEIT_TO_CELSIUS = 5/9
def convert_to_celsius(fahrenheit):
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS
    
3.
def convert_to_megabytes(bytes):
    return bytes / 1000000

# BYTES_IN_MEGABYTE is constant
BYTES_IN_MEGABYTE = 1000000
def convert_to_megabytes(bytes):
    return bytes / BYTES_IN_MEGABYTE

4.
def get_num_days_in_month(month):
    if month == 2:
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

# add the constants
DAYS_IN_FEBRUARY = 28
DAYS_IN_SHORT_MONTH = 30
DAYS_IN_LONG_MONTH = 31

def get_num_days_in_month(month):
    if month == 2:
        return DAYS_IN_FEBRUARY
    elif month in [4, 6, 9, 11]:
        return DAYS_IN_SHORT_MONTH
    else:
        return DAYS_IN_LONG_MONTH    
        
5.
def is_valid_size(size):
    return size >= 0 and size <= 1000

# MAX_SIZE is constant
MAX_SIZE = 1000
def is_valid_size(size):
    return size >= 0 and size <= MAX_SIZE

6. 

if not username or len(username) > 12 or len(username) < 3:
    raise ValueError("Invalid username")

# add the constants
MIN_USERNAME_LENGTH = 3
MAX_USERNAME_LENGTH = 12
if not username or len(username) > MAX_USERNAME_LENGTH or len(username) < MIN_USERNAME_LENGTH:
    raise ValueError("Invalid username")

7.

if len(my_list) != 0:
    print("List is not empty")

# IS_LIST_EMPTY is constant
IS_LIST_EMPTY = len(my_list) == 0
if not IS_LIST_EMPTY:
    print("List is not empty")

8.
import os
if os.environ.get("DEBUG") == "true":
    print("Debug mode enabled")

# DEBUG_MODE_ENABLED is constant
import os
DEBUG_MODE_ENABLED = os.environ.get("DEBUG") == "true"
if DEBUG_MODE_ENABLED:
    print("Debug mode enabled")

9.
def get_database_url():
    return "localhost:3306/mydatabase"

# add the constants
DATABASE_HOST = "localhost"
DATABASE_PORT = 3306
DATABASE_NAME = "mydatabase"
def get_database_url():
    return f"{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

10.
if user.role == 1:
    ...
elif user.role == 2:
    ...
elif user.role == 3:
    ...

# add the Class with constants for clarifying
class Role:
    ADMIN = 1
    USER = 2
    GUEST = 3

if user.role == Role.ADMIN:
    ...
elif user.role == Role.USER:
    ...
elif user.role == Role.GUEST:
    ...

11.
if time.time() - start_time > 60:
    ...
elif time.time() - start_time < 10:
    ...

# add the constants
TIMEOUT = 60
MIN_TIME = 10

if time.time() - start_time > TIMEOUT:
    ...
elif time.time() - start_time < MIN_TIME:
    ...

12.
def StartUp():
    global MAX_USERS
    MAX_USERS = 100
    
# Call the StartUp() function at the beginning of the program
StartUp()

# Use the constant in the program
if num_users > MAX_USERS:
    print("Maximum number of users exceeded.")









        
        
        
        
        
        
        
        
        
        
        
        
        
