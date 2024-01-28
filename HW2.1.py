import atheris
import sys

def fuzzed_data(data):
    
    from game_fuzz_2b4 import GameEngine

    # Используем фазз-данные в качестве входных данных
    try:
        game_engine = GameEngine()
        game_engine.start_game(player_input=data)
    except Exception as e:
        # Выводим информацию о возникшей ошибке
        print(f"Fuzz test failed with input: {data}")
        print(f"Error message: {str(e)}")

# Запускаем фаззер
atheris.Setup(sys.argv, fuzzed_data)
atheris.Fuzz()

