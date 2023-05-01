import pygame
import math

class arrow:


    def __init__ (self, start_point, surface, colors,
                  double = False, size = (100, 25),
                   arrow_height = 25, angle_rotate = 0,
                  border_size = 2, text = '', font = None,
                  font_size = 16, opposite = False):

        self.start_point = start_point
        self.blit_point = start_point
        self.original_blit_point = self.blit_point
        self.surface = surface
        self.colors = colors

        self.text = text
        self.font = font
        self.font_size = font_size
        #
        self.double = double
        self.opposite = opposite
        self.size = size
        self.border_size = border_size

        self.arrow_height = arrow_height
        self.angle_rotate = angle_rotate
        self.height = self.size[1] + self.font_size
        self.width = self.size[0]*2

    def check_click(self, clickpos):


        if (clickpos[1] > 0 and clickpos[0] > 0 and

                 clickpos[1] < self.height   and  clickpos[0] < self.width):
            return True

    def draw(self):
        self.arrow_surface = pygame.Surface((self.width,self.height ),  pygame.SRCALPHA)

        arrow_shift = self.arrow_height / 1
        if (not self.opposite):
            # Создаем поверхность для стрелки
            pygame.draw.polygon( self.arrow_surface, self.colors['border'], [(self.width/2 - self.arrow_height + self.width/2, arrow_shift)  , (self.width/2 + self.width/2, self.height / 2) ,
                                                                       (self.width/2 - self.arrow_height + self.width/2, self.height - arrow_shift)] )

        if (self.double or self.opposite):
            pygame.draw.polygon(self.arrow_surface, self.colors['border'],
                                [(self.arrow_height + self.width/2, arrow_shift) ,
                                 (0 + self.width/2, self.height / 2),
                                 (self.arrow_height + self.width/2, self.height - arrow_shift) ])
        pygame.draw.line( self.arrow_surface, self.colors['border'],
                         (self.width/2 + self.width/2, self.height / 2),
                         (0 + self.width/2, self.height / 2),
                         self.border_size)


        font = pygame.font.Font(self.font, self.font_size)
        self.text_surface = font.render(str(self.text), True, self.colors['border'])
        self.text_point = (self.width/2 * 1.5 - self.text_surface.get_width()/2, 0 )

        self.arrow_surface.blit(self.text_surface, self.text_point)
        self.arrow_surface = pygame.transform.rotate(self.arrow_surface, self.angle_rotate)

        # self.blit_point = ( int(self.start_point[0]  - self.arrow_surface.get_width()/2),
        #                int(self.start_point[1]  - self.arrow_surface.get_height()/2))
        #
        # pygame.draw.circle(self.surface, (255, 0, 0), self.blit_point,10)

        self.surface.blit(self.arrow_surface, self.blit_point)



