import pygame
from figure.arrow import arrow



class roughness_measure:

    def __init__(self, screen, colors, blit_point, size = (60,60),
                 angle_rotate = 0, font = 'arial', text_method = '',
                 text_base_len = '', text_designation = ''):

        self.screen = screen
        self.colors = colors
        self.blit_point = blit_point
        self.original_blit_point = self.blit_point
        self.angle_rotate = angle_rotate
        self.width, self.height = size

        self.font = font
        self.text_method = text_method
        self.text_base_len = text_base_len
        self.text_designation = text_designation
    def check_click(self, clickpos):

        if (clickpos[0] > 0 and clickpos[1] > 0
                and clickpos[0] < self.width and clickpos[1] < self.height ):
            return True


    def draw(self):
        self.surface = pygame.Surface((self.width ,self.height  ),  pygame.SRCALPHA)

        pygame.draw.line(self.surface, self.colors['border'], (0, 2.5*self.height/3), (self.width/5, self.height))
        pygame.draw.line(self.surface, self.colors['border'], (self.width/5, self.height), ( 1.2*self.width/3, 2*self.height/3))
        pygame.draw.line(self.surface, self.colors['border'], ( 1.2*self.width/3, 2*self.height/3),(self.width , 2*self.height / 3))

        font = pygame.font.Font(self.font ,int(self.height/3))
        self.text_surface = font.render(str(self.text_method), True, self.colors['border'])
        self.text_point = ( 1.2*self.width/3 + self.text_surface.get_width()/2, self.height/3)
        self.surface.blit(self.text_surface, self.text_point)


        font = pygame.font.Font(self.font, int(self.height / 3))
        self.text_surface = font.render(str(self.text_base_len), True, self.colors['border'])
        self.text_point = (1.2 * self.width / 3 + self.text_surface.get_width() / 2, 2*self.height / 3)
        self.surface.blit(self.text_surface, self.text_point)

        font = pygame.font.Font(self.font, int(self.height / 5))
        self.text_surface = font.render(str(self.text_designation), True, self.colors['border'])
        self.text_point = (0.7 * self.width / 3 + self.text_surface.get_width() / 2, 4 * self.height / 5)
        self.surface.blit(self.text_surface, self.text_point)

        self.surface = pygame.transform.rotate(self.surface, self.angle_rotate)

        # self.screen.blit(self.surface, (self.blit_point[0], self.blit_point[1]))


