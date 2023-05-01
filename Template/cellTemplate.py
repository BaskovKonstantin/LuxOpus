import pygame

class cell:

    def change_text(self, text):
        self.text = text
        # self.redraw()
    def check_coord(self, x,y):
        if (x > self.point_x and x < ( self.point_x + self.width*self.scale)) \
                and (y > self.point_y and y < ( self.point_y + self.height*self.scale) ):
            return True
        else:
            return False
    def set_base_border_color(self):

        self.current_border_color = self.base_border_color
    def set_selected_border_color(self):
        self.current_border_color = self.selected_color
    def redraw(self):
        self.font = pygame.font.Font(self.font_patch, self.font_size)
        self.text_render = self.font.render(
            self.text, True, self.base_text_color)
        self.text_width = self.text_render.get_width()
        self.text_height = self.text_render.get_height()

        if (self.text_rotate % 180 == 0):
            document_designation_text_x = \
                self.point_x + \
                self.width*self.scale/2 - self.text_width/2

            document_designation_text_y = \
                self.point_y + \
                self.height*self.scale/2 - self.text_height/2
        else:
            document_designation_text_x = self.point_x + self.width*self.scale/2 - self.text_height/2
            document_designation_text_y = self.point_y + self.height*self.scale/2 - self.text_width/2

        rect = pygame.Rect(self.point_x,
                           self.point_y,
                          self.width*self.scale,
                           self.height * self.scale)
        pygame.draw.rect(self.screen,  self.current_border_color, rect, self.border_size)

        self.text_render = pygame.transform.rotate(self.text_render, self.text_rotate)
        self.screen.blit(self.text_render,
                    (document_designation_text_x,
                     document_designation_text_y))

    def __init__(self,
                 name,
                 screen,
                 colors,
                 size,
                 start_point,
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
        self.size = size
        self.scale = scale
        self.margin = margin
        self.border_size = border_size
        self.font_patch = font
        self.text_rotate = text_rotate
        self.font_size = font_size

        self.screen_x, self.screen_y = self.screen.get_size()
        #Обозначение документа
        self.height = size[0]
        self.width = size[1]
        self.point_x = start_point[0]
        self.point_y = start_point[1]

        self.original_point_x = start_point[0]
        self.original_point_y = start_point[1]

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
                self.point_x + \
                self.width*scale/2 - self.text_width/2

            document_designation_text_y = \
                self.point_y + \
                self.height*scale/2 - self.text_height/2
        else:
            document_designation_text_x = self.point_x + self.width*scale/2 - self.text_height/2
            document_designation_text_y = self.point_y + self.height*scale/2 - self.text_width/2

        rect = pygame.Rect(self.point_x,
                           self.point_y,
                          self.width*scale,
                           self.height * scale)
        pygame.draw.rect(screen,  self.base_border_color, rect, border_size)

        self.text_render = pygame.transform.rotate(self.text_render, text_rotate)
        screen.blit(self.text_render,
                    (document_designation_text_x,
                     document_designation_text_y))