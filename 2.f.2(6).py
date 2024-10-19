from pymonad.tools import curry
from functools import reduce

@curry(3)
def initialize_board(N, M, battalion):
    board = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(0, len(battalion), 2):
        x, y = battalion[i] - 1, battalion[i+1] - 1
        board[x][y] = 1
    return board

def is_valid(N, M, x, y):
    return 0 <= x < N and 0 <= y < M

@curry(3)
def get_neighbors(N, M, pos):
    x, y = pos
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return list(filter(lambda p: is_valid(N, M, p[0], p[1]), 
                       map(lambda d: (x + d[0], y + d[1]), directions)))

@curry(3)
def simulate_day(N, M, board):
    controlled = [(x, y) for x in range(N) for y in range(M) if board[x][y] == 1]
    new_controlled = reduce(lambda acc, pos: acc + get_neighbors(N, M, pos), controlled, [])
    return [[1 if (x, y) in new_controlled or board[x][y] == 1 else 0 for y in range(M)] for x in range(N)]

def is_fully_controlled(board):
    return all(all(cell == 1 for cell in row) for row in board)

def conquest_step(N, M, day, board):
    if is_fully_controlled(board):
        return day
    else:
        return conquest_step(N, M, day + 1, simulate_day(N, M, board))

def ConquestCampaign(N, M, L, battalion):
    initial_board = initialize_board(N, M, battalion)
    return conquest_step(N, M, 1, initial_board)

result = ConquestCampaign(3, 4, 2, [2, 2, 3, 4])
print(result)