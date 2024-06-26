import pygame
from settings import *
from src.asteroid import Asteroid
from PIL import Image

class MachineGun(pygame.sprite.Sprite):
    bullets = pygame.sprite.Group()
    def __init__(self, pos: list[int, int], screen: pygame.Surface) -> None:
        self.velocity = 600 // FPSCAP
        self.window_size = pygame.display.get_window_size()
        self.skin = pygame.image.load("src/img/bullet.png")
        self.damage = 1
        self.pos = pos.copy()
        self.mask = pygame.mask.from_surface(self.skin.convert_alpha())
        self.screen = screen
        self.explosion = pygame.image.load("src/img/small_explosion.png")
        super().__init__()
        self.add(MachineGun.bullets)
    
    def update(self):
        self.pos[1] -= self.velocity
        self.rect = self.skin.get_rect(center=self.pos)
        self.screen.blit(self.skin, self.rect)

        collided = pygame.sprite.spritecollideany(self, Asteroid.asteroids, pygame.sprite.collide_mask)
        if collided:
            collided.health -= 3
            self.screen.blit(self.explosion, self.rect)
            self.screen.blit(self.explosion, self.rect)
            MachineGun.bullets.remove(self)
        
        if self.pos[1] < 0:
            MachineGun.bullets.remove(self)