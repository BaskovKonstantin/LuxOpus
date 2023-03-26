import pygame

class inputBox:

    def __init__(self, surface, pos, size,colors,  text='', font = None, font_size=18, border_size = 3, onChangeAction = lambda : ..., action = lambda : ...):

        self.pos = pos
        self.size = size
        self.colors = colors
        self.surface = surface
        self.border_size = border_size
        self.btnSurface = pygame.Surface(self.size, pygame.SRCALPHA)

        self.font = pygame.font.Font(font, font_size)

        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

        self.text = text
        self.prevText = text
        self.active = False
        self.action = action
        self.onChangeAction = onChangeAction

        self.redraw()

    def clear(self):
        self.text = ''



    def onChange(self):
        self.onChangeAction(self.text)


    def redraw(self):
        if self.text != self.prevText:
            self.prevText = self.text
            self.onChange()

        # Нарисовать поле ввода на экране
        pygame.draw.rect(self.surface, self.colors['border'], self.rect, 2)
        # Нарисовать текст в поле ввода
        text_surface = self.font.render(self.text, True, self.colors['text'])
        self.surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

