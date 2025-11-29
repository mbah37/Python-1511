import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

# Type checking is used to avoid circular imports.
if TYPE_CHECKING:
    from white_walker_army import WhiteWalkerArmy

class Walker(Sprite):
    """A class to represent a single White Walker (enemy).

    Each Walker is a sprite that belongs to a WhiteWalkerArmy. Walkers
    are positioned in a grid and move vertically up and down according
    to the army's direction, with occasional horizontal drops toward
    the left side of the screen.

    Attributes:
        army (WhiteWalkerArmy): The army instance that owns this walker.
        screen (pygame.Surface): The game's display surface.
        boundaries (pygame.Rect): Rect representing the screen boundaries.
        settings (Settings): Game settings for walker speed and sprite size.
        image (pygame.Surface): Loaded and scaled walker sprite image.
        rect (pygame.Rect): Rectangular area representing the walker's position.
        x (float): Horizontal position stored as a float.
        y (float): Vertical position stored as a float for smooth movement.
    """
    
    def __init__(self, army: 'WhiteWalkerArmy', x: float, y: float):
        """Initialize the walker and set its starting position.

        Args:
            army (WhiteWalkerArmy): The White Walker army that this walker belongs to.
            x (float): Initial x-coordinate for the walker.
            y (float): Initial y-coordinate for the walker.
        """
        
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
        """Move the walker vertically based on the army's direction.

        The walker's vertical position (y) is updated using the army's
        `army_direction` and the configured `army_speed`. The rect is then
        updated from the float coordinates.
        """
        
        temp_speed = self.settings.army_speed

        # Update the y-coordinate by adding (speed * direction).
        # Direction is 1 for down, -1 for up.
        self.y += temp_speed * self.army.army_direction
        
        # Update the rectangle's position from the float coordinates.
        self.rect.y = self.y
        # Note: self.x remains constant during vertical movement.
        self.rect.x = self.x

    def check_edges(self):
        """Check if the walker has reached the top or bottom edge.

        This method checks whether the walker's rect has collided with
        the top or bottom of the screen.

        Returns:
            bool: True if the walker is at or beyond the top or bottom edge,
            False otherwise.
        """
        return (self.rect.bottom >= self.boundaries.bottom or self.rect.top <= self.boundaries.top)
        
    def draw_walker(self):
        """Draw the walker sprite to the screen.

        This method blits the walker's image at its current rect on the
        game's display surface.
        """
        self.screen.blit(self.image, self.rect)