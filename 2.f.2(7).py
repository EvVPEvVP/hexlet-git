from functools import reduce

def second_max(numbers):
    if len(numbers) < 2:
        return None  # Возвращаем None, если в списке меньше двух элементов
    
    return reduce(lambda acc, x: (max(acc[0], x), max(acc[1], min(acc[0], x))), 
                  numbers[1:], 
                  (numbers[0], float('-inf')))[1]

# Пример
numbers = [5, 4, 3, 2, 5]
result = second_max(numbers)
print(result)  # Выведет: 5
