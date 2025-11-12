from pathlib import Path
class Settings:

    def __init__(self):
        self.name : str = 'White Walker Invasion'
        self.screen_width : int = 1200
        self.screen_height : int = 700
        self.FPS : int = 60
        self.bg_file : Path = Path.cwd() / 'Assets' / 'images' / 'Winterfell_background.png'

        #change variable to dragon_file and change path and other variables.
        # remove comments when done
        self.ship_file : Path = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_width : int = 40
        self.ship_height : int = 70
