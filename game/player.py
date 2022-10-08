class Player:
    """This class holds information about the player score and points earned or lost"""

    def __init__(self):
        """Sets the value for this class"""

        self.score = 300

    def win(self):
        """If the user guesses correctly gets 100+"""
        self.score += 100

    def lose(self):
        """If the user guesses wrong gets -75"""
        self.score -= 75
        if self.score < 0:
            self.score = 0

    def get_score(self):
        """Returns the current score"""
        return self.score
    
