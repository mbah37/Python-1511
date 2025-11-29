import pygame
from white_walker import Walker

from typing import TYPE_CHECKING

# Type checking is used to avoid circular imports.
if TYPE_CHECKING:
    from alien_invasion import WhiteWalkerInvasion

class WhiteWalkerArmy:
    """A class to manage the army of white walkers.

    The WhiteWalkerArmy class is responsible for creating the enemy
    formation, updating their movement, detecting edge collisions,
    handling drops toward the dragon, and checking for collisions with
    projectiles and critical boundaries.

    Attributes:
        game (WhiteWalkerInvasion): Reference to the main game instance.
        settings (Settings): Game settings used for army speed and size.
        army (pygame.sprite.Group): Group containing all active Walker sprites.
        army_direction (int): Vertical direction of movement (1 for down, -1 for up).
        army_drop_speed (float): Amount to move horizontally toward the dragon on a drop.
    """
   
    def __init__(self, game: 'WhiteWalkerInvasion'):
        """Create and initialize a new White Walker army.

        Args:
            game (WhiteWalkerInvasion): The active game instance, providing
                settings, screen, and access to the dragon.
        """
        self.game = game
        self.settings = game.settings
      
       # A Sprite Group to hold all active White Walker sprites.
        self.army = pygame.sprite.Group()
      
       # 1 for down, -1 for up, controls vertical movement.
        self.army_direction = self.settings.army_direction
        self.army_drop_speed = self.settings.army_drop_speed

        self.create_army() 

    def create_army(self):
        """Determine army dimensions, offsets, and create the walkers.

        This method calculates how many walkers fit in the right half of the
        screen (both vertically and horizontally), computes appropriate offsets
        to center the formation vertically and align it on the right side, and
        then creates and positions walker sprites in a grid.
        """
        
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
        """Create and position individual walkers in a grid formation.

        Args:
            walker_height (int): Height of each walker sprite.
            walker_width (int): Width of each walker sprite.
            army_height (int): Number of rows in the formation.
            army_width (int): Number of columns in the formation.
            y_offset (int): Starting y offset to vertically center the army.
            x_offset (int): Starting x offset to place the army on the right side.

        Returns:
            None
        """
        
        for column in range(army_width):
            for row in range(army_height):
                # Calculate the y-coordinate for the current walker
                current_y = walker_height * row + y_offset
                # Calculate the x-coordinate for the current walker
                current_x = walker_width * column + x_offset
                self._create_walker(current_x, current_y)

    def calc_offsets(self, walker_height, screen_height, walker_width, screen_width, army_height, army_width):
        """Calculate offsets to center the army vertically and place it on the right.

        This method computes:
        - The vertical offset required to vertically center the army given
          the number of rows and walker height.
        - The horizontal offset required to align the army on the right side
          of the screen with a small margin.

        Args:
            walker_height (int): Height of each walker sprite.
            screen_height (int): Total screen height.
            walker_width (int): Width of each walker sprite.
            screen_width (int): Total screen width.
            army_height (int): Number of rows in the formation.
            army_width (int): Number of columns in the formation.

        Returns:
            tuple[int, int]: (y_offset, x_offset) for the top-left walker.
        """
        
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
        """Calculate the maximum number of rows and columns that fit on the screen.

        The army is constrained to the right half of the screen horizontally.
        This method computes the maximum rows and columns that fit in that area,
        then adjusts them to be odd numbers (for aesthetic centering).

        Args:
            walker_height (int): Height of each walker sprite.
            screen_height (int): Total screen height.
            walker_width (int): Width of each walker sprite.
            screen_width (int): Total screen width.

        Returns:
            tuple[int, int]: (army_height, army_width) indicating rows and columns.
        """
       
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
        """Create a single Walker instance and add it to the army group.

        Args:
            current_x (int): X-coordinate of the new walker's position.
            current_y (int): Y-coordinate of the new walker's position.

        Returns:
            None
        """
       
        new_walker = Walker(self, current_x, current_y)
        self.army.add(new_walker)
    
    def _check_army_edges(self):
        """Check if any walker has reached a vertical edge and trigger a drop.

        If any walker reaches the top or bottom of the screen, the entire
        army is moved horizontally left (toward the dragon) and the vertical
        direction (`army_direction`) is reversed.

        Returns:
            None
        """
        
        walker: Walker
        for walker in self.army:
            if walker.check_edges():
                #Moving the army toward the dragon.
                self._drop_white_walker_army() 
                
                # Reverse the vertical movement direction (up/down).
                self.army_direction *= -1 
                break # Only need to drop once per direction change.
   
    def _drop_white_walker_army(self):
        """Move every walker horizontally towards the left side of the screen.

        This method decreases each walker's x-coordinate by the configured
        `army_drop_speed`, effectively dropping the army closer to the dragon.

        Returns:
            None
        """
        
        for walker in self.army:
            walker.x -= self.army_drop_speed


    def update_army(self):
        """Update the army's movement and position.

        This method checks whether the army has hit a vertical edge (and needs
        to drop and reverse direction), and then updates the position of each
        walker sprite in the army group.

        Returns:
            None
        """
        
        self._check_army_edges() # Check if vertical movement needs to be reversed and dropped.
        self.army.update() # Call the update method for every walker in the group.

    def draw(self):
        """Draw all walkers to the screen.

        Iterates over each walker in the army group and calls its draw
        method to render it on the game's display surface.
        """
        
        walker: 'Walker'
        for walker in self.army:
            walker.draw_walker()
    
    def check_collisions(self, other_group):
        """Check for collisions between walkers and a given projectile group.

        This method uses `pygame.sprite.groupcollide` to detect collisions
        between the army and another group (typically the dragon's elements).
        Colliding walkers and projectiles are removed from their groups.

        Args:
            other_group (pygame.sprite.Group): Group of projectiles to check
                collisions against.

        Returns:
            dict: A mapping from walker sprites to lists of collided projectiles.
        """
        
        # Checks for collisions:
        # True: remove the walker from the army group upon collision.
        # True: remove the projectile from the "other_group" upon collision.
        return pygame.sprite.groupcollide(self.army, other_group, True, True)
    
    def check_left_edge(self):
        """Check if any walker has moved past the critical left edge.

        This method checks whether any walker in the army has crossed a
        threshold near the left side of the screen, which can trigger a
        life loss or game over.

        Returns:
            bool: True if at least one walker has crossed the left edge threshold,
            False otherwise.
        """
        
        walker: Walker
        for walker in self.army:
            # Check if the white walker has crossed the left edge threshold.
            if walker.rect.left <= -10:
                return True # Indicate that the army has reached the edge
        return False

    def check_destroyed_status(self):
        """Return True if the army group is empty (all walkers destroyed).

        The army is considered destroyed when the sprite group is empty.

        Returns:
            bool: True if no walkers remain, False otherwise.
        """
        
        # An empty sprite group evaluates to False in a boolean context.
        return not self.army