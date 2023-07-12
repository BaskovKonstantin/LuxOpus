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
                 font: str = None,
                 font_size: int = 16,
                 scale: int = 1):

        self.surface_radius_origin = surface_radius
        self.radius_length_origin = radius_length
        self.radius_width_origin = radius_width
        self.triangle_width_origin = triangle_width
        self.triangle_length_origin = triangle_length
        self.end_pos = (0, 0)
        self.start_pos = (0, 0)
        self.scale = scale
        self.previous_scale = scale
        self.radius_type = radius_type
        self.screen = screen
        self.blit_point = blit_point
        self.colors = colors
        self.surface_radius = surface_radius * self.scale
        self.radius_length = radius_length * self.scale
        self.radius_width = radius_width * self.scale
        self.start_angle = angle
        self.moved_once = False
        self.angle = angle
        self.limit = limit
        self.last_mouse_pos = (0, 0)
        # self.triangle_length = self.radius_length * 1 / 4
        self.triangle_width = triangle_width * self.scale
        self.triangle_length = triangle_length * self.scale
        self.line_length = self.surface_radius - self.triangle_length/2
        self.font_size = font_size * self.scale
        self.font_name = font
        self.font = pygame.font.Font(self.font_name, self.font_size)
        self.text = text
        self.radius_text = self.font.render(text, True, self.colors['text'])

        self.create_surface()
        # creating new surface

    def create_surface(self):
        if self.radius_type == 1:
            self.surface = pygame.Surface((self.surface_radius * 2, self.surface_radius * 2),
                                          pygame.SRCALPHA)
            self.surface_center = [self.surface_radius, self.surface_radius]

        elif self.radius_type == 0:
            self.surface = pygame.Surface((self.surface_radius * 4, self.surface_radius * 4),
                                          pygame.SRCALPHA)
            self.surface_center = [self.surface_radius * 2, self.surface_radius * 2]

    def check_click(self, mouse_pos):

        offset_mouse = [int(mouse_pos[0]),
                        int(mouse_pos[1])]

        if self.surface.get_rect().collidepoint(offset_mouse):
            if self.radius_type == 1:
                end_point = self.triangle_points()[1]
                start_point = (
                    self.surface_center[0] - (self.surface_radius - self.radius_length) * math.sin(
                        math.radians(self.angle - 90)),
                    self.surface_center[1] - (self.surface_radius - self.radius_length) * math.cos(
                        math.radians(self.angle - 90)))
                # pygame.draw.circle(self.surface, self.colors['test'], end_point, 5)
                # pygame.draw.circle(self.surface, self.colors['test'], start_point, 5)
            elif self.radius_type == 0:
                start_point = self.triangle_points()[1]
                end_point = (self.surface_center[0] - (self.surface_radius + self.radius_length) * math.sin(
                    math.radians(self.angle - 90)),
                             self.surface_center[1] - (self.surface_radius + self.radius_length) * math.cos(
                                 math.radians(self.angle - 90)))
                # pygame.draw.circle(self.surface, self.colors['test'], end_point, 5)
                # pygame.draw.circle(self.surface, self.colors['test'], start_point, 5)
            if end_point[0] - self.triangle_width / 2 < offset_mouse[0] < start_point[0] + self.triangle_width / 2 and \
                    end_point[1] - self.triangle_width / 2 < offset_mouse[1] < start_point[1] + self.triangle_width / 2:
                print('Radius click works fine')
                self.last_mouse_pos = offset_mouse
                return True
            if end_point[0] - self.triangle_width / 2 < offset_mouse[0] < start_point[0] + self.triangle_width / 2 and \
                    start_point[1] - self.triangle_width / 2 < offset_mouse[1] < end_point[1] + self.triangle_width / 2:
                print('Radius click works fine')
                self.last_mouse_pos = offset_mouse
                return True
            if start_point[0] - self.triangle_width / 2 < offset_mouse[0] < end_point[0] + self.triangle_width / 2 and \
                    end_point[1] - self.triangle_width / 2 < offset_mouse[1] < start_point[1] + self.triangle_width / 2:
                print('Radius click works fine')
                self.last_mouse_pos = offset_mouse
                return True
            if start_point[0] - self.triangle_width / 2 < offset_mouse[0] < end_point[0] + self.triangle_width / 2 and \
                    start_point[1] - self.triangle_width / 2 < offset_mouse[1] < end_point[1] + self.triangle_width / 2:
                print('Radius click works fine')
                self.last_mouse_pos = offset_mouse
                return True

        return False

    def draw(self):

        # rescaling

        if self.scale != self.previous_scale:

            self.surface_radius = int(self.surface_radius_origin * self.scale)
            self.radius_length = int(self.radius_length_origin * self.scale)
            self.radius_width = int(self.radius_width_origin * self.scale)
            if self.radius_width < 1:
                self.radius_width = 1
            self.triangle_width = int(self.triangle_width_origin * self.scale)
            self.triangle_length = int(self.triangle_length_origin * self.scale)
            self.line_length = int(self.surface_radius - self.triangle_length/2)
            self.font = pygame.font.Font(self.font_name, int(self.font_size * self.scale))
            self.radius_text = self.font.render(self.text, True, self.colors['text'])

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

        # drawing pointer
        # drawing line
        self.get_line_points()
        pygame.draw.line(self.surface, self.colors['border'], self.start_pos, self.end_pos, width=self.radius_width)

        if self.radius_type == 1:
            pygame.draw.circle(self.surface, self.colors['transparent'], self.surface_center,
                               (self.surface_radius - self.radius_length))
        elif self.radius_type == 0:
            pygame.draw.circle(self.surface, self.colors['transparent'], self.surface_center,
                               self.surface_radius * 2 + 10, int(self.surface_radius - self.radius_length + 10))

        # drawing triangle
        pygame.draw.polygon(self.surface, self.colors['border'], self.triangle_points())

        # draw text
        if 90 < self.formatted_angle(self.angle) < 270:
            text_angle = self.angle + 180
        else:
            text_angle = self.angle
        t_height = self.radius_text.get_rect().height
        t_width = self.radius_text.get_rect().width
        text = pygame.transform.rotate(self.radius_text, text_angle)
        x_text = 0
        y_text = 0
        x_offset = 0
        y_offset = 0
        if self.radius_type == 0:
            center_text = self.surface_radius + self.radius_length / 2 + self.triangle_length / 2
            if 90 < self.formatted_angle(self.angle) <= 180:
                x_text = self.surface_center[0] - center_text * math.sin(
                    math.radians(self.angle - 90)) + self.radius_width / 2 * math.cos(math.radians(self.angle - 90))
                y_text = self.surface_center[1] - center_text * math.cos(
                    math.radians(self.angle - 90)) - self.radius_width / 2 * math.sin(math.radians(self.angle - 90))
                x_offset = t_width / 2 * math.sin(math.radians(self.angle - 90))
                y_offset = t_width / 2 * math.cos(math.radians(self.angle - 90)) + t_height * math.sin(
                    math.radians(self.angle - 90))
            elif 180 < self.formatted_angle(self.angle) <= 270:
                x_text = self.surface_center[0] - center_text * math.cos(
                    math.radians(self.angle - 180)) - self.radius_width / 2 * math.sin(math.radians(self.angle - 180))
                y_text = self.surface_center[1] + center_text * math.sin(
                    math.radians(self.angle - 180)) - self.radius_width / 2 * math.cos(math.radians(self.angle - 180))
                x_offset = t_height * math.sin(math.radians(self.angle - 180)) + t_width / 2 * math.cos(
                    math.radians(self.angle - 180))
                y_offset = t_height * math.cos(math.radians(self.angle - 180)) + t_width / 2 * math.sin(
                    math.radians(self.angle - 180))
            elif 0 <= self.formatted_angle(self.angle) <= 90:
                x_text = self.surface_center[0] + center_text * math.cos(
                    math.radians(self.angle)) - self.radius_width / 2 * math.sin(math.radians(self.angle))
                y_text = self.surface_center[1] - center_text * math.sin(
                    math.radians(self.angle)) - self.radius_width / 2 * math.cos(math.radians(self.angle))
                x_offset = t_height * math.sin(math.radians(self.angle)) + t_width / 2 * math.cos(
                    math.radians(self.angle))
                y_offset = t_height * math.cos(math.radians(self.angle)) + t_width / 2 * math.sin(
                    math.radians(self.angle))
            elif 270 < self.formatted_angle(self.angle) <= 360:
                x_text = self.surface_center[0] + center_text * math.sin(
                    math.radians(self.angle - 270)) + self.radius_width / 2 * math.cos(math.radians(self.angle - 270))
                y_text = self.surface_center[1] + center_text * math.cos(
                    math.radians(self.angle - 270)) - self.radius_width / 2 * math.sin(math.radians(self.angle - 270))
                x_offset = t_width / 2 * math.sin(math.radians(self.angle - 270))
                y_offset = t_width / 2 * math.cos(math.radians(self.angle - 270)) + t_height * math.sin(
                    math.radians(self.angle - 270))
        elif self.radius_type == 1:
            center_text = self.surface_radius - self.radius_length / 2 - self.triangle_length / 2
            if 90 < self.formatted_angle(self.angle) <= 180:
                x_text = self.surface_center[0] - center_text * math.sin(
                    math.radians(self.angle - 90)) + self.radius_width / 2 * math.cos(math.radians(self.angle - 90))
                y_text = self.surface_center[1] - center_text * math.cos(
                    math.radians(self.angle - 90)) - self.radius_width / 2 * math.sin(math.radians(self.angle - 90))
                x_offset = t_width / 2 * math.sin(math.radians(self.angle - 90))
                y_offset = t_width / 2 * math.cos(math.radians(self.angle - 90)) + t_height * math.sin(
                    math.radians(self.angle - 90))
            elif 180 < self.formatted_angle(self.angle) <= 270:
                x_text = self.surface_center[0] - center_text * math.cos(
                    math.radians(self.angle - 180)) - self.radius_width / 2 * math.sin(math.radians(self.angle - 180))
                y_text = self.surface_center[1] + center_text * math.sin(
                    math.radians(self.angle - 180)) - self.radius_width / 2 * math.cos(math.radians(self.angle - 180))
                x_offset = t_height * math.sin(math.radians(self.angle - 180)) + t_width / 2 * math.cos(
                    math.radians(self.angle - 180))
                y_offset = t_height * math.cos(math.radians(self.angle - 180)) + t_width / 2 * math.sin(
                    math.radians(self.angle - 180))
            elif 0 <= self.formatted_angle(self.angle) <= 90:
                x_text = self.surface_center[0] + center_text * math.cos(
                    math.radians(self.angle)) - self.radius_width / 2 * math.sin(math.radians(self.angle))
                y_text = self.surface_center[1] - center_text * math.sin(
                    math.radians(self.angle)) - self.radius_width / 2 * math.cos(math.radians(self.angle))
                x_offset = t_height * math.sin(math.radians(self.angle)) + t_width / 2 * math.cos(
                    math.radians(self.angle))
                y_offset = t_height * math.cos(math.radians(self.angle)) + t_width / 2 * math.sin(
                    math.radians(self.angle))
            elif 270 < self.formatted_angle(self.angle) < 360:
                x_text = self.surface_center[0] + center_text * math.sin(
                    math.radians(self.angle - 270)) + self.radius_width / 2 * math.cos(math.radians(self.angle - 270))
                y_text = self.surface_center[1] + center_text * math.cos(
                    math.radians(self.angle - 270)) - self.radius_width / 2 * math.sin(math.radians(self.angle - 270))
                x_offset = t_width / 2 * math.sin(math.radians(self.angle - 270))
                y_offset = t_width / 2 * math.cos(math.radians(self.angle - 270)) + t_height * math.sin(
                    math.radians(self.angle - 270))
        text_pos = (x_text - x_offset, y_text - y_offset)
        self.surface.blit(text, text_pos)
        # pygame.draw.rect(self.surface, self.colors['test'], self.surface.get_rect(), 1)
        # blit our surface on screen
        self.screen.blit(self.surface, self.blit_point)

    # def move_angle(self, last_mouse_pos: Tuple[int, int], pos_change: Tuple[int, int]):
    #
    #     mouse_pos = (last_mouse_pos[0] + pos_change[0], last_mouse_pos[1] + pos_change[1])
    #     # Значение x взял методом тыка
    #     x_diff = -193
    #     print(x_diff)
    #     y_diff = -pos_change[1]
    #     angle = math.degrees(math.atan2(x_diff, y_diff)) - 90
    #     if self.limit is not None:
    #         if self.limit[0] < self.formatted_angle(angle) < self.limit[1]:
    #             self.angle = angle
    #     else:
    #         self.angle = angle

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
            xH = end_point_x - (self.triangle_length * math.cos(math.radians(self.angle)))
            yH = end_point_y + (self.triangle_length * math.sin(math.radians(self.angle)))
            first_point_x = xH - (self.triangle_width / 2) * math.cos(math.radians(self.angle + 90))
            first_point_y = yH + (self.triangle_width / 2) * math.sin(math.radians(self.angle + 90))
            second_point_x = xH + (self.triangle_width / 2) * math.cos(math.radians(self.angle + 90))
            second_point_y = yH - (self.triangle_width / 2) * math.sin(math.radians(self.angle + 90))

        elif self.radius_type == 0:

            end_point_x = self.surface_center[0] + self.surface_radius * math.cos(math.radians(self.angle))
            end_point_y = self.surface_center[1] - self.surface_radius * math.sin(math.radians(self.angle))
            xH = end_point_x + (self.triangle_length * math.cos(math.radians(self.angle)))
            yH = end_point_y - (self.triangle_length * math.sin(math.radians(self.angle)))
            first_point_x = xH + (self.triangle_width / 2) * math.cos(math.radians(self.angle + 90))
            first_point_y = yH - (self.triangle_width / 2) * math.sin(math.radians(self.angle + 90))
            second_point_x = xH - (self.triangle_width / 2) * math.cos(math.radians(self.angle + 90))
            second_point_y = yH + (self.triangle_width / 2) * math.sin(math.radians(self.angle + 90))

        return [(first_point_x, first_point_y),
                (end_point_x, end_point_y),
                (second_point_x, second_point_y)]

    def formatted_angle(self, angle):
        if angle < 0:
            angle = angle + 360
        return angle
