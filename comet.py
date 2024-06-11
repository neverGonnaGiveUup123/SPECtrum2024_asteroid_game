import pygame
import math
from random import randint
from settings import *

class Comet(pygame.sprite.Sprite):
    comet = pygame.sprite.GroupSingle()
    def __init__(self, screen: pygame.Surface) -> None:
        self.window_size = pygame.display.get_window_size()
        self.y_intercept = randint(0, self.window_size[1])
        self.gradient = -1.0 * math.cos(0.003 * self.y_intercept)
        self.skin = pygame.Surface((self.window_size[0] // 20, self.window_size[0] // 20))
        self.skin.fill((0,0,255))
        self.pos = [0,0]
        self.velocity = 800 // FPSCAP
        self.pos[1] = self.y_intercept
        self.screen = screen
        super().__init__()
    
    def update(self):
        self.pos[0] += self.velocity
        self.pos[1] = self.gradient * self.pos[0] + self.y_intercept
        self.screen.blit(self.skin, self.pos)
    
    @classmethod
    def create_comet(cls, screen):
        cls.comet.add(Comet(screen))
    
    @classmethod
    def update_comet(cls):
        cls.comet.sprite.update()