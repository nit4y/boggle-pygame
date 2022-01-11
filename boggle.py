
from boggle_game import BoggleGame
from boggle_ui import BoggleUserInterface

if __name__ == "__main__":
    """
    Runs a user interacted Boggle game.
    see BoggleGame, BoggleUserInterface for more details
    """
    game = BoggleGame()
    ui = BoggleUserInterface(game)
    ui.run()
    