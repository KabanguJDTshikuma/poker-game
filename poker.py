from collections import Counter


class Deck:
    """ 1. create a deck.
        2. separate a value and suit of string representing a card.
        3. counts suits and values
    """
    def __init__(self, cards):
        self.cards = cards
        self.suits = ['H', 'D', 'C', 'S']
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.ranks = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12,
                      "K": 13, "A": 14}
        self.deck = [f'{value}{suit}' for suit in self.suits for value in self.values]
        self.cards_values = self.get_values()
        self.cards_suits = self.get_suits()
        self.values_count = Counter(self.cards_values)
        self.suits_count = Counter(self.cards_suits)

    def get_suits(self):
        return [card[-1].upper() for card in self.cards]

    def get_values(self):
        return [self.ranks[card[:-1].upper()] for card in self.cards]


class Hand(Deck):
    """ creation of hands """
    def __int__(self, cards):
        super().__init__(cards)

    @staticmethod
    def sequential_values(values):
        """evaluate if the elements of ranks are sequential"""
        count = 0
        for i in range(0, len(values) - 1):
            if values[i + 1] - 1 != values[i]:
                count += 1
        if count == 0:
            return True
        else:
            return False

    def check_suits_order(self):
        suits = []
        cards_zip = list(zip(self.get_values(), self.get_suits()))
        for k, v in self.values_count.items():
            if v == 2:
                for i in range(0, len(cards_zip)):
                    if k == cards_zip[i][0]:
                        suits.append(cards_zip[i][1])
        return suits

    def is_royal_flush(self):
        if len(set(self.cards_suits)) == 1 and set(self.cards_values) == set(
                range(10, 15)):
            return True
        return False

    def is_straight_flush(self):
        check_seq = self.sequential_values(sorted(self.cards_values))
        if len(set(self.cards_suits)) == 1 and check_seq is True and self.is_royal_flush() is False:
            return True
        return False

    def is_four_of_kind(self):
        if 4 in list(self.values_count.values()) and list(self.suits_count.values()).count(1) >= 3:
            return True
        return False

    def is_tree_of_kind(self):
        suits = sorted(list(self.suits_count.values()))
        if 3 in list(self.values_count.values()) and (
                suits.count(1) == 3 or suits == [1, 2, 2] or suits == [1, 1, 3]):
            return True
        return False

    def is_full_house(self):
        if self.is_tree_of_kind() and list(self.values_count.values()).count(2) == 1:
            suits = self.check_suits_order()
            if len(set(suits)) == 2:
                return True
        return False

    def is_flush(self):
        if len(set(self.cards_suits)) == 1:
            return True
        return False

    def is_straight(self):
        if self.sequential_values(sorted(self.cards_values)) and len(set(self.cards_suits)) > 1:
            return True
        return False

    def is_two_pairs(self):
        if list(self.values_count.values()).count(2) == 2:
            suits = self.check_suits_order()
            if len(suits) == 4:
                return True
        return False

    def is_pair(self):
        if list(self.values_count.values()).count(2) == 1:
            suits = self.check_suits_order()
            if len(suits) == 2:
                return True
        return False


class PlayPocker(Hand):
    def __int__(self, cards):
        super().__init__(cards)

    def poker_game(self):
        if self.is_royal_flush():
            return 'royal flush'
        elif self.is_straight_flush():
            return "straight flush"
        elif self.is_four_of_kind():
            return "four of kind"
        elif self.is_tree_of_kind():
            return "tree of kind"
        elif self.is_full_house():
            return "full house"
        elif self.is_flush():
            return "flush"
        elif self.is_straight():
            return "straight"
        elif self.is_two_pairs():
            return "two pairs"
        elif self.is_pair():
            return "pair"
        return "high card"


def main():
    hand = []
    cards = PlayPocker(hand)
    print(cards.deck)
    while True:
        if len(hand) < 5:
            card = input("Type a text card deck: ")
            if card.upper() in cards.deck:
                hand.append(card.upper())
            else:
                print("Please insert valid deck string!")
        else:
            print(cards.poker_game())
            hand = []


if __name__ == '__main__':
    main()
