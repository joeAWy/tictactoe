from .scene import Scene
from .gameOver import GameOver
from .tile import Tile, EMPTY_TILE, CROSS_TILE, CIRCLE_TILE
from pygame.sprite import Group
from pygame import Color
from pygame.event import post
from pygame.display import update
from pygame.locals import (
    MOUSEBUTTONDOWN,
    KEYDOWN,
    K_ESCAPE,
    QUIT
)

PLAYER1_SCORE = 0
PLAYER2_SCORE = 0

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
        self.quitButton = self.font.render("Quit Game?", True, Color(0,0,0))
        # pygame.Surface.get_rect(**kwargs) -> Rect : keyword args can set rect position
        self.quitButtonRect = self.quitButton.get_rect(center=(self.display.get_width() - 100, self.display.get_height() - 50))
        self.nextScene = GameOver(self.display)
        self.player1Score = self.font.render("Player 1:   " + str(PLAYER1_SCORE), True, Color(0,0,0))
        self.player2Score = self.font.render("Player 2:   " + str(PLAYER2_SCORE), True, Color(0,0,0))
        self.player1ScoreRect = self.player1Score.get_rect(center=(self.display.get_width() - 150, 50))
        self.player2ScoreRect = self.player2Score.get_rect(center=(self.display.get_width() - 150, 100))

    def handle_events(self, event):
        if event.type == MOUSEBUTTONDOWN:
            for tile in self.gameBoard:
                tile.check_mouse_collision(event.pos[0], event.pos[1])
            self.check_game_over()
            if self.quitButtonRect.collidepoint(event.pos):
                self.done = True
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                # self.done = True
                post(QUIT)

    # def update(self):
    #     self.check_game_over()
    #     return self.done

    def draw(self):  # todo make sure last draw occurs before changing to game-over screen
        self.display.fill((255,255,255))
        self.display.blit(self.quitButton, self.quitButtonRect)
        self.display.blit(self.player1Score, self.player1ScoreRect)
        self.display.blit(self.player2Score, self.player2ScoreRect)
        for tile in self.gameBoard: # todo test and see if i can replace loop with spritegroup.draw()
            self.display.blit(tile.image, tile.imageRect)
        update()
        

    def check_column_match(self):
        global PLAYER1_SCORE
        global PLAYER2_SCORE
        for x in range(self.columns):
            column = [y.imageIndex for y in self.gameBoard if y.columnNumber == x]
            if column[0] == column[1] and column[1] == column[2] and column[0] != EMPTY_TILE:
                if column[0] == CROSS_TILE:
                    PLAYER1_SCORE += 1
                else:
                    PLAYER2_SCORE += 1
                return True       
        return False
    
    def check_row_match(self):
        global PLAYER1_SCORE
        global PLAYER2_SCORE
        for x in range(self.rows):
            row = [y.imageIndex for y in self.gameBoard if y.rowNumber == x]
            if row[0] == row[1] and row[1] == row[2] and row[0] != EMPTY_TILE:
                if row[0] == CROSS_TILE:
                    PLAYER1_SCORE += 1
                else:
                    PLAYER2_SCORE += 1
                return True
        return False
    
    def check_diagonal_match(self):
        global PLAYER1_SCORE
        global PLAYER2_SCORE
        diagonal1 = [d1.imageIndex for d1 in self.gameBoard if d1.rowNumber == d1.columnNumber]
        if diagonal1[0] == diagonal1[1] and diagonal1[1] == diagonal1[2] and diagonal1[0] != EMPTY_TILE:
            if diagonal1[0] == CROSS_TILE:
                PLAYER1_SCORE += 1
            else:
                PLAYER2_SCORE += 1
            return True
                
        diagonal2 = [d2.imageIndex for d2 in self.gameBoard if d2.rowNumber + d2.columnNumber == 2]
        if diagonal2[0] == diagonal2[1] and diagonal2[1] == diagonal2[2] and diagonal2[0] != EMPTY_TILE:
            if diagonal2[0] == CROSS_TILE:
                PLAYER1_SCORE += 1
            else:
                PLAYER2_SCORE += 1
            return True
        return False
                
    def check_game_over(self):
        if self.check_column_match() == True:
            self.done = True
        if self.check_row_match() == True:
            self.done = True
        if self.check_diagonal_match() == True:
            self.done = True
        