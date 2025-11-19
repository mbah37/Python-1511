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

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        temp_speed = self.settings.army_speed

        if self.check_edges():
            self.settings.army_direction *= -1
            self.x -= self.settings.army_drop_speed

        self.y += temp_speed * self.settings.army_direction
        self.rect.y = self.y
        self.rect.x = self.x

    def check_edges(self):
        return (self.rect.bottom >= self.boundaries.bottom or self.rect.top <= self.boundaries.top)
        

    def draw_walker(self):
        self.screen.blit(self.image, self.rect)