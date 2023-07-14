from .scene import Scene
from .splashScene import SplashScene
from pygame.time import delay
# from .menuScene import MenuScene
# from .mainGame import MainGame
# from .gameOver import GameOver


class SceneManager:
    """ SceneManager is a state machine that changes scenes and sends Pygame 
        events to the current scene
    """
    def __init__(self, display):
        self.quit = False
        self.display = display
        self.currentScene: Scene = SplashScene(self.display)
        # self.previousScene = None

    def change_scene(self):
        if self.currentScene.done is True:
            delay(200)
            self.currentScene = self.currentScene.nextScene

        # if isinstance(self.currentScene, SplashScene):
        #     self.currentScene: Scene = MenuScene(self.display)
        # elif isinstance(self.currentScene, MenuScene):
        #     if self.currentScene.quit is True:
        #         self.quit = True
        #     else:
        #         self.currentScene: Scene = MainGame(self.display)
        # elif isinstance(self.currentScene, MainGame):
        #     self.currentScene: Scene = GameOver(self.display)
        # elif isinstance(self.currentScene, GameOver):
        #     if self.currentScene.quit is True:
        #         self.quit = True
        #     else:
        #         self.currentScene: Scene = MainGame(self.display)

    def handle_events(self, event):
        self.currentScene.handle_events(event)
        #self.change_scene()

    # def update(self):
    #     if self.currentScene.update() is True:
    #         self.change_scene()

    def draw(self):
        self.currentScene.draw()
