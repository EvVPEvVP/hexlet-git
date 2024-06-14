import math

# robot.py
x = 0.0
y = 0.0
angle = 0
state = 1  # WATER

WATER = 1
SOAP = 2
BRUSH = 3

def move(dist):
    global x, y
    angle_rads = angle * (math.pi/180.0)
    x += dist * math.cos(angle_rads)
    y += dist * math.sin(angle_rads)
    transfer(('POS(', x, ',', y, ')'))

def turn(turn_angle):
    global angle
    angle += turn_angle
    transfer(('ANGLE', angle))

def set_state(new_state):
    global state
    if new_state == 'water':
        state = WATER
    elif new_state == 'soap':
        state = SOAP
    elif new_state == 'brush':
        state = BRUSH
    transfer(('STATE', state))

def start():
    transfer(('START WITH', state))

def stop():
    transfer(('STOP',))

# command_parser.py
import robot

def parse_command(command):
    cmd = command.split(' ')
    if cmd[0] == 'move':
        robot.move(int(cmd[1]))
    elif cmd[0] == 'turn':
        robot.turn(int(cmd[1]))
    elif cmd[0] == 'set':
        robot.set_state(cmd[1])
    elif cmd[0] == 'start':
        robot.start()
    elif cmd[0] == 'stop':
        robot.stop()

def execute_commands(code):
    for command in code:
        parse_command(command)

# main.py
from command_parser import execute_commands

def transfer_to_cleaner(message):
    print(message)

def main():
    code = (
        'move 100',
        'turn -90',
        'set soap',
        'start',
        'move 50',
        'stop'
    )
    execute_commands(code)

if __name__ == '__main__':
    main()