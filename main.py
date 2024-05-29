import sys
import pygame
from src.buttons import Button

pygame.init()

SCREEN = pygame.display.set_mode((0,0))

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if keys[pygame.K_q]:
        pygame.quit()
        sys.exit()
    
    Button.onclick((200,200), (400,400))