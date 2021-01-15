import pygame

class Player():
    """A class to manage the player"""

    def __init__(self, hf_game):
        """Create the player and it's starting position"""
        super().__init__()
        self.screen = hf_game.screen
        self.screen_rect = hf_game.screen.get_rect()
        self.settings = hf_game.settings
        
        # load the player and its rect
        self.image = pygame.image.load("part2_projects\project1_alien_invasion\TRY\HelicopterFighter\images\player.png")
        self.rect = self.image.get_rect()

        # Start a new ship on the left of the screen
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the player's position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_up = False
        self.moving_right = False
        self.moving_down = False
        self.moving_left = False
        self.orientation = "Left"

   
    def update(self):
        """Update the player's position based on movement"""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.player_speed
        elif self.moving_right and self.rect.midright < self.screen_rect.center:
            self.x += self.settings.player_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.player_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.player_speed
        
        self.rect.x = self.x
        self.rect.y = self.y


    def blit_me(self):
        """Draw the player at its current position"""
        #if self.orientation == "Left":
        self.screen.blit(self.image, self.rect)
        #elif self.orientation == "Right":
        #    self.screen.blit(pygame.transform.flip(self.image, True, False), self.rect)
