# from pathlib import Path
import json

from typing import TYPE_CHECKING
from pathlib import Path # Import Path for type hinting in docstring

if TYPE_CHECKING:
    from alien_invasion import WhiteWalkerInvasion

class GameStats:
    """
    Track statistics for the game, including score, high score, and remaining lives.
    Handles loading and saving of the high score.
    """

    def __init__(self, game: 'WhiteWalkerInvasion'):
        """
        Initialize statistics attributes.

        Args:
            game: The main WhiteWalkerInvasion game instance.
        """
       
        self.game = game
        self.settings = game.settings
        self.max_score: int = 0 # Initialize the maximum score reached in the current game session.
        self.high_score: int = 0 # Initialize the all-time high score.
        self.path: Path = self.settings.scores_file # File path for high scores.

        self.init_saved_scores() # Load the high score from file.
        self.reset_stats() # Initialize in-game statistics (lives, current score, level).
    
    def init_saved_scores(self):
        """
        Load the all-time high score from a JSON file. 
        If the file is missing or empty, the high score is set to 0 and the file is created.
        """
        # Check if the file exists and has content
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            # Load the high score, defualting to zero if key is missing
            self.high_score = scores.get('high_score', 0)
        else:
            self.high_score = 0
            # save the file
            self.save_scores()

    def save_scores(self):
        """Save the current high score to the JSON file."""
        
        scores = {
            'high_score': self.high_score
        }
        # Dump the dictionary to a formatted JSON string.
        contents = json.dumps(scores, indent=4)
        try:
            # Write the content to the scores file.
            self.path.write_text(contents)
        except FileNotFoundError as e:
            # Fallback error handling.
            print(f"File Not Found: {e}")
    
    def reset_stats(self):
        """Initialize statistics that can change during the game (lives, score, level)."""
        
        # Initialize the number of dragons left (lives).
        self.dragons_left = self.settings.starting_dragon_count
        self.score = 0 # Initialize the current score for the game.
        self.level = 1 # Initialize the current game level.

    def update(self, collisions: dict):
        """
        Update the current score, max score for the session, and all-time high score.

        Args:
            collisions: A dictionary of detected collisions (e.g., from groupcollide) 
                        indicating which enemies were destroyed.
        """
        # Update the current score based on collisions.
        self._update_score(collisions) 
        # Update the maximum score reached in the current session.
        self._update_max_score()
        # Update the all-time high score.
        self._update_high_score()

    def _update_score(self, collisions: dict):
        """
        Calculate and update the current score based on the number of
        white walkers destroyed in collisions.
        
        Args:
            collisions: A dictionary of detected collisions.
        """
        # Count the number of walkers destroyed (the keys in the collisions dict).
        for Walker in collisions.values():
        # Add points for each destroyed walker.
            self.score += self.settings.walker_points
    
    def _update_max_score(self):
        """Check if the current score is the highest for this session and update max_score."""
        
        if self.score > self.max_score:
            self.max_score = self.score
    
    def _update_high_score(self):
        """Check if the current score is the all-time high score and update high_score."""
       
        if self.score > self.high_score:
            self.high_score = self.score
