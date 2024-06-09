import pygame
from random import randint
from settings import *

class Asteroid(pygame.sprite.Sprite):
    asteroids = pygame.sprite.Group()

    def __init__(self, screen: pygame.Surface) -> None:
        self.ran_dimension = randint(5,10)
        self.window_size = pygame.display.get_window_size()
        self.skin = pygame.Surface((self.window_size[0] // self.ran_dimension, self.window_size[1] // self.ran_dimension))
        self.skin.fill((0,255,0))
        self.velocity = randint(514,578) // FPSCAP
        self.pos = [randint(0, self.window_size[0]), -100]
        self.screen = screen
        super().__init__()
    
    def update(self):
        self.pos[1] += self.velocity
        self.new_pos = self.skin.get_rect(center=self.pos)
        self.screen.blit(self.skin, self.new_pos)
    
    @classmethod
    def add_asteroid(cls, obj):
        cls.asteroids.add(obj)