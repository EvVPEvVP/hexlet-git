# Рефлексия
# Комментарии перед кодом могут быть инструментом для повышения понимания кода на более высоком уровне. Они предоставляют контекст о том, как код вписывается в общую систему.
# Эти комментарии могут быть полезными для других разработчиков, которые будут поддерживать или взаимодействовать с кодом в будущем.
# Такие комментарии помогают понять, как класс или модуль взаимодействует с остальной системой. Это важно для глобального понимания функциональности.
# Разработчики, знакомые с общей структурой системы, смогут более эффективно поддерживать и модифицировать код.
# При необходимости внесения изменений в код или добавлении новых функций, понимание общего контекста поможет избежать ошибок и непредвиденных последствий.
# Без комментариев может быть сложно понять, какие именно компоненты взаимодействуют и как. Комментарии предоставляют абстрактное представление о взаимосвязях.
# Сложность кода может привести к недопониманию его смысла. Комментарии помогают уменьшить этот риск.
# Комментарии позволяют подниматься на уровень абстракции выше, чем детали реализации, облегчая восприятие целостной картины.
# Поддерживать чистоту и структурированность кода с комментариями способствует эффективной работе в команде.
# Комментарии перед кодом могут быть ключевым элементом при передаче проекта между разработчиками и сохранении его жизненного цикла.





# Класс Hand представляет руку игрока в покере. Этот класс отвечает за хранение карт на руке,
# добавление новых карт, очистку руки и оценку комбинации на руке. Оценка комбинации
# осуществляется с использованием различных методов, проверяющих наличие комбинаций
# в руке, таких как стрит-флеш, каре, фулл-хаус и другие. Класс не знает о деталях
# реализации системы и может быть использован в контексте более общего игрового движка.
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

