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
        self.previous_scale = scale
        self.line_width_origin = line_width
        self.surface_radius_origin = surface_radius
        self.size_origin = size
        self.font_size_origin = font_size
        self.font_name = font
        self.screen = screen
        self.colors = colors
        self.blit_point = blit_point
        self.line_width = line_width * scale
        self.surface_radius = surface_radius * scale
        self.roughness_type = roughness_type
        self.angle_rotate = angle_rotate
        self.limit = limit
        self.width, self.height = size[0] * scale, size[1] * scale
        self.text_method_origin = text_method
        self.text_designation_origin = text_designation
        self.text_base_len_origin = text_base_len
        self.font_size = font_size * scale
        self.font = pygame.font.Font(font, self.font_size)
        self.left_offset = self.height // 2 * tan(radians(30)) * 3 / 2
        self.text_method = self.font.render(text_method, True, self.colors['border'])
        self.text_base_len = self.font.render(text_base_len, True, self.colors['border'])
        self.text_designation = self.font.render(text_designation, True, self.colors['border'])
        self.last_mouse_pos = (0, 0)

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

        offset_mouse = [mouse_pos[0],
                        mouse_pos[1]]

        if self.surface.get_rect().collidepoint(offset_mouse):
            inaccuracy_x = self.roughness_rect.width / 10
            inaccuracy_y = self.roughness_rect.height / 10
            if (self.roughness_rect.left - inaccuracy_x < offset_mouse[
                0] < self.roughness_rect.right + inaccuracy_x) and (
                    self.roughness_rect.top - inaccuracy_y < offset_mouse[
                1] < self.roughness_rect.bottom + inaccuracy_y):
                print('click')
                self.last_mouse_pos = offset_mouse
                return True
        return False

    def draw(self):

        # rescaling
        if self.previous_scale != self.scale:
            self.line_width = int(self.line_width_origin * self.scale)
            self.surface_radius = int(self.surface_radius_origin * self.scale)
            self.width, self.height = int(self.size_origin[0] * self.scale), int(self.size_origin[1] * self.scale)

            self.font_size = int(self.font_size_origin * self.scale)
            self.font = pygame.font.Font(self.font_name, self.font_size)
            self.left_offset = self.height // 2 * tan(radians(30)) * 3 / 2
            self.text_method = self.font.render(self.text_method_origin, True, self.colors['border'])
            self.text_base_len = self.font.render(self.text_base_len_origin, True, self.colors['border'])
            self.text_designation = self.font.render(self.text_designation_origin, True, self.colors['border'])

            self.get_roughness_size()
            self.roughness_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            if self.roughness_type == 0:
                self.surface = pygame.Surface(((self.surface_radius + max(self.width, self.height)) * 2,
                                               (self.surface_radius + max(self.width, self.height)) * 2),
                                              pygame.SRCALPHA)
                self.surface_center = (self.surface_radius + max(self.width, self.height),
                                       self.surface_radius + max(self.width, self.height))
            elif self.roughness_type == 1:
                self.surface = pygame.Surface((self.surface_radius * 2,
                                               self.surface_radius * 2), pygame.SRCALPHA)
                self.surface_center = (self.surface_radius,
                                       self.surface_radius)

            self.build_surface()
            self.previous_scale = self.scale

        # surface
        self.surface.fill((0, 0, 0, 0))

        # pygame.draw.circle(self.surface, self.colors['test'], self.surface_center, self.surface_radius, 1)

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
            if 270 <= self.formatted_angle(self.angle_rotate) <= 360:
                x_offset = self.roughness_surface.get_width() / 2 * cos(radians(self.angle_rotate - 270)) + (
                    self.roughness_surface.get_height()) * sin(radians(self.angle_rotate - 270))
                y_offset = sin(radians(self.angle_rotate - 270)) * self.roughness_surface.get_width() / 2 + (
                    self.roughness_surface.get_height()) * cos(radians(self.angle_rotate - 270))

            self.surface.blit(roughness_surface_rotated, (dot_on_surface[0] - x_offset,
                                                          dot_on_surface[1] - y_offset))

            self.roughness_rect = pygame.rect.Rect(
                (dot_on_surface[0] - x_offset, dot_on_surface[1] - y_offset, roughness_surface_rotated.get_width(),
                 roughness_surface_rotated.get_height()))

            # pygame.draw.rect(self.surface, self.colors['test'], self.roughness_rect, 1)
            # pygame.draw.line(self.surface, self.colors['test'], self.surface_center, dot_on_surface)

    def get_roughness_size(self):

        len1 = self.text_method.get_width() + self.left_offset + self.font_size + self.text_designation.get_width() + self.font_size
        len2 = self.text_base_len.get_width() + self.left_offset + self.font_size
        self.width = max(len1, len2, self.width)

    # меняет угол, не перересовывая покрытие. учитывает лимит угла
    def move_angle(self, pos_change: Tuple[int, int]):
        mouse_pos = (self.last_mouse_pos[0] - pos_change[0], self.last_mouse_pos[1] - pos_change[1])
        # recalculate angle based on mouse pos
        x_diff = mouse_pos[0] - self.surface_center[0]
        y_diff = mouse_pos[1] - self.surface_center[1]
        angle = degrees(atan2(x_diff, y_diff)) - 90
        if self.limit is not None:
            if self.formatted_angle(self.limit[1]) < self.formatted_angle(self.limit[0]):
                if (0 <= self.formatted_angle(angle) < self.formatted_angle(self.limit[1])) or (
                        self.formatted_angle(self.limit[0]) < self.formatted_angle(angle) <= 360):
                    self.angle = angle
            else:
                if self.formatted_angle(self.limit[0]) < self.formatted_angle(angle) < self.formatted_angle(
                        self.limit[1]):
                    self.angle = angle
        else:
            self.angle = angle
        print(self.formatted_angle(self.angle))

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
