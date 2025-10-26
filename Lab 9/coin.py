import random 

class Coin:
    def __init__(self):
        self.__sideup = random.choice(["Heads", "Tails"])
        self.__amount = 20
    
    def toss(self):
        self.__sideup = "Heads" if random.randint(0, 1) == 0 else "Tails"
    
    def get_sideup(self):
        return self.__sideup
    
    def get_amount(self):
        return self.__amount
    
    def set_amount(self, change):
        self.__amount -= change

    
    

    






        

