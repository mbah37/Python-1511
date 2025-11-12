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

        # change variable to dragon. remove comment when done
        self.ship = Dragon(self)
    
    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
            self.screen.blit(self.bg, (0, 0))
            # change variable to dragon. remove comment when done
            self.ship.draw()
            pygame.display.flip()
            self.clock.tick(self.settings.FPS)

if __name__ == '__main__':
    ai = WhiteWalkerInvasion()
    ai.run_game()