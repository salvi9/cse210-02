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

#     "If player picks a high number and is correct is worth 100 points. Otherwise they lose 75 points"
#     def high(self):
#         if self.card_2 > self.card:
#             return +100
#         elif self.card_2 < self.card:
#             return -75
#
#     "If player picks a low number and is correct is worth 100 points. Otherwise they lose 75 points"
#     def low(self):
#         if self.card_2 < self.card:
#             return self.full_point + 100
#         elif self.card_2 > self.card:
#             return self.full_point - 75
#
# def main():
#     """Entry point of the app"""
#     score = 300
#     my_card = Card()
#     keep_playing = True
#     base_card = my_card.roll_card()
#     next_card = my_card.roll_card()
#     while keep_playing or (score <= 0):
#         print(f"The card is: {base_card}")
#         user_guess = input("Higher or lower= [h/l] ")
#         print(f"Next card was: {next_card}")
#         if user_guess.lower() == "h":
#             if next_card > base_card:
#                 score += 100
#             else:
#                 score -= 75
#         else:
#             if next_card < base_card:
#                 score += 100
#             else:
#                 score -= 75
#         print(f"Your score is: {score}")
#         play_again = input("Play Again? ")
#         if play_again.lower() == "y":
#             keep_playing = True
#         else:
#             keep_playing = False
#
#
# if __name__ == "__main__":
#     main()
