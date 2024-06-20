import math
from collections import namedtuple

RobotState = namedtuple("RobotState", "x y angle state")

# режимы работы устройства очистки
WATER = 1 # полив водой
SOAP  = 2 # полив мыльной пеной
BRUSH = 3 # чистка щётками

# взаимодействие с роботом вынесено в отдельную функцию
def transfer_to_cleaner(message):
    print(message)

# перемещение
def move(dist, state):
    angle_rads = state.angle * (math.pi / 180.0)
    new_state = RobotState(
        state.x + dist * math.cos(angle_rads),
        state.y + dist * math.sin(angle_rads),
        state.angle,
        state.state)
    transfer_to_cleaner(('POS(', new_state.x, ',', new_state.y, ')'))
    return new_state

# поворот
def turn(turn_angle, state):
    new_state = RobotState(
        state.x,
        state.y,
        state.angle + turn_angle,
        state.state)
    transfer_to_cleaner(('ANGLE', new_state.angle))
    return new_state

# установка режима работы
def set_state(new_internal_state, state):
    if new_internal_state == 'water':
        self_state = WATER
    elif new_internal_state == 'soap':
        self_state = SOAP
    elif new_internal_state == 'brush':
        self_state = BRUSH
    else:
        return state
    new_state = RobotState(
        state.x,
        state.y,
        state.angle,
        self_state)
    transfer_to_cleaner(('STATE', self_state))
    return new_state

# начало чистки
def start(state):
    transfer_to_cleaner(('START WITH', state.state))
    return state

# конец чистки
def stop(state):
    transfer_to_cleaner(('STOP',))
    return state

# интерпретация набора команд
def make(code, state):
    for command in code:
        cmd = command.split(' ')
        if cmd[0] == 'move':
            state = move(int(cmd[1]), state)
        elif cmd[0] == 'turn':
            state = turn(int(cmd[1]), state)
        elif cmd[0] == 'set':
            state = set_state(cmd[1], state)
        elif cmd[0] == 'start':
            state = start(state)
        elif cmd[0] == 'stop':
            state = stop(state)
    return state

# начальное состояние
initial_state = RobotState(0.0, 0.0, 0, WATER)

# конвейер
final_state = make(
    (
        'move 100',
        'turn -90',
        'set soap',
        'start',
        'move 50',
        'stop'
    ),
    initial_state
)
