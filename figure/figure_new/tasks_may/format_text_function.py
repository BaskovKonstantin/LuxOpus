from typing import Tuple, Dict

import pygame
from picture_class import Picture


def format_text(text: str,
                colors: Dict[str, Tuple[int, int, int]],
                font_size: int = 16,
                font_name: str = 'arial.ttf',
                scale: int = 1
                ):
    font_size = font_size * scale
    font = pygame.font.Font(font_name, font_size)
    small_font = pygame.font.Font(font_name, font_size // 2)
    formatted_text = font.render(text, True, colors['border'])
    next_char = 'normal'
    if '_' in text or '|' in text or '<' in text:
        number = ''
        surface = pygame.Surface((formatted_text.get_width()*2, formatted_text.get_height()), pygame.SRCALPHA)
        surface.fill(colors['transparent'])
        x_offset = 0
        for char in text:
            if char == '_':
                next_char = 'bottom'
            elif char == '|':
                next_char = 'top'
            elif char == '<':
                #if '>' in text:
                next_char = 'number'
            elif char == '>':
                next_char = 'normal'
                picture = Picture(pygame.Surface((0,0), pygame.SRCALPHA), (0,0), (formatted_text.get_height()*0.8, formatted_text.get_height()*0.8), colors, int(number), scale, scale, font_name)
                picture.draw()
                char_render = picture.surface
                surface.blit(char_render, (x_offset+formatted_text.get_height()*0.1, formatted_text.get_height()*0.1))
                x_offset += char_render.get_width() + formatted_text.get_height()*0.2
                number = ''
            else:
                if next_char == 'bottom':
                    char_render = small_font.render(char, True, colors['border'])
                    surface.blit(char_render,
                                 (x_offset, formatted_text.get_height() // 2))
                elif next_char == 'top':
                    char_render = small_font.render(char, True, colors['border'])
                    surface.blit(char_render, (x_offset, 0))
                elif next_char == 'normal':
                    char_render = font.render(char, True, colors['border'])
                    surface.blit(char_render, (x_offset, 0))
                if next_char == 'number':
                    number += char
                else:
                    next_char = 'normal'
                    x_offset += char_render.get_width()

        surface_extra = surface.copy()
        rect = surface.get_bounding_rect()
        surface = surface_extra.subsurface(rect)
        return surface
    else:
        return formatted_text
