import pygame
from settings import *

class Button:
    def __init__(self, colour: pygame.Color, size: list[int, int], pos: list[int, int], text = " ") -> None:
        self.colour = colour
        self.size = size
        self.pos = pos
        self.text = text
        self.surface = pygame.Surface(size, pygame.BLEND_RGB_MAX)
        self.surface.fill(self.colour)
        self.font = pygame.font.Font(FONT, pygame.display.get_window_size()[0] // 48)

    def display(self, screen: pygame.Surface):
        self.rect = self.surface.get_rect(center=self.pos)
        screen.blit(self.surface, self.rect)
        text = self.font.render(self.text, True, (0,0,0))
        text_rect = text.get_rect(center = self.pos)
        screen.blit(text, text_rect)

class Text:
    def __init__(self, font_size: int, font) -> None:
        self.font = pygame.font.Font(font, font_size)

    def display(self, text: str, pos: list[int, int], colour: pygame.Color, screen: pygame.Surface):
        rendered_text = self.font.render(text, True, colour)
        positioned_text = rendered_text.get_rect(center = pos)
        screen.blit(rendered_text, positioned_text)