from abc import ABC, abstractmethod
from pygame.font import SysFont

class Scene(ABC):
    """ Scene is the base class for all scenes. 
        display     -> pygame Surface for game screen
        quit        -> quit the game when True
        done        -> current scene is no longer active scene
        sceneName   -> name of current scene
        nextScene   -> next scene object
    """
    def __init__(self, display):
        self.display = display
        self.done = False
        # pygame.font.SysFont(name, size, bold=False, italic=False) -> Font
        self.font = SysFont("arialblack", 20)
        super().__init__()

    @abstractmethod
    def handle_events(self, event):
        pass
    
    # @abstractmethod
    # def update(self):
    #     pass

    @abstractmethod
    def draw(self):
        pass
