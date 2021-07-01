import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to manage the ship."""
    def __init__(self, ai_game):
        """Init the ship and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and get its rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # self.rect.midbottom = self.screen_rect.midbottom

        # Start each new alien at the left top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        