import sys
import pygame
from settings import Settings
from dragon import Dragon
from arsenal import DragonArsenal
#from white_walker import Walker
from white_walker_army import WhiteWalkerArmy

class WhiteWalkerInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg,
             (self.settings.screen_width, self.settings.screen_height))

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.element_sound = pygame.mixer.Sound(self.settings.element_sound)
        self.element_sound.set_volume(0.7)
        
        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(0.7)
        
        
        self.dragon = Dragon(self, DragonArsenal(self))
        self.white_walker_army = WhiteWalkerArmy(self)
        # the higher you go the y value the lower you are on the screen
        # the higher the x value the more right you are on the screen
        self.white_walker_army.create_army()     
    
    def run_game(self):
        # Main loop for the game.
        while self.running:
            self._check_events()
            self.dragon.update()
            self.white_walker_army.update_army()
            self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):
        #check collisions for dragons
        if self.dragon.check_collision(self.white_walker_army.army):
            self._reset_level()
            #subtract a life

        #check collisions for white walkers hitting left side of the screen
        if self.white_walker_army.check_left_edge():
            self._reset_level()

        #check collions for projectiles and white walkers
        collisions = self.white_walker_army.check_collisions(self.dragon.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(1250)
        
        if self.white_walker_army.check_destroyed_status():
            self._reset_level()
        
        

    def _reset_level(self):
        self.dragon.arsenal.arsenal.empty()
        self.white_walker_army.army.empty()
        self.white_walker_army.create_army()

    def _update_screen(self):
        self.screen.blit(self.bg, (0, 0))
        self.dragon.draw()
        self.white_walker_army.draw()
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.dragon.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.dragon.moving_down = False
        

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.dragon.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.dragon.moving_down = True
        elif event.key == pygame.K_SPACE:
            if self.dragon.shoot():
                self.element_sound.play()
                self.element_sound.fadeout(1250)
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()
        


if __name__ == '__main__':
    ai = WhiteWalkerInvasion()
    ai.run_game()


