from typing import Tuple, Dict

import pygame
import math


class Radius:
    def __init__(self,
                 screen: pygame.Surface,
                 blit_point: Tuple[int, int],
                 colors: Dict[str, Tuple[int, int, int]],
                 surface_radius: int,
                 radius_length: int,
                 radius_width: int,
                 triangle_width: int,
                 triangle_length: int,
                 angle: int,
                 text: str,
                 radius_type: int,
                 limit: Tuple[int, int] = None,
                 font: str = 'arial.ttf',
                 font_size: int = 16,
                 scale: int = 1):

        self.end_pos = (0, 0)
        self.start_pos = (0, 0)
        self.scale = scale
        self.radius_type = radius_type
        self.screen = screen
        self.blit_point = blit_point
        self.colors = colors
        self.surface_radius = surface_radius * self.scale
        self.radius_length = radius_length * self.scale
        self.radius_width = radius_width * self.scale
        self.angle = angle
        self.limit = limit
        self.triangle_length = self.radius_length * 1 / 4
        self.line_length = self.surface_radius * 0.95
        self.font = pygame.font.Font(font, font_size)
        self.radius_text = self.font.render(text, True, self.colors['text'])

        # creating new surface
        if self.radius_type == 1:
            self.surface = pygame.Surface((self.surface_radius * 2, self.surface_radius * 2),
                                          pygame.SRCALPHA)
            self.surface_center = [self.surface_radius, self.surface_radius]

        elif self.radius_type == 0:
            self.surface = pygame.Surface((self.surface_radius * 4, self.surface_radius * 4),
                                          pygame.SRCALPHA)
            self.surface_center = [self.surface_radius * 2, self.surface_radius * 2]

    def check_click(self, mouse_pos):

        offset_mouse = [mouse_pos[0] - self.blit_point[0],
                        mouse_pos[1] - self.blit_point[1]]

        if self.surface.get_rect().collidepoint(offset_mouse):

            if self.surface.get_at(offset_mouse) == (255, 255, 255):

                return True

        return False

    def draw(self):
        # filling with black
        self.surface.fill(self.colors['transparent'])

        # drawing circle (only for development)
        # pygame.draw.circle(self.surface, self.colors['border'], self.surface_center, self.surface_radius, 1)
        #
        # drawing pointer
        # drawing line
        self.get_line_points()
        pygame.draw.line(self.surface, self.colors['border'], self.start_pos, self.end_pos, width=self.radius_width)

        if self.radius_type == 1:
            pygame.draw.circle(self.surface, self.colors['transparent'], self.surface_center,
                               (self.surface_radius - self.radius_length))
        elif self.radius_type == 0:
            pygame.draw.circle(self.surface, self.colors['transparent'], self.surface_center,
                               self.surface_radius * 2 + 10, (self.surface_radius - self.radius_length + 10))

        # drawing triangle
        pygame.draw.polygon(self.surface, self.colors['border'], self.triangle_points())

        # draw text
        if 90 < self.formatted_angle(self.angle) < 270:
            text_angle = self.angle + 180
        else:
            text_angle = self.angle

        t_height = self.radius_text.get_rect().height

        text = pygame.transform.rotate(self.radius_text, text_angle)

        text_rect = text.get_rect()

        if self.radius_type == 1:
            offset_pos_x = self.surface_center[0] + (self.surface_radius - self.radius_length) * math.cos(
                math.radians(self.angle))
            offset_pos_y = self.surface_center[1] - (self.surface_radius - self.radius_length) * math.sin(
                math.radians(self.angle))

        elif self.radius_type == 0:
            offset_pos_x = self.surface_center[0] + (self.surface_radius + self.radius_length) * math.cos(
                math.radians(self.angle))
            offset_pos_y = self.surface_center[1] - (self.surface_radius + self.radius_length) * math.sin(
                math.radians(self.angle))

        if 90 <= self.formatted_angle(self.angle) < 180 or 270 <= self.formatted_angle(self.angle) < 360:
            text_pos = ((offset_pos_x + self.end_pos[0]) / 2 - text_rect.width / 2 + 10,
                        (offset_pos_y + self.end_pos[1]) / 2 - text_rect.height / 2 - 10)
        if 0 <= self.formatted_angle(self.angle) < 90 or 180 <= self.formatted_angle(self.angle) < 270:
            text_pos = ((offset_pos_x + self.end_pos[0]) / 2 - text_rect.width/2 - 10,
                        (offset_pos_y + self.end_pos[1]) / 2 - text_rect.height/2 - 10)

        self.surface.blit(text, text_pos)
        # pygame.draw.rect(self.surface,self.colors['border'],(text_pos[0], text_pos[1], text_rect.width, text_rect.height ), 1)
        # blit our surface on screen
        self.screen.blit(self.surface, self.blit_point)

    def move_angle(self, mouse_pos):

        # recalculate angle based on mouse pos
        x_diff = mouse_pos[0] - (self.blit_point[0] + self.surface_center[0])
        y_diff = mouse_pos[1] - (self.blit_point[1] + self.surface_center[1])
        angle = math.degrees(math.atan2(x_diff, y_diff)) - 90
        if self.limit is not None:
            if self.limit[0] < self.formatted_angle(angle) < self.limit[1]:
                self.angle = angle
        else:
            self.angle = angle

    def get_line_points(self):

        if self.radius_type == 1:

            # getting the end pos of pointer
            end_x = self.surface_center[0] + self.line_length * math.cos(math.radians(self.angle))
            end_y = self.surface_center[1] - self.line_length * math.sin(math.radians(self.angle))

            # changing start pos so the line will not start from the center
            start_x = self.surface_center[0]
            start_y = self.surface_center[1]

        elif self.radius_type == 0:

            # changing start pos so the line will not start from the center
            start_x = self.surface_center[0] + self.surface_radius * 2 * math.cos(math.radians(self.angle))
            start_y = self.surface_center[1] - self.surface_radius * 2 * math.sin(math.radians(self.angle))

            # getting the end pos of pointer
            end_x = self.surface_center[0] + (self.surface_radius * 2 - self.line_length) * math.cos(
                math.radians(self.angle))
            end_y = self.surface_center[1] - (self.surface_radius * 2 - self.line_length) * math.sin(
                math.radians(self.angle))

        self.end_pos = (end_x, end_y)
        self.start_pos = (start_x, start_y)

    def triangle_points(self):

        if self.radius_type == 1:

            end_point_x = self.surface_center[0] + self.surface_radius * math.cos(math.radians(self.angle))
            end_point_y = self.surface_center[1] - self.surface_radius * math.sin(math.radians(self.angle))
            first_point_x = end_point_x + self.triangle_length * math.cos(math.radians(self.angle + 160))
            first_point_y = end_point_y - self.triangle_length * math.sin(math.radians(self.angle + 160))
            second_point_x = end_point_x + self.triangle_length * math.cos(math.radians(self.angle + 200))
            second_point_y = end_point_y - self.triangle_length * math.sin(math.radians(self.angle + 200))

        elif self.radius_type == 0:

            end_point_x = self.surface_center[0] + self.surface_radius * math.cos(math.radians(self.angle))
            end_point_y = self.surface_center[1] - self.surface_radius * math.sin(math.radians(self.angle))
            first_point_x = end_point_x - self.triangle_length * math.cos(math.radians(self.angle + 160))
            first_point_y = end_point_y + self.triangle_length * math.sin(math.radians(self.angle + 160))
            second_point_x = end_point_x - self.triangle_length * math.cos(math.radians(self.angle + 200))
            second_point_y = end_point_y + self.triangle_length * math.sin(math.radians(self.angle + 200))

        return [(first_point_x, first_point_y),
                (end_point_x, end_point_y),
                (second_point_x, second_point_y)]

    def formatted_angle(self, angle):
        if angle < 0:
            angle = angle + 360
        return angle
