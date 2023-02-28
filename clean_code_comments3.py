1.

Redundant comments:

# Initialize variables
x = 0  # x is 0
y = 1  # y is 1
z = 2  # z is 2

# Perform some calculation
result = x + y + z  # Calculate the sum of x, y, and z

Rewrite:
x = 0  # Initialize x to 0
y = 1  # Initialize y to 1
z = 2  # Initialize z to 2

result = x + y + z  # Calculate the sum of x, y, and z

2.

Mandated comments:

def divide_numbers(num1, num2):
    # Perform division
    result = num1 / num2

    # Return the result
    return result
        
Rewrite:
def divide_numbers(num1, num2):
    result = num1 / num2  # Perform division

    return result 
    
3.

Mumbling comments:

def perform_action(data):
    # Do some stuff here
    result = process_data(data)

    # Check the result
    if result is not None:
        # Do something with the result
        return result

Rewrite:

def perform_action(data):
    processed_data = process_data(data)  # Perform data processing

    if processed_data is not None:  # Check if the result is valid
        return processed_data  # Return the processed data
        
        
4.

Commented-out code:

def calculate_sum(numbers):
    # This code calculates the sum of a list of numbers
    # sum = 0
    # for number in numbers:
    #     sum += number
    # return sum

Rewrite:

def calculate_sum(numbers):
    sum = 0  # Calculate the sum of a list of numbers
    for number in numbers:
        sum += number
    return sum        
        
5.

Mandated comments:

class Animal:
    def __init__(self, name, age):
        # Set instance variables
        self.name = name
        self.age = age

Rewrite:

class Animal:
    def __init__(self, name, age):
        self.name = name  # Set the name of the animal
        self.age = age  # Set the age of the animal        
        
6.

Position markers:

# Import necessary libraries
import pandas as pd
import numpy as np

# Define data
data = np.random.rand(10, 5)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'])

# Perform analysis
# -------------------------------------------
# Analysis 1
mean_A = df['A'].mean()
std_A = df['A'].std()

# Analysis 2
mean_B = df['B'].mean()
std_B = df['B'].std()

# Print results
print("Mean of A:", mean_A)
print("Std of A:", std_A)
print("Mean of B:", mean_B)
print("Std of B:", std_B)
# -------------------------------------------

Rewrite:

import pandas as pd
import numpy as np

# Define data
data = np.random.rand(10, 5)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'])

# Perform analysis 1
mean_A = df['A'].mean()
std_A = df['A'].std()

# Perform analysis 2
mean_B = df['B'].mean()
std_B = df['B'].std()

# Print results
print("Mean of A:", mean_A)
print("Std of A:", std_A)
print("Mean of B:", mean_B)
print("Std of B:", std_B)        
        
    
7.

Mumbling comments:    
        
# Calculate the average of the given numbers
def average(numbers):
    # First, we calculate the sum of all the numbers
    total = sum(numbers)
    # Then, we divide the sum by the total count of numbers
    return total / len(numbers)

Rewrite:

def average(numbers):
    """
    Calculates the average of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The average of the given numbers.
    """
    total = sum(numbers)
    average = total / len(numbers)
    return average
        
8.

Commented-out code

# def add(a, b):
#     return a + b

def subtract(a, b):
    return a - b
    
Rewrite:

def subtract(a, b):
    """Subtracts two numbers and returns the result."""
    return a - b        
        
9.

Non-descriptive comments

# Start the loop
for i in range(10):
    # Do some stuff here
    pass

Rewrite:

for i in range(10):
    # Perform a task on each iteration of the loop
    pass        
        
10.

Non-obvious comments:

# Returns the factorial of n
def factorial(n):
    if n == 0:
        return 1
    else:
        # Compute the factorial using recursion
        return n * factorial(n-1)

Rewrite:

def factorial(n):
    """
    Computes the factorial of a given number.

    Args:
        n (int): The number to compute the factorial of.

    Returns:
        int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)        
        
        
11.

Redundant comment:

# Initialize variable x to 0
x = 0

# Perform loop operation
for i in range(10):
    x += 1
    # Add 1 to x
    
print(x)

Rewrite:

# Initialize the count of x to 0
x = 0

# Loop through 10 times, incrementing x each time
for i in range(10):
    x += 1

# Print the final value of x
print(x)

12.

Misleading comment

# Calculate the average of a list of numbers
def average(numbers):
    # Calculate the sum of the numbers
    total = sum(numbers)
    
    # Divide the sum by the number of elements
    avg = total / len(numbers)
    
    # Return the average
    return avg

Rewrite:

# Calculate the average value of a list of numbers
def average(numbers):
    # Calculate the sum of the numbers in the list
    total = sum(numbers)
    
    # Divide the sum by the number of elements in the list to get the average
    avg = total / len(numbers)
    
    # Return the calculated average value
    return avg

13.

Non-descriptive comment

# Calculate total
def calc_total(lst):
    total = 0
    for i in lst:
        total += i
    return total

Rewrite:

# Calculate the total sum of all numbers in the list
def calc_total(lst):
    total = 0
    for i in lst:
        total += i
    return total
       
14. 

Gratuitous comments:

# Initialize counter to zero
count = 0

# Loop through items in list
for item in my_list:
    # Increment counter by one
    count += 1

Rewrite:

count = 0

# Count the number of items in the list
for item in my_list:
    count += 1
        
15.


Gratuitous comments:

# This is a variable to store the user's name
user_name = "John"

# Print the welcome message
print("Welcome, " + user_name + "!")

Rewrite:

user_name = "John"

# Display the welcome message with the user's name
print("Welcome, " + user_name + "!")





