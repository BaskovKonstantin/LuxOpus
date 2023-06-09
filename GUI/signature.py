from Template.cellTemplate import cell
import pygame


class signature(cell):

    def redraw(self):
        self.font = pygame.font.Font(self.font_patch, self.font_size)
        self.text_render = self.font.render(
            self.text, True, self.base_text_color)
        self.text_width = self.text_render.get_width()
        self.text_height = self.text_render.get_height()
        self.text_render = pygame.transform.rotate(self.text_render, self.text_rotate)
        self.screen.blit(self.text_render, (self.point_x, self.point_y))