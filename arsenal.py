from element import Element
import pygame

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import WhiteWalkerInvasion

class DragonArsenal:
    def __init__(self, game: 'WhiteWalkerInvasion'):
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        self.arsenal.update()
        self._remove_elements_offscreen()

    def _remove_elements_offscreen(self):
        for element in self.arsenal.copy():
            if element.rect.right >= self.game.screen.get_rect().right:
                self.arsenal.remove(element)


    def draw(self):
        for element in self.arsenal: 
            element.draw_element()

    def shoot_element(self):
        if len(self.arsenal) < self.settings.element_amount:
            new_element = Element(self.game)
            self.arsenal.add(new_element)
            return True
        return False
