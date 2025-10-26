#Moustapha Bah
#Coin class used for Coin Matching Game
#10/25/2025

import random 

class Coin:
    def __init__(self):
        self.__sideup = random.choice(["Heads", "Tails"])
        self.__amount = 20
    
    def toss(self):
        # Sets the side up of the coin to heads or tails randomly
        self.__sideup = "Heads" if random.randint(0, 1) == 0 else "Tails"
    
    def get_sideup(self):
        # Returns the current side up of the coin
        return self.__sideup
    
    def get_amount(self):
       # Returns the current amount of coins the player has
        return self.__amount
    
    def set_amount(self, change):
        # Updates the amount of coins the player has
        self.__amount += change

    
    

    






        

