import math
from collections import namedtuple

RobotState = namedtuple("RobotState", "x y angle state")

# режимы работы устройства очистки
WATER = 1  # полив водой
SOAP = 2   # полив мыльной пеной
BRUSH = 3  # чистка щётками


# взаимодействие с роботом вынесено в отдельную функцию
def transfer_to_cleaner(message):
    print(message)

# перемещение
def move(transfer, dist, state):
    angle_rads = state.angle * (math.pi / 180.0)
    new_state = RobotState(
        state.x + dist * math.cos(angle_rads),
        state.y + dist * math.sin(angle_rads),
        state.angle,
        state.state)
    transfer(('POS(', new_state.x, ',', new_state.y, ')'))
    return new_state

# поворот
def turn(transfer, turn_angle, state):
    new_state = RobotState(
        state.x,
        state.y,
        state.angle + turn_angle,
        state.state)
    transfer(('ANGLE', new_state.angle))
    return new_state

# установка режима работы
def set_state(transfer, new_internal_state, state):
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
    transfer(('STATE', self_state))
    return new_state

# начало чистки
def start(transfer, state):
    transfer(('START WITH', state.state))
    return state

# конец чистки
def stop(transfer, state):
    transfer(('STOP',))
    return state

# интерпретация набора команд в постфиксной нотации
def execute_concatenative(transfer, stream, initial_state):
    stack = []
    state = initial_state

    for token in stream.split():
        if token.isdigit() or (token[1:].isdigit() and token[0] == '-'):
            stack.append(int(token))
        else:
            if token == 'move':
                dist = stack.pop()
                state = move(transfer, dist, state)
            elif token == 'turn':
                turn_angle = stack.pop()
                state = turn(transfer, turn_angle, state)
            elif token == 'set':
                mode = stack.pop()
                if mode == WATER:
                    state = set_state(transfer, 'water', state)
                elif mode == SOAP:
                    state = set_state(transfer, 'soap', state)
                elif mode == BRUSH:
                    state = set_state(transfer, 'brush', state)
            elif token == 'start':
                state = start(transfer, state)
            elif token == 'stop':
                state = stop(transfer, state)

    return state



initial_state = RobotState(0, 0, 0, WATER)
command_stream = "100 move -90 turn soap set start 50 move stop"
execute_concatenative(transfer_to_cleaner, command_stream, initial_state)
