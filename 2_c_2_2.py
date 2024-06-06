class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0
        self.cleaning_device = 'water'
        self.cleaning_state = False

    def move(self, distance):
        import math
        radians = math.radians(self.angle)
        self.x += distance * math.cos(radians)
        self.y += distance * math.sin(radians)
        print(f"POS {self.x:.2f},{self.y:.2f}")

    def turn(self, angle):
        self.angle += angle
        print(f"ANGLE {self.angle % 360}")

    def set_cleaning_device(self, device):
        self.cleaning_device = device
        print(f"STATE {self.cleaning_device}")

    def start_cleaning(self):
        self.cleaning_state = True
        print(f"START WITH {self.cleaning_device}")

    def stop_cleaning(self):
        self.cleaning_state = False
        print("STOP")

    def execute_command(self, command):
        parts = command.split()
        action = parts[0].lower()
        
        if action == 'move':
            self.move(float(parts[1]))
        elif action == 'turn':
            self.turn(float(parts[1]))
        elif action == 'set':
            self.set_cleaning_device(parts[1].lower())
        elif action == 'start':
            self.start_cleaning()
        elif action == 'stop':
            self.stop_cleaning()
        else:
            print(f"Unknown command: {command}")

def main(commands):
    robot = Robot()
    for command in commands:
        robot.execute_command(command)

commands = [
    'move 100',
    'turn -90',
    'set soap',
    'start',
    'move 50',
    'stop'
]

main(commands)




