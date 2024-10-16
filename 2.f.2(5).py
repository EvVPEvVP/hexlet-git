from pymonad.tools import curry
from pymonad.state import State

# Начальное состояние космической станции
initial_state = {
    'energy': 1000,
    'materials': 500,
    'crew': 100
}

# Определяем действия, которые можно выполнять на станции
@curry(2)
def mine_asteroids(amount, state):
    def computation(s):
        new_state = s.copy()
        new_state['energy'] -= amount * 2
        new_state['materials'] += amount
        return None, new_state
    return State(computation)

@curry(2)
def build_solar_panels(count, state):
    def computation(s):
        new_state = s.copy()
        new_state['energy'] += count * 50
        new_state['materials'] -= count * 30
        new_state['crew'] -= count * 2
        return None, new_state
    return State(computation)

@curry(2)
def train_crew(count, state):
    def computation(s):
        new_state = s.copy()
        new_state['energy'] -= count * 10
        new_state['crew'] += count
        return None, new_state
    return State(computation)

# Создаем цепочку действий
station_operations = State.insert(initial_state) \
    .then(mine_asteroids(100)) \
    .then(build_solar_panels(3)) \
    .then(train_crew(10)) \
    .then(mine_asteroids(50))

# Выполняем операции и получаем конечное состояние
final_state = station_operations.run(initial_state)[1]

print("Конечное состояние станции:")
print(f"Энергия: {final_state['energy']}")
print(f"Материалы: {final_state['materials']}")
print(f"Экипаж: {final_state['crew']}")