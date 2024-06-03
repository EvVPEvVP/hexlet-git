class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0
        self.cleaning_device = 'water'
        self.cleaning_state = False

    def execute_command(self, command):
        parts = command.split()
        action = parts[0].lower()

        if action == 'move':
            distance = int(parts[1])
            self.move(distance)
        elif action == 'turn':
            angle = int(parts[1])
            self.turn(angle)
        elif action == 'set':
            device = parts[1].lower()
            self.set_device(device)
        elif action == 'start':
            self.start_cleaning()
        elif action == 'stop':
            self.stop_cleaning()

    def move(self, distance):
        from math import radians, cos, sin
        angle_rad = radians(self.angle)
        self.x += distance * cos(angle_rad)
        self.y += distance * sin(angle_rad)
        print(f"POS {self.x:.2f},{self.y:.2f}")

    def turn(self, angle):
        self.angle = (self.angle + angle) % 360
        print(f"ANGLE {self.angle}")

    def set_device(self, device):
        if device in ['water', 'soap', 'brush']:
            self.cleaning_device = device
            print(f"STATE {self.cleaning_device}")

    def start_cleaning(self):
        self.cleaning_state = True
        print(f"START WITH {self.cleaning_device}")

    def stop_cleaning(self):
        self.cleaning_state = False
        print("STOP")

def main():
    commands = [
        'move 100',
        'turn -90',
        'set soap',
        'start',
        'move 50',
        'stop'
    ]

    robot = Robot()
    for command in commands:
        robot.execute_command(command)

if __name__ == "__main__":
    main()
