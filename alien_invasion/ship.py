import pygame
"""A class to manage the ship"""

class Ship:
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load a ship image and get its rect.
        self.image = pygame.image.load("alien_invasion/images/ship.bmp")
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        #Movement flags : start with a ship that isn't moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ships position based on the movement flag"""
        if self.moving_right:
            self.rect.x += 2
        if self.moving_left:
            self.rect.x -= 2


    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)    
