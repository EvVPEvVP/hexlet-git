# Отчет:

#Проект – взял код из курса по ООП (монолит игра).
#Строк – 130
#Ошибки – ошибок выявил очень много, это из-за моего кода, где на вход подаются определенные значения и происходит действие мага. Здесь больше смотрел, какие данные подаёт на вход atheris. Там абсолютно необычные значения, например – “b123/asd/asd/asd/ads/#”. Самостоятельно естественно вряд ли бы тестировал такие случаи.



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

