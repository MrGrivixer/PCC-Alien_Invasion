import sys
import pygame as pg
from settings import Settings

class Game:

    def __init__(self):
        pg.init()
        self.settings = Settings()

        self.screen = pg.display.set_mode((1280, 720))
        pg.display.set_caption("Test Game")

    def run_game(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            self._update_screen()

    def _update_screen(self):
        """Update images on the screen"""
        self.screen.fill(self.settings.bg_color)

        pg.display.flip()

if __name__ == '__main__':
    game = Game()
    game.run_game()