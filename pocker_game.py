from collections import Counter
from collections import defaultdict

def sequential_values(ranks:list):
    """evaluate if the elements of ranks are sequential"""
    count = 0
    for i in range(0, len(ranks)-1):
        if ranks[i+1] - 1 != ranks[i]:
            count += 1
    if count == 0:
        return True
    else:
        return False


def hand_split(hand:list, value_dict=None):
    """split suits and ranks from the hand and return them as dictionary of lists"""
    suits = [card[-1] for card in hand]
    values = [value_dict[card[:-1]] for card in hand]
    hand_split_dict = list(zip(values, suits))
    return {'suits': suits, 'values': values, 'hands': hand_split_dict}




class Deck:
    def __init__(self):
        # suits = ['Hearts','Diamonds','Clubs','Spades'] 
        suits = ['H', 'D', 'C', 'S']
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.ranks = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13, "A":14}
        self.cards = [f'{value}{suit}' for suit in suits for value in self.values]
    


    def royal_flash(self, hand:list):
        if len(set(hand_split(hand, self.ranks)['suits'])) == 1 and set(hand_split(hand, self.ranks)['values']) == set(range(10, 15)):
            return True
        return False

    def straight_flush(self, hand:list):
        values = sorted(hand_split(hand, self.ranks)['values'])
        if len(set(hand_split(hand, self.ranks)['suits'])) == 1 and sequential_values(values) == True and self.royal_flash(hand) == False:
            return True
        return False


    def four_of_kind(self, hand:list):
        value_count = Counter(hand_split(hand, self.ranks)['values'])
        suits_count = Counter(hand_split(hand, self.ranks)['suits'])

        if 4 in list(value_count.values()) and list(suits_count.values()).count(1) >=4:
            return True
        return False

    def tree_of_kind(self, hand:list):
        value_count = Counter(hand_split(hand, self.ranks)['values'])
        suits_count = Counter(hand_split(hand, self.ranks)['suits'])
        suits = list(suits_count.values())
        # print(hand_split(hand, self.ranks)['hands'])

        if 3 in list(value_count.values()) and (suits.count(1) == 3 or sorted(suits) == [1, 2, 2] or sorted(suits) == [1, 1, 3]):
            return True
        return False

    def full_house(self, hand:list):
        value_count = Counter(hand_split(hand, self.ranks)['values'])
        # suits_count = Counter(hand_split(hand, self.ranks)['suits'])
        hands_zip = hand_split(hand, self.ranks)['hands']
        suits = []
        if self.tree_of_kind(hand) and list(value_count.values()).count(2) == 1:
            for k,v in value_count.items():
                if v == 2:
                    for i in range(0, len(hands_zip)):
                        if k == hands_zip[i][0]:
                            suits.append(hands_zip[i][1])
            if len(set(suits)) == 2:
                return True
            else:
                return False
        
        return False

    def flash(self, hand:list):
        if len(set(hand_split(hand, self.ranks)['suits'])) == 1:
            return True
        return False

    def straight(self, hand:list):
        values = sorted(hand_split(hand, self.ranks)['values'])
        print(values, sequential_values(values))
        if sequential_values(values) and len(set(hand_split(hand, self.ranks)['suits'])) > 1:
            return True
        return False

    def two_pairs(self, hand:list):
        value_count = Counter(hand_split(hand, self.ranks)['values'])
        # suits_count = Counter(hand_split(hand, self.ranks)['suits'])
        hands_zip = hand_split(hand, self.ranks)['hands']
        suits = []
        if list(value_count.values()).count(2) == 2:
            for k,v in value_count.items():
                if v == 2:
                    for i in range(0, len(hands_zip)):
                        if k == hands_zip[i][0]:
                            suits.append(hands_zip[i][1])
            if len(suits) == 4:
                print(suits)
                return True
            else:
                return False

    def pair(self, hand:list):
        value_count = Counter(hand_split(hand, self.ranks)['values'])
        # suits_count = Counter(hand_split(hand, self.ranks)['suits'])
        hands_zip = hand_split(hand, self.ranks)['hands']
        suits = []
        if list(value_count.values()).count(2) == 1:
            for k,v in value_count.items():
                if v == 2:
                    for i in range(0, len(hands_zip)):
                        if k == hands_zip[i][0]:
                            suits.append(hands_zip[i][1])
            if len(suits) == 2:
                return True
            else:
                return False
        
        return False

    def high_card(self, hand:list):
        if not self.pair(hand) and not self.two_pairs(hand) and not self.flash(hand) and not straight(hand) and not self.royal_flash(hand) and not self.straight_flush(hand) and not self.four_of_kind(hand) and not self.tree_of_kind(hand) and not self.full_house(hand) and not self.flash(hand):
            return True
        return False


hand = ['9S', '10H', '6C', '6S','2D']
deck = Deck()
# print(deck.values)
print(deck.pair(hand))