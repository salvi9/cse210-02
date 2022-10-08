import random


class Card:
    """card that is chosen and the numbers of turns."""
    
    def __init__(self):
        self.card = 0

    "card chooses a random number (1,13)"
    def roll_card(self):
        self.card = random.randint(1, 13)
        return self.card
        # self.num_turns += 1

