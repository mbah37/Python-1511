from element import Element
import pygame

from typing import TYPE_CHECKING

# Type checking is used to avoid circular imports.
if TYPE_CHECKING:
    from alien_invasion import WhiteWalkerInvasion

class DragonArsenal:
    """A class to manage the dragon's projectiles."""
    
    def __init__(self, game: 'WhiteWalkerInvasion'):
        """Initialize the arsenal attributes."""
        
        self.game = game
        self.settings = game.settings
        # A Sprite Group to hold all active Element projectiles.
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """Update the position of elements and get rid of old ones."""
       
        # Calls the update() method for every sprite in the group.
        self.arsenal.update() 
        # Clean up elements that have left the screen.
        self._remove_elements_offscreen() 

    def _remove_elements_offscreen(self):
        """Remove elements that have traveled off the right edge of the screen."""
        
        # Iterate over a copy to allow safe removal from the original group.
        for element in self.arsenal.copy():
            
            # Check if the element's right edge is past the screen's right edge.
            if element.rect.right >= self.game.screen.get_rect().right:
                self.arsenal.remove(element)

    def draw(self):
        """Draw all elements to the screen."""
        
        for element in self.arsenal: 
            element.draw_element()

    def shoot_element(self):
        """Create a new element and add it to the arsenal, if the limit hasn't been reached."""
        
        # Check if the current number of elements is less than the allowed maximum.
        if len(self.arsenal) < self.settings.element_amount:
            
            new_element = Element(self.game) # Create a new projectile instance.
            self.arsenal.add(new_element) # Add the new element to the Sprite Group.
            
            return True # Indicate that a shot was successfully fired.
        
        return False # Indicate that no shot was fired (rate limit hit).