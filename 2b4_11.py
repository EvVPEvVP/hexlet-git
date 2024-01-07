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
    def __init__(self, health, mana):
        self.health = health
        self.mana = mana

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def cast_spell(self, spell):
        print(f"Casting {spell} spell!")

    def take_damage(self, amount):
        self.health -= amount


class GameEngine:
    def __init__(self):
        self.game_state = GameState()

    def start_game(self):
        self.game_state.initiate_game()

    def end_game(self):
        # Implement game ending logic
        pass

    def get_game_state(self):
        return self.game_state


class GameState:
    def __init__(self):
        self.current_phase = TurnPhase()

    def initiate_game(self):
        print("Game initiated.")

class TurnPhase:
    def __init__(self):
        self.current_phase = "Start"

    def get_current_phase(self):
        return self.current_phase

    def proceed_to_next_phase(self):
        print("Moving to the next phase.")
        self.current_phase = "NextPhase"

def main():
    # Создаем экземпляры классов
    card1 = Card("Fireball", {"damage": 10})
    card2 = Card("Healing", {"heal": 5})
    
    deck = Deck()
    deck.add_card_to_deck(card1)
    deck.add_card_to_deck(card2)

    mage = Mage(30, 10)

    game_engine = GameEngine()
    game_engine.start_game()

    print("Initial Mage Health:", mage.get_health())
    print("Initial Deck:", deck.view_deck())

    mage.cast_spell("Fireball")
    mage.take_damage(5)

    print("Mage Health after taking damage:", mage.get_health())

    game_state = game_engine.get_game_state()
    print("Current Game Phase:", game_state.current_phase.get_current_phase())
    game_state.current_phase.proceed_to_next_phase()
    print("Updated Game Phase:", game_state.current_phase.get_current_phase())

if __name__ == "__main__":
    main()


