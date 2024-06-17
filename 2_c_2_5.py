from pure_robot import RobotState, make, transfer_to_cleaner

class RobotAPI:
    def __init__(self, x=0, y=0, angle=0, state='water'):
        self.state = RobotState(x, y, angle, state)

    def move(self, distance):
        self.state = make(transfer_to_cleaner, [f'move {distance}'], self.state)

    def turn(self, angle):
        self.state = make(transfer_to_cleaner, [f'turn {angle}'], self.state)

    def set_state(self, new_state):
        self.state = make(transfer_to_cleaner, [f'set {new_state}'], self.state)

    def start_cleaning(self):
        self.state = make(transfer_to_cleaner, ['start'], self.state)

    def stop_cleaning(self):
        self.state = make(transfer_to_cleaner, ['stop'], self.state)

    def execute_commands(self, commands):
        self.state = make(transfer_to_cleaner, commands, self.state)

    def get_position(self):
        return self.state.x, self.state.y

    def get_angle(self):
        return self.state.angle

    def get_state(self):
        return self.state.state