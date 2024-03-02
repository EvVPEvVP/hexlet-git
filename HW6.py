#Изменения в коде старались делаться минимальными и фокусировались на решении конкретных задач.
#Начиная с написания тестов перед кодом, каждый коммит был совершен после успешного прохождения соответствующих тестов.
#Динамика такая, что коммиты со временем становились чаще. А кол-во коммитов увеличивалось.
#Коммиты производились после завершения каждой небольшой задачи, что способствовало более частым итерациям и поддерживало высокое качество кода.
#В среднем, на каждую даже легкую задачу приходилось около 2-4 коммитов.
#Применение TDD в реальной работе важно, так как это обеспечивает постоянную проверку корректности кода и предотвращает возможные проблемы еще на этапе разработки.
#Мелкие итерации с частыми коммитами обеспечивают легкость отката изменений в случае неудачных экспериментов.


#Code1
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

#Test1
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add_positive_numbers(self):
        result = self.calculator.add(3, 5)
        self.assertEqual(result, 8)

    def test_add_negative_numbers(self):
        result = self.calculator.add(-2, -4)
        self.assertEqual(result, -6)

    def test_subtract_numbers(self):
        result = self.calculator.subtract(10, 7)
        self.assertEqual(result, 3)

    def test_multiply_numbers(self):
        result = self.calculator.multiply(2, 4)
        self.assertEqual(result, 8)

    def test_divide_numbers(self):
        result = self.calculator.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(5, 0)

if __name__ == '__main__':
    unittest.main()


#Code2
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def clear(self):
        self.cards = []

    def evaluate(self):
        # Проверка наличия минимального количества карт для оценки
        if len(self.cards) < 5:
            return None

        # Сортировка карт по значению
        sorted_cards = sorted(self.cards, key=lambda x: x.value, reverse=True)

        # Проверка наличия комбинаций
        if self.is_straight_flush(sorted_cards):
            return "Straight Flush"
        elif self.is_four_of_a_kind(sorted_cards):
            return "Four of a Kind"
        elif self.is_full_house(sorted_cards):
            return "Full House"
        elif self.is_flush(sorted_cards):
            return "Flush"
        elif self.is_straight(sorted_cards):
            return "Straight"
        elif self.is_three_of_a_kind(sorted_cards):
            return "Three of a Kind"
        elif self.is_two_pair(sorted_cards):
            return "Two Pair"
        elif self.is_one_pair(sorted_cards):
            return "One Pair"
        else:
            return "High Card"

    def is_straight_flush(self, cards):
        return self.is_straight(cards) and self.is_flush(cards)

    def is_four_of_a_kind(self, cards):
        for i in range(len(cards) - 3):
            if cards[i].value == cards[i + 1].value == cards[i + 2].value == cards[i + 3].value:
                return True
        return False

    def is_full_house(self, cards):
        return self.is_three_of_a_kind(cards) and self.is_one_pair(cards)

    def is_flush(self, cards):
        suits = set(card.suit for card in cards)
        return len(suits) == 1

    def is_straight(self, cards):
        for i in range(len(cards) - 1):
            if cards[i].value - 1 != cards[i + 1].value:
                return False
        return True

    def is_three_of_a_kind(self, cards):
        for i in range(len(cards) - 2):
            if cards[i].value == cards[i + 1].value == cards[i + 2].value:
                return True
        return False

    def is_two_pair(self, cards):
        pairs = 0
        for i in range(len(cards) - 1):
            if cards[i].value == cards[i + 1].value:
                pairs += 1
        return pairs == 2

    def is_one_pair(self, cards):
        for i in range(len(cards) - 1):
            if cards[i].value == cards[i + 1].value:
                return True
        return False

#Test2
import unittest
from hand import Hand, Card

class TestHand(unittest.TestCase):
    def test_evaluate_straight_flush(self):
        hand = Hand()
        hand.add_card(Card("Spades", 10))
        hand.add_card(Card("Spades", 9))
        hand.add_card(Card("Spades", 8))
        hand.add_card(Card("Spades", 7))
        hand.add_card(Card("Spades", 6))
        
        result = hand.evaluate()
        self.assertEqual(result, "Straight Flush")

    def test_evaluate_four_of_a_kind(self):
        hand = Hand()
        hand.add_card(Card("Hearts", 7))
        hand.add_card(Card("Diamonds", 7))
        hand.add_card(Card("Spades", 7))
        hand.add_card(Card("Clubs", 7))
        hand.add_card(Card("Hearts", 2))
        
        result = hand.evaluate()
        self.assertEqual(result, "Four of a Kind")


if __name__ == '__main__':
    unittest.main()



