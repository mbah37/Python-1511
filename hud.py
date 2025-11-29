import pygame.font

# from typing import TYPE_CHECKING

# # Type checking is used to avoid circular imports.
# if TYPE_CHECKING:
#     from alien_invasion import WhiteWalkerInvasion

class HUD:
    """HUD (Heads-Up Display) for in-game information.

    This class renders and positions:
    - current score
    - maximum score for the current session
    - all-time high score
    - current level
    - remaining lives (as dragon icons)

    Attributes:
        game: Reference to the main game instance.
        settings: Game settings used for fonts, colors, and image paths.
        screen (pygame.Surface): The game's display surface.
        boundaries (pygame.Rect): The screen boundaries for alignment.
        game_stats (GameStats): Live game statistics (score, level, lives).
        font (pygame.font.Font): Font used for all HUD text.
        padding (int): Margin in pixels used for spacing HUD elements.
        life_image (pygame.Surface): Icon used to represent a remaining life.
        life_rect (pygame.Rect): Rect used to determine life icon size.
        score_image, max_score_image, high_score_image, level_image (pygame.Surface):
            Rendered text surfaces for different HUD elements.
        score_rect, max_score_rect, high_score_rect, level_rect (pygame.Rect):
            Rectangles defining positions of the respective text surfaces.
    """

    def __init__(self, game):
        """Initialize HUD attributes and prepare initial text/images.

        Args:
            game: The active game instance that owns this HUD.
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.game_stats = game.game_stats

        # Use the custom font and configured size from settings.
        self.font = pygame.font.Font(self.settings.font_file, 
                                     self.settings.HUD_font_size)
        # Padding used for margins from screen edges and between HUD lines.
        self.padding = 20

        # Prepare the initial score, max score, and high score images.
        self.update_scores()
        # Prepare the small life icon image used to draw remaining lives.
        self._setup_life_image()
        # Prepare the initial level text.
        self.update_level()


    def _setup_life_image(self):
        """Load and scale the dragon image used to represent a life icon.

        This uses the same dragon image as the player's sprite, scaled to
        the same configured width and height for consistency.
        """
        self.life_image = pygame.image.load(self.settings.dragon_file)
        self.life_image = pygame.transform.scale(self.life_image, (
            self.settings.dragon_width, self.settings.dragon_height))
        self.life_rect = self.life_image.get_rect()

    def update_scores(self):
        """Update all score-related text surfaces.

        This method regenerates the rendered text for:
        - current score
        - max score (session)
        - high score (all-time)

        It should be called whenever the underlying stats change.
        """
        
        self._update_score()
        self._update_max_score()
        self._update_high_score()

    def _update_score(self):
        """Render the current score text and position it on the bottom right."""
        
        score_str = f"Score: {self.game_stats.score: ,.0f}"
        self.score_image = self.font.render(score_str, True,
                                            self.settings.text_color, None)
        self.score_rect = self.score_image.get_rect()
        # --- Position at bottom right ---
        self.score_rect.right = self.boundaries.right - self.padding
        self.score_rect.bottom = self.boundaries.bottom - self.padding
    
    def _update_max_score(self):
        """Render the maximum score for this session and position it above score."""
        
        max_score_str = f"Max-Score: {self.game_stats.max_score: ,.0f}"
        self.max_score_image = self.font.render(max_score_str, True,
                                            self.settings.text_color, None)
        
        self.max_score_rect = self.max_score_image.get_rect()
        # --- Position right above 'score' on the bottom right ---
        self.max_score_rect.right = self.boundaries.right - self.padding
        self.max_score_rect.bottom = self.score_rect.top - self.padding 
        
    def _update_high_score(self):
        """Render the all-time high score and position it at the bottom center."""
        
        high_score_str = f"High-Score: {self.game_stats.high_score: ,.0f}"
        self.high_score_image = self.font.render(high_score_str, True,
                                            self.settings.text_color, None)
        self.high_score_rect = self.high_score_image.get_rect()
        # --- Position at bottom center ---
        self.high_score_rect.midbottom = (self.boundaries.centerx, 
                                          self.boundaries.bottom - self.padding)

    def update_level(self):
        """Render the current level text and position it on the bottom left."""
        
        level_str = f"Level: {self.game_stats.level: ,.0f}"
        self.level_image = self.font.render(level_str, True,
                                            self.settings.text_color, None)
        self.level_rect = self.level_image.get_rect()
        # --- Position at bottom left ---
        self.level_rect.left = self.padding
        self.level_rect.bottom = self.boundaries.bottom - self.padding

    def _draw_lives(self):
        """Draw a row of life icons representing remaining lives.

        Each remaining life is represented by a dragon icon. Icons are drawn
        starting from the top-left corner and laid out horizontally.
        """
        
        current_x = self.padding
        current_y = self.padding
        # Draw one icon for each remaining dragon (life).
        for _ in range(self.game_stats.dragons_left):
            self.screen.blit(self.life_image, (current_x, current_y))
            # Move to the right for the next life icon, with some overlap/padding.
            current_x += self.life_rect.width - self.padding

    def draw(self):
        """Draw all HUD elements onto the screen.

        This method blits:
        - high score text
        - max score text
        - current score text
        - level text
        - remaining lives icons
        """
        
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self._draw_lives()
