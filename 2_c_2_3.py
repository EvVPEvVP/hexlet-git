class Robot:
    def __init__(self):
        self.position = Position()
        self.angle = Angle()
        self.cleaning_device = CleaningDevice()
    
    def execute_command(self, command):
        parts = command.split()
        action = parts[0].lower()

        if action == 'move':
            distance = int(parts[1])
            self.position.move(distance, self.angle.current_angle)
        elif action == 'turn':
            angle = int(parts[1])
            self.angle.turn(angle)
        elif action == 'set':
            device = parts[1].lower()
            self.cleaning_device.set_device(device)
        elif action == 'start':
            self.cleaning_device.start_cleaning()
        elif action == 'stop':
            self.cleaning_device.stop_cleaning()
        else:
            print("Unknown command")

class Position:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, distance, angle):
        from math import cos, sin, radians
        self.x += distance * cos(radians(angle))
        self.y += distance * sin(radians(angle))
        print(f"POS {self.x:.2f},{self.y:.2f}")

class Angle:
    def __init__(self):
        self.current_angle = 0

    def turn(self, angle):
        self.current_angle = (self.current_angle + angle) % 360
        print(f"ANGLE {self.current_angle}")

class CleaningDevice:
    def __init__(self):
        self.device = 'water'
        self.active = False

    def set_device(self, device):
        if device in ['water', 'soap', 'brush']:
            self.device = device
            print(f"STATE {self.device}")
        else:
            print("Unknown device")

    def start_cleaning(self):
        if not self.active:
            self.active = True
            print(f"START WITH {self.device}")

    def stop_cleaning(self):
        if self.active:
            self.active = False
            print("STOP")


robot = Robot()
commands = [
    'move 100',
    'turn -90',
    'set soap',
    'start',
    'move 50',
    'stop'
]

for command in commands:
    robot.execute_command(command)
