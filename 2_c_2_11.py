import math
from collections import namedtuple

RobotState = namedtuple("RobotState", "x y angle state")

# режимы работы устройства очистки
WATER = 1 # полив водой
SOAP  = 2 # полив мыльной пеной
BRUSH = 3 # чистка щётками

class StateMonad:
    def __init__(self, func):
        self.func = func

    def __call__(self, state):
        return self.func(state)

    def bind(self, f):
        return StateMonad(lambda s: 
            let(self(s), 
                lambda result, new_state: f(result)(new_state)))

    def __rshift__(self, f):
        return self.bind(f)

def let(value, f):
    return f(*value)

def transfer_to_cleaner(message):
    print(message)

def move(dist):
    def inner(state):
        angle_rads = state.angle * (math.pi/180.0)   
        new_state = RobotState(
            state.x + dist * math.cos(angle_rads),
            state.y + dist * math.sin(angle_rads),
            state.angle,
            state.state)  
        transfer_to_cleaner(('POS(',new_state.x,',',new_state.y,')'))
        return (None, new_state)
    return StateMonad(inner)

def turn(turn_angle):
    def inner(state):
        new_state = RobotState(
            state.x,
            state.y,
            state.angle + turn_angle,
            state.state)
        transfer_to_cleaner(('ANGLE',new_state.angle))
        return (None, new_state)
    return StateMonad(inner)

def set_state(new_internal_state):
    def inner(state):
        if new_internal_state=='water':
            self_state = WATER  
        elif new_internal_state=='soap':
            self_state = SOAP
        elif new_internal_state=='brush':
            self_state = BRUSH
        else:
            return (None, state)
        new_state = RobotState(
            state.x,
            state.y,
            state.angle,
            self_state)
        transfer_to_cleaner(('STATE',self_state))
        return (None, new_state)
    return StateMonad(inner)

def start():
    def inner(state):
        transfer_to_cleaner(('START WITH',state.state))
        return (None, state)
    return StateMonad(inner)

def stop():
    def inner(state):
        transfer_to_cleaner(('STOP',))
        return (None, state)
    return StateMonad(inner)

def run_commands(commands):
    initial_state = RobotState(0, 0, 0, WATER)
    
    monad = StateMonad(lambda s: (None, s))
    for command in commands:
        cmd = command.split(' ')
        if cmd[0] == 'move':
            monad = monad >> move(int(cmd[1]))
        elif cmd[0] == 'turn':
            monad = monad >> turn(int(cmd[1]))
        elif cmd[0] == 'set':
            monad = monad >> set_state(cmd[1])
        elif cmd[0] == 'start':
            monad = monad >> start()
        elif cmd[0] == 'stop':
            monad = monad >> stop()
    
    return monad(initial_state)[1]

# Пример использования
commands = [
    "move 100",
    "turn -90",
    "set soap",
    "start",
    "move 50",
    "stop"
]

final_state = run_commands(commands)
print(f"Final state: {final_state}")

# Альтернативный способ использования
def run_chain():
    initial_state = RobotState(0, 0, 0, WATER)
    chain = (
        StateMonad(lambda s: (None, s))
        >> move(100)
        >> turn(-90)
        >> set_state('soap')
        >> start()
        >> move(50)
        >> stop()
    )
    return chain(initial_state)[1]

final_state_chain = run_chain()
print(f"Final state from chain: {final_state_chain}")