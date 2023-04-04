import os
import pygame
from src.constants import DEFAULT_DISPLAY
 
#*****Finds the path when or if you move the program onto another computer.
"""if getattr(sys, 'frozen', False):
    path = os.path.dirname(sys.executable)
elif __file__:
    path = os.path.dirname(__file__)"""

def main():
    """" Main program function """
    pygame.init()
    display = pygame.display.set_mode(DEFAULT_DISPLAY)
    pygame.display.set_caption("Pygame Tic Tac Toe")

    from game import Game
    game = Game(display)
    game.run_game()

    pygame.quit()

""" call the main function and start up the game """
if __name__ == "__main__":
    main()
