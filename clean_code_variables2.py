In examples "With recommendation"  minimizing the scope of variables and making the code simpler and easier to understand

1.

Without recommendation:
def calculate_sum(numbers):
    result = 0
    
    for i in range(len(numbers)):
        result += numbers[i]
        
    print("The sum is:", result)
    
    print("The value of i is:", i)

calculate_sum([1, 2, 3, 4, 5])



With recommendation:
def calculate_sum(numbers):
    result = 0
    
    for num in numbers:
        result += num
        
    print("The sum is:", result)

calculate_sum([1, 2, 3, 4, 5])

2.

Without recommendation:
def find_duplicates(numbers):
    duplicates = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                duplicates.append(numbers[i])
                
    print("The value of i is:", i)
                
    if len(duplicates) > 0:
        print("The duplicates are:", duplicates)
    else:
        print("There are no duplicates.")
        
find_duplicates([1, 2, 3, 2, 4, 5, 3])



With recommendation:
def find_duplicates(numbers):
    duplicates = []
    for i, num_i in enumerate(numbers):
        for j, num_j in enumerate(numbers[i+1:], i+1):
            if num_i == num_j:
                duplicates.append(num_i)
                
    if len(duplicates) > 0:
        print("The duplicates are:", duplicates)
    else:
        print("There are no duplicates.")
        
find_duplicates([1, 2, 3, 2, 4, 5, 3])

3.

Without recommendation:
def calculate_average(numbers):
    total = 0
    count = 0
    
    for i in range(len(numbers)):
        total += numbers[i]
        count += 1
        
    average = total / count
    
    return average, i

nums = [1, 2, 3, 4, 5]
avg, i = calculate_average(nums)
print("The average is:", avg)



With recommendation:
def calculate_average(numbers):
    total = 0
    count = 0
    
    for num in numbers:
        total += num
        count += 1
        
    average = total / count
    
    return average

nums = [1, 2, 3, 4, 5]
avg = calculate_average(nums)
print("The average is:", avg)

4.

Without recommendation:
def calculate_area(width, height):
    area = 0
    if width > 0 and height > 0:
        area = width * height
    return area
    
    

With recommendation:
def calculate_area(width, height):
    if width > 0 and height > 0:
        area = width * height
        return area
    else:
        return 0
    
5.

Without recommendation:
def calculate_gpa(grades):
    total = 0
    for grade in grades:
        total += grade
    gpa = total / len(grades)
    return round(gpa, 2)

grades = [85, 92, 78, 90]
print("The GPA is:", calculate_gpa(grades))



With recommendation:
def calculate_gpa(grades):
    total = sum(grades)
    gpa = total / len(grades)
    return round(gpa, 2)

grades = [85, 92, 78, 90]
print("The GPA is:", calculate_gpa(grades))


6.

Without recommendation:
def calculate_discount(total_amount):
    discount = 0
    if total_amount >= 100:
        discount = 10
    elif total_amount >= 50:
        discount = 5
    final_amount = total_amount - discount
    return final_amount
    


With recommendation:
def calculate_discount(total_amount):
    discount = 0
    if total_amount >= 100:
        discount = 10
    elif total_amount >= 50:
        discount = 5
    return total_amount - discount

7.

Without recommendation:
def calculate_average(numbers):
    sum = 0
    count = 0
    for num in numbers:
        sum += num
        count += 1
    average = sum / count
    return average
    
    
With recommendation:    
def calculate_average(numbers):
    sum_of_numbers = sum(numbers)
    count_of_numbers = len(numbers)
    average = sum_of_numbers / count_of_numbers
    return average
    
8.

Without recommendation:
def calculate_interest(principal, rate, years):
    interest = 0
    if principal > 0 and rate > 0 and years > 0:
        interest = (principal * rate * years) / 100
    return interest
    
    

With recommendation:
def calculate_interest(principal, rate, years):
    if principal <= 0 or rate <= 0 or years <= 0:
        return 0
    interest = (principal * rate * years) / 100
    return interest
    
9.

Without recommendation:
def calculate_grade(points):
    if points >= 90:
        grade = 'A'
    elif points >= 80:
        grade = 'B'
    elif points >= 70:
        grade = 'C'
    elif points >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade
    
    

With recommendation:
def calculate_grade(points):
    if points >= 90:
        return 'A'
    elif points >= 80:
        return 'B'
    elif points >= 70:
        return 'C'
    elif points >= 60:
        return 'D'
    else:
        return 'F'
              
10.

Without recommendation:
def find_max(numbers):
    max_number = 0
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number
    
    

With recommendation:    
def find_max(numbers):
    if len(numbers) == 0:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number
    
11.

Without recommendation:
def calculate_discounted_price(price, discount):
    discounted_price = 0
    if price > 0 and discount > 0:
        discounted_price = price - (price * discount)
    return discounted_price
    
    

With recommendation:
def calculate_discounted_price(price, discount):
    if price <= 0 or discount <= 0:
        return 0
    discounted_price = price - (price * discount)
    return discounted_price
    
12.

Without recommendation:
def calculate_average(numbers):
    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1
    average = total / count
    return average
         
  

With recommendation:
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average
    
13.

Without recommendation:
def calculate_price(quantity, price_per_unit):
    total_price = 0
    if quantity > 0 and price_per_unit > 0:
        total_price = quantity * price_per_unit
    return total_price
    
  
    
With recommendation:
def calculate_price(quantity, price_per_unit):
    if quantity > 0 and price_per_unit > 0:
        total_price = quantity * price_per_unit
        return total_price
    return 0    

14.

Without recommendation:
def find_max(numbers):
    max_num = 0
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
    
    
    
With recommendation:
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
    
15.

Without recommendation:
def calculate_total_price(items):
    total_price = 0
    for item in items:
        item_price = item.get('price')
        item_quantity = item.get('quantity')
        total_price += item_price * item_quantity
    return total_price
    


With recommendation:
def calculate_total_price(items):
    total_price = 0
    for item in items:
        total_price += item.get('price') * item.get('quantity')
    return total_price









