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

points = 0

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
    if player.check_collision(Asteroid.get_asteroids(), False):
        print(f"You lose! Points gained: {pygame.time.get_ticks() + points}")
        pygame.quit()
        sys.exit()

def track_points() -> int:
    if player.check_collision(Comet.comet, True):
        return 10000
    else:
        return 0

def mainloop() -> None:
    global points
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
        if Comet.comet_exists():
            Comet.update_comet()
        else:
            Comet.create_comet(SCREEN)
            
        player.update()
        points += track_points()

        check_lose_conditions()

        pygame.display.flip()

if __name__ == "__main__":
    mainloop()