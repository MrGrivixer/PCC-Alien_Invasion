import sys
import pygame
from settings import Settings
from player import Player

class HelicopterFighter:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Helicopter Fighter")

        self.player = Player(self)

        self.settings.initialize_dynamic_settings()

    def run_game(self):
        while True:
            
            self._check_events()
            self.player.update()
            self._update_screen()

            key = pygame.key.get_pressed()
            self._check_key_pressed(key)
            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

    def _check_key_pressed(self, key):
        """Respond to key presses"""
        #if key[pygame.K_UP]:
        #    self.player.moving_up = True
        #    print("UP")
        #if key[pygame.K_RIGHT]:
        #    self.player.moving_right = True
        #    self.player.orientation = "Right"
        #    print("RIGHT")
        #if key[pygame.K_DOWN]:
        #    self.player.moving_down = True
        #    print("LEFT")
        #if key[pygame.K_LEFT]:
        #    self.player.moving_left = True
        #    self.player.orientation = "Left"
        #    print("DOWN")


    def _check_events(self):
        """Respond to keypresses"""
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to a keydown event"""
        # Movement
        if event.key == pygame.K_UP:
            self.player.moving_up = True
        elif event.key == pygame.K_RIGHT:
            self.player.moving_right = True
            self.player.orientation = "Right"
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = True
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True
            self.player.orientation = "Left"
        
        # Quit
        if event.key == pygame.K_q:
            sys.exit(0)

    def _check_keyup_events(self, event):
        """Respond to a keyup event"""
        # Movement
        if event.key == pygame.K_UP:
            self.player.moving_up = False
        elif event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False

    def _update_screen(self):
        """Update images on the screen"""
        self.screen.fill(self.settings.bg_color)
        self.player.blit_me()

        # Make the most recent screen visible
        pygame.display.flip()

if __name__ == '__main__':
    hf = HelicopterFighter()
    hf.run_game()