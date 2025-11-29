"""Projectile management for the dragon's attacks.

This module defines the DragonArsenal class, which maintains a pygame sprite
group of Element instances, updates their positions, removes offscreen
projectiles, and provides the interface used by the dragon to shoot.
"""

from element import Element
import pygame

from typing import TYPE_CHECKING

# Type checking is used to avoid circular imports.
if TYPE_CHECKING:
    from alien_invasion import WhiteWalkerInvasion

class DragonArsenal:
    """A class to manage the dragon's projectiles.

    This class maintains a group of active Element sprites fired by the
    dragon. It is responsible for updating their positions, removing
    projectiles that leave the visible area, drawing them on the screen,
    and enforcing a limit on the number of simultaneous projectiles.
    
    Attributes:
        game (WhiteWalkerInvasion): Reference to the main game instance.
        settings (Settings): Game settings used for projectile configuration.
        arsenal (pygame.sprite.Group): Group containing all active element sprites.
    """
    
    def __init__(self, game: 'WhiteWalkerInvasion'):
        """Initialize the arsenal attributes.

        Args:
            game (WhiteWalkerInvasion): The active game instance that owns this arsenal.
        """
        
        self.game = game
        self.settings = game.settings
        # A Sprite Group to hold all active Element projectiles.
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """Update the position of elements and remove any that are offscreen.

        This method calls the `update()` method on each Element sprite in the
        group to move them across the screen, then removes any projectiles
        that have traveled beyond the right edge of the screen.
        """
       
        # Calls the update() method for every sprite in the group.
        self.arsenal.update() 
        # Clean up elements that have left the screen.
        self._remove_elements_offscreen() 

    def _remove_elements_offscreen(self):
        """Remove elements that have traveled off the right edge of the screen.

        Iterates over a copy of the arsenal group and removes any Element
        whose rect exceeds the screen's right boundary.
        """
        
        # Iterate over a copy to allow safe removal from the original group.
        for element in self.arsenal.copy():
            # Check if the element's right edge is past the screen's right edge.
            if element.rect.right >= self.game.screen.get_rect().right:
                self.arsenal.remove(element)

    def draw(self):
        """Draw all elements to the screen.

        This method calls `draw_element()` on each Element in the arsenal
        group so they are rendered onto the game's display surface.
        """
        
        for element in self.arsenal: 
            element.draw_element()

    def shoot_element(self):
        """Create a new element and add it to the arsenal if the limit allows.

        This method checks the current number of active projectiles against
        the configured maximum (`settings.element_amount`). If the limit has
        not been reached, it creates a new Element, adds it to the arsenal
        group, and returns True. Otherwise, it does nothing and returns False.

        Returns:
            bool: True if a new projectile was created and added, False otherwise.
        """
        
        # Check if the current number of elements is less than the allowed maximum.
        if len(self.arsenal) < self.settings.element_amount:
            
            new_element = Element(self.game) # Create a new projectile instance.
            self.arsenal.add(new_element) # Add the new element to the Sprite Group.
            
            return True # Indicate that a shot was successfully fired.
        
        return False # Indicate that no shot was fired (rate limit hit).