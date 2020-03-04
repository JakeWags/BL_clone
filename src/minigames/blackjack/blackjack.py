##
# This is blackjack, a minigame in the BL_clone
# Author: Jake Wagoner
##
import sys
from deck import Deck
from hand import Hand


class Blackjack:
    # constructors
    def __init__(self):
        self.p_hand = Hand()
        self.d_hand = Hand()
        self.hands = [self.p_hand, self.d_hand]
        self.deck = Deck()
        self.deal(self.hands, 2)

    # public non-static methods

    # Deals random cards from the game deck into the hands specified
    # hands: array containing Hand instances
    # num: number of cards to deal to each
    def deal(self, hands, num):
        for h in hands:
            for i in range(0, num):
                h.add_card(self.deck.get_random_card())

    # todo
    def play(self):
        pass

    def reset(self):
        self.__init__()


g = Blackjack()
print(g.p_hand)
print(g.d_hand)


