import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

# Type checking is used to avoid circular imports.
if TYPE_CHECKING:
    from alien_invasion import WhiteWalkerInvasion

class Element(Sprite):
    """A class to manage the elements fired by the dragon.

    Elements are projectiles that originate from the dragon's mouth and
    travel horizontally across the screen. This class handles loading the
    projectile sprite, positioning it at the dragon, updating its movement,
    and drawing it to the screen.

    Attributes:
        screen (pygame.Surface): The game's display surface.
        settings (Settings): Game settings used for element speed and size.
        image (pygame.Surface): Loaded and scaled element sprite image.
        rect (pygame.Rect): Rectangular area representing the element's position.
        x (float): Horizontal position stored as a float for smooth movement.
    """
    
    def __init__(self, game: 'WhiteWalkerInvasion'):
        """Initialize the element attributes.

        Args:
            game (WhiteWalkerInvasion): The active game instance, providing
                access to screen, settings, and the dragon's position.
        """
       
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
        """Move the element across the screen horizontally.

        The element's x-coordinate is incremented by the configured element
        speed each frame, and the rect is updated to match the new float value.
        """
        
        self.x += self.settings.element_speed # Increase x-coordinate by the speed.
        self.rect.x = self.x # Update the rectangle's position.

    def draw_element(self):
        """Draw the element sprite to the screen.

        This method blits the element's image at its current rect on the
        game's display surface.
        """
        self.screen.blit(self.image, self.rect)
