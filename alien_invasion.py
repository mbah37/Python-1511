import sys
import pygame
from settings import Settings
from game_stats import GameStats
from dragon import Dragon
from arsenal import DragonArsenal
from white_walker_army import WhiteWalkerArmy
from time import sleep
from button import Button

class WhiteWalkerInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        
        pygame.init() # Initialize all imported pygame modules.
        
        # Load game settings and initialize game statistics.
        self.settings = Settings()
        self.game_stats = GameStats(self.settings.starting_dragon_count)

        # Set up the main game screen (display surface).
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption(self.settings.name) # Set the window title.

        # Load and scale the background image.
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg,
             (self.settings.screen_width, self.settings.screen_height))

        self.running = True # variable to control the main game loop.
        self.clock = pygame.time.Clock() # Object to manage timing and frame rate.

        # Initialize the mixer for sound effects.
        pygame.mixer.init()
        
        # Load and set volume for the dragon's element sound.
        self.element_sound = pygame.mixer.Sound(self.settings.element_sound)
        self.element_sound.set_volume(0.7)
        
        # Load and set volume for the impact sound (White Walker dies).
        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(0.7)
        
        
        # Create the Dragon instance, passing the game and a new DragonArsenal for its projectiles.
        self.dragon = Dragon(self, DragonArsenal(self))
        
        # Create the WhiteWalkerArmy instance to manage all enemies.
        self.white_walker_army = WhiteWalkerArmy(self)
        
        # the higher you go the y value the lower you are on the screen
        # the higher the x value the more right you are on the screen
        
        # Populate the screen with White Walkers.
        self.white_walker_army.create_army() 
        
        # Create the Play button.
        self.play_button = Button(self, "Play") 
        
        # Flag to indicate if the game is currently running (not paused or game over).
        self.game_active = False 
    
    def run_game(self):
        """Start the main loop for the game."""
        
        while self.running:
            
            # Checking for user input
            self._check_events() 
            if self.game_active:
                self.dragon.update() # Update the dragon's position and arsenal.
                self.white_walker_army.update_army() # Update the White Walker army's position.
                self._check_collisions() # Check for all in-game collisions.
                
            self._update_screen() # Redraw the screen elements.
            self.clock.tick(self.settings.FPS) # Limit the frame rate to the defined FPS.

    def _check_collisions(self):
        """Handle all collision checks and their consequences."""
        
        # Check for collision between the Dragon and any White Walker.
        if self.dragon.check_collision(self.white_walker_army.army):
            # Handle loss of a life/game over.
            # If a collision occurred, the Dragon is reset
            self._check_game_status() 

        # Check if any White Walker has reached the left edge of the screen
        # (game-resetting condition).
        if self.white_walker_army.check_left_edge():
            self._check_game_status()

        # This function handles the destruction of both element and walker upon collision
        collisions = self.white_walker_army.check_collisions(self.dragon.arsenal.arsenal)
        
        if collisions:
            # If any collision occurred, play the impact sound.
            self.impact_sound.play()
            self.impact_sound.fadeout(1250) 
        
        # Check if the entire White Walker army has been destroyed.
        if self.white_walker_army.check_destroyed_status():
            #resets and recreates the army
            self._reset_level() 
        
        
    def _check_game_status(self):
        """Handle the consequence of the dragon or army reaching a critical state."""
        
        # If the dragon has lives remaining.
        if self.game_stats.dragons_left > 0:
            self.game_stats.dragons_left -= 1 
            self._reset_level() # Clear the screen and create a new army.
            sleep(0.75) # Pause the game briefly to give the player time to react.
        else:
            # No lives left, end the game.
            self.game_active = False

    def _reset_level(self):
        """Reset game elements (projectiles and army) for a new life or level."""
        
        self.dragon.arsenal.arsenal.empty() # Clear all existing projectiles.
        self.white_walker_army.army.empty() # Clear all existing White Walkers.
        self.white_walker_army.create_army() # Reset formation of White Walkers.

    def restart_game(self):
        # set up dynamic settings
        # restart game statistics
        # update scoreboard images (HUD)
        # reset the level
        self._reset_level()
        # recenter the dragon
        self.dragon._center_dragon()
        
        self.game_active = True
        pygame.mouse.set_visible(False) # Hide the mouse cursor.

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        
        self.screen.blit(self.bg, (0, 0)) # Draw the background image.
        self.dragon.draw() # Draw the dragon and its projectiles.
        self.white_walker_army.draw() # Draw all White Walkers.
        
        if not self.game_active:
            self.play_button.draw() # Draw the Play button if the game is inactive.
            pygame.mouse.set_visible(True) # Show the mouse cursor.
        
        pygame.display.flip() # Make the most recently drawn screen visible.

    def _check_events(self):
        """Respond to keypresses and mouse/window events."""
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False # Stop the main game loop.
                pygame.quit() # Uninitialize pygame modules.
                sys.exit() # Exit the program.
            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event) # Handle key press (down) events.
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event) # Handle key release (up) events.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_button_clicked(self):
        mouse_position = pygame.mouse.get_pos() 
        if self.play_button.check_click(mouse_position):
            self.restart_game()
                    


    def _check_keyup_events(self, event):
        """Respond to key releases, stopping movement."""
        
        if event.key == pygame.K_UP:
            self.dragon.moving_up = False # Stop upward movement.
        elif event.key == pygame.K_DOWN:
            self.dragon.moving_down = False # Stop downward movement.
        

    def _check_keydown_events(self, event):
        """Respond to key presses, initiating movement or actions."""
        
        if event.key == pygame.K_UP:
            self.dragon.moving_up = True # Start upward movement.
        elif event.key == pygame.K_DOWN:
            self.dragon.moving_down = True # Start downward movement.
        elif event.key == pygame.K_SPACE:
           
            # Attempt to shoot a projectile. The shoot() method handles rate limiting.
            if self.dragon.shoot():
                self.element_sound.play() # Play the shooting sound.
                self.element_sound.fadeout(1250) 
        elif event.key == pygame.K_q:
            # 'q' is a shortcut to quit the game.
            self.running = False
            pygame.quit()
            sys.exit()
        


if __name__ == '__main__':
    # Create a game instance and run the game.
    ai = WhiteWalkerInvasion()
    ai.run_game()