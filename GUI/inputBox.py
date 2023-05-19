import pygame

class inputBox:

    def set_base_border_color(self):

        self.current_border_color = self.base_border_color
    def set_selected_border_color(self):
        self.current_border_color = self.selected_color

    def __init__(self, surface, pos, size,colors,  text='',
                 font = None, font_size=14, border_size = 3,
                 onChangeAction = lambda : ..., action = lambda : ...,
                 sign = ''):

        self.pos = pos
        self.size = size
        self.colors = colors
        self.surface = surface
        self.border_size = border_size
        self.btnSurface = pygame.Surface(self.size, pygame.SRCALPHA)

        self.font = pygame.font.Font(font, font_size)

        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

        self.text = text
        self.sign = sign
        self.prevText = text
        self.active = False
        self.action = action
        self.onChangeAction = onChangeAction
        self.base_border_color = self.colors['border']
        self.selected_color = self.colors['selected']
        self.current_border_color = self.base_border_color

        self.redraw()

    def clear(self):
        # self.text = ''
        self.text = self.text

    def onChange(self):
        self.onChangeAction(self.text)

    def redraw(self):
        if self.text != self.prevText:
            self.prevText = self.text
            self.onChange()

        # Нарисовать поле ввода на экране
        if (self.active):
            self.current_border_color = self.selected_color
        else:
            self.current_border_color = self.base_border_color
        pygame.draw.rect(self.surface, self.current_border_color, self.rect, 2)
        # Нарисовать текст в поле ввода
        text_surface = self.font.render(self.text, True, self.colors['text'])
        self.surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

        sign_surface = self.font.render(self.sign, True, self.colors['text'])
        self.surface.blit(sign_surface, (self.rect.x - sign_surface.get_width() - 15, self.rect.y + sign_surface.get_height()/2))



