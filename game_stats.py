#Volatile Game Stats

class GameStats:
    """Track statistics for the game."""

    def __init__(self, dragons_left):
        """Initialize statistics."""
       
        # Initialize the number of lives/dragons the player has remaining.
        self.dragons_left = dragons_left
