from .scene import Scene
from pygame import Color
from pygame.locals import (KEYDOWN, K_ESCAPE, K_RETURN)

class SplashScene(Scene):
    def __init__(self, display):
        super().__init__(display)
        # pygame.font.render(text, antialias, color background=None) -> Surface
        self.title = self.font.render("Pygame Tic Tac Toe", True, Color(0,255,0))
        # pygame.Surface.get_rect(**kwargs) -> Rect : keyword args can set rect position
        self.titleRect = self.title.get_rect(center=(self.display.get_width()/2, self.display.get_height()/2))

    def handle_events(self, event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE or event.key == K_RETURN:
                self.done = True

    def draw(self):
        self.display.fill((0,0,0))
        self.display.blit(self.title, self.titleRect)
    
    def update(self):
        return self.done