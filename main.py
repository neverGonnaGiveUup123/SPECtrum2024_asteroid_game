import sys
import pygame
from settings import *
from rocket import Rocket
from asteroid import Asteroid

pygame.init()

SCREEN = pygame.display.set_mode(WINDOWSIZE)

clock = pygame.time.Clock()

player = Rocket(SCREEN)

for i in range(5):
    Asteroid.add_asteroid(Asteroid(SCREEN))

def check_quit_conditions() -> None:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if keys[pygame.K_q]:
        pygame.quit()
        sys.exit()

def mainloop() -> None:
    while True:
        clock.tick(FPSCAP)

        check_quit_conditions()

        SCREEN.fill((0,0,0))

        for i in Asteroid.asteroids:
            i.update()

        player.update()

        pygame.display.flip()

if __name__ == "__main__":
    mainloop()