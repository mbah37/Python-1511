class Dog:
    """
    A simple class to represent a dog.
    """
    def __init__(self, name, breed):
        """
        Initializes a new Dog object.

        Args:
            name: The dog's name.
            breed: The dog's breed.
        """
        self.__name = name
        self._breed = breed
        self._tricks = []  # Initialize an empty list of tricks

    def get_name(self):
        return self.__name
    
    def add_trick(self, trick):
        """
        Adds a new trick to the dog's list of tricks.

        Args:
            trick: The trick to add.
        """
        self._tricks.append(trick)

    def bark(self):
        """
        Returns a string representing the dog's bark.
        """
        return "Woof!"
  

    