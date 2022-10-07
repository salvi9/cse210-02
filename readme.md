# Hilo Game
#### cse210-02
Repository for our weekly Teams meeting.

## Overview
Hilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than the previous one. Points are won or lost based on whether or not the player guessed correctly.

## Rules
Hilo is played according to the following rules.

The player starts the game with 300 points. Individual cards are represented as a number from 1 to 13. The current card is displayed. The player guesses if the next one will be higher or lower. The the next card is displayed. The player earns 100 points if they guessed correctly. The player loses 75 points if they guessed incorrectly. If a player reaches 0 points the game is over. If a player has more than 0 points they decide if they want to keep playing. If a player decides not to play again the game is over.

## Requirements
The program must also meet the following requirements.

The program must include a README file. The program must include class and method comments. The program must have at least two classes. The program must remain true to game play described in the overview.

Teams Activity week 3
Object: keep Score

Class #1: Director
Behavior: Update players score start the game retrieve players input end the game Display current card End the game when player reaches 0

Method:
def start_game(self) def update_score () def players_input() def still_playing() def end_game() def display_card()

Class #2: Card Behavior: Pick a random card from # 1 to 13 Method: def card()