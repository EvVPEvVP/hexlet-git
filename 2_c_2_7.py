-- Интерфейсы

from abc import ABC, abstractmethod

class IRobotState(ABC):

    @abstractmethod
    def get_x(self):
        pass

    @abstractmethod
    def get_y(self):
        pass

    @abstractmethod
    def get_angle(self):
        pass

    @abstractmethod
    def get_state(self):
        pass


class IRobotOperations(ABC):

    @abstractmethod
    def move(self, distance, state: IRobotState) -> IRobotState:
        pass

    @abstractmethod
    def turn(self, angle, state: IRobotState) -> IRobotState:
        pass

    @abstractmethod
    def set_state(self, new_state, state: IRobotState) -> IRobotState:
        pass

    @abstractmethod
    def start(self, state: IRobotState) -> IRobotState:
        pass

    @abstractmethod
    def stop(self, state: IRobotState) -> IRobotState:
        pass


-- Имплементация интерфейсов

import pure_robot

class RobotState(IRobotState):

    def __init__(self, x, y, angle, state):
        self.x = x
        self.y = y
        self.angle = angle
        self.state = state

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_angle(self):
        return self.angle

    def get_state(self):
        return self.state


class RobotOperations(IRobotOperations):

    def move(self, distance, state: IRobotState) -> IRobotState:
        return pure_robot.move(distance, state)

    def turn(self, angle, state: IRobotState) -> IRobotState:
        return pure_robot.turn(angle, state)

    def set_state(self, new_state, state: IRobotState) -> IRobotState:
        return pure_robot.set_state(new_state, state)

    def start(self, state: IRobotState) -> IRobotState:
        return pure_robot.start(state)

    def stop(self, state: IRobotState) -> IRobotState:
        return pure_robot.stop(state)


-- Класс CleanerApi

class CleanerApi:

    def __init__(self, state: IRobotState, operations: IRobotOperations):
        self.cleaner_state = state
        self.operations = operations

    def transfer_to_cleaner(self, message):
        print(message)

    def get_x(self):
        return self.cleaner_state.get_x()

    def get_y(self):
        return self.cleaner_state.get_y()

    def get_angle(self):
        return self.cleaner_state.get_angle()

    def get_state(self):
        return self.cleaner_state.get_state()

    def activate_cleaner(self, code):
        for command in code:
            cmd = command.split(' ')
            action = cmd[0]
            if action == 'move':
                self.cleaner_state = self.operations.move(int(cmd[1]), self.cleaner_state)
            elif action == 'turn':
                self.cleaner_state = self.operations.turn(int(cmd[1]), self.cleaner_state)
            elif action == 'set':
                self.cleaner_state = self.operations.set_state(cmd[1], self.cleaner_state)
            elif action == 'start':
                self.cleaner_state = self.operations.start(self.cleaner_state)
            elif action == 'stop':
                self.cleaner_state = self.operations.stop(self.cleaner_state)

-- Клиентская часть

from your_module import CleanerApi, RobotState, RobotOperations  
# главная программа
initial_state = RobotState(0.0, 0.0, 0, pure_robot.WATER)
operations = RobotOperations()
cleaner_api = CleanerApi(initial_state, operations)

commands = [
    'move 100',
    'turn -90',
    'set soap',
    'start',
    'move 50',
    'stop'
]

cleaner_api.activate_cleaner(commands)

print(cleaner_api.get_x(), cleaner_api.get_y(), cleaner_api.get_angle(), cleaner_api.get_state())
