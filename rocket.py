import pygame
from settings import *

class Rocket:
    def __init__(self, screen: pygame.Surface) -> None:
        self.window_size = pygame.display.get_window_size()
        self.body = pygame.Surface((self.window_size[0] // 10, self.window_size[1] // 10))
        self.body.fill((255,0,0))
        self.velocity = 420 // FPSCAP
        self.pos = [self.window_size[0] // 2, self.window_size[1] // 5 * 4]
        self.screen = screen

    def handle_movement(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            print("EEE")
            print(self.velocity)
            self.pos[1] -= self.velocity
            print(self.pos)
        if keys[pygame.K_d]:
            self.pos[0] += self.velocity
        if keys[pygame.K_s]:
            self.pos[1] += self.velocity
        if keys[pygame.K_a]:
            self.pos[0] -= self.velocity
        
        self.updated_rect = self.body.get_rect(center=self.pos)
    
    def update(self) -> None:
        self.handle_movement()
        # print(self.pos)

        self.screen.blit(self.body, self.updated_rect)