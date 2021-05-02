import unittest

from poker_game import Poker


class TestPoker(unittest.TestCase):
    poker_game = Poker()

    def test_royal_flash(self):
        hand = ['10H', 'JH', 'QH', 'KH', 'AH']
        royal_flash = self.poker_game.royal_flash(hand)
        self.assertEqual(royal_flash, True)

    def test_royal_flash_lower_case(self):
        hand = ['10h', 'jH', 'Qh', 'kh', 'ah']
        royal_flash = self.poker_game.royal_flash(hand)
        self.assertEqual(royal_flash, True)

    def test_non_royal_flash(self):
        hand = ['8S', '7S', '6S', '5S', '4S']
        royal_flash = self.poker_game.royal_flash(hand)
        self.assertEqual(royal_flash, False)

    def test_straight_flush(self):
        hand = ['8S', '7S', '6S', '5S', '4S']
        straight_flat = self.poker_game.straight_flush(hand)
        self.assertEqual(straight_flat, True)

    def test_straight_flush_lowercase(self):
        hand = ['8s', '7s', '6s', '5s', '4s']
        straight_flat = self.poker_game.straight_flush(hand)
        self.assertEqual(straight_flat, True)

    def test_non_straight_flush(self):
        hand = ['5D', '5C', '5H', '5S', '3H']
        straight_flat = self.poker_game.straight_flush(hand)
        self.assertEqual(straight_flat, False)

    def test_four_of_kind(self):
        hand = ['5D', '5C', '5H', '5S', '3H']
        four_of_kind = self.poker_game.four_of_kind(hand)
        self.assertEqual(four_of_kind, True)

    def test_four_of_kind_lowercase(self):
        hand = ['5d', '5c', '5h', '5s', '3h']
        four_of_kind = self.poker_game.four_of_kind(hand)
        self.assertEqual(four_of_kind, True)

    def test_non_four_of_kind(self):
        hand = ['KC', 'KH', 'KS', '5C', '8D']
        four_of_kind = self.poker_game.four_of_kind(hand)
        self.assertEqual(four_of_kind, False)

    def test_tree_of_kind(self):
        hand = ['KC', 'KH', 'KS', '5C', '8D']
        tree_of_kind = self.poker_game.tree_of_kind(hand)
        self.assertEqual(tree_of_kind, True)

    def test_tree_of_kind_lowercase(self):
        hand = ['Kc', 'kH', 'ks', '5c', '8d']
        tree_of_kind = self.poker_game.tree_of_kind(hand)
        self.assertEqual(tree_of_kind, True)

    def test_non_tree_of_kind(self):
        hand = ['4D', '8D', '6D', '7D', '2D']
        tree_of_kind = self.poker_game.tree_of_kind(hand)
        self.assertEqual(tree_of_kind, False)

    def test_full_house(self):
        hand = ['QC', 'QH', 'QS', '6C', '6D']
        full_house = self.poker_game.full_house(hand)
        self.assertEqual(full_house, True)

    def test_non_full_house(self):
        hand = ['QC', 'QH', 'kC', '6C', '6D']
        full_house = self.poker_game.full_house(hand)
        self.assertEqual(full_house, False)

    def test_flash(self):
        hand = ['4D', '8D', '6D', '7D', '2D']
        flash = self.poker_game.flash(hand)
        self.assertEqual(flash, True)

    def test_non_flash(self):
        hand = ['4D', '8S', '6D', '7D', '2D']
        flash = self.poker_game.flash(hand)
        self.assertEqual(flash, False)

    def test_straight(self):
        hand = ['3C', '4H', '5D', '6S', '7H']
        straight = self.poker_game.straight(hand)
        self.assertEqual(straight, True)

    def test_non_straight(self):
        hand = ['3C', '9H', '5D', '6S', '7H']
        straight = self.poker_game.straight(hand)
        self.assertEqual(straight, False)

    def test_two_pairs(self):
        hand = ['3S', '9C', '9H', '5D', '5S']
        two_pairs = self.poker_game.two_pairs(hand)
        self.assertEqual(two_pairs, True)

    def test_non_two_pairs(self):
        hand = ['3S', '9C', '9H', '5D', '4S']
        two_pairs = self.poker_game.two_pairs(hand)
        self.assertEqual(two_pairs, False)

    def test_pair(self):
        hand = ['9C', '10H', '6S', '6C', '2D']
        pair = self.poker_game.pair(hand)
        self.assertEqual(pair, True)

    def test_non_pair(self):
        hand = ['9C', '10H', '6S', '7C', '2D']
        pair = self.poker_game.pair(hand)
        self.assertEqual(pair, False)


if __name__ == '__main__':
    unittest.main()
