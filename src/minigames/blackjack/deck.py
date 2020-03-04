##
# Deck of cards
# Author: Jake Wagoner
##
from random import randint
from card import Card


class Deck:
    # instance variables
    card_names = ["two", "three", "four", "five", "six", "seven",
                  "eight", "nine", "ten", "jack", "queen", "king", "ace"]

    # constructors
    def __init__(self):
        self.deck = []
        self.__init_deck()

    # private methods
    def __init_deck(self):
        for name in self.card_names:
            for i in range(0, 4):
                self.deck.append(Card(name))

    # public non-static methods
    def get_deck(self):
        return self.deck

    def get_card_names(self):
        return self.card_names

    def get_random_card(self):
        n = randint(0, len(self.deck) - 1)
        d = self.deck[n]
        del self.deck[n]
        return d

    def __str__(self):
        return str(self.deck)
