import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import WhiteWalkerInvasion

class Button:

    def __init__(self, game: 'WhiteWalkerInvasion', msg):
        """Initialize button attributes."""
        
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings

        self.font = pygame.font.Font(self.settings.font_file, 
                                     self.settings.button_font_size)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.settings.button_width,
                                 self.settings.button_height)
        self.rect.center = self.boundaries.center

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

        
    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """Draw blank button and then draw message."""
        
        # Draw the button rectangle.
        self.screen.fill(self.settings.button_color, self.rect)
        
        # Draw the message image on the button.
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_click(self, mouse_position):
        """Return True if the button is clicked to play the game."""
        
        return self.rect.collidepoint(mouse_position)