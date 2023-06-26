from typing import Tuple, Dict
from math import sqrt

import pygame.surface


class Picture:
    def __init__(self,
                 screen: pygame.Surface,
                 blit_point: Tuple[int, int],
                 size: Tuple[int, int],
                 colors: Dict[str, Tuple[int,int,int]],
                 picture_type: int,
                 line_width: int = 1,
                 scale: int = 1,
                 font_name: str = None):
        self.scale = scale
        self.previous_scale = scale
        self.screen = screen
        self.colors = colors
        self.line_width_origin = line_width
        self.line_width = line_width * scale
        self.size_origin = size
        self.size = (size[0] * self.scale, size[1] * self.scale)
        self.blit_point = blit_point
        self.picture_type = picture_type
        self.surface = pygame.Surface(self.size, pygame.SRCALPHA)

    def draw(self):

        # scaling
        if self.scale != self.previous_scale:
            self.size = (int(self.size_origin[0] * self.scale), int(self.size_origin[1] * self.scale))
            self.line_width = int(self.line_width_origin * self.scale)
            self.surface = pygame.Surface(self.size, pygame.SRCALPHA)
            self.previous_scale = self.scale

        # drawing
        self.build_picture()

        # отображение
        #pygame.draw.rect(self.surface, self.colors['test'], self.surface.get_rect(), 1)
        self.screen.blit(self.surface, self.blit_point)

    def build_picture(self):

        self.surface = pygame.Surface(self.size, pygame.SRCALPHA)

        # допуск прямолинейности
        if self.picture_type == 1:
            pygame.draw.line(self.surface, self.colors['border'],
                             (0, self.size[1] // 2 - self.line_width // 4),
                             (self.size[0], self.size[1] // 2 - self.line_width // 4), self.line_width)
        # допуск плоскостности
        if self.picture_type == 2:
            pygame.draw.line(self.surface, self.colors['border'],
                             (0 + self.line_width // 4, self.size[1] * 3 / 4),
                             (self.size[0] / 6 + self.line_width // 4, self.size[1] / 4), self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (self.size[0] / 6, self.size[1] / 4 + self.line_width // 4),
                             (self.size[0], self.size[1] / 4 + self.line_width // 4), self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (self.size[0] - self.line_width // 4, self.size[1] / 4),
                             (self.size[0] * 5 / 6 - self.line_width // 4, self.size[1] * 3 / 4), self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (self.size[0] * 5 / 6, self.size[1] * 3 / 4 - self.line_width // 4),
                             (0, self.size[1] * 3 / 4 - self.line_width // 4), self.line_width)
        # допуск круглости
        if self.picture_type == 3:
            radius = min(self.size) // 2
            pygame.draw.circle(self.surface, self.colors['border'], (self.size[0] // 2, self.size[1] // 2), radius,
                               self.line_width)
        # допуск цилиндричности
        if self.picture_type == 4:
            radius = min(self.size) * 2.9 / 9
            pygame.draw.circle(self.surface, self.colors['border'], (self.size[0] // 2, self.size[1] // 2), radius,
                               self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (0, self.size[1]),
                             (self.size[0] // 3, 0), self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (self.size[0] * 2 // 3 - self.line_width // 4, self.size[1]),
                             (self.size[0] - self.line_width // 4, 0), self.line_width)
        # допуск профиля продольного сечения
        if self.picture_type == 5:
            pygame.draw.line(self.surface, self.colors['border'],
                             (0, self.size[1] / 3),
                             (self.size[0], self.size[1] / 3), self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (0, self.size[1] * 2 / 3),
                             (self.size[0], self.size[1] * 2 / 3), self.line_width)
        # допуск параллельности
        if self.picture_type == 6:
            pygame.draw.line(self.surface, self.colors['border'],
                             (self.size[0] // 6, self.size[1]),
                             (self.size[0] * 5 // 8, 0), self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (self.size[0] * 3 // 8, self.size[1]),
                             (self.size[0] * 5 // 6, 0), self.line_width)
        # допуск перпендикулярности
        if self.picture_type == 7:
            pygame.draw.line(self.surface, self.colors['border'],
                             (self.size[0] // 2, 0),
                             (self.size[0] // 2, self.size[1]), self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             ((self.size[0] - self.size[1]) / 2, self.size[1] - self.line_width / 2),
                             ((self.size[0] - self.size[1]) / 2 + self.size[1], self.size[1] - self.line_width / 2),
                             self.line_width)
        # допуск наклона
        if self.picture_type == 8:
            pygame.draw.line(self.surface, self.colors['border'],
                             (0, self.size[1] * 3 / 5),
                             (self.size[0], self.size[1] * 3 / 5), self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (0, self.size[1] * 3 / 5),
                             (self.size[0], self.size[1] * 1 / 5), self.line_width)
        # допуск соосности
        if self.picture_type == 9:
            radius_small = max(self.size) / 4
            radius_big = max(self.size) / 2
            pygame.draw.circle(self.surface, self.colors['border'], (self.size[0] // 2, self.size[1] // 2),
                               radius_small, self.line_width)
            pygame.draw.circle(self.surface, self.colors['border'], (self.size[0] // 2, self.size[1] // 2), radius_big,
                               self.line_width)
        # допуск симметричности
        if self.picture_type == 10:
            pygame.draw.line(self.surface, self.colors['border'],
                             (self.size[0] // 6, self.size[1] // 3),
                             (self.size[0] * 5 // 6, self.size[1] // 3), self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (self.size[0] // 6, self.size[1] * 2 // 3),
                             (self.size[0] * 5 // 6, self.size[1] * 2 // 3), self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (0, self.size[1] // 2 - self.line_width // 4),
                             (self.size[0], self.size[1] // 2 - self.line_width // 4), self.line_width)
        # позиционный допуск
        if self.picture_type == 11:
            radius = max(self.size) / 4
            pygame.draw.circle(self.surface, self.colors['border'], (self.size[0] // 2, self.size[1] // 2), radius,
                               self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (self.size[0] // 4 - radius, self.size[1] // 2),
                             (self.size[0] // 2 + radius * 2, self.size[1] // 2), self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (self.size[0] // 2, 0),
                             (self.size[0] // 2, self.size[1]), self.line_width)
        # допуск пересечения осей
        if self.picture_type == 12:
            pygame.draw.line(self.surface, self.colors['border'],
                             (self.size[0] // 4, self.size[1] // 4),
                             (self.size[0] * 3 // 4, self.size[1] * 3 // 4), self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (self.size[0] // 4, self.size[1] * 3 // 4),
                             (self.size[0] * 3 // 4, self.size[1] // 4), self.line_width)
        # допуск радиального биения
        if self.picture_type == 13:
            pygame.draw.line(self.surface, self.colors['border'],
                             (0, self.size[1]),
                             (self.size[0] - self.line_width * 2, self.line_width * 2), self.line_width)
            pygame.draw.polygon(self.surface, self.colors['border'],
                                ((self.size[0], 0),
                                 (self.size[0] * 5 // 10, self.size[1] * 3 // 10),
                                 (self.size[0] * 7 // 10, self.size[1] * 5 // 10)))
        # допуск полного радиального биения
        if self.picture_type == 14:
            pygame.draw.line(self.surface, self.colors['border'],
                             (0, self.size[1] // 2),
                             (self.size[0] // 2 - self.line_width * 2, self.line_width * 2), self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (self.size[0] // 2, self.size[1] // 2),
                             (self.size[0] - self.line_width * 2, self.line_width * 2), self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (0 + self.line_width // 2, self.size[1] // 2 - self.line_width // 2),
                             (self.size[0] // 2 + self.line_width // 2, self.size[1] // 2 - self.line_width // 2),
                             self.line_width)
            pygame.draw.polygon(self.surface, self.colors['border'],
                                ((self.size[0], 0),
                                 (self.size[0] * 7 // 10, self.size[1] * 2 // 10),
                                 (self.size[0] * 8 // 10, self.size[1] * 3 // 10)))
            pygame.draw.polygon(self.surface, self.colors['border'],
                                ((self.size[0] // 2, 0),
                                 (self.size[0] * 2 // 10, self.size[1] * 2 // 10),
                                 (self.size[0] * 3 // 10, self.size[1] * 3 // 10)))
        # допуск формы заданного профиля
        if self.picture_type == 15:
            pygame.draw.circle(self.surface, self.colors['border'], (self.size[0] // 2, self.size[1]),
                               self.size[1] // 2, self.line_width)
        # допуск формы заданной поверхности
        if self.picture_type == 16:
            pygame.draw.circle(self.surface, self.colors['border'], (self.size[0] // 2, self.size[1]),
                               self.size[1] // 2, self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (0, self.size[1] - self.line_width // 2),
                             (self.size[0], self.size[1] - self.line_width // 2), self.line_width)

        if self.picture_type in (i for i in range(17, 29)):
            radius = max(self.size) / 2
            center = (self.size[0]//2, self.size[1]//2)
            pygame.draw.circle(self.surface, self.colors['border'], center, radius, self.line_width)
        # Внешние непрозрачные
        if self.picture_type == 17:
            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0] - self.size[0] // 4 * sqrt(2),
                              center[1] - self.size[1] // 4 * sqrt(2)),
                             (center[0], center[1] + self.size[1] / 2 - self.line_width),
                             self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0], center[1] + self.size[1] / 2 - self.line_width),
                             (center[0] + self.size[0] // 4 * sqrt(2) - self.line_width,
                              center[1] - self.size[1] // 4 * sqrt(2)), self.line_width)
        # Внутренние непрозрачные
        if self.picture_type == 18:
            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0] - self.size[0] // 4 * sqrt(2),
                              center[1] + self.size[1] // 4 * sqrt(2)),
                             (center[0], center[1] - self.size[1] / 2 + self.line_width),
                             self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0], center[1] - self.size[1] / 2 + self.line_width),
                             (center[0] + self.size[0] // 4 * sqrt(2) - self.line_width,
                              center[1] + self.size[1] // 4 * sqrt(2)), self.line_width)
        # Светоделительные
        if self.picture_type == 19:
            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0] - self.size[0] // 2 + self.line_width, center[1]),
                             (center[0] + self.size[0] // 2 - self.line_width, center[1]),
                             self.line_width)
        # Фильтры
        if self.picture_type == 20:
            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0] - self.line_width // 4,
                              center[1] - self.size[1] // 2 + self.line_width),
                             (center[0] - self.line_width // 4,
                              center[1] + self.size[1] // 2 - self.line_width), self.line_width)
        # Защитные непрозрачные
        if self.picture_type == 21:
            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0] - self.size[0] // 2 + self.line_width,
                              center[1] - self.size[1] // 10),
                             (center[0] + self.size[0] // 2 - self.line_width,
                              center[1] - self.size[1] // 10), self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0] - self.size[0] // 2 + self.line_width,
                              center[1] + self.size[1] // 10),
                             (center[0] + self.size[0] // 2 - self.line_width,
                              center[1] + self.size[1] // 10), self.line_width)
        # Токопроводящие
        if self.picture_type == 22:
            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0] + self.line_width // 4 - self.size[0] // 10,
                              center[1] - self.size[1] // 2 + self.line_width),
                             (center[0] + self.line_width // 4 - self.size[0] // 10,
                              center[1] + self.size[1] // 2 - self.line_width), self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0] - self.line_width // 4 + self.size[0] // 10,
                              center[1] - self.size[1] // 2 + self.line_width),
                             (center[0] - self.line_width // 4 + self.size[0] // 10,
                              center[1] + self.size[1] // 2 - self.line_width), self.line_width)
        # Просветвляющие
        if self.picture_type == 23:
            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0] - self.size[0] // 4 * sqrt(2) + self.line_width,
                              center[1] - self.size[1] // 4 * sqrt(2)),
                             (center[0] + self.size[0] // 4 * sqrt(2) - self.line_width,
                              center[1] + self.size[1] // 4 * sqrt(2)), self.line_width)

            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0] - self.size[0] // 4 * sqrt(2) + self.line_width,
                              center[1] + self.size[1] // 4 * sqrt(2)),
                             (center[0] + self.size[0] // 4 * sqrt(2) - self.line_width,
                              center[1] - self.size[1] // 4 * sqrt(2)), self.line_width)
        # Отрезающие
        if self.picture_type == 24:
            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0] - self.size[0] // 4 * sqrt(3) + self.line_width // 2,
                              center[1] + self.size[1] // 4 * sqrt(1)),
                             (center[0] + self.line_width // 2, center[1] + self.size[1] // 4 * sqrt(1)),
                             self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0], center[1] + self.size[1] // 4 * sqrt(1)),
                             (center[0], center[1] - self.size[1] // 4 * sqrt(1)), self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0] - self.line_width // 3, center[1] - self.size[1] // 4 * sqrt(1)),
                             (center[0] + self.size[0] // 4 * sqrt(3) - self.line_width // 2,
                              center[1] - self.size[1] // 4 * sqrt(1)), self.line_width)
        # Узкополостные
        if self.picture_type == 25:
            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0] - self.size[0] // 4 * sqrt(3) + self.line_width // 2,
                              center[1] + self.size[1] // 4 * sqrt(1)),
                             (center[0] + self.size[0] // 4 * sqrt(3) - self.line_width // 2,
                              center[1] + self.size[1] // 4 * sqrt(1)), self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0] - self.line_width // 4, center[1] - self.size[1] // 2),
                             (center[0] - self.line_width // 4, center[1] + self.size[1] // 4 * sqrt(1)),
                             self.line_width)
        # Полосовые
        if self.picture_type == 26:
            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0] - self.size[0] // 4 * sqrt(3) + self.line_width // 2,
                              center[1] + self.size[1] // 4 * sqrt(1)),
                             (center[0] - (self.size[0] // 4 * sqrt(2)) * 0.65,
                              center[1] + (self.size[1] // 4 * sqrt(1))), self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0] - self.size[0] // 4 * sqrt(1) - self.line_width // 4,
                              center[1] + (self.size[1] // 4 * sqrt(2)) * 0.7),
                             (center[0] - self.size[0] // 4 * sqrt(1) - self.line_width // 4,
                              center[1] - self.size[0] // 4 * sqrt(3) + self.line_width * 0.75),
                             self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0] - self.size[0] // 4 * sqrt(1) - self.line_width // 4,
                              center[1] - self.size[0] // 4 * sqrt(3) + self.line_width * 0.75),
                             (center[0] + self.size[0] // 4 * sqrt(1) - self.line_width // 4,
                              center[1] - self.size[0] // 4 * sqrt(3) + self.line_width * 0.75),
                             self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0] + self.size[0] // 4 * sqrt(1) - self.line_width // 4,
                              center[1] - self.size[0] // 4 * sqrt(3) + self.line_width * 0.75),
                             (center[0] + self.size[0] // 4 * sqrt(1) - self.line_width // 4,
                              center[1] + (self.size[1] // 4 * sqrt(2)) * 0.7), self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0] + (self.size[0] // 4 * sqrt(1)) - self.line_width // 4,
                              center[1] + (self.size[1] // 4 * sqrt(1))),
                             (center[0] + self.size[0] // 4 * sqrt(3) - self.line_width // 2,
                              center[1] + self.size[1] // 4 * sqrt(1)), self.line_width)
        # Поляризующие
        if self.picture_type == 27:
            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0] - self.size[0] // 4 * sqrt(2) + self.line_width // 4,
                              center[1] - self.size[0] // 4 * sqrt(2) + self.line_width / 4),
                             (center[0] + self.size[0] // 4 * sqrt(2) - self.line_width // 4,
                              center[1] - self.size[0] // 4 * sqrt(2) + self.line_width / 4), self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0] + self.size[0] // 4 * sqrt(2) - self.line_width // 4,
                              center[1] - self.size[0] // 4 * sqrt(2) + self.line_width / 4),
                             (center[0] + self.size[0] // 4 * sqrt(2) - self.line_width // 4,
                              center[1] + self.size[0] // 4 * sqrt(2) - self.line_width / 2), self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0] + self.size[0] // 4 * sqrt(2) - self.line_width // 4,
                              center[1] + self.size[0] // 4 * sqrt(2) - self.line_width / 2),
                             (center[0] - self.size[0] // 4 * sqrt(2) + self.line_width // 4,
                              center[1] + self.size[0] // 4 * sqrt(2) - self.line_width / 2), self.line_width)
            pygame.draw.line(self.surface, self.colors['border'],
                             (center[0] - self.size[0] // 4 * sqrt(2) + self.line_width // 4,
                              center[1] + self.size[0] // 4 * sqrt(2) - self.line_width / 2),
                             (center[0] - self.size[0] // 4 * sqrt(2) + self.line_width // 4,
                              center[1] - self.size[0] // 4 * sqrt(2) + self.line_width / 4), self.line_width)
        # Специальные
        if self.picture_type == 28:
            font = pygame.font.Font(self.font_name, int(self.size[1] / 5 * 4))
            sign = font.render("C", True, self.colors['border'])
            self.surface.blit(sign,
                              (center[0] - sign.get_width() / 2, center[1] - sign.get_height() / 2))


        # pygame.draw.rect(self.surface, self.colors['test'], self.surface.get_rect(), 1)
