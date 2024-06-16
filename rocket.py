import pygame
from settings import *


class Rocket:
    def __init__(self, screen: pygame.Surface) -> None:
        self.window_size = pygame.display.get_window_size()
        self.size = (self.window_size[0] // 10, self.window_size[0] // 10)
        self.skin = pygame.Surface(self.size)
        self.skin.fill((255, 0, 0))
        self.velocity = 512 // FPSCAP
        self.pos = [self.window_size[0] // 2, self.window_size[1] // 5 * 4]
        self.screen = screen
        self.mask = pygame.mask.from_surface(self.skin.convert_alpha())

    def handle_movement(self) -> None:
        keys = pygame.key.get_pressed()
        # print(self.pos)
        if keys[pygame.K_w] and self.pos[1] - self.size[1] // 2 > 0:
            self.pos[1] -= self.velocity
        if keys[pygame.K_d] and self.pos[0] + self.size[0] // 2 < self.window_size[0]:
            self.pos[0] += self.velocity
        if keys[pygame.K_s] and self.pos[1] + self.size[1] // 2 < self.window_size[1]:
            self.pos[1] += self.velocity
        if keys[pygame.K_a] and self.pos[0] - self.size[0] // 2 > 0:
            self.pos[0] -= self.velocity

        self.rect = self.skin.get_rect(center=self.pos)

    def check_collision(self, sprite_group, kill: bool) -> False:
        if pygame.sprite.spritecollide(
            self, sprite_group, kill, pygame.sprite.collide_mask
        ):
            return True
        else:
            return False

    def update(self) -> None:
        self.handle_movement()
        # print(self.pos)
        self.screen.blit(self.skin, self.rect)

    def set_pos(self, pos: list[int, int]):
        self.pos = pos
