import pygame
from typing import TYPE_CHECKING

# Type checking is used to avoid circular imports.
if TYPE_CHECKING:
    from alien_invasion import WhiteWalkerInvasion
    from arsenal import DragonArsenal
    
class Dragon:
    """A class to manage the dragon (player character).

    The Dragon class manages the player sprite, including loading and drawing
    the image, updating its position based on movement flags, enforcing screen
    boundaries, and delegating projectile firing to the associated arsenal.

    Attributes:
        game (WhiteWalkerInvasion): Reference to the main game instance.
        settings (Settings): Game settings for movement speed and sprite size.
        screen (pygame.Surface): The game's display surface.
        boundaries (pygame.Rect): Rect representing the screen area.
        image (pygame.Surface): Loaded and scaled dragon sprite image.
        rect (pygame.Rect): Rectangular area representing the dragon's position.
        y (float): Vertical position stored as a float for smooth movement.
        moving_down (bool): Whether the dragon is moving downward.
        moving_up (bool): Whether the dragon is moving upward.
        arsenal (DragonArsenal): Manages the dragon's fired projectiles.
    """
    
    def __init__(self, game: 'WhiteWalkerInvasion', arsenal: 'DragonArsenal'):
        """Initialize the dragon and set its starting position.

        Args:
            game (WhiteWalkerInvasion): The active game instance.
            arsenal (DragonArsenal): Projectile manager associated with the dragon.
        """
        
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        # Get the rectangle representing the screen area.
        self.boundaries = self.screen.get_rect() 

        # Load the dragon image and scale it to the specified size.
        self.image = pygame.image.load(self.settings.dragon_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.dragon_width, self.settings.dragon_height))
        
        self.rect = self.image.get_rect() # Get the rectangular area of the image.
        self._center_dragon() # Set the initial position.
        
        # Movement flags. True when the corresponding key is held down.
        # Down is left arrow, up is right arrow
        self.moving_down = False
        self.moving_up = False
        self.arsenal = arsenal # A reference to the DragonArsenal instance.

    def _center_dragon(self):
        """Position the dragon at the vertical center on the left edge of the screen.

        This method sets the dragon's rect so that its mid-left point is aligned
        with the screen's mid-left, and stores the y-coordinate as a float to
        allow for smooth movement updates.
        """
        
        self.rect.midleft = self.boundaries.midleft
        # Store the dragon's y-coordinate as a float for precise movement calculations.
        self.y = float(self.rect.y)
    
    def update(self):
        """Update the dragon's position and its arsenal.

        This method:
        - Updates the dragon's vertical position based on movement flags.
        - Updates all active projectiles in the dragon's arsenal.
        """
        
        self._update_dragon_movement() # Calculate new position based on flags.
        self.arsenal.update_arsenal() # Update the position of all fired projectiles.

    def _update_dragon_movement(self):
        """Update the dragon's vertical position based on movement flags.

        This method adjusts the dragon's y value according to whether the
        `moving_up` or `moving_down` flags are set, while ensuring that the
        dragon does not move beyond the top or bottom boundaries of the screen.
        The rect's y coordinate is then updated from the float y value.
        """
        
        temp_speed = self.settings.dragon_speed
        
        # Check for downward movement and ensure the dragon is not moving past the bottom edge.
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += temp_speed
        
        # Check for upward movement and ensure the dragon is not moving past the top edge.
        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= temp_speed
        
        # Update the dragon's rectangle position from the floating-point y value.
        self.rect.y = self.y

    def draw(self):
        """Draw the dragon and its projectiles to the screen.

        This method draws all active projectiles first (via the arsenal),
        then blits the dragon sprite at its current position onto the screen.
        """
        
        self.arsenal.draw() # Draw all active projectiles first.
        # Draw the dragon image at its current rectangle.
        self.screen.blit(self.image, self.rect) 
    
    def shoot(self):
        """Ask the arsenal to fire a projectile.

        Delegates to `self.arsenal.shoot_element()` to create a new Element
        if possible.

        Returns:
            bool: True if a shot was fired, False otherwise.
        """
        
        return self.arsenal.shoot_element() # Returns True if a shot was fired, False otherwise.

    def check_collision(self, other_group):
        """Check for collision with any sprite in the given group.

        This method checks whether the dragon collides with any sprite in the
        provided group (e.g., the White Walker army). If a collision occurs,
        the dragon is re-centered on the left side of the screen.

        Args:
            other_group (pygame.sprite.Group): Group of sprites to test collision against.

        Returns:
            bool: True if a collision occurred, False otherwise.
        """
        
        # pygame.sprite.spritecollideany returns the first sprite in the group that collides.
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_dragon() # If collision occurs, reset the dragon's position.
            return True # Indicates a collision happened.
        return False # No collision.