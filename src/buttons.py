import pygame

class Button:
    @staticmethod
    def onclick(coords0, coords1):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            print("Pressed")
            if mouse_pos[0] <= coords1[0] and mouse_pos[0] >= coords0[0]:
                if mouse_pos[1] >= coords0[1] and mouse_pos[1] <= coords1[1]:
                    return True
    
    def hide():
        pass

    def show():
        pass