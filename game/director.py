from game.hilo import Card


class Director:

    def __init__(self):
        self.card = Card()
        self.base_card = self.card.roll_card()
        self.next_card = self.card.roll_card()
        self.user_guess = ""
        self.score = 300
        self.keep_playing = True

    def start_game(self):
        """Gets things going and will be cycled through every time they choose to play another round"""
        while self.keep_playing:
            self.do_updates()
            self.do_outputs()
            self.get_inputs()

    def get_inputs(self):
        """Starts things out by getting assigning card_1"""
        play_again = input("Play Again: ")
        if play_again.lower() == "y":
            self.keep_playing = True
        else:
            self.keep_playing = False

    def do_updates(self):
        """Checks the guess of the player by reaching into Card.py and gives or takes points accordingly."""
        if self.user_guess.lower() == "high":
            if self.next_card > self.base_card:
                self.score += 100
            else:
                self.score -= 75
        else:
            if self.next_card < self.base_card:
                self.score += 100
            else:
                self.score -= 75
        self.keep_playing = True if self.score > 0 else False
        print(f"Your score is: {self.score}")

    def do_outputs(self):
        # Outputs the important game information for each round of play. it shows the player
        # their first card and shows them their score. it then asks them if they would like another card
        # if yes, it gets their guess and start everything over.
        # if no, it stops the game.
        print(f"The card is: {self.base_card}")
        self.user_guess = input("High or Low? [high/low]: ")
        print(f"Next Card is: {self.next_card}")
