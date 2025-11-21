from pathlib import Path


class Settings:
    """A class to store all settings for White Walker Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        
        # --- Screen Settings ---
        self.name : str = 'White Walker Invasion' # Window title.
        self.screen_width : int = 1200 # Width of the game window 
        self.screen_height : int = 700 # Height of the game window
        self.FPS : int = 60 # Target frame rate.
        
        # Construct the file path for the background image.
        self.bg_file : Path = Path.cwd() / 'Assets' / 'images' / 'Winterfell1.png'

        # --- Dragon (Player) Settings ---
        
        # Construct the file path for the dragon image.
        self.dragon_file : Path = Path.cwd() / 'Assets' / 'images' / 'Drogon.png'
        
        self.dragon_width : int = 100 # Width of the dragon
        self.dragon_height : int = 100 # Height of the dragon
        self.dragon_speed : int = 5 # Speed of the dragon
        self.starting_dragon_count : int = 3 # Number of lives the dragon has

        # --- Element (Projectile) Settings ---
        
        # Construct the file path for the element image.
        self.element_file : Path = Path.cwd() / 'Assets' / 'images' / 'fire1.png'
        
        # Construct the file path for the shooting sound.
        self.element_sound : Path = Path.cwd() / 'Assets' / 'sound' / 'roar.wav'
        
        # Construct the file path for the impact/death sound.
        self.impact_sound : Path = Path.cwd() / 'Assets' / 'sound' / 'WWdies.wav'

        self.element_width : int = 70 # Width of the element 
        self.element_height : int = 80 # Height of the element 
        self.element_speed : int = 7 # Speed of the element
        self.element_amount : int = 5 # Maximum number of elements allowed on screen at once.
       
        # --- White Walker (Enemy) Settings ---
        
        # Construct the file path for the enemy image.
        self.walker_file : Path = Path.cwd() / 'Assets' / 'images' / 'WWenemy.png'
        
        self.walker_width : int = 100 # Width of a white walker 
        self.walker_height : int = 70 # Height of a white walker
        self.army_speed : float = 1.0 # speed of the army.
        self.army_direction : int = 1 # 1 means initial movement is Down, -1 is Up.
        # How many pixels the army drops down when changing direction.
        self.army_drop_speed : int = 50 