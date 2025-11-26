
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
        self.reset_stats() 

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

    def _update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score

    def _update_score(self, collisions):
        for Walker in collisions.values():
            self.score += self.settings.walker_points

    def update_level(self):
        self.level += 1
        print(self.level)
        
