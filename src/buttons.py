import pygame

class Button:
    build_menu_buttons = []
    main_menu_buttons = []

    def __init__(self, dimensions: list[int, int], text: str, font_type = pygame.font.get_default_font(), font_size = 18, font_colour = (255,255,255)) -> None:
        self.dimensions = dimensions
        self.pos = [0,0]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.dimensions[0], self.dimensions[1])
        self.colour = pygame.color.Color(255,255,255,255)
        self.text = text
        self.font_colour = font_colour
        self.font_size = font_size
        self.font_type = font_type
        self.font = pygame.font.Font(self.font_type, self.font_size)
        self.rendered_text = self.font.render(self.text, True, self.font_colour)
    
    def set_colour(self, colour: tuple, alpha=255):
        self.colour.update(colour[0], colour[1], colour[2], alpha)

    def set_pos(self, pos: list[int, int]):
        self.rect.center = pos
        self.text_rect = self.rendered_text.get_rect(center=pos)

    def pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            print("Pressed")
            if mouse_pos[0] <= self.dimensions[0] and mouse_pos[0] >= self.pos[0]:
                if mouse_pos[1] >= self.pos[1] and mouse_pos[1] <= self.dimensions[1]:
                    return True
    
    def display(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.colour, self.rect)
        screen.blit(self.rendered_text, self.text_rect)