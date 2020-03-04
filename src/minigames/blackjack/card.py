class Card:
    cards = {
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "jack": 10,
        "queen": 10,
        "king": 10,
        "ace": 11
    }

    @staticmethod
    def get_card_val(name):
        if name in Card.cards:
            return Card.cards[name]
        else:
            return None

    def __init__(self, name):
        self.name = name
        self.value = Card.get_card_val(name)

    def get_value(self):
        return self.value

    def get_name(self):
        return self.name

    def set_value(self, val):
        self.value = val

    def __str__(self):
        return self.name
