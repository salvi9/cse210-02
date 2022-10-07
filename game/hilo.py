import random


class Card:
    "card that is chosen and the numbers of turns."
    
    def __init__(self):
        self.card_1 = 0
        self.card_2 = 0
    

    "card chooses a random number (1,13)"
    def card(self):
        self.card_1 = random.randint(1, 13)
        return self.card_1        
        # self.num_turns += 1


    "If player picks a high number and is correct is worth 100 points. Otherwise they lose 75 points"
    def high(self):
        if self.card_2 > self.card_1:
            return +100
        elif self.card_2 < self.card_1:
            return -75

    "If player picks a low number and is correct is worth 100 points. Otherwise they lose 75 points"
    def low(self):
        if self.card_2 < self.card_1:
            return self.full_point +100
        elif self.card_2 > self.card_1:
            return self.full_point -75