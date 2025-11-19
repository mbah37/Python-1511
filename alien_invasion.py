import sys
import pygame
from settings import Settings
from dragon import Dragon
from arsenal import DragonArsenal
from walker import Walker

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
        
        
        self.dragon = Dragon(self, DragonArsenal(self))
        # the higher you go the y value the lower you are on the screen
        # the higher the x value the more right you are on the screen
        self.walker = Walker(self, 10, 10)
     
    
    def run_game(self):
        while self.running:
            self._check_events()
            self.dragon.update()
            self.walker.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _update_screen(self):
        self.screen.blit(self.bg, (0, 0))
        self.dragon.draw()
        self.walker.draw_walker()
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


