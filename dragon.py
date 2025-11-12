import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import WhiteWalkerInvasion
    from arsenal import Arsenal

class Dragon:
    
    def __init__(self, game: 'WhiteWalkerInvasion', arsenal = 'Arsenal'):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.dragon_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.dragon_width, self.settings.dragon_height))
        
        self.rect = self.image.get_rect()
        self.rect.midleft = self.boundaries.midleft
        # Down is left arrow, up is right arrow
        self.moving_down = False
        self.moving_up = False
        self.y = float(self.rect.y)
        self.arsenal = arsenal
    
    def update(self):
        # Checking the position of the dragon and updating its position
        self._update_dragon_movement()
        self.arsenal.update_arsenal()

    def _update_dragon_movement(self):
        temp_speed = self.settings.dragon_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += temp_speed
        
        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= temp_speed
        
        self.rect.y = self.y

    def draw(self):
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)
    
    def shoot(self):
        return self.arsenal.shoot_element()

class Dragon:
    
    def __init__(self, game: 'WhiteWalkerInvasion'):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        #change variable to dragon for height and width. remove comment when done
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.ship_width, self.settings.ship_height))
        
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def draw(self):
        self.screen.blit(self.image, self.rect)
