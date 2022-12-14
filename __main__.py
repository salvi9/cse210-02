from game.director import Director
from game.player import Player


def main():
    """This function tells the director to start the game at the same time that it *creates* a player """

    player = Player()
    director = Director(player)
    director.start_game()


if __name__ == "__main__":
    main()
