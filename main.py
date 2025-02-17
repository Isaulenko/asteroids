# this allows us to use code from
# the open-source pygame library
# throughout this file

import os
os.environ["SDL_AUDIODRIVER"] = "dummy"  # Disable audio


import sys
import pygame
from pygame.locals import *


from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawble = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawble)
    Shot.containers = (shots, updatable, drawble)
    Asteroid.containers = (asteroids,updatable,drawble)
    AsteroidField.containers = updatable


    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collisions(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collisions(shot):
                    shot.kill()
                    asteroid.split()
        
        screen.fill((0, 0, 0))
        
        for obj in drawble:
            obj.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()