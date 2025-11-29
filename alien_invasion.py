import sys
import pygame
from settings import Settings
from game_stats import GameStats
from dragon import Dragon
from arsenal import DragonArsenal
from white_walker_army import WhiteWalkerArmy
from time import sleep
from button import Button
from hud import HUD

class WhiteWalkerInvasion:
    """Overall class to manage game assets and behavior.

    This class sets up and runs the White Walker Invasion game. It handles
    initialization of pygame, game settings, sprites (dragon and army),
    sounds, HUD, and the main loop that processes events, updates the game
    state, and draws everything to the screen.
    
    Attributes:
        settings (Settings): Game configuration object with all settings.
        screen (pygame.Surface): Main display surface for the game.
        bg (pygame.Surface): Scaled background image surface.
        game_stats (GameStats): Tracks score, level, lives, and high score.
        HUD (HUD): Heads-up display for scores, level, and lives.
        running (bool): Controls the overall game loop execution.
        clock (pygame.time.Clock): Used to regulate the frame rate.
        element_sound (pygame.mixer.Sound): Sound effect when the dragon shoots.
        impact_sound (pygame.mixer.Sound): Sound effect when a White Walker is hit.
        dragon (Dragon): Player-controlled dragon instance.
        white_walker_army (WhiteWalkerArmy): Manager for all White Walker enemies.
        play_button (Button): Button used to start or restart the game.
        game_active (bool): Whether the game is currently active (playing) or not.
    """

    def __init__(self):
        """Initialize the game, and create game resources.

        This method initializes pygame, loads settings, creates the main
        display surface, loads the background image, sets up game statistics,
        the HUD, clock, mixer, sounds, player dragon, enemy army, and the
        Play button. It also sets the initial game state flags.
        """
        
        pygame.init() # Initialize all imported pygame modules.
        
        # Load game settings and initialize game statistics.
        self.settings = Settings()
        self.settings.initialize_dynamic_settings()
        # Set up the main game screen (display surface).
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption(self.settings.name) # Set the window title.

        # Load and scale the background image.
        self.bg: pygame.Surface = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg,
             (self.settings.screen_width, self.settings.screen_height))

        self.game_stats = GameStats(self)
        self.HUD = HUD(self)
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
        
        # Populate the screen with White Walkers.
        self.white_walker_army.create_army() 
        
        # Create the Play button.
        self.play_button = Button(self, "Play") 
        
        # Flag to indicate if the game is currently running (not paused or game over).
        self.game_active = False 
    
    def run_game(self):
        """Start and manage the main loop for the game.

        This loop runs while `self.running` is True. It repeatedly:
        - Processes user input events.
        - Updates the dragon, army, and collision logic when the game is active.
        - Redraws the screen.
        - Regulates the frame rate using the settings FPS value.
        """
        
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
        """Handle all collision checks and their consequences.

        This method checks:
        - Collisions between the dragon and any White Walker, updating game
          status and lives as needed.
        - Whether any White Walker has reached the left edge, which triggers
          a life loss or game over.
        - Collisions between dragon projectiles and White Walkers, updating
          score, playing sound effects, and updating the HUD.
        - Whether the entire army has been destroyed, in which case a new
          level starts and difficulty is increased.
        """
        
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
            self.game_stats.update(collisions) # Update score and max score.
            self.HUD.update_scores()

        # Check if the entire White Walker army has been destroyed.
        if self.white_walker_army.check_destroyed_status():
            #resets and recreates the army
            self._reset_level()
            self.settings.increase_difficulty() # Increase game difficulty. 
            
            # update level in game stats
            self.game_stats.update_level()
            
            # update HUD view
            self.HUD.update_level()
        
    def _check_game_status(self):
        """Handle the consequence of the dragon or army reaching a critical state.

        If the dragon still has remaining lives, this method decrements the
        lives counter, resets the level (army and projectiles), and briefly
        pauses the game. If there are no lives left, it marks the game as
        inactive, which stops updates and shows the Play button.

        Returns:
            None
        """
        
        # If the dragon has lives remaining.
        if self.game_stats.dragons_left > 0:
            self.game_stats.dragons_left -= 1 
            self._reset_level() # Clear the screen and create a new army.
            sleep(0.75) # Pause the game briefly to give the player time to react.
        else:
            # No lives left, end the game.
            self.game_active = False

    def _reset_level(self):
        """Reset game elements (projectiles and army) for a new life or level.

        This method:
        - Clears all active dragon projectiles.
        - Clears the existing White Walker army.
        - Recreates a fresh army formation.

        It is called when a life is lost or when the army is fully destroyed.
        """
        
        self.dragon.arsenal.arsenal.empty() # Clear all existing projectiles.
        self.white_walker_army.army.empty() # Clear all existing White Walkers.
        self.white_walker_army.create_army() # Reset formation of White Walkers.

    def restart_game(self):
        """Restart the game to its initial state.

        This method:
        - Reinitializes dynamic settings.
        - Resets game statistics.
        - Updates HUD score images.
        - Resets the level (army and projectiles).
        - Recenters the dragon.
        - Hides the mouse cursor and marks the game as active.
        """
        
       
        self.settings.initialize_dynamic_settings() # set up dynamic settings
        self.game_stats.reset_stats() # restart game statistics
        self.HUD.update_scores()# update scoreboard images (HUD)
        self._reset_level() # reset the level
        self.dragon._center_dragon() # recenter the dragon
        
        self.game_active = True
        pygame.mouse.set_visible(False) # Hide the mouse cursor.

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen.

        Draws, in order:
        - The background image.
        - The dragon and its projectiles.
        - All White Walkers.
        - The HUD (score, lives, level).
        - The Play button, if the game is inactive.

        Finally, it flips the display to show the newly drawn frame.
        """
        
        self.screen.blit(self.bg, (0, 0)) # Draw the background image.
        self.dragon.draw() # Draw the dragon and its projectiles.
        self.white_walker_army.draw() # Draw all White Walkers.
        self.HUD.draw() # Draw the HUD (score, lives, level).

        if not self.game_active:
            self.play_button.draw() # Draw the Play button if the game is inactive.
            pygame.mouse.set_visible(True) # Show the mouse cursor.
        
        pygame.display.flip() # Make the most recently drawn screen visible.

    def _check_events(self):
        """Respond to keypresses and mouse/window events.

        This method polls pygame's event queue and:
        - Handles window quit events by stopping the game and saving scores.
        - Delegates keydown events to `_check_keydown_events` when the game is active.
        - Delegates keyup events to `_check_keyup_events`.
        - Handles mouse button clicks by checking if the Play button was pressed.
        """
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False # Stop the main game loop.
                self.game_stats.save_scores()
                pygame.quit() # Uninitialize pygame modules.
                sys.exit() # Exit the program.
            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event) # Handle key press (down) events.
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event) # Handle key release (up) events.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_button_clicked(self):
        """Handle mouse click events for the Play button.

        This method gets the current mouse position and checks whether the
        Play button has been clicked. If so, it restarts the game.

        Returns:
            None
        """
        mouse_position = pygame.mouse.get_pos() 
        if self.play_button.check_click(mouse_position):
            self.restart_game()
                    

    def _check_keyup_events(self, event):
        """Respond to key releases, stopping movement.

        This method is called when a KEYUP event is detected. It checks for
        arrow key releases and clears the corresponding movement flags on
        the dragon.

        Args:
            event (pygame.event.Event): The pygame event representing the key release.

        Returns:
            None
        """
        
        if event.key == pygame.K_UP:
            self.dragon.moving_up = False # Stop upward movement.
        elif event.key == pygame.K_DOWN:
            self.dragon.moving_down = False # Stop downward movement.
        

    def _check_keydown_events(self, event):
        """Respond to key presses, initiating movement or actions.

        This method is called when a KEYDOWN event is detected and the game
        is active. It:
        - Starts upward or downward movement of the dragon when arrow keys
          are pressed.
        - Attempts to fire a projectile when the space bar is pressed.
        - Quits the game when 'q' is pressed.

        Args:
            event (pygame.event.Event): The pygame event representing the key press.

        Returns:
            None
        """
        
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
            self.game_stats.save_scores()
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    # Create a game instance and run the game.
    ai = WhiteWalkerInvasion()
    ai.run_game()