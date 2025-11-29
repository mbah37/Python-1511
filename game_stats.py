# from pathlib import Path
import json

from typing import TYPE_CHECKING
from pathlib import Path # Import Path for type hinting in docstring

if TYPE_CHECKING:
    from alien_invasion import WhiteWalkerInvasion

class GameStats:
    """
    Track statistics for the game, including score, high score, and remaining lives.

    This class also handles loading and saving the all-time high score from
    a JSON file on disk.

    Attributes:
        game (WhiteWalkerInvasion): Reference to the main game instance.
        settings (Settings): Game settings used to configure scoring and lives.
        max_score (int): Highest score achieved during the current session.
        high_score (int): All-time high score loaded from / saved to disk.
        path (Path): Filesystem path of the JSON file used to store scores.
        dragons_left (int): Remaining lives for the current game run.
        score (int): Current score for the ongoing game.
        level (int): Current game level.
    """

    def __init__(self, game: 'WhiteWalkerInvasion'):
        """
        Initialize statistics attributes.

        This sets up references to the game and settings, prepares attributes
        for scores and lives, loads any saved high score, and initializes
        runtime statistics.

        Args:
            game (WhiteWalkerInvasion): The main WhiteWalkerInvasion game instance.
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

        If the file exists and has some content, this method attempts to
        read a JSON object from it and load the 'high_score' value. If the
        file is missing or considered empty, the high score is set to 0
        and a fresh file is created via save_scores().
        """
        # Check if the file exists and has content.
        # NOTE: This uses self.path.stat.__sizeof__() as a crude check;
        # the intention is to not treat an obviously empty file as valid data.
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            # Load the high score, defualting to zero if key is missing.
            self.high_score = scores.get('high_score', 0)
        else:
            # If the file does not exist or is effectively empty,
            # default the high score to 0 and create the file.
            self.high_score = 0
            # Save the file with an initial high_score entry.
            self.save_scores()

    def save_scores(self):
        """Save the current high score to the JSON file.

        This writes a small JSON object containing the `high_score` value
        to the path specified in settings (self.path).
        """
        
        scores = {
            'high_score': self.high_score
        }
        # Dump the dictionary to a formatted JSON string.
        contents = json.dumps(scores, indent=4)
        try:
            # Write the content to the scores file.
            self.path.write_text(contents)
        except FileNotFoundError as e:
            # Fallback error handling if the directory structure is missing.
            print(f"File Not Found: {e}")
    
    def reset_stats(self):
        """Initialize statistics that can change during the game (lives, score, level).

        This is called at the start of a new game (or restart). It pulls the
        starting number of lives from settings, and resets score and level.
        """
        
        # Initialize the number of dragons left (lives).
        self.dragons_left = self.settings.starting_dragon_count
        # Current score for the active playthrough.
        self.score = 0
        # Level starts at 1 for a new game.
        self.level = 1

    def update(self, collisions: dict):
        """
        Update the current score, max score for the session, and all-time high score.

        This method is typically called after collisions between projectiles and
        White Walkers are detected.

        Args:
            collisions (dict): A dictionary returned from something like
                pygame.sprite.groupcollide, mapping destroyed enemies to the
                projectiles that hit them.
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
            collisions (dict): A dictionary of detected collisions.
                Keys are enemy sprites, values are lists of projectiles
                that collided with that enemy.
        """
        # Count the number of walkers destroyed (the keys or values in the collisions dict).
        # NOTE: The loop below assumes that each entry represents at least one walker.
        for Walker in collisions.values():
            # Add points for each destroyed walker.
            # Each collision yields points defined in settings.walker_points.
            self.score += self.settings.walker_points
    
    def _update_max_score(self):
        """Check if the current score is the highest for this session and update max_score.

        If the current score exceeds the previously recorded `max_score`,
        this method updates `max_score` to the new value.
        """
        
        if self.score > self.max_score:
            self.max_score = self.score
    
    def _update_high_score(self):
        """Check if the current score is the all-time high score and update high_score.

        If the current score exceeds the stored `high_score`, this method updates
        the `high_score` attribute. Persisting it to disk is handled elsewhere.
        """
       
        if self.score > self.high_score:
            self.high_score = self.score

    def update_level(self):
        self.level += 1
