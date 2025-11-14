import sys
import pygame
from settings import Settings
from dragon import Dragon

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

        self.dragon = Dragon(self)
    
    def run_game(self):
        while self.running:
            self._check_events()
            self.dragon.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _update_screen(self):
        self.screen.blit(self.bg, (0, 0))
        self.dragon.draw()
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
        if event.key == pygame.K_DOWN:
            self.dragon.moving_down = False
        

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.dragon.moving_up = True
        if event.key == pygame.K_DOWN:
            self.dragon.moving_down = True
        if event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()
        


if __name__ == '__main__':
    ai = WhiteWalkerInvasion()
    ai.run_game()