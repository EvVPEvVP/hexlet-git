3.1.1
def merge_lists(list1, list2):
    # Create a new empty list to hold the merged list
    merged_list = []
    # Loop through both lists until all elements have been merged
    while len(list1) > 0 and len(list2) > 0:
        # Compare the first elements of both lists
        if list1[0] < list2[0]:
            # Append the smaller element to the merged list and remove it from list1
            merged_list.append(list1.pop(0))
        else:
            # Append the smaller element to the merged list and remove it from list2
            merged_list.append(list2.pop(0))
    # Append any remaining elements from list1 or list2 to the merged list
    merged_list += list1
    merged_list += list2
    # Return the merged list
    return merged_list

3.1.2
def calculate_fibonacci_sequence(n):
    # If n is zero, return an empty list
    if n == 0:
        return []
    # If n is one, return a list with a single element: 0
    elif n == 1:
        return [0]
    # If n is greater than one, calculate the Fibonacci sequence up to the nth term
    else:
        # Start the sequence with the first two terms: 0 and 1
        sequence = [0, 1]
        # Loop until the sequence has n terms
        while len(sequence) < n:
            # Calculate the next term by adding the last two terms
            next_number = sequence[-1] + sequence[-2]
            # Append the next term to the sequence
            sequence.append(next_number)
        # Return the complete sequence
        return sequence

3.1.3

def sort_list(lst):
    # Check if the list is already sorted
    if sorted(lst) == lst:
        # If the list is already sorted, return it
        return lst
    
    # Otherwise, sort the list using selection sort
    for i in range(len(lst)):
        # Find the minimum element in the unsorted portion of the list
        min_idx = i
        for j in range(i+1, len(lst)):
            # Check if the current element is smaller than the current minimum
            if lst[j] < lst[min_idx]:
                # If it is, update the minimum index to the current index
                min_idx = j
        # Swap the minimum element with the first unsorted element
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    
    # Return the sorted list
    return lst

3.1.4

def calculate_distance(x1, y1, x2, y2):
    # Calculate the distance between two points using the Pythagorean theorem
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

3.1.5

def find_duplicate(nums):
    # Keep track of previously seen elements using a set
    seen = set()
    # Iterate over the list
    for num in nums:
        # If the current element has been seen before, it is a duplicate
        if num in seen:
            # Return the duplicate element
            return num
        # Otherwise, add the current element to the set of seen elements
        seen.add(num)
    # If no duplicates were found, return None
    return None



3.2.

1)
a)
# This function takes a list of numbers and returns the sum of the squares
def calculate_sum_of_squares(numbers):
    result = 0
    for number in numbers:
        square = number ** 2
        result += square
    return result
    
b)
def sum_of_squares(numbers):
    return sum([num ** 2 for num in numbers])

2)
a)
# Open the file and read its contents
file = open('data.txt', 'r')
content = file.read()
file.close()

# Split the content into lines and print each line
lines = content.split('\n')
for line in lines:
    print(line)
    
b)
with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip())
        
3)
a)
# Define a function that takes two lists and returns their intersection
def intersection(list1, list2):
    result = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                result.append(item1)
    return result

b)
def intersection(list1, list2):
    return list(set(list1).intersection(set(list2)))

4)
a)
# Define a function that calculates the factorial of a number
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is only defined for non-negative integers")
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

b)
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is only defined for non-negative integers")
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

5)
a)
# Define a function that takes a string and returns a list of words in the string
def split_string(input_string):
    word_list = []
    current_word = ""
    for char in input_string:
        if char == " ":
            if current_word != "":
                word_list.append(current_word)
                current_word = ""
        else:
            current_word += char
    if current_word != "":
        word_list.append(current_word)
    return word_list

b)
def split_string(input_string):
    return input_string.split()





