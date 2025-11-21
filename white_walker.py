import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

# Type checking is used to avoid circular imports.
if TYPE_CHECKING:
    from white_walker_army import WhiteWalkerArmy

class Walker(Sprite):
    """A class to represent a single White Walker (enemy)."""
    
    def __init__(self, army: 'WhiteWalkerArmy', x: float, y: float):
        
        """Initialize the walker and set its starting position."""
        super().__init__() # Initialize the Sprite parent class.
        self.army = army
        self.screen = army.game.screen
        self.boundaries = army.game.screen.get_rect()
        self.settings = army.game.settings

        # Load and scale the walker image.
        self.image = pygame.image.load(self.settings.walker_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.walker_width, self.settings.walker_height))
        
        self.rect = self.image.get_rect() # Get the rectangular area of the image.
        
        # Set the initial position based on the provided coordinates.
        self.rect.x = x
        self.rect.y = y

        # Store coordinates as floats for smooth movement.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move the walker vertically based on the army's direction."""
        
        temp_speed = self.settings.army_speed

        # Update the y-coordinate by adding (speed * direction).
        # Direction is 1 for down, -1 for up.
        self.y += temp_speed * self.army.army_direction
        
        # Update the rectangle's position from the float coordinates.
        self.rect.y = self.y
        # Note: self.x remains constant during vertical movement.
        self.rect.x = self.x

    def check_edges(self):
        """Return True if the walker has reached the top or bottom edge of the screen."""
        return (self.rect.bottom >= self.boundaries.bottom or self.rect.top <= self.boundaries.top)
        
    def draw_walker(self):
        """Draw the walker to the screen."""
        self.screen.blit(self.image, self.rect)