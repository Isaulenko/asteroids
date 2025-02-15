# this allows us to use code from
# the open-source pygame library
# throughout this file
import os
os.environ["SDL_AUDIODRIVER"] = "dummy"  # Disable audio



import pygame
from pygame.locals import *


from constants import *



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    main()