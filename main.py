# this allows us to use code from
# the open-source pygame library
# throughout this file
import os
os.environ["SDL_AUDIODRIVER"] = "dummy"  # Disable audio



import pygame
from pygame.locals import *


from constants import *
from player import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawble = pygame.sprite.Group()

    Player.containers = (updatable,drawble)
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        screen.fill((0, 0, 0))
        
        for obj in drawble:
            obj.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()