import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import WhiteWalkerInvasion

class Dragon:
    
    def __init__(self, game: 'WhiteWalkerInvasion'):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.dragon_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.dragon_width, self.settings.dragon_height))
        
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def draw(self):
        self.screen.blit(self.image, self.rect)