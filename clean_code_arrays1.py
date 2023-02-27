1.

a)
def get_average(my_array):
   
    sum = my_array[0] + my_array[-1]
    avg = sum / 2.0
    return avg

my_array = [1, 2, 3, 4, 5]
print(get_average(my_array))

b)
def get_average(my_array):
    
    sum = 0
    for i in range(len(my_array)):
        if i == 0 or i == len(my_array) - 1:
            sum += my_array[i]
    avg = sum / 2.0
    return avg

my_array = [1, 2, 3, 4, 5]
print(get_average(my_array))


2.

a)
def reverse_string(my_string):
    
    char_array = []

    for char in my_string:
        char_array.append(char)

    reversed_array = char_array[::-1]
    reversed_string = "".join(reversed_array)

    return reversed_string

my_string = "hello, world!"
print(reverse_string(my_string))

b)
def reverse_string(my_string):
    char_stack = []

    for char in my_string:
        char_stack.append(char)

    reversed_string = ""
    while len(char_stack) > 0:
        reversed_string += char_stack.pop()

    return reversed_string


my_string = "hello, world!"
print(reverse_string(my_string))

3.

a)
def get_middle_element(arr):
    if len(arr) % 2 == 0:
        return (arr[len(arr) // 2 - 1] + arr[len(arr) // 2]) / 2
    else:
        return arr[len(arr) // 2]


arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4, 5, 6]
print(get_middle_element(arr1))
print(get_middle_element(arr2))

b)
def get_middle_element_seq_access(arr):
    count = len(arr)
    middle_index = count // 2
    middle_element = None
    prev_element = None
    
    for i, item in enumerate(arr):
        if i == middle_index:
            middle_element = item
            if count % 2 == 0:
                prev_index = middle_index - 1
                prev_element = arr[prev_index]
            break
            
        if count % 2 == 0 and i == middle_index - 1:
            prev_element = item

    if count % 2 == 0:
        middle_element = (prev_element + middle_element) / 2
        
    return middle_element

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4, 5, 6]
print(get_middle_element_seq_access(arr1))
print(get_middle_element_seq_access(arr2))


4.

a)
def find_element_by_index(arr, index):
	return arr[index]

b)
def find_element_by_value(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1

5.

a)
def find_element_by_index(arr, index):
    if index < 0 or index >= len(arr):
        return None
    return arr[index]

my_arr = [1, 2, 3, 4, 5]
print(find_element_by_index(my_arr, 3))

b)
def find_element_by_value(arr, value):
    for item in arr:
        if item == value:
            return item
    return None

my_arr = [1, 2, 3, 4, 5]
print(find_element_by_value(my_arr, 4))


