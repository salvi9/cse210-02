from game.hilo import Card


class Director:
    "This class controls and starts the game "

    def __init__(self, player):
        "This function sets the value for this class"
        self.card = Card()
        self.base_card = 0
        self.next_card = 0
        self.user_guess = ""
        self.player = player 
        


    def high_low(self):
        "This function ask the user input if they want high or low cards"
        self.user_guess = input("High or low? [h/l] ")
        return (self.user_guess)
    
    def show_score(self):
        "This function will act according if the player guessed correctly or wrong, by adding or removing the corresponding points"

        if (self.base_card < self.next_card and self.user_guess == "h"):
            self.player.win()
        elif (self.base_card > self.next_card and self.user_guess == "l"):
            self.player.win()
        else:
            self.player.lose()

    def start_game(self):
        "This function starts the game in a loop until the player chooses to stop or quit"
        continue_playing = "y"
        while(continue_playing == "y"):

            self.base_card = self.card.roll_card()
            print("The card is ", self.base_card)

            self.user_guess = self.high_low()

            self.next_card = self.card.roll_card()
            print("The next card was ", self.next_card)

            self.user_guess = self.show_score()
            print("Your socre is: ", self.player.get_score())

            if (self.player.get_score() > 0):
                continue_playing = input("Continue? [y/n]")
            else:
                continue_playing = "n"
