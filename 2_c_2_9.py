import pure_robot

class RobotApi:

    def setup(self, f_injection):
        self.functions = f_injection()

    def make(self, command):
        if not hasattr(self, 'cleaner_state'):
            self.cleaner_state = pure_robot.RobotState(0.0, 0.0, 0, pure_robot.WATER)

        cmd = command.split(' ')
        if cmd[0] == 'move':
            self.cleaner_state = self.functions['move'](self.functions['transfer'], int(cmd[1]), self.cleaner_state)
        elif cmd[0] == 'turn':
            self.cleaner_state = self.functions['turn'](self.functions['transfer'], int(cmd[1]), self.cleaner_state)
        elif cmd[0] == 'set':
            self.cleaner_state = self.functions['set_state'](self.functions['transfer'], cmd[1], self.cleaner_state)
        elif cmd[0] == 'start':
            self.cleaner_state = self.functions['start'](self.functions['transfer'], self.cleaner_state)
        elif cmd[0] == 'stop':
            self.cleaner_state = self.functions['stop'](self.functions['transfer'], self.cleaner_state)
        return self.cleaner_state

    def __call__(self, command):
        return self.make(command)


def inject_dependencies():
    return {
        'move': pure_robot.move,
        'turn': pure_robot.turn,
        'set_state': pure_robot.set_state,
        'start': pure_robot.start,
        'stop': pure_robot.stop,
        'transfer': transfer_to_cleaner
    }

def transfer_to_cleaner(message):
    print(message)

def double_move(transfer, dist, state):
    return pure_robot.move(transfer, dist * 2, state)


api = RobotApi()
api.setup(inject_dependencies)
# api.setup(lambda: {'move': double_move, 'turn': pure_robot.turn, 'set_state': pure_robot.set_state, 'start': pure_robot.start, 'stop': pure_robot.stop, 'transfer': transfer_to_cleaner})

client.py

from cleaner_api import api

api('move 100')
api('turn -90')
api('set soap')
api('start')
api('move 50')
s = api('stop')
