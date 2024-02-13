import random
from datetime import datetime

class Player:
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank
        self.hand = []

    def make_bet(self, amount):
        self.bank -= amount
        return amount

    def receive_cards(self, cards):
        self.hand += cards

class PokerGame:
    def __init__(self, players):
        self.players = [Player(name, 1000) for name in players]  # банк 1000
        self.deck = self.generate_deck()
        self.community_cards = []
        self.pot = 0
        self.current_player = random.choice(self.players)

    def generate_deck(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
        random.shuffle(deck)
        return deck

    def deal_cards(self):
        for _ in range(2):
            for player in self.players:
                card = self.deck.pop()
                player.receive_cards([card])

    def bet(self, player, amount):
        self.pot += player.make_bet(amount)

    def flop(self):
        self.community_cards += self.deck[:3]
        del self.deck[:3]

    def turn(self):
        self.community_cards.append(self.deck.pop())

    def river(self):
        self.community_cards.append(self.deck.pop())

    def evaluate_hands(self):
        print("Player Hands:")
        for player in self.players:
            print(f"{player.name}: {player.hand}")
        print("\nCommunity Cards:")
        print(self.community_cards)

    def pay_out(self):
        winner = max(self.players, key=lambda player: self.evaluate_hand(player.hand + self.community_cards))
        winner.bank += self.pot
        print(f"{winner.name} wins the pot of {self.pot} chips!")
        self.pot = 0

    def next_round(self):
        for player in self.players:
            self.bet(player, 10)
        self.flop()
        for player in self.players:
            self.bet(player, 20)
        self.turn()
        for player in self.players:
            self.bet(player, 20)
        self.river()
        for player in self.players:
            self.bet(player, 20)
        self.evaluate_hands()
        self.pay_out()
        self.end_round()

    def end_game(self):
        print("Thanks for playing Texas Hold'em Heads-Up!")

    def display_table(self):
        print("Current Table State:")
        print(f"Community Cards: {self.community_cards}")
        print(f"Pot: {self.pot}")
        print(f"Current Player: {self.current_player.name}")

    def check_fold(self):
        print(f"{self.current_player.name} checks or folds.")

    def validate_input(self):
        return True

    def end_round(self):
        self.display_table()
        self.check_fold()
        if self.validate_input():
            self.next_round()
        else:
            self.end_game()

    def reset_game(self):
        self.deck = self.generate_deck()
        self.community_cards = []

if __name__ == "__main__":
    players = ["Player 1", "Player 2"]
    poker_game = PokerGame(players)
    print("Welcome to Texas Hold'em Heads-Up!")
    while True:
        poker_game.reset_game()
        poker_game.deal_cards()
        poker_game.next_round()
        poker_game.end_round()


