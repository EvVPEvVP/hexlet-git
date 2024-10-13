from pymonad.Maybe import Just, Nothing

# посадка птиц на левую сторону
to_left = lambda num: lambda pole: (
    Nothing()
    if abs((pole[0] + num) - pole[1]) > 4
    else Just((pole[0] + num, pole[1]))
)

# посадка птиц на правую сторону
to_right = lambda num: lambda pole: (
    Nothing()
    if abs((pole[1] + num) - pole[0]) > 4
    else Just((pole[0], pole[1] + num))
)

# банановая кожура
banana = lambda x: Nothing()

# отображение результата
def show(maybe):
    result = maybe.getValue()  # используем getValue() для извлечения данных из Maybe
    if result is None:
        print("Канатоходец упал!")
    else:
        left_birds, right_birds = result
        print(f"Канатоходец удержался! Птицы слева: {left_birds}, птицы справа: {right_birds}")

# начальное состояние
begin = lambda: Just((0, 0))

# Тесты
show(
    begin()
    >> to_left(2)
    >> to_right(5)
    >> to_left(-2)  # Канатоходец упадет тут
)

show(
    begin()
    >> to_left(2)
    >> to_right(5)
    >> to_left(-1)  # Все нормально
)

show(
    begin()
    >> to_left(2)
    >> banana  # Банановая кожура
    >> to_right(5)
    >> to_left(-1)
)
