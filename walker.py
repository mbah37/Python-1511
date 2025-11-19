import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import WhiteWalkerInvasion

class Walker(Sprite):
    def __init__(self, game: 'WhiteWalkerInvasion', x: float, y: float):
        super().__init__()
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.walker_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.walker_width, self.settings.walker_height))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        #self.x = float(self.rect.x)

    def update(self):
        pass

    def draw_walker(self):
        self.screen.blit(self.image, self.rect)