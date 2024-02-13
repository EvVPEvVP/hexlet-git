import random
from datetime import datetime

last_cached_time = datetime.now()

def last_midnight():
    return datetime.combine(datetime.today(), datetime.min.time())

def last_noon():
    return datetime.combine(datetime.today(), datetime.max.time() / 2)

def generate_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def deal_cards(players, deck):
    player_hands = {player: [] for player in players}
    for _ in range(2):
        for player in players:
            card = deck.pop()
            player_hands[player].append(card)
    return player_hands

def bet(player, amount, pot):
    pot += amount
    return pot

def flop(deck, community_cards):
    community_cards += deck[:3]
    del deck[:3]
    return community_cards

def turn(deck, community_cards):
    community_cards.append(deck.pop())
    return community_cards

def river(deck, community_cards):
    community_cards.append(deck.pop())
    return community_cards

def evaluate_hands(player_hands, community_cards):
    print("Player Hands:")
    for player, hand in player_hands.items():
        print(f"{player}: {hand}")
    print("\nCommunity Cards:")
    print(community_cards)

def pay_out(pot, players):
    winner = random.choice(players)
    print(f"{winner} wins the pot of {pot} chips!")
    return 0

def next_round(players, deck, pot, community_cards):
    bet("Player 1", 10, pot)
    bet("Player 2", 10, pot)
    flop(deck, community_cards)
    bet("Player 1", 20, pot)
    bet("Player 2", 20, pot)
    turn(deck, community_cards)
    bet("Player 1", 20, pot)
    bet("Player 2", 20, pot)
    river(deck, community_cards)
    bet("Player 1", 20, pot)
    bet("Player 2", 20, pot)
    evaluate_hands(deal_cards(players, deck), community_cards)
    pay_out(pot, players)

def end_game():
    print("Thanks for playing Texas Hold'em Heads-Up!")

def display_table(current_player, community_cards, pot):
    print("Current Table State:")
    print(f"Community Cards: {community_cards}")
    print(f"Pot: {pot}")
    print(f"Current Player: {current_player}")

def check_fold(current_player):
    print(f"{current_player} checks or folds.")

def validate_input():
    return True

def end_round(current_player, community_cards, pot, players, deck):
    display_table(current_player, community_cards, pot)
    check_fold(current_player)
    if validate_input():
        next_round(players, deck, pot, community_cards)
    else:
        end_game()

def reset_game(deck):
    deck = generate_deck()
    community_cards = []
    return deck, community_cards

if __name__ == "__main__":
    players = ["Player 1", "Player 2"]
    deck = generate_deck()
    community_cards = []
    pot = 0
    current_player = random.choice(players)

    print("Welcome to Texas Hold'em Heads-Up!")
    while True:
        deck, community_cards = reset_game(deck)
        player_hands = deal_cards(players, deck)
        next_round(players, deck, pot, community_cards)
        end_round(current_player, community_cards, pot, players, deck)

