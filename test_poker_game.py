import unittest

from poker import Hand


class TestPoker(unittest.TestCase):

    def test_royal_flash(self):
        hand = ['10H', 'JH', 'QH', 'KH', 'AH']
        poker = Hand(hand)
        royal_flash = poker.is_royal_flush()
        self.assertEqual(royal_flash, True)

    def test_royal_flash_lower_case(self):
        hand = ['10h', 'jH', 'Qh', 'kh', 'ah']
        poker = Hand(hand)
        royal_flash = poker.is_royal_flush()
        self.assertEqual(royal_flash, True)

    def test_non_royal_flash(self):
        hand = ['8S', '7S', '6S', '5S', '4S']
        poker = Hand(hand)
        royal_flash = poker.is_royal_flush()
        self.assertEqual(royal_flash, False)

    def test_straight_flush(self):
        hand = ['8S', '7S', '6S', '5S', '4S']
        poker = Hand(hand)
        straight_flat = poker.is_straight_flush()
        self.assertEqual(straight_flat, True)

    def test_straight_flush_lowercase(self):
        hand = ['8s', '7s', '6s', '5s', '4s']
        poker = Hand(hand)
        straight_flat = poker.is_straight_flush()
        self.assertEqual(straight_flat, True)

    def test_non_straight_flush(self):
        hand = ['5D', '5C', '5H', '5S', '3H']
        poker = Hand(hand)
        straight_flat = poker.is_straight_flush()
        self.assertEqual(straight_flat, False)

    def test_four_of_kind(self):
        hand = ['5D', '5C', '5H', '5S', '3H']
        poker = Hand(hand)
        four_of_kind = poker.is_four_of_kind()
        self.assertEqual(four_of_kind, True)

    def test_four_of_kind_lowercase(self):
        hand = ['5d', '5c', '5h', '5s', '3h']
        poker = Hand(hand)
        four_of_kind = poker.is_four_of_kind()
        self.assertEqual(four_of_kind, True)

    def test_non_four_of_kind(self):
        hand = ['KC', 'KH', 'KS', '5C', '8D']
        poker = Hand(hand)
        four_of_kind = poker.is_four_of_kind()
        self.assertEqual(four_of_kind, False)

    def test_tree_of_kind(self):
        hand = ['KC', 'KH', 'KS', '5C', '8D']
        poker = Hand(hand)
        tree_of_kind = poker.is_tree_of_kind()
        self.assertEqual(tree_of_kind, True)

    def test_tree_of_kind_lowercase(self):
        hand = ['Kc', 'kH', 'ks', '5c', '8d']
        poker = Hand(hand)
        tree_of_kind = poker.is_tree_of_kind()
        self.assertEqual(tree_of_kind, True)

    def test_non_tree_of_kind(self):
        hand = ['4D', '8D', '6D', '7D', '2D']
        poker = Hand(hand)
        tree_of_kind = poker.is_tree_of_kind()
        self.assertEqual(tree_of_kind, False)

    def test_full_house(self):
        hand = ['QC', 'QH', 'QS', '6C', '6D']
        poker = Hand(hand)
        full_house = poker.is_full_house()
        self.assertEqual(full_house, True)

    def test_non_full_house(self):
        hand = ['QC', 'QH', 'kC', '6C', '6D']
        poker = Hand(hand)
        full_house = poker.is_full_house()
        self.assertEqual(full_house, False)

    def test_flash(self):
        hand = ['4D', '8D', '6D', '7D', '2D']
        poker = Hand(hand)
        flash = poker.is_flush()
        self.assertEqual(flash, True)

    def test_non_flash(self):
        hand = ['4D', '8S', '6D', '7D', '2D']
        poker = Hand(hand)
        flash = poker.is_flush()
        self.assertEqual(flash, False)

    def test_straight(self):
        hand = ['3C', '4H', '5D', '6S', '7H']
        poker = Hand(hand)
        straight = poker.is_straight()
        self.assertEqual(straight, True)

    def test_non_straight(self):
        hand = ['3C', '9H', '5D', '6S', '7H']
        poker = Hand(hand)
        straight = poker.is_straight()
        self.assertEqual(straight, False)

    def test_two_pairs(self):
        hand = ['3S', '9C', '9H', '5D', '5S']
        poker = Hand(hand)
        two_pairs = poker.is_two_pairs()
        self.assertEqual(two_pairs, True)

    def test_non_two_pairs(self):
        hand = ['3S', '9C', '9H', '5D', '4S']
        poker = Hand(hand)
        two_pairs = poker.is_two_pairs()
        self.assertEqual(two_pairs, False)

    def test_pair(self):
        hand = ['9C', '10H', '6S', '6C', '2D']
        poker = Hand(hand)
        pair = poker.is_pair()
        self.assertEqual(pair, True)

    def test_non_pair(self):
        hand = ['9C', '10H', '7S', '6C', '2D']
        poker = Hand(hand)
        pair = poker.is_pair()
        self.assertEqual(pair, False)


if __name__ == '__main__':
    unittest.main()
