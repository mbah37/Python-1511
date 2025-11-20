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
        walker_width = self.settings.walker_width
        screen_width = self.settings.screen_width

        army_height, army_width = self.calc_army_size(walker_height, screen_height, walker_width, screen_width)
        
        y_offset, x_offset = self.calc_offsets(walker_height, screen_height, walker_width, screen_width, army_height, army_width)
        
        self._army_formation(walker_height, walker_width, army_height, army_width, y_offset, x_offset)

    def _army_formation(self, walker_height, walker_width, army_height, army_width, y_offset, x_offset):
        for column in range(army_width):
            for row in range(army_height):
                current_y = walker_height * row + y_offset
                current_x = walker_width * column + x_offset
                self._create_walker(current_x, current_y)

    def calc_offsets(self, walker_height, screen_height, walker_width, screen_width, army_height, army_width):
        army_vertical_space = army_height * walker_height 
        army_horizonal_space = army_width * walker_width
        y_offset = int(screen_height - army_vertical_space) // 2
        x_offset = screen_width - army_horizonal_space - 10
        return y_offset, x_offset


    def calc_army_size(self, walker_height, screen_height, walker_width, screen_width):
        army_height = (screen_height // walker_height)
        army_width = ((screen_width/2) // walker_width)
        

        if army_height % 2 == 0:
            army_height -= 1
        else:
            army_height -= 2
        
        if army_width % 2 == 0:
            army_width -= 1
        else:
            army_width -= 2

        return int(army_height), int(army_width)

    
    def _create_walker(self, current_x: int, current_y: int):
        new_walker = Walker(self, current_x, current_y)
        self.army.add(new_walker)
    
    def _check_army_edges(self):
        walker: Walker
        for walker in self.army:
            if walker.check_edges():
                self._drop_white_walker_army()
                self.army_direction *= -1
                break
   
    def _drop_white_walker_army(self):
        for walker in self.army:
            walker.x -= self.army_drop_speed


    def update_army(self):
        self._check_army_edges()
        self.army.update()

    def draw(self):
        walker: 'Walker'
        for walker in self.army:
            walker.draw_walker()
    
    def check_collisions(self, other_group):
        return pygame.sprite.groupcollide(self.army, other_group, True, True)
    
    def check_left_edge(self):
        walker: Walker
        for walker in self.army:
            if walker.rect.left <= -10:
                return True
        return False

    def check_destroyed_status(self):
        return not self.army




