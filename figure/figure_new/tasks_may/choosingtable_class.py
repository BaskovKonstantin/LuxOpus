from typing import Tuple, Dict, Callable

import pygame

from picture_class import Picture


class ChoosingTable:
    def __init__(self,
                 screen: pygame.Surface,
                 blit_point: Tuple[int, int],
                 colors: Dict[str, Tuple[int, int, int]],
                 table_size: Tuple[int, int],
                 tables: Dict[str, Tuple],
                 function: Callable,
                 scale: int = 1,
                 font: str = None,
                 font_size: int = 16
                 ):
        self.scale = scale
        self.screen = screen
        self.blit_point = blit_point
        self.colors = colors
        self.table_size = (table_size[0] * self.scale, table_size[1] * self.scale)
        self.tables = tables
        self.function = function
        self.font_name = font
        self.font_size = font_size * self.scale
        self.font = pygame.font.Font(font, self.font_size)
        self.chosen_table = next(iter(tables.values()))
        self.chosen_key = next(iter(tables.keys()))
        self.table_names_rects = []
        self.table_names_texts = []
        self.cells_rects = []
        self.cells_texts = []
        self.cell_width = 0
        self.cell_height = 0
        self.offset_y = 0

        self.set_up_table()

        self.surface = pygame.surface.Surface(self.table_size)

    def draw(self):
        self.surface.fill(self.colors['transparent'])

        for unit in range(len(self.table_names_rects)):
            if self.chosen_key == self.table_names_rects[unit][0]:
                line_width = 3
            else:
                line_width = 1
            pygame.draw.rect(self.surface, self.colors['border'], self.table_names_rects[unit][1], line_width)
            self.surface.blit(self.table_names_texts[unit][0], self.table_names_texts[unit][1])

        for unit in range(len(self.cells_rects)):
            pygame.draw.rect(self.surface, self.colors['border'], self.cells_rects[unit], 1)
            self.surface.blit(self.cells_texts[unit][0], self.cells_texts[unit][1])

        self.screen.blit(self.surface, self.blit_point)

    def check_click(self, mouse_pos):

        offset_mouse = [mouse_pos[0] - self.blit_point[0],
                        mouse_pos[1] - self.blit_point[1]]

        if self.surface.get_rect().collidepoint(offset_mouse) and offset_mouse[1] < self.offset_y + self.cell_height*len(self.chosen_table):
            if offset_mouse[1] < self.offset_y:
                for rect in self.table_names_rects:
                    if pygame.rect.Rect(rect[1]).collidepoint(offset_mouse):
                        self.chosen_key = rect[0]
                        self.chosen_table = self.tables[self.chosen_key]
                        self.set_up_table()
                        break
            elif offset_mouse[1] > self.offset_y + self.cell_height and offset_mouse[0] > self.cell_width:
                variant = self.chosen_table[int((offset_mouse[1] - self.offset_y) // self.cell_height)][
                    int(offset_mouse[0] // self.cell_width)]
                if isinstance(variant, str) or isinstance(variant, int) or isinstance(variant, float):
                    self.function(variant)
                else:
                    self.function(variant[1])
                # for rect in self.cells_rects:
                #    if pygame.rect.Rect(rect).collidepoint(offset_mouse):


    def set_up_table(self):

        self.table_names_rects = []
        self.table_names_texts = []
        self.cells_rects = []
        self.cells_texts = []

        # отрисуем список таблиц
        x, y = 0, 0

        for table_name in self.tables.keys():
            rendered_text = self.font.render(table_name, True, self.colors['border'])
            width, height = rendered_text.get_width() * 1.4, rendered_text.get_height() * 1.4
            if x + width > self.table_size[0]:
                x = 0
                y += height
            if self.chosen_key == table_name:
                line_width = 3
            else:
                line_width = 1
            # pygame.draw.rect(self.surface, self.colors['border'], (x, y, width, height), line_width)
            self.table_names_rects.append((table_name, (x, y, width, height)))
            self.table_names_texts.append((rendered_text, (x + width/7, y + height/7)))
            # self.surface.blit(rendered_text, (x + width / 7, y + height / 7))
            x = x + width

        # отрисуем саму таблицу
        self.offset_y = y + height * 2

        self.cell_width = self.table_size[0] // len(self.chosen_table[0])
        self.cell_height = (self.table_size[1] - self.offset_y) // len(self.chosen_table)#self.font.render(str(self.chosen_table[0][0]), True, self.colors['border']).get_height() * 1.5

        # Отрисовка таблицы и текста
        for row in range(len(self.chosen_table)):
            for col in range(len(self.chosen_table[row])):
                # Координаты верхнего левого угла ячейки
                x = col * self.cell_width
                y = row * self.cell_height + self.offset_y

                # Отрисовка границ ячейки
                # pygame.draw.rect(self.surface, self.colors['border'], (x, y, cell_width, cell_height), 1)
                self.cells_rects.append((x, y, self.cell_width, self.cell_height))
                # Создание текстовой поверхности для ячейки
                i = 1
                text_surface = self.font.render(str(self.chosen_table[row][col]), True, self.colors['border'])
                while text_surface.get_width() > self.cell_width:
                    if isinstance(self.chosen_table[row][col], str) or isinstance(self.chosen_table[row][col], int) or isinstance(self.chosen_table[row][col], float):
                        text_surface = pygame.font.Font(self.font_name, self.font_size - i).render(
                            str(self.chosen_table[row][col]), True, self.colors['border'])
                    else:
                        side = min(self.cell_width, self.cell_height)*0.8
                        self.chosen_table[row][col][0].size = (side, side)
                        self.chosen_table[row][col][0].build_picture()
                        text_surface = self.chosen_table[row][col][0].surface
                    i += 1

                # Вычисление позиции текста внутри ячейки
                text_x = x + (self.cell_width - text_surface.get_width()) // 2
                text_y = y + (self.cell_height - text_surface.get_height()) // 2

                # Отображение текста внутри ячейки
                # self.surface.blit(text_surface, (text_x, text_y))
                self.cells_texts.append((text_surface, (text_x, text_y)))
