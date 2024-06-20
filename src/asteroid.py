import pygame
from random import randint
from settings import *
from PIL import Image


class Asteroid(pygame.sprite.Sprite):
    asteroids = pygame.sprite.Group()

    def __init__(self, screen: pygame.Surface) -> None:
        self.random = randint(0, 2)
        self.window_size = pygame.display.get_window_size()
        match self.random:
            case 0:
                self.skin = pygame.image.load("src/img/small_asteroid_skin.png")
            case 1:
                self.skin = pygame.image.load("src/img/medium_asteroid_skin.png")
            case 2:
                self.skin = pygame.image.load("src/img/large_asteroid_skin.png")
        self.velocity = randint(514, 578) // FPSCAP
        self.pos = [randint(0, self.window_size[0]), -100]
        self.screen = screen
        self.mask = pygame.mask.from_surface(self.skin.convert_alpha())
        self.health = 12
        self.explosion = pygame.image.load("src/img/large_explosion.png")
        super().__init__()
    
    def explode(self):
        self.screen.blit(self.explosion, self.skin.get_rect(center=self.pos))

    def update(self):
        self.pos[1] += self.velocity
        self.rect = self.skin.get_rect(center=self.pos)
        self.screen.blit(self.skin, self.rect)

    @classmethod
    def update_all(cls):
        for i in cls.asteroids:
            if i.pos[1] > i.window_size[1] + 100:
                cls.asteroids.remove(i)
                del i
            elif i.health <= 0:
                i.explode()
                cls.asteroids.remove(i)
                del i
            else:
                i.update()

    @classmethod
    def add_asteroid(cls, obj):
        cls.asteroids.add(obj)

    @classmethod
    def get_asteroids(cls):
        return cls.asteroids