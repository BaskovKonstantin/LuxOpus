import pygame
import math
from figure.arrow import arrow



class facet_measure:

    def __init__(self, screen, colors, blit_point, size = (60,60),
                 angle_rotate = 0, font = 'arial', text = ''):

        self.screen = screen
        self.colors = colors
        self.blit_point = blit_point
        self.angle_rotate = angle_rotate
        self.width, self.height = size

        self.font = font
        self.text = text

    def check_click(self, clickpos):

        if (clickpos[0] > 0 and clickpos[1] > 0
                and clickpos[0] < self.width and clickpos[1] < self.height ):
            return True


    def draw(self):
        self.surface = pygame.Surface((self.width ,self.height  ),  pygame.SRCALPHA)


        pygame.draw.line(self.surface, self.colors['border'], (self.width/5, self.height), ( 1.2*self.width/3, 2*self.height/3))
        pygame.draw.line(self.surface, self.colors['border'], ( 1.2*self.width/3, 2*self.height/3),(self.width , 2*self.height / 3))

        # задаем начальную и конечную точки для стрелки
        start_pos = (( 1.2*self.width/3, 2*self.height/3))
        end_pos =  (self.width/5, self.height)

        # рисуем линию от начальной до конечной точки
        pygame.draw.line(self.surface, self.colors['border'], start_pos, end_pos)

        # находим угол между начальной и конечной точками линии
        dx = end_pos[0] - start_pos[0]
        dy = end_pos[1] - start_pos[1]
        angle = math.atan2(dy, dx)

        # определяем координаты вершин стрелки, повернутой на найденный угол
        arrow_points = [
            end_pos,  # вершина стрелки
            (end_pos[0] - 5, end_pos[1] - 5),  # один из концов основания стрелки
            (end_pos[0] - 5, end_pos[1] + 5)  # второй конец основания стрелки
        ]
        rotated_arrow_points = []
        for x, y in arrow_points:
            rx = math.cos(angle) * (x - end_pos[0]) - math.sin(angle) * (y - end_pos[1]) + end_pos[0]
            ry = math.sin(angle) * (x - end_pos[0]) + math.cos(angle) * (y - end_pos[1]) + end_pos[1]
            rotated_arrow_points.append((rx, ry))

        # рисуем полигон с координатами вершин повернутой стрелки
        pygame.draw.polygon(self.surface, self.colors['border'], rotated_arrow_points)

        font = pygame.font.SysFont(self.font ,int(self.height/3))
        self.text_surface = font.render(str(self.text), True, self.colors['border'])
        self.text_point = ( 1.2*self.width/3 + self.text_surface.get_width()/2, self.height/3)
        self.surface.blit(self.text_surface, self.text_point)



        self.surface = pygame.transform.rotate(self.surface, self.angle_rotate)

        # self.screen.blit(self.surface, (self.blit_point[0], self.blit_point[1]))


