from pathlib import Path
class Settings:

    def __init__(self):
        self.name : str = 'White Walker Invasion'
        self.screen_width : int = 1200
        self.screen_height : int = 700
        self.FPS : int = 60
        self.bg_file : Path = Path.cwd() / 'Assets' / 'images' / 'Winterfell1.png'

        self.dragon_file : Path = Path.cwd() / 'Assets' / 'images' / 'Drogon.png'
        self.dragon_width : int = 100
        self.dragon_height : int = 100
        self.dragon_speed : int = 5

        self.element_file : Path = Path.cwd() / 'Assets' / 'images' / 'fire1.png'
        self.element_sound : Path = Path.cwd() / 'Assets' / 'sound' / 'roar.wav'

        self.element_width : int = 70
        self.element_height : int = 80
        self.element_speed : int = 7
        self.element_amount : int = 5
       
        self.walker_file : Path = Path.cwd() / 'Assets' / 'images' / 'WWenemy.png'
        self.walker_width : int = 100
        self.walker_height : int = 70
        self.army_speed : float = 0.8
        self.army_direction : int = 1  
        self.army_drop_speed : int = 50

        

    