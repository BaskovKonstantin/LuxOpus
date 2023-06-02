from typing import Tuple, Dict
import pygame
from math import sin, cos, atan2, radians, degrees


class CoversMeasure:

    def __init__(self, screen: pygame.Surface,
                 blit_point: Tuple[int, int],
                 colors: Dict[str, Tuple[int, int, int]],
                 surface_radius: int, cover_size: Tuple[int, int],
                 angle: int, line_width: int,
                 cover_type: int,
                 limit: Tuple[int, int] = None,
                 scale: int = 1):

        self.scale = scale
        self.screen = screen
        self.blit_point = blit_point
        self.width, self.height = cover_size[0] * scale, cover_size[1] * scale
        self.angle_position = angle
        self.surface_radius = surface_radius * scale
        self.cover_type = cover_type
        self.limit = limit
        self.colors = colors
        self.line_width = line_width
        self.end_pos = [0, 0]

        if self.cover_type == 0:
            self.surface = pygame.Surface(
                ((self.surface_radius + self.width) * 2, (self.surface_radius + self.height) * 2),
                pygame.SRCALPHA)
            self.surface_center = (self.surface_radius + self.height, self.surface_radius + self.width)

        elif self.cover_type == 1:
            self.surface = pygame.Surface((self.surface_radius * 2, self.surface_radius * 2), pygame.SRCALPHA)
            self.surface_center = (self.surface_radius, self.surface_radius)

    # проверяет нажатие по покрытию (окружности и линиям). возвращает True/False
    def check_click(self, mouse_pos) -> bool:

        offset_mouse = [mouse_pos[0] - self.blit_point[0],
                        mouse_pos[1] - self.blit_point[1]]

        if self.surface.get_rect().collidepoint(offset_mouse):

            # if self.surface.get_at(offset_mouse) == self.colors['border']:
            #     print('RIGHT IN COVER!')
            return True

        return False

    # отрисовка покрытия, ничего не возвращает, блитит на скрин
    def draw(self):

        # заливаем фон прозрачным
        self.surface.fill(self.colors['transparent'])
        #
        # # рисуем окружность *для разработки*
        # pygame.draw.circle(self.surface, self.colors['test'], self.surface_center, self.surface_radius, 1)

        # Рисуем крестик на поверхности
        self.get_cover_points()

        pygame.draw.line(self.surface, self.colors['border'],
                         (self.end_pos[0] - self.width // 2 + self.line_width, self.end_pos[1]),
                         (self.end_pos[0] + self.width // 2 - self.line_width, self.end_pos[1]), self.line_width)

        pygame.draw.line(self.surface, self.colors['border'],
                         (self.end_pos[0], self.end_pos[1] - self.height // 2 + self.line_width),
                         (self.end_pos[0], self.end_pos[1] + self.height // 2 - self.line_width), self.line_width)

        # Рисуем круг на поверхности
        pygame.draw.circle(self.surface, self.colors['border'], self.end_pos, self.width // 2, self.line_width)

        self.screen.blit(self.surface, self.blit_point)

    # вспомогательная функция для draw, математически вычисления
    def get_cover_points(self):

        # находим центральную точку покрытия относительно центра поверхности
        if self.cover_type == 0:
            length = self.surface_radius + self.width // 2
        elif self.cover_type == 1:
            length = self.surface_radius - self.width // 2

        end_pos_x = self.surface_center[0] + length * cos(radians(self.angle_position))
        end_pos_y = self.surface_center[1] - length * sin(radians(self.angle_position))
        self.end_pos = [end_pos_x, end_pos_y]

    # меняет угол, не перересовывая покрытие. учитывает лимит угла
    def move_angle(self, mouse_pos):

        # recalculate angle based on mouse pos
        x_diff = mouse_pos[0] - (self.blit_point[0] + self.surface_center[0])
        y_diff = mouse_pos[1] - (self.blit_point[1] + self.surface_center[1])
        angle = degrees(atan2(x_diff, y_diff)) - 90
        if self.limit is not None:
            if self.limit[0] < self.formatted_angle(angle) < self.limit[1]:
                self.angle_position = angle
        else:
            self.angle_position = angle

    # вспомогательная функция для move_angle
    def formatted_angle(self, angle):
        if angle < 0:
            angle = angle + 360
        return angle
