7.1.

x - success
y - active
y1 - error
s - valid
x1 - available

7.2

def process_data(data, error):
    if error:
        return None
    processed_data = data + 10
    return processed_data

def validate_user(user, success):
    if success:
        if user.username == "admin" and user.password == "password" and "admin" in user.permissions and user.age >= 18 and user.location == "Russia" and user.status == "active":
            return "User validation successful. Welcome, {}!".format(user.username)
        return False
    return "User validation failed."

7.3

for vote in votes:
    x = vote / sum * 100
    ....

7.4

1.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first = True
last = False

for i in range(len(numbers)):
    number = numbers[i]
    if i == 0:
        first = True
    else:
        first = False

    if i == len(numbers) - 1:
        last = True
    else:
        last = False

    if first and last:
        print("This is the only number: {}".format(number))
    elif first:
        print("This is the first number: {}".format(number))
    elif last:
        print("This is the last number: {}".format(number))
    else:
        print("This is a number in the middle: {}".format(number))

2.

def calculate_speed(distance, time):
    speed = distance / time
    return speed

def determine_speed(speed):
    if speed > 20:
        return "fast"
    elif speed >= 10:
        return "average"
    return "slow"

fast = True
slow = not fast
distance = 30
time = 2

speed = calculate_speed(distance, time)
speed_category = determine_speed(speed)

if fast and (speed_category == "fast"):
    print("You are moving fast.")
elif slow and (speed_category == "slow"):
    print("You are moving slow.")
else:
    print("You are moving at an average speed.")

7.5

1. #код выше переписан с улучшенными переменными

def calculate_speed(x, y):
    z = x / y
    return z

def determine_speed(x):
    if x > 20:
        return "fast"
    elif x >= 10:
        return "average"
    return "slow"

distance = 30
time = 2
speed = calculate_speed(distance, time)
speed_category = determine_speed(speed)

2. #код переписан с улучшенными временными переменными

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])

    def transpose(self):
        transposed_matrix = []
        for j in range(self.columns):
            row = []
            for i in range(self.rows):
                row.append(self.matrix[i][j])
            transposed_matrix.append(row)
        self.matrix = transposed_matrix
        self.rows, self.columns = self.columns, self.rows