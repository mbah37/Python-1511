import pygame
from white_walker import Walker

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import WhiteWalkerInvasion

class WhiteWalkerArmy:
    def __init__(self, game: 'WhiteWalkerInvasion'):
       self.game = game
       self.settings = game.settings
       self.army = pygame.sprite.Group()
       self.army_direction = self.settings.army_direction
       self.army_drop_speed = self.settings.army_drop_speed

       self.create_army()

    def create_army(self):
        walker_height = self.settings.walker_height
        screen_height = self.settings.screen_height

        army_height = self.calc_army_size(walker_height, screen_height)

        army_vertical_space = army_height * walker_height 
        y_offset = int(screen_height - army_vertical_space) // 2

        current_x = screen_height - walker_height + 475
        for row in range(army_height):
            current_y = walker_height * row + y_offset
            self._create_walker(current_x, current_y)


    def calc_army_size(self, walker_height, screen_height):
        army_height = (screen_height // walker_height)
        

        if army_height % 2 == 0:
            army_height -= 1
        else:
            army_height -= 2

        return army_height

    
    def _create_walker(self, current_x: int, current_y: int):
        new_walker = Walker(self, current_x, current_y)
        self.army.add(new_walker)

    def draw(self):
        walker: 'Walker'
        for walker in self.army:
            walker.draw_walker()





