from .scene import Scene
from .splashScene import SplashScene
from .menuScene import MenuScene
from .mainGame import MainGame


class SceneManager:
    """ SceneManager is a state machine that changes scenes and sends Pygame 
        events to the current scene
    """
    def __init__(self, display):
        self.quit = False
        self.display = display
        self.currentScene: Scene = SplashScene(self.display)
        self.previousScene = None

    def change_scene(self):
        if isinstance(self.currentScene, SplashScene):
            self.previousScene = self.currentScene
            self.currentScene: Scene = MenuScene(self.display)
        elif isinstance(self.currentScene, MenuScene):
            self.previousScene = self.currentScene
            self.currentScene: Scene = MainGame(self.display)

    def handle_events(self, event):
        self.currentScene.handle_events(event)

    def update(self):
        if self.currentScene.update() is True:
            self.change_scene()
        if self.currentScene.quit is True:
            self.quit = True

    def draw(self):
        self.currentScene.draw()
