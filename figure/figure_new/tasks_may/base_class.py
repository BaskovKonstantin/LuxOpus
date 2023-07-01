import math
from typing import Tuple, Dict

import pygame

class Base:
    def __init__(self,
                 screen: pygame.Surface,
                 blit_point: Tuple[int, int],
                 colors: Dict[str, Tuple[int, int, int]],
                 surface_radius: int,
                 triangle_width: int,
                 triangle_length: int,
                 square_size: Tuple[int, int],
                 angle: int,
                 text: str,
                 base_type: int,
                 limit: Tuple[int, int] = None,
                 font: str = None,
                 font_size: int = 16,
                 scale: int = 1):
        self.surface_radius_origin = surface_radius
        self.square_size_origin = square_size
        self.triangle_width_origin = triangle_width
        self.triangle_length_origin = triangle_length
        self.start_angle = angle
        self.moved_once = False
        self.previous_scale = scale
        self.scale = scale
        self.screen = screen
        self.blit_point = blit_point
        self.colors = colors
        self.surface_radius = surface_radius * self.scale
        self.triangle_width = triangle_width * self.scale
        self.triangle_length = triangle_length * self.scale
        self.square_size = (square_size[0] * self.scale, square_size[1] * self.scale)
        self.angle = angle
        self.text = text
        self.base_type = base_type
        self.limit = limit
        self.font_name = font
        self.font_size = font_size * self.scale
        self.font = pygame.font.Font(self.font_name, self.font_size)
        self.square_text = self.font.render(self.text, True, self.colors['text'])

        self.create_surface()

    def create_surface(self):
        if self.base_type == 1:
            self.surface = pygame.Surface((self.surface_radius * 2, self.surface_radius * 2),
                                          pygame.SRCALPHA)
            self.surface_center = [self.surface_radius, self.surface_radius]

        elif self.base_type == 0:
            self.surface = pygame.Surface(((self.surface_radius+self.triangle_length+self.square_size[0]*2) * 2,
                                           (self.surface_radius+self.triangle_length+self.square_size[0]*2) * 2),
                                          pygame.SRCALPHA)
            self.surface_center = [self.surface_radius+self.triangle_length+self.square_size[0]*2,
                                   self.surface_radius+self.triangle_length+self.square_size[0]*2]

    def draw(self):

        # rescaling

        if self.scale != self.previous_scale:

            self.surface_radius = int(self.surface_radius_origin * self.scale)
            self.square_size = (int(self.square_size_origin[0] * self.scale), int(self.square_size_origin[1]*self.scale))
            self.triangle_width = int(self.triangle_width_origin * self.scale)
            self.triangle_length = int(self.triangle_length_origin * self.scale)
            self.font = pygame.font.Font(self.font_name, int(self.font_size * self.scale))
            self.square_text = self.font.render(self.text, True, self.colors['text'])

            self.create_surface()

            self.previous_scale = self.scale
        # filling with black
        self.surface.fill(self.colors['transparent'])

        # drawing circle (only for development)
        # pygame.draw.circle(self.surface, self.colors['test'], self.surface_center, self.surface_radius, 1)

        # kostb1l
        if not self.moved_once:
            self.angle = self.start_angle

        if self.limit is not None:
            if self.formatted_angle(self.limit[0]) > self.formatted_angle(self.limit[1]):
                if self.formatted_angle(self.limit[1]) < self.formatted_angle(self.angle) < self.formatted_angle(self.limit[0]):
                    if abs(self.formatted_angle(self.angle) - self.formatted_angle(self.limit[1])) < abs(self.formatted_angle(self.angle)-self.formatted_angle(self.limit[0])):
                        self.angle = self.limit[1]
                    else:
                        self.angle = self.limit[0]
            elif self.formatted_angle(self.limit[0]) < self.formatted_angle(self.limit[1]):
                if self.formatted_angle(self.limit[1]) < self.formatted_angle(self.angle) or self.formatted_angle(self.angle) < self.formatted_angle(self.limit[0]):
                    if abs(self.formatted_angle(self.angle) - self.formatted_angle(self.limit[1])) < abs(self.formatted_angle(self.angle)-self.formatted_angle(self.limit[0])):
                        self.angle = self.limit[1]
                    else:
                        self.angle = self.limit[0]

        # triangle
        pygame.draw.polygon(self.surface, self.colors['border'], self.triangle_points())

        # line
        line_points = self.line_points()
        pygame.draw.line(self.surface, self.colors['border'], line_points[0], line_points[1], 1)

        rect = self.square_points()
        # square
        pygame.draw.rect(self.surface, self.colors['border'], rect, 1)

        # text
        self.square_text = self.font.render(self.text, True, self.colors['text'])
        i = 1
        while self.square_text.get_height() > self.square_size[1]*4/5 or self.square_text.get_width() > self.square_size[0]*4/5:
            self.font = pygame.font.Font(self.font_name, int(self.font_size-i * self.scale))
            self.square_text = self.font.render(self.text, True, self.colors['text'])
            i += 1
        i = 1
        while self.square_text.get_height() < self.square_size[1]*3/5 or self.square_text.get_width() > self.square_size[0]*3/5:
            self.font = pygame.font.Font(self.font_name, int(self.font_size+i * self.scale))
            self.square_text = self.font.render(self.text, True, self.colors['text'])
            i += 1
        self.surface.blit(self.square_text, (rect[0]+(self.square_size[0]-self.square_text.get_width())/2,
                                             rect[1]+(self.square_size[1]-self.square_text.get_height())/2))
        self.screen.blit(self.surface, self.blit_point)

    def check_click(self, mouse_pos):

        offset_mouse = [int(mouse_pos[0]),
                        int(mouse_pos[1])]

        if self.surface.get_rect().collidepoint(offset_mouse):
            if self.base_type == 1:
                end_point = (self.surface_center[0] + self.surface_radius * math.cos(math.radians(self.angle)),
                             self.surface_center[1] - self.surface_radius * math.sin(math.radians(self.angle)))
                start_point = (self.surface_center[0] + (self.surface_radius-self.triangle_length-self.square_size[0]*2.4) * math.cos(math.radians(self.angle)),
                               self.surface_center[1] - (self.surface_radius-self.triangle_length-self.square_size[0]*2.4) * math.sin(math.radians(self.angle)))
                pygame.draw.circle(self.surface, self.colors['test'], end_point, 5)
                pygame.draw.circle(self.surface, self.colors['test'], start_point, 5)
            elif self.base_type == 0:
                start_point = (self.surface_center[0] + self.surface_radius * math.cos(math.radians(self.angle)),
                               self.surface_center[1] - self.surface_radius * math.sin(math.radians(self.angle)))
                end_point = (self.surface_center[0] + (self.surface_radius+self.triangle_length+self.square_size[0]*2.4) * math.cos(math.radians(self.angle)),
                             self.surface_center[1] - (self.surface_radius+self.triangle_length+self.square_size[0]*2.4) * math.sin(math.radians(self.angle)))
                # pygame.draw.circle(self.surface, self.colors['test'], end_point, 5)
                # pygame.draw.circle(self.surface, self.colors['test'], start_point, 5)
            if end_point[0] - self.square_size[0] < offset_mouse[0] < start_point[0] + self.square_size[0] and \
                    end_point[1] - self.square_size[0] < offset_mouse[1] < start_point[1] + self.square_size[0]:
                print('Base click works fine')
                self.last_mouse_pos = offset_mouse
                return True
            if end_point[0] - self.square_size[0] < offset_mouse[0] < start_point[0] + self.square_size[0] and \
                    start_point[1] - self.square_size[0] < offset_mouse[1] < end_point[1] + self.square_size[0]:
                print('Base click works fine')
                self.last_mouse_pos = offset_mouse
                return True
            if start_point[0] - self.square_size[0] < offset_mouse[0] < end_point[0] + self.square_size[0] and \
                    end_point[1] - self.square_size[0] < offset_mouse[1] < start_point[1] + self.square_size[0]:
                print('Base click works fine')
                self.last_mouse_pos = offset_mouse
                return True
            if start_point[0] - self.square_size[0] < offset_mouse[0] < end_point[0] + self.square_size[0] and \
                    start_point[1] - self.square_size[0] < offset_mouse[1] < end_point[1] + self.square_size[0]:
                print('Base click works fine')
                self.last_mouse_pos = offset_mouse
                return True

        return False

    def move_angle(self, pos_change: Tuple[int, int]):
        self.moved_once = True
        mouse_pos = (self.last_mouse_pos[0] - pos_change[0], self.last_mouse_pos[1] - pos_change[1])
        # recalculate angle based on mouse pos
        x_diff = mouse_pos[0] - self.surface_center[0]
        y_diff = mouse_pos[1] - self.surface_center[1]
        angle = math.degrees(math.atan2(x_diff, y_diff)) - 90
        if self.limit is not None:
            if self.formatted_angle(self.limit[1]) < self.formatted_angle(self.limit[0]):
                if (0 <= self.formatted_angle(angle) <= self.formatted_angle(self.limit[1])) or (self.formatted_angle(self.limit[0]) <= self.formatted_angle(angle) <= 360):
                    self.angle = angle
            else:
                if self.formatted_angle(angle) < self.formatted_angle(self.limit[0]):
                    self.angle = self.limit[0]
                elif self.formatted_angle(angle) > self.formatted_angle(self.limit[1]):
                    self.angle = self.limit[1]
                elif self.formatted_angle(self.limit[0]) <= self.formatted_angle(angle) <= self.formatted_angle(self.limit[1]):
                    self.angle = angle
        else:
            self.angle = angle

    def line_points(self):

        if self.base_type == 1:
            line_second_point_x = self.triangle_points()[1][0] - self.square_size[0] * math.cos(math.radians(self.angle))
            line_second_point_y = self.triangle_points()[1][1] + self.square_size[0] * math.sin(math.radians(self.angle))
            line_first_point_x = self.triangle_points()[1][0] + self.square_size[0] / 5 * math.cos(math.radians(self.angle))
            line_first_point_y = self.triangle_points()[1][1] - self.square_size[0] / 5 * math.sin(math.radians(self.angle))

        elif self.base_type == 0:
            line_second_point_x = self.triangle_points()[1][0] + self.square_size[0] * math.cos(math.radians(self.angle))
            line_second_point_y = self.triangle_points()[1][1] - self.square_size[0] * math.sin(math.radians(self.angle))
            line_first_point_x = self.triangle_points()[1][0] - self.square_size[0] / 5 * math.cos(math.radians(self.angle))
            line_first_point_y = self.triangle_points()[1][1] + self.square_size[0] / 5 * math.sin(math.radians(self.angle))

        return ((line_first_point_x, line_first_point_y),
                (line_second_point_x, line_second_point_y))

    def triangle_points(self):

        if self.base_type == 1:

            end_point_x = self.surface_center[0] + (self.surface_radius-self.triangle_length) * math.cos(math.radians(self.angle))
            end_point_y = self.surface_center[1] - (self.surface_radius-self.triangle_length) * math.sin(math.radians(self.angle))
            xH = end_point_x + (self.triangle_length * math.cos(math.radians(self.angle)))
            yH = end_point_y - (self.triangle_length * math.sin(math.radians(self.angle)))
            first_point_x = xH - (self.triangle_width / 2) * math.cos(math.radians(self.angle + 90))
            first_point_y = yH + (self.triangle_width / 2) * math.sin(math.radians(self.angle + 90))
            second_point_x = xH + (self.triangle_width / 2) * math.cos(math.radians(self.angle + 90))
            second_point_y = yH - (self.triangle_width / 2) * math.sin(math.radians(self.angle + 90))

        elif self.base_type == 0:

            end_point_x = self.surface_center[0] + (self.surface_radius+self.triangle_length) * math.cos(math.radians(self.angle))
            end_point_y = self.surface_center[1] - (self.surface_radius+self.triangle_length) * math.sin(math.radians(self.angle))
            xH = end_point_x - (self.triangle_length * math.cos(math.radians(self.angle)))
            yH = end_point_y + (self.triangle_length * math.sin(math.radians(self.angle)))
            first_point_x = xH + (self.triangle_width / 2) * math.cos(math.radians(self.angle + 90))
            first_point_y = yH - (self.triangle_width / 2) * math.sin(math.radians(self.angle + 90))
            second_point_x = xH - (self.triangle_width / 2) * math.cos(math.radians(self.angle + 90))
            second_point_y = yH + (self.triangle_width / 2) * math.sin(math.radians(self.angle + 90))

        return [(first_point_x, first_point_y),
                (end_point_x, end_point_y),
                (second_point_x, second_point_y)]

    def square_points(self):

        if self.base_type == 1:
            if 0 <= self.formatted_angle(self.angle) <= 90:
                right_top_x = self.line_points()[1][0]
                right_top_y = self.line_points()[1][1]
                left_top_x = right_top_x - self.square_size[0]
                left_top_y = right_top_y
            if 90 <= self.formatted_angle(self.angle) <= 180:
                left_top_x = self.line_points()[1][0]
                left_top_y = self.line_points()[1][1]
            if 180 <= self.formatted_angle(self.angle) <= 270:
                left_bottom_x = self.line_points()[1][0]
                left_bottom_y = self.line_points()[1][1]
                left_top_x = left_bottom_x
                left_top_y = left_bottom_y - self.square_size[1]
            if 270 <= self.formatted_angle(self.angle) <= 360:
                right_bottom_x = self.line_points()[1][0]
                right_bottom_y = self.line_points()[1][1]
                left_top_x = right_bottom_x - self.square_size[0]
                left_top_y = right_bottom_y - self.square_size[1]

        elif self.base_type == 0:
            if 0 <= self.formatted_angle(self.angle) <= 90:
                left_bottom_x = self.line_points()[1][0]
                left_bottom_y = self.line_points()[1][1]
                left_top_x = left_bottom_x
                left_top_y = left_bottom_y - self.square_size[1]
            elif 90 <= self.formatted_angle(self.angle) <= 180:
                right_bottom_x = self.line_points()[1][0]
                right_bottom_y = self.line_points()[1][1]
                left_top_x = right_bottom_x - self.square_size[0]
                left_top_y = right_bottom_y - self.square_size[1]
            elif 180 <= self.formatted_angle(self.angle) <= 270:
                right_top_x = self.line_points()[1][0]
                right_top_y = self.line_points()[1][1]
                left_top_x = right_top_x - self.square_size[0]
                left_top_y = right_top_y
            elif 270 <= self.formatted_angle(self.angle) <= 360:
                left_top_x = self.line_points()[1][0]
                left_top_y = self.line_points()[1][1]

        return (left_top_x, left_top_y, self.square_size[0], self.square_size[1])

    def formatted_angle(self, angle):
        if angle < 0:
            angle = angle + 360
        return angle