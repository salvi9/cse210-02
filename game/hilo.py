"""I used randrange because it was easier to use it for me in a function than randomrandint without having to use if
statements """
from random import randrange


class Card:
    """This class has the information of the random cards being displayed."""

    def __init__(self):
        print()

    "card chooses a random number (1,13)"

    def roll_card(self):
        """Then returns the random value to roll card"""
        return randrange(1, 13)
