import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import WhiteWalkerInvasion

class Button:
    """A simple clickable button displayed on the game screen.

    This class is responsible for creating a rectangular button surface
    centered on the screen, rendering a text label on it, drawing it,
    and checking whether the button has been clicked.

    Attributes:
        game (WhiteWalkerInvasion): Reference to the active game instance.
        screen (pygame.Surface): Surface on which the button is drawn.
        boundaries (pygame.Rect): Rect representing the screen boundaries.
        settings (Settings): Game settings used for button size and colors.
        font (pygame.font.Font): Font used to render the button text.
        rect (pygame.Rect): Rectangular area representing the button.
        msg_image (pygame.Surface): Rendered image of the button text.
        msg_image_rect (pygame.Rect): Rect that positions the text on the button.
    """

    def __init__(self, game: 'WhiteWalkerInvasion', msg):
        """Initialize button attributes.

        Args:
            game (WhiteWalkerInvasion): The active game instance.
            msg (str): The text message to display on the button.
        """
        
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
        """Turn the button message into a rendered image and center it.

        This method renders the text (msg) using the button's font and
        positions it so that it is centered within the button rectangle.

        Args:
            msg (str): The text message to render on the button.

        Returns:
            None
        """
        
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """Draw the button and its message to the screen.

        First, the button rectangle area is filled with the configured
        button color, then the rendered text image is blitted onto it.
        """
        
        # Draw the button rectangle.
        self.screen.fill(self.settings.button_color, self.rect)
        
        # Draw the message image on the button.
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_click(self, mouse_position):
        """Return True if the button is clicked to play the game.

        This method checks whether the given mouse coordinates lie within
        the button's rectangle. 

        Args:
            mouse_position (tuple[int, int]): The (x, y) coordinates of the mouse.

        Returns:
            bool: True if the mouse position is inside the button rect, False otherwise.
        """
        
        return self.rect.collidepoint(mouse_position)