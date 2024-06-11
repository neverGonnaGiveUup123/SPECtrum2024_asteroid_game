import sys
import pygame
from settings import *
from rocket import Rocket
from asteroid import Asteroid
from comet import Comet

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

def check_lose_conditions() -> None:
    if player.check_collision(Asteroid.get_asteroids()):
        pygame.quit()
        print("You lose!")
        sys.exit()

def mainloop() -> None:
    cooldown = ASTEROIDSPAWNRATE
    Comet.create_comet(SCREEN)
    while True:
        clock.tick(FPSCAP)

        check_quit_conditions()

        SCREEN.fill((0,0,0))
        cooldown -= 1
        # print(cooldown)
        if cooldown <= 0:
            Asteroid.add_asteroid(Asteroid(SCREEN))
            cooldown = ASTEROIDSPAWNRATE
            cooldown -= pygame.time.get_ticks() // 1000

        Asteroid.update_all()
        Comet.update_comet()
        player.update()

        check_lose_conditions()

        pygame.display.flip()

if __name__ == "__main__":
    mainloop()