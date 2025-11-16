import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import WhiteWalkerInvasion

class Element(Sprite):
    def __init__(self, game: 'WhiteWalkerInvasion'):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.element_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.element_width, self.settings.element_height))
        
        self.rect = self.image.get_rect()
        self.rect.midright = game.dragon.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.element_speed
        self.rect.x = self.x

    def draw_element(self):
        self.screen.blit(self.image, self.rect)