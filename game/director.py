from game.hilo import Card


class Director:
    """This class controls and starts the game """

    def __init__(self, player):
        """This function sets the value for this class"""
        self.card = Card()
        self.base_card = 0
        self.next_card = 0
        self.user_guess = ""
        self.player = player 

    def high_low(self):
        """This function asks the user's input to guess the next card as high or low"""
        self.user_guess = input("High or low? [h/l]: ")
        return self.user_guess
        
    def show_score(self):
        """This function will act according if the player guessed correctly or wrong, by adding or removing the
        corresponding points """

        if self.base_card < self.next_card and self.user_guess == "h":
            self.player.win()
            print()
            print("You're an awesome guesser!")
            print("You earned points!")
            print()
        elif self.base_card > self.next_card and self.user_guess == "l":
            self.player.win()
            print()
            print("You're an awesome guesser!")
            print("You earned points!")
        else:
            self.player.lose()
            print()
            print("I'm sorry, you lose points!")
            print()
    def start_game(self):
        """This function starts the game in a loop until the player chooses to stop or quit"""
        continue_playing = "y"
        while continue_playing == "y":

            self.base_card = self.card.roll_card()
            print("\nThe card is: ", self.base_card)
            print()
            print("That's an awesome card!")
            print()
            self.user_guess = self.high_low()

            self.next_card = self.card.roll_card()
            print("The next card was: ", self.next_card)

            self.show_score()
            print("Your score is: ", self.player.get_score())
            print("Keep going, you've got this!")
            if self.player.get_score() > 0:
                continue_playing = input("\nKeep playing? [y/n]")
            else:
                continue_playing = "n"
            if continue_playing == "y":
                print()
                print("Okay, awesome!")
                print()
            else:
                print()
                print("Okay, see you next time!")
                print()