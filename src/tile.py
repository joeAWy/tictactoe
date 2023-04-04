from pygame.sprite import Sprite
from pygame.image import load
import os
from .constants import DEFAULT_DISPLAY, MAX_COLUMNS, MAX_ROWS

TILE_IMAGES = []
TILE_IMAGES.append(load(os.path.join("assets", "empty_t.png")).convert())
TILE_IMAGES.append(load(os.path.join("assets", "cross_t.png")).convert())
TILE_IMAGES.append(load(os.path.join("assets", "circle_t.png")).convert())

class Tile(Sprite):
    def __init__(self, row, column):
        super().__init__()
        self.imageIndex = 0
        self.image = TILE_IMAGES[self.imageIndex]
        self.imageRect = TILE_IMAGES[self.imageIndex].get_rect()
        self.rowNumber = row
        self.columnNumber = column
        self.imageRect.centerx = round(float((DEFAULT_DISPLAY[0] - self.image.get_width() * MAX_COLUMNS) / 2) + self.image.get_width() * self.columnNumber + self.image.get_width() / 3)
        self.imageRect.centery = round(float((DEFAULT_DISPLAY[1] - self.image.get_height() * MAX_ROWS) / 2) + self.image.get_height() * self.rowNumber + self.image.get_height() / 3)

    def check_mouse_collision(self, x, y):
        if self.imageRect.collidepoint(x, y):
            if self.imageIndex == 2:
                self.imageIndex = 0
            else:
                self.imageIndex = self.imageIndex + 1
            self.image = TILE_IMAGES[self.imageIndex]
