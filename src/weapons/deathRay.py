import pygame
from settings import *
from src.asteroid import Asteroid

class DeathRay(pygame.sprite.Sprite):
    death_ray = pygame.sprite.GroupSingle()
    def __init__(self, screen: pygame.Surface, pos: list[int, int]) -> None:
        self.screen = screen
        self.pos = pos.copy()
        self.window_size = pygame.display.get_window_size()
        self.skin = pygame.Surface((self.window_size[0] // 10, 9999))
        self.colours = [(0,255,0), (0,205,0), (0,155,0), (0,105,0), (0,55,0)]
        self.has_fired = False
        self.rect = self.skin.get_rect(center=self.pos)
        self.cooldown = 600 // FPSCAP
        self.selected_colour = 0
        self.mask = pygame.mask.from_surface(self.skin.convert_alpha())
        super().__init__()
    
    def update(self):
        self.cooldown -= 1
        self.skin.fill(self.colours[self.selected_colour])
        self.screen.blit(self.skin, self.rect)

        if self.cooldown <= 0:
            self.selected_colour += 1
            self.cooldown = 600 // FPSCAP
        
        if self.selected_colour == 5:
            DeathRay.death_ray.remove(self)
            return

        if self.has_fired == False:
            collided = pygame.sprite.spritecollide(self, Asteroid.asteroids, False, pygame.sprite.collide_mask)

            for i in collided:
                i.health -= 99

            self.has_fired = True
        
