from random import randrange
"I used randrange because it was easier to use it for me in a function than randomrandint without having to use if statements"

class Card:
    "This class has the information of the random cards being displayed."
    
    def __init__(self):
        print()

    "card chooses a random number (1,13)"
    def roll_card(self):
        return randrange(1,13)

        "Then returns the random value to roll card"
