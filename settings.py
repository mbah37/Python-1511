from pathlib import Path
class Settings:

    def __init__(self):
        self.name : str = 'White Walker Invasion'
        self.screen_width : int = 1200
        self.screen_height : int = 700
        self.FPS : int = 60
        self.bg_file : Path = Path.cwd() / 'Assets' / 'images' / 'Winterfell_background.png'

        self.dragon_file : Path = Path.cwd() / 'Assets' / 'images' / 'Drogon1.png'
        self.dragon_width : int = 100
        self.dragon_height : int = 100
        self.dragon_speed : int = 5
