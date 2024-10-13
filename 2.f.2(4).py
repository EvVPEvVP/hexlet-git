from pymonad.maybe import Just, Nothing, Maybe
from pymonad.tools import curry

# посадка птиц на левую сторону
@curry(2)
def to_left(num, pole):
    if abs((pole[0] + num) - pole[1]) > 4:
        return Nothing
    else:
        return Just((pole[0] + num, pole[1]))

# посадка птиц на правую сторону
@curry(2)
def to_right(num, pole):
    if abs((pole[1] + num) - pole[0]) > 4:
        return Nothing
    else:
        return Just((pole[0], pole[1] + num))

# банановая кожура
def banana(_):
    return Nothing

# отображение результата
def show(maybe):
    if maybe == Nothing:
        print("Канатоходец упал!")
    else:
        left_birds, right_birds = maybe.value
        print(f"Канатоходец удержался! Птицы слева: {left_birds}, птицы справа: {right_birds}")

# начальное состояние
begin = lambda: Just((0, 0))

# Тесты
show(
    begin()
    .bind(to_left(2))
    .bind(to_right(5))
    .bind(to_left(-2))  # Канатоходец упадет тут
)

show(
    begin()
    .bind(to_left(2))
    .bind(to_right(5))
    .bind(to_left(-1))  # Все нормально
)

show(
    begin()
    .bind(to_left(2))
    .bind(banana)  # Банановая кожура
    .bind(to_right(5))
    .bind(to_left(-1))
)
