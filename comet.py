import pygame
import math
from random import randint
from settings import *

class Comet(pygame.sprite.Sprite):
    comet = pygame.sprite.GroupSingle()
    def __init__(self, screen: pygame.Surface) -> None:
        self.window_size = pygame.display.get_window_size()
        self.y_intercept = randint(0, self.window_size[1])
        self.gradient = self.window_size[1] // self.window_size[0]
        self.skin = pygame.Surface((self.window_size[0] // 20, self.window_size[0] // 20))
        self.skin.fill((0,0,255))
        self.pos = [0,0]
        self.velocity = 800 // FPSCAP
        self.pos[1] = self.y_intercept
        self.screen = screen
        self.mask = pygame.mask.from_surface(self.skin.convert_alpha())
        super().__init__()
    
    def update(self):
        self.pos[0] += self.velocity
        self.pos[1] = self.gradient * self.pos[0] + self.y_intercept
        self.rect = self.skin.get_rect(center=self.pos)
        self.screen.blit(self.skin, self.rect)
    
    @classmethod
    def create_comet(cls, screen):
        cls.comet.add(Comet(screen))
    
    @classmethod
    def update_comet(cls):
        if cls.comet.sprite:
            cls.comet.sprite.update()
    
    def comet_exists(cls) -> bool:
        if cls.comet.sprite:
            return True
        else:
            return False