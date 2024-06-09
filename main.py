import sys
import pygame
from settings import *
from rocket import Rocket
from asteroid import Asteroid

pygame.init()

SCREEN = pygame.display.set_mode(WINDOWSIZE)

clock = pygame.time.Clock()

player = Rocket(SCREEN)

def check_quit_conditions() -> None:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if keys[pygame.K_q]:
        pygame.quit()
        sys.exit()

def spawn_asteroids(cooldown) -> None:
    cooldown -= 1
    if cooldown <= 0:
        Asteroid.add_asteroid(Asteroid(SCREEN))
        # print("E")
        cooldown = 10
    return cooldown


def mainloop() -> None:
    asteroid_cooldown = 10
    while True:
        clock.tick(FPSCAP)

        check_quit_conditions()

        asteroid_cooldown = spawn_asteroids(asteroid_cooldown)

        SCREEN.fill((0,0,0))

        [asteroid.update() for asteroid in Asteroid.asteroids]

        player.update()

        pygame.display.flip()

if __name__ == "__main__":
    mainloop()