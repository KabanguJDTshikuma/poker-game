def sequential_values(values):
    count = 0
    for i in range(0, len(values)-1):
        if values[i+1] - 1 != values[i]:
            count += 1
    if count == 0:
        return True
    else:
        return False


def hand_split(hand):
    suits = [card[-1] for card in hand]
    values = [card[:-1] for card in hand]
    return {'suits': suits, 'values': values}




class Deck:
    def __init__(self):
        # suits = ['Hearts','Diamonds','Clubs','Spades'] 
        suits = ['H', 'D', 'C', 'S']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [f'{value}{suit}' for suit in suits for value in self.ranks]
        self._royal_flash = ['A', 'K', 'Q', 'j', '10']

        def __repr__(self):
            return "Cards remaining in deck: {}".format(len(self.cards))

    def royal_flash(self, hand):
        if len(set(hand_split(hand)['suits'])) == 1 and hand_split(hand)['values'].sort() == self._royal_flash.sort():
            return True
        else:
            return False

    def straight_flush(self, hand):
        suits = [card[-1] for card in hand]
        values = [card[:-1] for card in hand]
        if len(set(suits)) == 1 and values.sort() == self._royal_flash.sort():
            return True






hand = ['10H', 'JH', 'QH', 'KH', 'AH']
deck = Deck()
print(deck.cards)
print(deck.royal_flash(hand))