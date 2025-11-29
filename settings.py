from pathlib import Path

class Settings:
    """
    A class to store all settings for White Walker Invasion.

    Manages screen dimensions, game resources, difficulty scaling,
    and game element properties (Dragon, Elements, White Walkers).
    """

    def __init__(self):
        """Initialize the game's static settings."""
        
        # --- Screen Settings ---
        self.name: str = 'White Walker Invasion' # Window title.
        self.screen_width: int = 1200 # Width of the game window.
        self.screen_height: int = 700 # Height of the game window.
        self.FPS: int = 60 # Target frame rate for the game loop.
        
        # Construct the file path for the background image.
        self.bg_file: Path = Path.cwd() / 'Assets' / 'images' / 'Winterfell1.png'

        # Multiplier for increasing difficulty (speed and score) after a level is cleared.
        self.difficulty_scale: float = 1.1 
        # Path to the file for saving high scores.
        self.scores_file: Path = Path.cwd() / 'Assets' / 'file' / 'scores.json'

        # --- Dragon (Player) Settings ---
        
        # Construct the file path for the dragon image.
        self.dragon_file: Path = Path.cwd() / 'Assets' / 'images' / 'Drogon.png'
        
        self.dragon_width: int = 100 # Width of the dragon.
        self.dragon_height: int = 100 # Height of the dragon.
        
        # --- Element (Projectile) Settings ---
        
        # Construct the file path for the element (projectile) image.
        self.element_file: Path = Path.cwd() / 'Assets' / 'images' / 'fire1.png'
        
        # --- White Walker (Enemy) Settings ---

        # Construct the file path for the white walker image.
        self.walker_file: Path = Path.cwd() / 'Assets' / 'images' / 'WWenemy.png'
        
        self.walker_width: int = 100 # Width of a single white walker.
        self.walker_height: int = 100 # Height of a single white walker.
        
        # Number of rows in the initial army formation.
        self.army_rows : int = 3 
        # Number of columns in the initial army formation.
        self.army_cols : int = 6 
        # Initial direction of vertical movement for the army (1 for down).
        self.army_direction : int = 1 
        
        # --- HUD and Button Settings ---

        # Dimensions of the play button.
        self.button_width : int = 200 
        self.button_height : int = 50 
        
        # Color settings.
        self.button_color : tuple = (0, 0, 0) # Color of the play button (RGB).
        self.text_color : tuple = (255, 255, 255) # Color of the text (RGB).
        
        # Font settings.
        self.button_font_size : int = 48 # Font size for the button text.
        self.HUD_font_size : int = 20 # Font size for the HUD text.
        
        # Path to the font file.
        self.font_file : Path = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'TrajanPro-Regular.ttf'

        # --- Sound Settings (Assumed file paths) ---
        self.element_sound: Path = Path.cwd() / 'Assets' / 'Sounds' / 'roar.wav' 
        self.impact_sound: Path = Path.cwd() / 'Assets' / 'Sounds' / 'WWdies.wav' 

    def initialize_dynamic_settings(self):
        """
        Initialize settings that change throughout the game, 
        such as speed and starting lives.
        These are reset when a new game starts.
        """
       
        self.dragon_speed : float = 5.0 # Speed of the dragon.
        self.starting_dragon_count : int = 3 # Number of lives the dragon has.

        self.element_speed : float = 7.0 # Speed of the element (projectile).
        
        # Maximum number of elements allowed on screen at once.
        self.element_amount : int = 5 
        self.element_width : int = 70 # Width of the element. 
        self.element_height : int = 80 # Height of the element.   
        
        self.army_speed : float = 1.0 # Base vertical speed of the white walker army.
        
        # How many pixels the army drops down when changing vertical direction.
        self.army_drop_speed : int = 50 
        self.walker_points : int = 50 # Points awarded for defeating a white walker.

    
    def increase_speed(self):
        """
        Increase the speed of game elements and the point value of walkers 
        to increase game difficulty.
        """
        # Increase speed settings by the difficulty scale multiplier.
        self.dragon_speed *= self.difficulty_scale
        self.element_speed *= self.difficulty_scale
        self.army_speed *= self.difficulty_scale

        # Round point value to the nearest integer.
        self.walker_points = int(self.walker_points * self.difficulty_scale)