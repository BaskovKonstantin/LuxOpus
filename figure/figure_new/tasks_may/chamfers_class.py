from typing import Tuple, Dict

import pygame
from math import sin, cos, atan2, degrees, radians, sqrt


class Chamfers:

    def __init__(self, screen: pygame.Surface, colors: "Dict[str, Tuple[int,int,int]]",
                 line_length: int, line_width: int, pointer_length: int, text: str,
                 chamfer_type: int,
                 first_point: Tuple[int, int],
                 angle: int = 45,
                 triangle_part: int = 0.5,
                 second_point: Tuple[int, int] = None,
                 scale: int = 1, font: str = None, font_size: int = 16):
        self.line_length_origin = line_length
        self.pointer_length_origin = pointer_length
        self.line_width_origin = line_width
        self.scale = scale
        self.previous_scale = scale
        self.screen = screen
        self.colors = colors
        self.line_length = line_length * self.scale
        self.pointer_length = pointer_length * self.scale
        self.triangle_part = triangle_part
        self.line_width = line_width * self.scale
        self.text = text
        self.chamfer_type = chamfer_type
        self.first_point = first_point
        self.angle = angle
        self.second_point = second_point
        self.scale = scale
        self.font_name = font
        self.font_size = font_size
        self.font = pygame.font.Font(self.font_name, self.font_size * self.scale)
        # self.rendered_text = self.font.render(self.text, True, self.colors['border'])
        #
        # self.first_dot, self.line_dot, self.text_dot = self.get_main_dots()
        # self.polygon_dots = self.get_polygon_dots()
        #
        # self.offset = (abs(self.text_dot[0]), abs(self.text_dot[1]))

        self.create_surface()

    def check_click(self, mouse_pos) -> bool:

        if self.chamfer_type == 1 or self.chamfer_type == 3:
            offset_mouse = [int(mouse_pos[0] - (self.first_point[0] - self.offset[0])),
                            int(mouse_pos[1] - (self.first_point[1] - self.offset[1]))]
        elif self.chamfer_type == 2:
            offset_mouse = [int(mouse_pos[0] - (self.second_point[0] - self.offset[0])),
                            int(mouse_pos[1] - (self.second_point[1] - self.offset[1]))]

        if self.surface.get_rect().collidepoint(offset_mouse):

            if self.surface.get_at(offset_mouse) == self.colors['border']:
                print('RIGHT IN CHAMFER!')
                return True

        return False

    def draw(self):

        # rescaling

        # if self.previous_scale != self.scale:
        self.line_length = int(self.line_length_origin * self.scale)
        self.pointer_length = int(self.pointer_length_origin * self.scale)
        self.line_width = int(self.line_width_origin * self.scale)
        self.font = pygame.font.Font(self.font_name, int(self.font_size * self.scale))
        # self.create_surface()

        self.previous_scale = self.scale

        # self.rendered_text = self.font.render(self.text, True, self.colors['border'])
        #
        # self.first_dot, self.line_dot, self.text_dot = self.get_main_dots()
        # self.polygon_dots = self.get_polygon_dots()
        #
        # self.offset = (abs(self.text_dot[0]), abs(self.text_dot[1]))

        self.create_surface()

        # pygame.draw.rect(self.screen, self.colors['test'], [self.first_point[0]-self.offset[0], self.first_point[1] - self.offset[1], self.surface.get_width(), self.surface.get_height()], 1)
        self.surface.blit(self.rendered_text, (self.text_dot[0] + self.offset[0], self.text_dot[1] + self.offset[1]))

        pygame.draw.line(self.surface, self.colors['border'],
                         (self.first_dot[0]//4 + self.offset[0], self.first_dot[1]//4 + self.offset[1]),
                         (self.first_dot[0] + self.offset[0], self.first_dot[1] + self.offset[1]), self.line_width)

        pygame.draw.line(self.surface, self.colors['border'],
                         (self.first_dot[0] + self.offset[0], self.first_dot[1] + self.offset[1]),
                         (self.line_dot[0] + self.offset[0], self.line_dot[1] + self.offset[1]), self.line_width)

        pygame.draw.polygon(self.surface, self.colors['border'],
                            ((self.polygon_dots[0][0]+self.offset[0], self.polygon_dots[0][1]+self.offset[1]),
                             (self.polygon_dots[1][0]+self.offset[0], self.polygon_dots[1][1]+self.offset[1]),
                             (self.polygon_dots[2][0]+self.offset[0], self.polygon_dots[2][1]+self.offset[1])))

        if self.chamfer_type == 2:
            pygame.draw.line(self.surface, self.colors['border'],
                             (self.offset[0] - (self.second_point[0] - self.first_point[0]), self.offset[1]),
                             (self.first_dot[0] + self.offset[0], self.first_dot[1] + self.offset[1]), self.line_width)

            mid_dot = (self.first_dot[0] * self.triangle_part - (self.second_point[0] - self.first_point[0])*(1-self.triangle_part), self.first_dot[1]*self.triangle_part)
            # for dvlp
            pygame.draw.circle(self.surface, self.colors['test'], (self.offset[0] - (self.second_point[0] - self.first_point[0]), self.offset[1]), 5)
            left_dot = (mid_dot[0] - self.pointer_length // 4 * self.triangle_part * cos(radians(self.angle)),
                        mid_dot[1] - self.pointer_length // 4 * self.triangle_part * sin(radians(self.angle)))
            right_dot = (mid_dot[0] + self.pointer_length // 4 * self.triangle_part * cos(radians(self.angle)),
                         mid_dot[1] + self.pointer_length // 4 * self.triangle_part * sin(radians(self.angle)))

            pygame.draw.polygon(self.surface, self.colors['border'],
                                ((left_dot[0] + self.offset[0], left_dot[1] + self.offset[1]),
                                (right_dot[0] + self.offset[0], right_dot[1] + self.offset[1]),
                                (self.offset[0] - (self.second_point[0] - self.first_point[0]), self.offset[1])))
            if self.second_point[0] > self.first_point[0]:
                self.blit_point = (self.second_point[0] - self.offset[0], self.second_point[1] - self.offset[1])
                self.screen.blit(self.surface, self.blit_point)
            else:
                self.blit_point = (self.first_point[0] - self.offset[0], self.first_point[1] - self.offset[1])
                self.screen.blit(self.surface, self.blit_point)

        elif self.chamfer_type == 1 or self.chamfer_type == 3:
            self.blit_point = (self.first_point[0] - self.offset[0], self.first_point[1] - self.offset[1])
            self.screen.blit(self.surface, self.blit_point)

    def get_surface_size(self):

        if self.chamfer_type == 1:
            width = self.line_length
            height = self.rendered_text.get_height() + self.line_width + cos(
                radians(self.angle)) * self.pointer_length + 10

        elif self.chamfer_type == 2 or self.chamfer_type == 3:
            width = self.line_length + sin(radians((90 - self.angle))) * self.pointer_length + 10
            height = self.rendered_text.get_height() + self.line_width + cos(
                radians(self.angle)) * self.pointer_length + 10

        return (width, height)

    def get_main_dots(self):

        if self.chamfer_type == 1:
            first_dot = (
            sin(radians(self.angle)) * self.pointer_length, -cos(radians(self.angle)) * self.pointer_length)
        elif self.chamfer_type == 3:
            first_dot = (
            -sin(radians(self.angle)) * self.pointer_length, -cos(radians(self.angle)) * self.pointer_length)
        elif self.chamfer_type == 2:
            temp = (self.second_point[0] - self.first_point[0]) // 2
            first_dot = (-temp, -sqrt(self.pointer_length ** 2 - temp ** 2))

        line_dot = (first_dot[0] - self.line_length, first_dot[1])

        text_dot = (line_dot[0], line_dot[1] - self.rendered_text.get_height() - self.line_width)

        return first_dot, line_dot, text_dot

    def create_surface(self):

        self.rendered_text = self.font.render(self.text, True, self.colors['border'])

        self.first_dot, self.line_dot, self.text_dot = self.get_main_dots()
        self.polygon_dots = self.get_polygon_dots()
        if self.second_point is not None:
            if (self.second_point[0] - self.first_point[0]) > abs(self.text_dot[0]):
                self.offset = (self.second_point[0] - self.first_point[0], abs(self.text_dot[1]))
            else:
                self.offset = (abs(self.text_dot[0]), abs(self.text_dot[1]))
        else:
            self.offset = (abs(self.text_dot[0]), abs(self.text_dot[1]))

        if self.chamfer_type == 2 or self.chamfer_type == 3:
            #print(abs(self.text_dot[0]))
            #print((self.second_point[0] - self.first_point[0]))
            if self.second_point is not None:
                if (self.second_point[0] - self.first_point[0]) > abs(self.text_dot[0]):
                    self.surface = pygame.Surface((self.second_point[0] - self.first_point[0], abs(self.text_dot[1])))
                else:
                    self.surface = pygame.Surface((abs(self.text_dot[0]), abs(self.text_dot[1])))
            else:
                self.surface = pygame.Surface((abs(self.text_dot[0]), abs(self.text_dot[1])))

        elif self.chamfer_type == 1:
            self.surface = pygame.Surface((abs(self.text_dot[0]) + self.first_dot[0], abs(self.text_dot[1])))
            # print(surface.get_rect())

        #return surface

    def get_polygon_dots(self):

        if self.chamfer_type == 3 or self.chamfer_type == 2:
            mid_dot = (self.first_dot[0] * self.triangle_part, self.first_dot[1] * self.triangle_part)
            left_dot = (mid_dot[0] - self.pointer_length // 4 * self.triangle_part * cos(radians(self.angle)),
                        mid_dot[1] + self.pointer_length // 4 * self.triangle_part * sin(radians(self.angle)))
            right_dot = (mid_dot[0] + self.pointer_length // 4 * self.triangle_part * cos(radians(self.angle)),
                         mid_dot[1] - self.pointer_length // 4 * self.triangle_part * sin(radians(self.angle)))

        if self.chamfer_type == 1:
            mid_dot = (self.first_dot[0] * self.triangle_part, self.first_dot[1] * self.triangle_part)
            left_dot = (mid_dot[0] - self.pointer_length // 4 * self.triangle_part * cos(radians(self.angle)),
                        mid_dot[1] - self.pointer_length // 4 * self.triangle_part * sin(radians(self.angle)))
            right_dot = (mid_dot[0] + self.pointer_length // 4 * self.triangle_part * cos(radians(self.angle)),
                         mid_dot[1] + self.pointer_length // 4 * self.triangle_part * sin(radians(self.angle)))

        return ((0,0), left_dot, right_dot)
