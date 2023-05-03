import pygame
from figure.arrow import arrow

class line_measure:

    def __init__(self, surface, start_point, end_point, colors, width,
                 border_size = 2, angle_rotate = 0, text = False,
        arrow_height = 10,
        font_size = 24,
        font = None, scale = 1):

        self.start_point = start_point
        self.end_point = end_point

        self.width = width
        self.scale = scale
        self.measure_shift = (self.start_point[1] - self.end_point[1])

        self.arrow_height = arrow_height
        self.font_size = font_size
        self.border_size = border_size

        self.font = font
        self.angle_rotate = angle_rotate

        self.colors = colors

        if (not text):
            self.text = str(self.width)
        else:
            self.text = str(text)




        self.surface = surface

    def check_click(self, click_pos):
        inaccuracy = 20
        if (self.angle_rotate == 0):


            if (self.measure_shift*self.scale > 0):
                if (click_pos[1] < self.arrow.blit_point[1] + inaccuracy and click_pos[1] > self.text_point[1] - inaccuracy):

                    print('click measure Horizontal')
                    return True
                else:
                    return False
            else:

                if (click_pos[1] < self.arrow.blit_point[1] + inaccuracy and click_pos[1] > self.text_point[1] - inaccuracy):

                    print('click measure Horizontal')
                    return True
                else:
                    return False

        if (self.angle_rotate == -90):

            if (self.measure_shift*self.scale > 0):
                if (click_pos[0] < self.measure_shift*self.scale - inaccuracy - self.arrow.start_point[0] + self.arrow_height
                        and click_pos[0] > self.measure_shift*self.scale - inaccuracy - self.arrow.start_point[0] - self.arrow_height):

                    print('click measure Vertical')
                    return True
                else:
                    return False
            else:
                if (click_pos[0] < -self.measure_shift*self.scale + inaccuracy + self.arrow.start_point[0] - self.arrow_height
                        and click_pos[0] > self.measure_shift*self.scale + inaccuracy + self.arrow.start_point[0] + self.arrow_height):

                    print('click measure Vertical')
                    return True
                else:
                    return False

    def draw(self):
        self.measure_surface = pygame.Surface((self.width, abs(self.measure_shift*self.scale )), pygame.SRCALPHA)

        # self.measure_surface.fill(self.colors['test'])
        self.arrow = arrow((self.arrow_height , self.measure_shift*self.scale ), self.measure_surface,
                           self.colors, True,
                           (int(self.width - self.arrow_height/2), self.arrow_height),
                           self.arrow_height , 0)


        if (self.measure_shift*self.scale > 0):
            pygame.draw.line(self.measure_surface, self.colors['border'],
                             (self.width - 5, 0 + self.font_size),
                             (self.width - 5, self.measure_shift*self.scale),
                             self.border_size - 1)

            pygame.draw.line(self.measure_surface, self.colors['border'],
                             (0, 0 + self.font_size),
                             (0, self.measure_shift*self.scale),
                             self.border_size - 1)
            self.arrow.blit_point = (0 - int(self.width - self.arrow_height/2), 0 + self.font_size)
            self.arrow.draw()


            font = pygame.font.Font(self.font, self.font_size)
            self.text_surface = font.render(str(self.text), True, self.colors['border'])
            self.text_point =  (self.width / 2 -  self.text_surface.get_width() / 2, 0 +
                                                     self.font_size/2)
            self.measure_surface.blit( self.text_surface, self.text_point)

            self.measure_surface = pygame.transform.rotate(self.measure_surface, self.angle_rotate)


            if (self.angle_rotate == 0):
                self.blit_point = (self.end_point[0], self.end_point[1] + ((self.start_point[1] - self.end_point[1]) - self.measure_shift*self.scale))
            if (self.angle_rotate == -90 or self.angle_rotate ==90):
                self.blit_point = (self.end_point[0] , self.end_point[1] )
            # self.surface.blit(self.measure_surface, self.blit_point)
        else:
            pygame.draw.line(self.measure_surface, self.colors['border'],
                             (self.width - 5, abs(self.measure_shift*self.scale)),
                             (self.width - 5, abs(00)),
                             self.border_size - 1)

            pygame.draw.line(self.measure_surface, self.colors['border'],
                             (0, abs(self.measure_shift*self.scale )),
                             (0, abs(0)),
                             self.border_size - 1)

            self.arrow.blit_point = (0 - int(self.width - self.arrow_height/2), abs(self.measure_shift*self.scale) - self.arrow_height*2)
            self.arrow.draw()

            font = pygame.font.Font(self.font, self.font_size)
            self.text_surface = font.render(str(self.text), True, self.colors['border'])
            self.text_point =  (self.width / 2 -  self.text_surface.get_width() / 2,
                                                     abs(self.measure_shift*self.scale ) - self.arrow_height - self.font_size)
            self.measure_surface.blit( self.text_surface, self.text_point)

            self.measure_surface = pygame.transform.rotate(self.measure_surface, self.angle_rotate)
            self.blit_point = (self.end_point[0], self.start_point[1] )
            if (self.angle_rotate == 0):
                self.blit_point = (self.end_point[0], self.start_point[1])
            if (self.angle_rotate == -90 or self.angle_rotate ==-90):
                self.blit_point = (self.end_point[0] + ( self.measure_shift*self.scale), self.start_point[1] - self.width + 2*self.border_size + 2*self.arrow_height)

