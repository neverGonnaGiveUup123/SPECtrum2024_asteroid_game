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
        self.size = self.window_size[0] // 20
        self.skin = pygame.Surface((self.size, self.size))
        self.trail = [
            pygame.Surface((self.size, self.size), pygame.SRCALPHA),
            pygame.Surface((self.size, self.size), pygame.SRCALPHA),
            pygame.Surface((self.size, self.size), pygame.SRCALPHA),
            pygame.Surface((self.size, self.size), pygame.SRCALPHA),
        ]
        alpha = 220
        for i in self.trail:
            i.fill((0,0,255,alpha))
            alpha -= 50

        self.skin.fill((0,0,255))
        self.pos = [0,0]
        self.velocity = 1200 // FPSCAP
        self.pos[1] = self.y_intercept
        self.screen = screen
        self.rect = self.skin.get_rect()
        self.mask = pygame.mask.from_surface(self.skin.convert_alpha())
        super().__init__()
    
    def update(self):
        self.pos[0] += self.velocity
        self.pos[1] = self.gradient * self.pos[0] + self.y_intercept
        self.rect = self.skin.get_rect(center=self.pos)
        self.screen.blit(self.skin, self.rect)
        self.make_trail()
        if self.pos[0] > self.window_size[0] + 100:
            Comet.comet.empty()
    
    def make_trail(self):
        tmp_interval = self.velocity
        for i in self.trail:
            # print(i)
            tmp_pos = self.pos.copy()
            tmp_pos[0] += tmp_interval
            tmp_pos[1] = self.gradient * tmp_pos[0] + self.y_intercept
            tmp_rect = i.get_rect(center=tmp_pos)
            # print(tmp_pos)
            self.screen.blit(i, tmp_rect)
            tmp_interval -= self.velocity*2
    
    @classmethod
    def create_comet(cls, screen):
        if pygame.time.get_ticks() % 100 == 0:
            cls.comet.add(Comet(screen))
    
    @classmethod
    def update_comet(cls):
        if cls.comet.sprite:
            cls.comet.sprite.update()
    
    @classmethod
    def comet_exists(cls) -> bool:
        if cls.comet.sprite:
            return True
        else:
            return False