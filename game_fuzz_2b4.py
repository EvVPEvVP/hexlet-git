class Card:
    def __init__(self, card_type, attributes):
        self.card_type = card_type
        self.attributes = attributes

    def get_type(self):
        return self.card_type

    def get_attributes(self):
        return self.attributes


class Deck:
    def __init__(self):
        self.cards = []

    def view_deck(self):
        return [card.get_type() for card in self.cards]

    def add_card_to_deck(self, card):
        self.cards.append(card)

    def remove_card_from_deck(self, card):
        if card in self.cards:
            self.cards.remove(card)


class Mage:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.mana = 0

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def cast_spell(self, spell):
        print(f"{self.name} casts {spell}! -2 health.")
        self.health -= 2

    def hit_with_staff(self):
        print(f"{self.name} hits with a staff! -1 health.")
        self.health -= 1

    def heal(self):
        print(f"{self.name} heals himself! +2 health.")
        self.health += 2


class TurnPhase:
    def __init__(self):
        self.current_phase = "Start"

    def get_current_phase(self):
        return self.current_phase

class GameController:
    def __init__(self):
        self.turn_phase = TurnPhase()


class GameState:
    def __init__(self):
        self.score = [0, 0]

    def initiate_game(self):
        print("Game initiated.")


class GameEngine:
    def __init__(self):
        self.game_state = GameState()
        self.winning_score = 10

    def start_game(self):
        self.game_state.initiate_game()

        while not self.check_for_winner():
            self.process_player_turn(1)
            self.print_game_state()

            if self.check_for_winner():
                break

            self.process_player_turn(2)
            self.print_game_state()

        print("Game Over. Player", self.get_winner(), "wins!")

    def process_player_turn(self, player_number, player_input):
        print("\nPlayer", player_number, "'s turn:")
        #player_input = input("Enter your move (f for Fireball, p for staff hit, h for heal): ")

        if player_input == 'f':
            self.game_state.score[player_number - 1] += 2
            print("Casting Fireball! -2 health.")
        elif player_input == 'p':
            self.game_state.score[player_number - 1] += 1
            print("Hitting with a staff! -1 health.")
        elif player_input == 'h':
            other_player_number = 3 - player_number  # Получаем номер другого игрока
            self.game_state.score[other_player_number - 1] -= 2  # Убираем 2 балла у другого игрока
            print("Healing! +2 health to Player", other_player_number)
        else:
            print("Invalid move. Try again.")

    def print_game_state(self):
        print("Current Scores:", self.game_state.score)

    def check_for_winner(self):
        for score in self.game_state.score:
            if score >= self.winning_score:
                return True
        return False

    def get_winner(self):
        max_score = max(self.game_state.score)
        return self.game_state.score.index(max_score) + 1


def main(player_input=None):
    game_engine = GameEngine()
    game_engine.start_game(player_input)


if __name__ == "__main__":
    main()

