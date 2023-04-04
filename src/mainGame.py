from .scene import Scene
from .tile import Tile
from pygame.sprite import Group
from pygame import Color
from pygame.locals import (
    MOUSEBUTTONDOWN,
    KEYDOWN,
    K_ESCAPE
)


class MainGame(Scene):
    def __init__(self, display):
        super().__init__(display)
        self.gameBoard = Group()
        self.rows = 3
        self.columns = 3
        for x in range(self.rows):
            for y in range(self.columns):
                self.gameBoard.add(Tile(x, y))
        # pygame.font.render(text, antialias, color background=None) -> Surface
        self.quitButton = self.font.render("Quit Game", True, Color(0,0,0))
        # pygame.Surface.get_rect(**kwargs) -> Rect : keyword args can set rect position
        self.quitButtonRect = self.quitButton.get_rect(center=(self.display.get_width() - 100, self.display.get_height() - 50))

    def handle_events(self, event):
        if event.type == MOUSEBUTTONDOWN:
            for tile in self.gameBoard:
                tile.check_mouse_collision(event.pos[0], event.pos[1])
            if self.quitButtonRect.collidepoint(event.pos):
                self.quit = True
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self.quit = True

    def update(self):
        return self.done

    def draw(self):
        self.display.fill((255,255,255))
        self.display.blit(self.quitButton, self.quitButtonRect)
        for tile in self.gameBoard:
            self.display.blit(tile.image, tile.imageRect)