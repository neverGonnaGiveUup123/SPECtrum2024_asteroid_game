import pygame
from settings import *
from machineGun import MachineGun
from deathRay import DeathRay

class Rocket:
    def __init__(self, screen: pygame.Surface) -> None:
        self.window_size = pygame.display.get_window_size()
        self.size = (self.window_size[0] // 10 // 3, self.window_size[0] // 10)
        self.skin = pygame.Surface(self.size)
        self.skin.fill((255, 0, 0))
        self.velocity = 512 // FPSCAP
        self.pos = [self.window_size[0] // 2, self.window_size[1] // 5 * 4]
        self.screen = screen
        self.points_multiplier = 1
        self.mask = pygame.mask.from_surface(self.skin.convert_alpha())

    def handle_movement(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_s] and self.pos[1] + self.size[1] // 2 < self.window_size[1]:
            self.pos[1] += self.velocity
        if keys[pygame.K_a] and self.pos[0] - self.size[0] // 2 > 0:
            self.pos[0] -= self.velocity
        if keys[pygame.K_w] and self.pos[1] - self.size[1] // 2 > 0:
            self.pos[1] -= self.velocity
        if keys[pygame.K_d] and self.pos[0] + self.size[0] // 2 < self.window_size[0]:
            self.pos[0] += self.velocity

        self.rect = self.skin.get_rect(center=self.pos)

    def check_collision(self, sprite_group, kill: bool) -> False:
        if pygame.sprite.spritecollide(
            self, sprite_group, kill, pygame.sprite.collide_mask
        ):
            return True
        else:
            return False

    def update(self) -> None:
        keys = pygame.key.get_pressed()
        self.handle_movement()

        if self.selected_weapon == 0:
            self.fire_machine_gun()
        
        if self.selected_weapon == 1:
            self.tmp -= 1
            if self.tmp <= 0 and keys[pygame.K_SPACE]:
                DeathRay.death_ray.add(DeathRay(self.screen, self.pos))
                self.tmp = self.weapon_cooldown
            
            laser = DeathRay.death_ray.sprite
            if laser:
                laser.update() 
        

        self.screen.blit(self.skin, self.rect)

    def set_pos(self, pos: list[int, int]):
        self.pos = pos

    def fire_machine_gun(self):
        self.tmp -= 1
        if self.tmp <= 0:
            MachineGun.bullets.add(MachineGun(self.pos, self.screen))
            self.tmp = self.weapon_cooldown
        
        for i in MachineGun.bullets:
            i.update()

    def import_rocket_designer_vals(self, velocity: int, points_multiplier: float, skin: pygame.Surface, weapon: int):
        self.velocity = velocity
        self.points_multiplier = points_multiplier
        self.skin = skin.convert_alpha()
        self.mask = pygame.mask.from_surface(self.skin)

        if weapon == 0:
            self.weapon_cooldown = 1200 // FPSCAP
            self.tmp = 0
            self.selected_weapon = 0
        else:
            self.weapon_cooldown = 28800 // FPSCAP
            self.tmp = 0
            self.selected_weapon = 1