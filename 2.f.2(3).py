from pymonad.tools import curry
from pymonad.maybe import Just, Nothing
from pymonad.list import ListMonad

# Каррированная функция сложения
@curry(2)
def add(x, y):
    return x + y

# Создаём функцию add10(), которая прибавляет 10 к переданному функтору
def add10(funct):
    return funct.map(add(10))

# Just
result_just = add10(Just(5))  # Just(15)

# ListMonad
result_list = add10(ListMonad(1, 2, 3))  # ListMonad(11, 12, 13)
