import pygame
from white_walker import Walker

from typing import TYPE_CHECKING

# Type checking is used to avoid circular imports.
if TYPE_CHECKING:
    from alien_invasion import WhiteWalkerInvasion

class WhiteWalkerArmy:
    """A class to manage the army of white walkers."""
   
    def __init__(self, game: 'WhiteWalkerInvasion'):
       self.game = game
       self.settings = game.settings
      
       # A Sprite Group to hold all active White Walker sprites.
       self.army = pygame.sprite.Group()
      
       # 1 for down, -1 for up, controls vertical movement.
       self.army_direction = self.settings.army_direction
       self.army_drop_speed = self.settings.army_drop_speed

       self.create_army() 

    def create_army(self):
        """Determine army dimensions, offsets, and create the walkers."""
        
        walker_height = self.settings.walker_height
        screen_height = self.settings.screen_height
        walker_width = self.settings.walker_width
        screen_width = self.settings.screen_width

        # Calculate the number of rows (height) and columns (width) that fit.
        army_height, army_width = self.calc_army_size(walker_height, screen_height, walker_width, screen_width)
        
        # Calculate the starting (x, y) coordinates for the top-left walker.
        y_offset, x_offset = self.calc_offsets(walker_height, screen_height, walker_width, screen_width, army_height, army_width)
        
        # Populate the army based on the calculated formation.
        self._army_formation(walker_height, walker_width, army_height, army_width, y_offset, x_offset)

    def _army_formation(self, walker_height, walker_width, army_height, army_width, y_offset, x_offset):
        """Create and position individual walkers in a grid formation."""
        
        for column in range(army_width):
            for row in range(army_height):
                # Calculate the y-coordinate for the current walker
                current_y = walker_height * row + y_offset
                # Calculate the x-coordinate for the current walker
                current_x = walker_width * column + x_offset
                self._create_walker(current_x, current_y)

    def calc_offsets(self, walker_height, screen_height, walker_width, screen_width, army_height, army_width):
        """Calculate the top (y) and right (x) offset to center the army vertically and position it on the right."""
        
        # Total vertical space the army occupies.
        army_vertical_space = army_height * walker_height 
        
        # Total horizontal space the army occupies.
        army_horizonal_space = army_width * walker_width
        
        # Calculate the vertical offset to center the army (remaining height / 2).
        y_offset = int(screen_height - army_vertical_space) // 2
        
        # Calculate the horizontal offset to position the army on the right side
        x_offset = screen_width - army_horizonal_space - 10
        
        return y_offset, x_offset


    def calc_army_size(self, walker_height, screen_height, walker_width, screen_width):
        """Calculate the maximum number of rows and columns that fit on the screen."""
       
        # Maximum possible rows (height).
        army_height = (screen_height // walker_height)
        
        # Maximum possible columns (width) in the right half of the screen.
        army_width = ((screen_width/2) // walker_width)
        

        # Ensure army_height is an odd number (by subtracting 1 or 2) for aesthetic centering.
        if army_height % 2 == 0:
            army_height -= 1
        else:
            army_height -= 2
        
        # Ensure army_width is an odd number (by subtracting 1 or 2).
        if army_width % 2 == 0:
            army_width -= 1
        else:
            army_width -= 2

        return int(army_height), int(army_width)

    
    def _create_walker(self, current_x: int, current_y: int):
        """Create a single Walker instance and add it to the army group."""
       
        new_walker = Walker(self, current_x, current_y)
        self.army.add(new_walker)
    
    def _check_army_edges(self):
        """Check if any walker has reached the top or bottom screen edge and trigger a drop."""
        
        walker: Walker
        for walker in self.army:
            if walker.check_edges():
                #Moving the army toward the dragon.
                self._drop_white_walker_army() 
                
                # Reverse the vertical movement direction (up/down).
                self.army_direction *= -1 
                break # Only need to drop once per direction change.
   
    def _drop_white_walker_army(self):
        """Move every walker horizontally towards the left side of the screen."""
        
        for walker in self.army:
            walker.x -= self.army_drop_speed


    def update_army(self):
        """Update the army's movement and position."""
        
        self._check_army_edges() # Check if vertical movement needs to be reversed and dropped.
        self.army.update() # Call the update method for every walker in the group.

    def draw(self):
        """Draw all walkers to the screen."""
        
        walker: 'Walker'
        for walker in self.army:
            walker.draw_walker()
    
    def check_collisions(self, other_group):
        """Check for collisions between walkers and a given group (elements)."""
        
        # Checks for collisions:
        # True: remove the walker from the army group upon collision.
        # True: remove the projectile from the "other_group" upon collision.
        return pygame.sprite.groupcollide(self.army, other_group, True, True)
    
    def check_left_edge(self):
        """Check if any walker has moved past the critical point on the left edge."""
        
        walker: Walker
        for walker in self.army:
            # Check if the white walker has crossed the left edge threshold.
            if walker.rect.left <= -10:
                return True # Indicate that the army has reached the edge
        return False

    def check_destroyed_status(self):
        """Return True if the army group is empty (all walkers destroyed)."""
        
        # An empty sprite group evaluates to False in a boolean context.
        return not self.army