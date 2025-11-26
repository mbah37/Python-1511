# from pathlib import Path
import json

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import WhiteWalkerInvasion

class GameStats:
    """Track statistics for the game."""

    def __init__(self, game: 'WhiteWalkerInvasion'):
        """Initialize statistics."""
       
        self.game = game
        self.settings = game.settings
        self.max_score : int = 0 # Initialize the maximum score.
        self.init_saved_scores()
        self.reset_stats() 
    
    def init_saved_scores(self):
        '''Initialize statistics that are saved between games.'''

        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 80:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.high_score = scores.get('high_score', 0)
        else:
            self.high_score = 0
            # save the file
            self.save_scores()

    def save_scores(self):
        scores = {
            'high_score': self.high_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f"File Not Found: {e}")
    
    def reset_stats(self):
        '''Initialize statistics that can change during the game.'''
        
        # Initialize the number of dragons left (lives).
        self.dragons_left = self.settings.starting_dragon_count
        self.score = 0 #Initialize the score.
        self.level = 1 #Initialize the level.

    def update(self, collisions):
        #update score
        self._update_score(collisions) 

        #update max score
        self._update_max_score()
        #update high score
        self._update_high_score

    def _update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score
    
    def _update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score


    def _update_score(self, collisions):
        for Walker in collisions.values():
            self.score += self.settings.walker_points

    def update_level(self):
        self.level += 1
        print(self.level)

