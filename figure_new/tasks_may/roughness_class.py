import math
from typing import Tuple, Dict

import pygame
from math import sin, cos, atan2, radians, degrees, tan


class RoughnessMeasure:

    def __init__(self, screen: pygame.Surface,
                 blit_point: Tuple[int, int],
                 colors: Dict[str, Tuple[int, int, int]],
                 font_size: int,
                 line_width: int,
                 surface_radius: int,
                 roughness_type: int,
                 size: Tuple[int, int] = (60, 60),
                 angle_rotate: int = 90,
                 font: str = 'ariali.ttf',
                 text_method: str = '',
                 text_base_len: str = '',
                 text_designation: str = '',
                 scale: int = 1,
                 limit: Tuple[int, int] = None):

        self.scale = scale
        self.screen = screen
        self.colors = colors
        self.blit_point = blit_point
        self.line_width = line_width * scale
        self.surface_radius = surface_radius * scale
        self.roughness_type = roughness_type
        self.angle_rotate = angle_rotate
        self.limit = limit
        self.width, self.height = size[0] * scale, size[1] * scale

        self.font_size = font_size * scale
        self.font = pygame.font.Font(font, self.font_size)
        self.left_offset = self.height // 2 * tan(radians(30)) * 3 / 2
        self.text_method = self.font.render(text_method, True, self.colors['border'])
        self.text_base_len = self.font.render(text_base_len, True, self.colors['border'])
        self.text_designation = self.font.render(text_designation, True, self.colors['border'])

        self.get_roughness_size()
        self.roughness_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        if self.roughness_type == 0:
            self.surface = pygame.Surface(((self.surface_radius + max(self.width, self.height)) * 2,
                                           (self.surface_radius + max(self.width, self.height)) * 2), pygame.SRCALPHA)
            self.surface_center = (self.surface_radius + max(self.width, self.height),
                                   self.surface_radius + max(self.width, self.height))
        elif self.roughness_type == 1:
            self.surface = pygame.Surface((self.surface_radius * 2,
                                           self.surface_radius * 2), pygame.SRCALPHA)
            self.surface_center = (self.surface_radius,
                                   self.surface_radius)

        self.build_surface()

    def check_click(self, mouse_pos) -> bool:

        offset_mouse = [mouse_pos[0] - self.blit_point[0],
                        mouse_pos[1] - self.blit_point[1]]

        if self.surface.get_rect().collidepoint(offset_mouse):

            if self.surface.get_at(offset_mouse) == self.colors['border']:
                print('RIGHT IN ROUGHNESS!')
                return True

        return False

    def draw(self):

        # surface
        self.surface.fill((0, 0, 0, 0))

        #pygame.draw.circle(self.surface, self.colors['test'], self.surface_center, self.surface_radius, 1)

        if self.roughness_type == 1:

            short_radius = math.sqrt(
                self.surface_radius ** 2 - (self.roughness_surface.get_width() / 2 - self.left_offset / 3) ** 2)
            dot_on_surface = (self.surface_center[0] + short_radius * cos(radians(self.angle_rotate)),
                              self.surface_center[1] - short_radius * sin(radians(self.angle_rotate)))

            if 90 < self.formatted_angle(self.angle_rotate) < 270:
                angle = self.angle_rotate - 180 - 90
            else:
                angle = self.angle_rotate + 90
            roughness_surface_rotated = pygame.transform.rotate(self.roughness_surface, angle)

            if 0 <= self.formatted_angle(self.angle_rotate) < 90:
                x_offset = self.roughness_surface.get_height() * cos(
                    radians(self.angle_rotate)) + self.roughness_surface.get_width() / 2 * sin(
                    radians(self.angle_rotate))
                y_offset = cos(radians(self.angle_rotate)) * self.roughness_surface.get_width() / 2
            if 90 <= self.formatted_angle(self.angle_rotate) < 180:
                x_offset = self.roughness_surface.get_width() / 2 * cos(radians(self.angle_rotate - 90))
                y_offset = sin(radians(self.angle_rotate - 90)) * self.roughness_surface.get_width() / 2
            if 180 <= self.formatted_angle(self.angle_rotate) < 270:
                x_offset = self.roughness_surface.get_width() / 2 * sin(radians(self.angle_rotate - 180))
                y_offset = cos(radians(
                    self.angle_rotate - 180)) * self.roughness_surface.get_width() / 2 + self.roughness_surface.get_height() * sin(
                    radians(self.angle_rotate - 180))
            if 270 <= self.formatted_angle(self.angle_rotate) < 360:
                x_offset = self.roughness_surface.get_width() / 2 * cos(radians(self.angle_rotate - 270)) + (
                            self.roughness_surface.get_height()) * sin(radians(self.angle_rotate - 270))
                y_offset = sin(radians(self.angle_rotate - 270)) * self.roughness_surface.get_width() / 2 + (
                            self.roughness_surface.get_height()) * cos(radians(self.angle_rotate - 270))

            self.surface.blit(roughness_surface_rotated, (dot_on_surface[0] - x_offset,
                                                          dot_on_surface[1] - y_offset))
            """
            pygame.draw.rect(self.surface, self.colors['test'], (
            dot_on_surface[0] - x_offset, dot_on_surface[1] - y_offset, roughness_surface_rotated.get_width(),
            roughness_surface_rotated.get_height()), 1)
            pygame.draw.line(self.surface, self.colors['test'], self.surface_center, dot_on_surface)
            """

        elif self.roughness_type == 0:

            big_radius = self.height + self.surface_radius
            dot_on_surface = (self.surface_center[0] + big_radius * cos(radians(self.angle_rotate)),
                              self.surface_center[1] - big_radius * sin(radians(self.angle_rotate)))

            if 90 < self.formatted_angle(self.angle_rotate) < 270:
                angle = self.angle_rotate - 180 - 270
            else:
                angle = self.angle_rotate + 270
            roughness_surface_rotated = pygame.transform.rotate(self.roughness_surface, angle)

            if 0 <= self.formatted_angle(self.angle_rotate) < 90:
                x_offset = self.roughness_surface.get_height() * cos(
                    radians(self.angle_rotate)) + self.left_offset / 3 * sin(
                    radians(self.angle_rotate))
                y_offset = cos(radians(self.angle_rotate)) * self.left_offset / 3
            if 90 <= self.formatted_angle(self.angle_rotate) < 180:
                x_offset = self.width / 2 * cos(radians(self.angle_rotate - 90)) - (self.width / 2 - self.left_offset / 3) * cos(radians(self.angle_rotate-90))
                y_offset = sin(radians(self.angle_rotate - 90)) * self.width / 2 + (self.width / 2 - self.left_offset / 3) * sin(radians(self.angle_rotate-90))
            if 180 <= self.formatted_angle(self.angle_rotate) < 270:
                x_offset = self.width / 2 * sin(radians(self.angle_rotate - 180)) + (self.width / 2 - self.left_offset / 3) * sin(radians(self.angle_rotate-180))
                y_offset = cos(radians(self.angle_rotate - 180)) * self.width / 2 + self.height * sin(
                    radians(self.angle_rotate - 180)) + (self.width / 2 - self.left_offset / 3) * cos(radians(self.angle_rotate-180))
            if 270 <= self.formatted_angle(self.angle_rotate) < 360:
                x_offset = self.width / 2 * cos(radians(self.angle_rotate - 270)) + (
                    self.height) * sin(radians(self.angle_rotate - 270)) + (self.width / 2 - self.left_offset / 3) * cos(radians(self.angle_rotate-270))
                y_offset = sin(radians(self.angle_rotate - 270)) * self.width / 2 + (
                    self.height) * cos(radians(self.angle_rotate - 270)) - (self.width / 2 - self.left_offset / 3) * sin(radians(self.angle_rotate-270))

            self.surface.blit(roughness_surface_rotated, (dot_on_surface[0] - x_offset,
                                                          dot_on_surface[1] - y_offset))

            """
            pygame.draw.rect(self.surface, self.colors['test'], (
                dot_on_surface[0] - x_offset, dot_on_surface[1] - y_offset, roughness_surface_rotated.get_width(),
                roughness_surface_rotated.get_height()), 1)
            pygame.draw.line(self.surface, self.colors['test'], self.surface_center, dot_on_surface)
            """

        self.screen.blit(self.surface, self.blit_point)

    def get_roughness_size(self):

        len1 = self.text_method.get_width() + self.left_offset + self.font_size + self.text_designation.get_width() + self.font_size
        len2 = self.text_base_len.get_width() + self.left_offset + self.font_size
        self.width = max(len1, len2, self.width)

    # меняет угол, не перересовывая покрытие. учитывает лимит угла
    def move_angle(self, mouse_pos):
        x_diff = mouse_pos[0] - (self.blit_point[0] + self.surface_center[0])
        y_diff = mouse_pos[1] - (self.blit_point[1] + self.surface_center[1])
        angle = degrees(atan2(x_diff, y_diff)) - 90
        if self.limit is not None:
            if self.limit[0] < self.formatted_angle(angle) < self.limit[1]:
                self.angle_rotate = angle
        else:
            self.angle_rotate = angle

    def build_surface(self):

        pygame.draw.line(self.roughness_surface, self.colors['border'],
                         (0, self.height * 3 / 4),
                         (self.left_offset / 3, self.height),
                         self.line_width)

        pygame.draw.line(self.roughness_surface, self.colors['border'],
                         (self.left_offset / 3, self.height),
                         (self.left_offset, self.height // 2),
                         self.line_width)

        pygame.draw.line(self.roughness_surface, self.colors['border'],
                         (self.left_offset, self.height // 2),
                         (self.width, self.height // 2),
                         self.line_width)

        self.roughness_surface.blit(self.text_base_len,
                                    (self.left_offset + (
                                            self.width - self.left_offset) // 2 - self.text_base_len.get_width() // 2 + self.text_designation.get_width() // 2,
                                     self.height // 2 + (self.height // 2 - self.text_base_len.get_height()) // 2))

        self.roughness_surface.blit(self.text_method,
                                    (self.left_offset + (
                                            self.width - self.left_offset) // 2 - self.text_method.get_width() // 2,
                                     self.height // 2 - self.font_size // 8 - self.text_method.get_height()))

        self.roughness_surface.blit(self.text_designation,
                                    (self.left_offset,
                                     self.height // 2 + (self.height // 2 - self.text_designation.get_height()) // 2))

        # удаляем всё прозрачное
        surface = self.roughness_surface.copy()
        rect = self.roughness_surface.get_bounding_rect()

        # обрезка изображения по прямоугольнику
        self.roughness_surface = surface.subsurface(rect)
        self.width, self.height = self.roughness_surface.get_width(), self.roughness_surface.get_height()

    # вспомогательная функция для move_angle
    def formatted_angle(self, angle):
        if angle < 0:
            angle = angle + 360
        return angle