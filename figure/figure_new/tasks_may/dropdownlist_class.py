import math
from typing import Tuple, Dict, Callable

import pygame


class DropdownList:
    def __init__(self, screen: pygame.Surface,
                 blit_point: Tuple[int, int],
                 colors: Dict[str, Tuple[int, int, int]],
                 cell_size: Tuple[int, int],
                 variants: Tuple[str, ...],
                 max_height: int,
                 function: Callable,
                 default_value: str = '',
                 font: str = 'arial.ttf',
                 font_size: int = 16,
                 scale: int = 1):
        self.screen = screen
        self.scale = scale
        self.blit_point = blit_point
        self.colors = colors
        self.cell_size = [cell_size[0] * self.scale, cell_size[1] * self.scale]
        self.variants = variants
        self.max_height = max_height
        self.function = function
        self.font_size = font_size * self.scale
        self.font = pygame.font.Font(font, self.font_size)
        self.is_opened = False
        self.default_value = default_value
        self.scroll_offset = 0
        self.scrolling = False
        self.temp = (self.cell_size[1] * (self.max_height + 1) - (self.cell_size[1] + self.cell_size[1])) / (
                len(self.variants) - self.max_height + 1)

        self.main_rect = pygame.rect.Rect((0, 0, self.cell_size[0], self.cell_size[1]))
        self.helping_rect = pygame.rect.Rect(
            (0, self.cell_size[1], self.cell_size[0], self.cell_size[1] * min(self.max_height, len(self.variants))))

        self.surface = pygame.Surface((self.cell_size[0], self.cell_size[1] * (self.max_height + 1)), pygame.SRCALPHA)

    def draw(self):

        self.surface.fill((0, 0, 0, 0))

        pygame.draw.rect(self.surface, self.colors['border'], self.main_rect, 1)
        default = self.font.render(self.default_value, True, self.colors['border'])
        self.surface.blit(default, (
            self.cell_size[1] / 2 - default.get_height() / 2, self.cell_size[1] / 2 - default.get_height() / 2))

        if self.is_opened:

            if len(self.variants) > self.max_height:

                for cell in range(1, self.max_height + 1):
                    pygame.draw.rect(self.surface, self.colors['border'],
                                     (0, self.cell_size[1] * cell, self.cell_size[0], self.cell_size[1]), 1)
                    self.surface.blit(self.font.render(self.variants[self.scroll_offset // self.cell_size[1] + cell - 1], True,
                                                       self.colors['border']),
                                      (self.cell_size[1] / 2 - default.get_height() / 2,
                                       self.cell_size[1] / 2 - default.get_height() / 2 + self.cell_size[1] * cell))

                # scrolling
                # заливаем черным
                pygame.draw.rect(self.surface, self.colors['background'], (
                    self.cell_size[0] - self.cell_size[1] / 2, self.cell_size[1], self.cell_size[1] / 2,
                    self.cell_size[1] * self.max_height))
                # кнопка вверх
                pygame.draw.rect(self.surface, self.colors['border'], (
                    self.cell_size[0] - self.cell_size[1] / 2, self.cell_size[1] + self.cell_size[1] / 2,
                    self.cell_size[1] / 2,
                    self.cell_size[1] * self.max_height - self.cell_size[1]), 1)
                pygame.draw.line(self.surface, self.colors['border'], (
                    self.cell_size[0] - self.cell_size[1] / 2 + self.cell_size[1] / 2 / 4,
                    self.cell_size[1] + self.cell_size[1] / 2 / 4 * 3), (
                                     self.cell_size[0] - self.cell_size[1] / 2 + self.cell_size[1] / 2 / 2,
                                     self.cell_size[1] + self.cell_size[1] / 2 / 4), 2*self.scale)
                pygame.draw.line(self.surface, self.colors['border'], (
                    self.cell_size[0] - self.cell_size[1] / 2 + self.cell_size[1] / 2 / 2,
                    self.cell_size[1] + self.cell_size[1] / 2 / 4), (
                                     self.cell_size[0] - self.cell_size[1] / 2 + self.cell_size[1] / 2 / 4 * 3,
                                     self.cell_size[1] + self.cell_size[1] / 2 / 4 * 3), 2*self.scale)
                # кнопка вниз
                pygame.draw.rect(self.surface, self.colors['border'], (
                    self.cell_size[0] - self.cell_size[1] / 2, self.cell_size[1], self.cell_size[1] / 2,
                    self.cell_size[1] / 2), 1)
                pygame.draw.line(self.surface, self.colors['border'], (
                    self.cell_size[0] - self.cell_size[1] / 2 + self.cell_size[1] / 2 / 4,
                    self.cell_size[1] * (self.max_height + 1) - self.cell_size[1] / 2 / 4 * 3), (
                                     self.cell_size[0] - self.cell_size[1] / 2 + self.cell_size[1] / 2 / 2,
                                     self.cell_size[1] * (self.max_height + 1) - self.cell_size[1] / 2 / 4), 2*self.scale)
                pygame.draw.line(self.surface, self.colors['border'], (
                    self.cell_size[0] - self.cell_size[1] / 2 + self.cell_size[1] / 2 / 2,
                    self.cell_size[1] * (self.max_height + 1) - self.cell_size[1] / 2 / 4), (
                                     self.cell_size[0] - self.cell_size[1] / 2 + self.cell_size[1] / 2 / 4 * 3,
                                     self.cell_size[1] * (self.max_height + 1) - self.cell_size[1] / 2 / 4 * 3), 2*self.scale)
                # пространство для ползунка
                pygame.draw.rect(self.surface, self.colors['border'], (self.cell_size[0] - self.cell_size[1] / 2,
                                                                       self.cell_size[1] * (self.max_height + 1) -
                                                                       self.cell_size[1] / 2,
                                                                       self.cell_size[1] / 2,
                                                                       self.cell_size[1] / 2), 1)

                # ползунок
                pygame.draw.rect(self.surface, self.colors['border'], (self.cell_size[0] - self.cell_size[1] / 2,
                                                                       self.cell_size[1] + self.cell_size[
                                                                           1] / 2 + self.scroll_offset //
                                                                       self.cell_size[1] * self.temp,
                                                                       self.cell_size[1] / 2, self.temp))

            elif len(self.variants) <= self.max_height:

                for cell in range(1, len(self.variants) + 1):
                    pygame.draw.rect(self.surface, self.colors['border'],
                                     (0, self.cell_size[1] * cell, self.cell_size[0], self.cell_size[1]), 1)
                    self.surface.blit(self.font.render(self.variants[cell - 1], True, self.colors['border']),
                                      (self.cell_size[1] / 2 - default.get_height() / 2,
                                       self.cell_size[1] / 2 - default.get_height() / 2 + self.cell_size[1] * cell))

        self.screen.blit(self.surface, self.blit_point)

    def handle_event(self, event, mouse_x, mouse_y):
        mouse_pos = (mouse_x, mouse_y)
        offset_mouse = [int(mouse_pos[0]),
                        int(mouse_pos[1])]

        if self.helping_rect.collidepoint(offset_mouse) and self.is_opened:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # колёсико вверх
                if event.button == 4:
                    if self.scroll_offset > 0:
                        self.scroll_offset -= self.cell_size[1]
                # колёсико вниз
                elif event.button == 5:
                    if self.scroll_offset < (len(self.variants) - self.max_height) * self.cell_size[1]:
                        self.scroll_offset += self.cell_size[1]
                # ЛКМ
                elif event.button == 1:
                    # клик по ползунку
                    if self.cell_size[0] - self.cell_size[1] / 2 < offset_mouse[0] < self.cell_size[0]:
                        if self.cell_size[1] + self.cell_size[1] / 2 < offset_mouse[1] < self.cell_size[1] * (
                                self.max_height + 1) - self.cell_size[1] / 2:
                            self.scrolling = True
                    # выбор варианта в списке
                    if offset_mouse[0] < self.cell_size[0] - self.cell_size[1] / 2:
                        button_number = (offset_mouse[1] + self.scroll_offset) // self.cell_size[1] - 1
                        self.default_value = self.variants[button_number]
                        self.function(self.variants[button_number])
                        self.is_opened = False
                    # кнопка вверх вниз
                    else:
                        if self.cell_size[1] < offset_mouse[1] < self.cell_size[1] + self.cell_size[1] / 2:
                            if self.scroll_offset > 0:
                                self.scroll_offset -= self.cell_size[1]
                        elif self.cell_size[1] * (self.max_height + 1) - self.cell_size[1] / 2 < offset_mouse[1] < \
                                self.cell_size[1] * (self.max_height + 1):
                            if self.scroll_offset < (len(self.variants) - self.max_height) * self.cell_size[1]:
                                self.scroll_offset += self.cell_size[1]

            elif event.type == pygame.MOUSEBUTTONUP:
                self.scrolling = False

        elif self.main_rect.collidepoint(offset_mouse):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.is_opened is True:
                        self.is_opened = False
                    elif self.is_opened is False:
                        self.is_opened = True

        if self.scrolling:
            change = (offset_mouse[1] - (self.cell_size[1] + self.cell_size[1] / 2)) // self.temp
            self.scroll_offset = min(max(int(change * self.cell_size[1]), 0),
                                     (len(self.variants) - self.max_height) * self.cell_size[1])
