##
# This is blackjack, a minigame in the BL_clone
# Author: Jake Wagoner
##

##
# Planned features:
#   - Currency, actual gambling
#   - Sprites
#   - Better dialogues / formatting
##

from deck import Deck
from hand import Hand


class Blackjack:
    # constructors
    def __init__(self):
        self.p_hand = Hand()
        self.d_hand = Hand()
        self.hands = [self.p_hand, self.d_hand]
        self.deck = Deck()
        self.playing = True
        self.deal(self.hands, 2)

    # public non-static methods

    # Deals random cards from the game deck into the hands specified
    # hands: array containing Hand instances
    # num: number of cards to deal to each
    def deal(self, hands, num):
        for h in hands:
            for i in range(0, num):
                h.add_card(self.deck.get_random_card())

    def play(self):
        print("It's time to play some Blackjack!")
        print("I'll deal you in, get as close to 21 as possible without going over and beat me!")
        print("Here's your cards: " + str(self.p_hand))
        print("The dealer's hand looks like this: [****, " + self.d_hand.get_card(-1).__str__() + "]")

        while self.playing:
            if self.make_action() == "1":
                self.__hit(self.p_hand)
                print("Here's your cards: " + str(self.p_hand))
                print("The dealer's hand looks like this: [****, " + self.d_hand.get_card(-1).__str__() + "]")
            else:
                self.__stay()

            if self.p_hand.get_value() > 21:
                print("Bust! You went over 21.")
                self.__lose()

    def make_action(self):
        print("Would you like to hit or stay?")
        print("1: Hit\n2: Stay")
        ans = input("--> ")
        if ans == '1' or ans == '2':
            return ans
        else:
            print("\n=======================")
            print("Invalid input.")
            print("=======================\n")
            self.make_action()

    def __hit(self, hand):
        self.deal([hand], 1)
        print("The new card is a " + hand.get_card(-1).__str__())

    def __stay(self):
        self.__dealer_actions()
        self.__end_game()

    # The dealer's actions
    def __dealer_actions(self):
        if self.d_hand.get_value() > 21:
            print("The dealer went over 21...")
            print("The dealer's hand looked like this: " + self.d_hand.__str__())
            self.__win()
        elif self.d_hand.get_value() < 17:
            self.__hit(self.d_hand)
            self.__dealer_actions()
        else:
            self.__compare_scores()

    def __compare_scores(self):
        print(self.p_hand)
        print(self.d_hand)

        if self.p_hand.get_value() > self.d_hand.get_value():
            self.__win()
        elif self.p_hand.get_value() < self.d_hand.get_value():
            self.__lose()
        else:
            self.__tie()

    def __win(self):
        print("You win!")
        self.__end_game()

    def __lose(self):
        print("You lose...")
        self.__end_game()

    def __tie(self):
        print("===========================")
        print("    You tied! Try again    ")
        print("===========================")
        self.__end_game()
        self.reset()

    def __end_game(self):
        self.playing = False

    def reset(self):
        self.__init__()
        self.play()


g = Blackjack()
g.play()


