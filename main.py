import sys
import pygame
from src.buttons import Button

pygame.init()

SCREEN = pygame.display.set_mode((0,0))
WINDOWSIZE = pygame.display.get_window_size()

main_menu_button = Button([WINDOWSIZE[0] // 2, 100], "Press spacebar to start", font_size=36)
main_menu_button.set_colour((255,10,10), 255)
main_menu_button.set_pos([WINDOWSIZE[0] // 2, WINDOWSIZE[1] // 2])

clock = pygame.time.Clock()

started = False
while True:
    clock.tick(60)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if keys[pygame.K_q]:
        pygame.quit()
        sys.exit()

    SCREEN.fill((0,0,0))

    if started == False:
        main_menu_button.display(SCREEN)
        pygame.display.flip()
        if keys[pygame.K_SPACE]:
            started = True
        continue

    pygame.display.flip()