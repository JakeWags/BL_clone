##
# Hand of cards for blackjack
# Author: Jake Wagoner
##


class Hand:
    # constructors
    def __init__(self):
        self.hand = []
        self.value = 0
        self.ace_indexes = []
        self.current_ace_index = 0

    # public non-static methods
    def add_card(self, card):
        self.hand.append(card)
        if card.get_name() == "ace":
            self.ace_indexes.append(len(self.hand) - 1)
        self.__sum_values()

    def __change_ace(self, card):
        card.set_value(1)
        self.current_ace_index += 1

    def get_hand(self):
        return self.hand

    def get_value(self):
        return self.value

    def get_card(self, index):
        return self.hand[index]

    def clear_hand(self):
        self.hand = []

    def has_ace(self):
        if len(self.ace_indexes) > 0:
            return True
        else:
            return False

    def __sum_values(self):
        self.value = 0
        for c in self.hand:
            self.value += c.get_value()

        if self.value > 21 and self.has_ace() and self.current_ace_index < len(self.ace_indexes):
            self.__change_ace(self.hand[self.ace_indexes[self.current_ace_index]])
            self.__sum_values()

    def __len__(self):
        return len(self.hand)

    def __str__(self):
        ret_val = []
        for card in self.hand:
            ret_val.append(card.__str__())
        return str(ret_val) + " :: Value = " + str(self.get_value())
