import pygame

class cell:

    def change_text(self, text):
        self.text = text
        # self.redraw()

    def check_coord(self, x,y):
        if (x > self.cell_point_x and x < ( self.cell_point_x + self.cell_width*self.scale)) \
                and (y > self.cell_point_y and y < ( self.cell_point_y + self.cell_height*self.scale) ):
            # print(self.name, ' ', self.cell_point_x, self.cell_point_y, ' mouse ', x, ' ', y)
            return True
        else:
            return False

    def set_base_border_color(self):

        self.current_border_color = self.base_border_color
        # print(self.current_border_color)
        # self.redraw()

    def set_selected_border_color(self):
        self.current_border_color = self.selected_color
        # print(self.current_border_color)
        # self.redraw()

    def redraw(self):
        self.font = pygame.font.Font(self.font_patch, self.font_size)
        self.text_render = self.font.render(
            self.text, True, self.base_text_color)
        self.text_width = self.text_render.get_width()
        self.text_height = self.text_render.get_height()

        if (self.text_rotate % 180 == 0):
            document_designation_text_x = \
                self.cell_point_x + \
                self.cell_width*self.scale/2 - self.text_width/2

            document_designation_text_y = \
                self.cell_point_y + \
                self.cell_height*self.scale/2 - self.text_height/2
        else:
            document_designation_text_x = self.cell_point_x + self.cell_width*self.scale/2 - self.text_height/2
            document_designation_text_y = self.cell_point_y + self.cell_height*self.scale/2 - self.text_width/2

        rect = pygame.Rect(self.cell_point_x,
                           self.cell_point_y,
                          self.cell_width*self.scale,
                           self.cell_height * self.scale)
        pygame.draw.rect(self.screen,  self.current_border_color, rect, self.border_size)

        self.text_render = pygame.transform.rotate(self.text_render, self.text_rotate)
        self.screen.blit(self.text_render,
                    (document_designation_text_x,
                     document_designation_text_y))

    def __init__(self,
                 name,
                 screen,
                 colors,
                 cell_size,
                 cell_start_point,
                 scale,
                 margin,
                 border_size,
                 text,
                 font,
                 font_size,
                 text_rotate=0):
        self.name = name
        self.screen = screen
        self.colors = colors
        self.cell_size = cell_size
        self.scale = scale
        self.margin = margin
        self.border_size = border_size
        self.font_patch = font
        self.text_rotate = text_rotate
        self.font_size = font_size

        self.screen_x, self.screen_y = self.screen.get_size()
        #Обозначение документа
        self.cell_height = cell_size[0]
        self.cell_width = cell_size[1]
        self.cell_point_x = cell_start_point[0]
        self.cell_point_y = cell_start_point[1]


        self.base_text_color = colors['text']
        self.base_border_color = colors['border']
        self.selected_color = colors['selected']
        self.current_border_color = self.base_border_color
        self.current_text_color = self.base_text_color

        self.font = pygame.font.Font(self.font_patch, font_size)
        self.text = text
        self.text_render = self.font.render(
            self.text, True, self.base_text_color)
        self.text_width = self.text_render.get_width()
        self.text_height = self.text_render.get_height()



        if (text_rotate % 180 == 0):
            document_designation_text_x = \
                self.cell_point_x + \
                self.cell_width*scale/2 - self.text_width/2

            document_designation_text_y = \
                self.cell_point_y + \
                self.cell_height*scale/2 - self.text_height/2
        else:
            document_designation_text_x = self.cell_point_x + self.cell_width*scale/2 - self.text_height/2
            document_designation_text_y = self.cell_point_y + self.cell_height*scale/2 - self.text_width/2

        rect = pygame.Rect(self.cell_point_x,
                           self.cell_point_y,
                          self.cell_width*scale,
                           self.cell_height * scale)
        pygame.draw.rect(screen,  self.base_border_color, rect, border_size)

        self.text_render = pygame.transform.rotate(self.text_render, text_rotate)
        screen.blit(self.text_render,
                    (document_designation_text_x,
                     document_designation_text_y))