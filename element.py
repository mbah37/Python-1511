import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

# Type checking is used to avoid circular imports.
if TYPE_CHECKING:
    from alien_invasion import WhiteWalkerInvasion

class Element(Sprite):
    """A class to manage the elements fired by the dragon."""
    
    def __init__(self, game: 'WhiteWalkerInvasion'):
        """Initialize the element attributes."""
       
        super().__init__() # Initialize the Sprite parent class.
        self.screen = game.screen
        self.settings = game.settings

        # Load and scale the element image.
        self.image = pygame.image.load(self.settings.element_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.element_width, self.settings.element_height))
        
        self.rect = self.image.get_rect() # Get the rectangular area of the image.
        
        # Position the element to launch from the dragon's middle-right side.(his mouth)
        self.rect.midright = game.dragon.rect.midright

        # Store the element's x-coordinate as a float for smooth movement.
        self.x = float(self.rect.x)

    def update(self):
        """Move the element across the screen (horizontally)."""
        
        self.x += self.settings.element_speed # Increase x-coordinate by the speed.
        self.rect.x = self.x # Update the rectangle's position.

    def draw_element(self):
        """Draw the element to the screen."""
        self.screen.blit(self.image, self.rect)