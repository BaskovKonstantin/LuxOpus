import pygame

class button:

    def redraw(self):
        self.surface.blit(self.font.render(self.text, True, self.colors['text']), self.text_rect)

        self.surface.blit(self.btnSurface, self.pos)

    def click(self):
        self.action()

    def __init__(self, surface, pos, size,colors, action,  text = 'TEST', font = None, font_size=18, border_size = 3):

        self.pos = pos
        self.size = size
        self.colors = colors
        self.action = action
        self.btnSurface = pygame.Surface(self.size, pygame.SRCALPHA)



        self.rect_text = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.rect = pygame.Rect(0, 0, self.size[0], self.size[1])

        self.surface = surface
        pygame.draw.rect(self.btnSurface, self.colors['border'], self.rect, border_size)

        self.text = text
        self.font = pygame.font.Font(font, font_size)

        self.text_rect = self.font.render(self.text, True, self.colors['text']).get_rect(center=self.rect_text.center)
        self.surface.blit(self.font.render(self.text, True, self.colors['text']), self.text_rect)

        self.surface.blit(self.btnSurface, self.pos)

        self.action = action
