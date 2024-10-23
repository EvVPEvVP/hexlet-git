from functools import reduce
from operator import mul, add

def odometer(oksana):
    # Получаем скорости и времена
    speeds = oksana[::2]
    times = oksana[1::2]
    
    # Вычисляем интервалы времени
    time_intervals = [times[0]] + list(map(lambda x, y: x - y, times[1:], times[:-1]))
    
    # Вычисляем расстояния и суммируем их
    return reduce(add, map(mul, speeds, time_intervals))
