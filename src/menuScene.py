import pygame
from .scene import Scene

from pygame.locals import (
    MOUSEBUTTONDOWN,
    KEYDOWN,
    K_ESCAPE
)

class MenuScene(Scene):
    """ MainMenu is the main menu of the game. Has clickable buttons for starting
        the game, setting options, and exiting the game. Inherits from abstract class
        Scene
    """
    def __init__(self, display):
        super().__init__(display)
        # pygame.font.render(text, antialias, color background=None) -> Surface
        self.playButton = self.font.render("Play Game", True, pygame.Color(0,255,0))
        # pygame.Surface.get_rect(**kwargs) -> Rect : keyword args can set rect position
        self.playButtonRect = self.playButton.get_rect(center=(self.display.get_width()/2, self.display.get_height()/2 - (self.display.get_height()/7)))
        # pygame.font.SysFont(name, size, bold=False, italic=False) -> Font
        self.quitButton = self.font.render("Quit Game", True, pygame.Color(0,255,0))
        self.quitButtonRect = self.quitButton.get_rect(center=(self.display.get_width()/2, self.display.get_height()/2 + (self.display.get_height()/7)))

    def handle_events(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.playButtonRect.collidepoint(event.pos):
                self.done = True
            elif self.quitButtonRect.collidepoint(event.pos):
                self.quit = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            self.quit = True
        

    def update(self):
        return self.done

    def draw(self):
        self.display.fill((0,0,0))
        self.display.blit(self.playButton, self.playButtonRect)
        self.display.blit(self.quitButton, self.quitButtonRect)


