import pygame
from src.sceneManager import SceneManager

from pygame.locals import (
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
    MOUSEMOTION,
    QUIT,
    KEYDOWN,
    K_ESCAPE,
    K_LEFT,
    K_RIGHT
)

class Game:
    """ GameEngine checks and handles Pygame events, maintains the game clock,
        sets the display resolution, and sends events to the SceneManager
    """
    def __init__(self, screen):
        self.isRunning = True
        self.display = screen
        pygame.event.set_allowed([MOUSEBUTTONDOWN, QUIT, KEYDOWN])
        self.clock = pygame.time.Clock()
        self.FPS = 25
        self.scene = SceneManager(self.display)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.isRunning = False
            elif event.type == MOUSEBUTTONDOWN or event.type == KEYDOWN:
                self.scene.handle_events(event)

    # def update(self):
    #     if self.scene.quit is True:
    #         self.isRunning = False
    #     self.scene.update()

    def draw(self):
        self.scene.draw()

    def run_game(self):
        while self.isRunning is True:
            self.clock.tick(self.FPS)
            self.handle_events()
            self.draw()
            self.scene.change_scene()
