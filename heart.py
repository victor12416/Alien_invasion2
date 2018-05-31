import pygame
from pygame.sprite import Sprite


class Heart(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        super(Heart, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the heart image and get its rect
        self.image = pygame.image.load('images/heart.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
