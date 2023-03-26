import pygame
import math

class lens:


    def check_click(self, click_pos):
        left_point = (int(self.surface_width/2) + self.R1/12, self.axis_center_point - self.diametr/2)
        right_point = (int(self.surface_width/2) + self.width + self.R2/24,self.axis_center_point + self.diametr/2)

        # print('left_point',left_point)
        # print('right_point', right_point)
        # print('click_pos', click_pos)


        if (click_pos[0] > left_point[0] and click_pos[0] < right_point[0] and
                click_pos[1] > left_point[1] and click_pos[1] < right_point[1]):
            print('Click on lens')
            return True
        return False


    def get_hatching_unit(self, side_size = 30, width = 2):

        image_surface = pygame.Surface((side_size, side_size))
        image_surface.fill(self.colors['transparent'])  # Заполняем белым цветом
        pygame.draw.line(image_surface, self.colors['border'], (0, side_size), (side_size, 0), width)
        pygame.draw.line(image_surface, self.colors['border'], (0, side_size/2), (side_size/2, 0), width)
        pygame.draw.line(image_surface, self.colors['border'], (side_size, side_size/2), (side_size/2, side_size), width)

        return image_surface

    def draw_arrow(self, start_point, double = False, size = (100, 25), arrow_height = 25, angle_rotate = 0 , surface = False):
        if (not surface):
            surface = self.surface
        # Создаем поверхность для стрелки
        arrow_surface = pygame.Surface(size, pygame.SRCALPHA)
        pygame.draw.polygon(arrow_surface, self.colors['border'], [(size[0] - arrow_height, 0), (size[0], size[1]/4), (size[0] - arrow_height, 0.5*size[1])])

        if (double):
            pygame.draw.polygon(arrow_surface, self.colors['border'], [(arrow_height, 0), (0, size[1]/4), (arrow_height, 0.5*size[1])])
        pygame.draw.line(arrow_surface, self.colors['border'],
                         (size[0],size[1]/4),
                         (0,size[1]/4),
                          self.border_size)

        arrow_surface = pygame.transform.rotate(arrow_surface, angle_rotate)

        start_point = (start_point[0] - 7, start_point[1])
        surface.blit(arrow_surface, start_point)

    def draw_measure(self, key_point_1, width, measure_shift, angle_rotate = 0, text = False):
        arrow_height = 10
        font_size = 24
        if (not text):
            text = str(width)

        measure_surface = pygame.Surface((width, measure_shift*2), pygame.SRCALPHA)
        # measure_surface.fill((255,255,255))

        pygame.draw.line(measure_surface, self.colors['border'],

                         (int(self.surface_width/2), measure_shift*2),
                         (int(self.surface_width/2),measure_shift),
                         self.border_size - 1)
        pygame.draw.line(measure_surface, self.colors['border'],
                         (width - 5, measure_shift*2),
                         (width - 5, measure_shift ),
                         self.border_size - 1)

        self.draw_arrow((arrow_height,measure_shift),
                        True, size=(width- arrow_height, 25), arrow_height=arrow_height, angle_rotate=0, surface=measure_surface)

        font = pygame.font.SysFont(self.font, font_size)
        text_surface = font.render(str(text), True, self.colors['border'])
        measure_surface.blit(text_surface, (width/2 - text_surface.get_width()/2, measure_shift - font_size))

        measure_surface = pygame.transform.rotate(measure_surface, angle_rotate)
        self.surface.blit(measure_surface, (key_point_1[0], key_point_1[1] - measure_shift*2))

    def drawLens(self):
        self.types = self.lens_type[self.type]

        self.surface = pygame.Surface((2 * self.R1 if self.R1 > self.R2 else 2 * self.R2, 4 * self.R1 if self.R1 >self. R2 else 4 * self.R2), pygame.SRCALPHA)

        self.surface_width = self.surface.get_width()

        arrow_height = 15
        angle_start_R1 = 0
        angle_start_R2 = 0
        angle_end_R1 = 0
        angle_end_R2 = 0

        #Отображение размеров
        if (self.show_measure):

            hatching_unit_side_size = 30
            step = 15
            hatching_unit = self.get_hatching_unit(side_size = hatching_unit_side_size)

            for position_x in range( int(self.surface_width/2) , int(self.surface_width/2) + self.width, hatching_unit_side_size + step):

                for position_y in range(int(self.axis_center_point - self.diametr/2), int(self.axis_center_point + self.diametr/2), hatching_unit_side_size + step):
                    self.surface.blit(hatching_unit, (position_x, position_y))
            pygame.draw.rect(self.surface, self.colors['transparent'], pygame.Rect( int(self.surface_width/2), int(self.axis_center_point + self.diametr/2), self.width, hatching_unit_side_size) )

        #Левый
        if (self.types[0] == 1):
            if (self.show_measure):
                pygame.draw.circle(self.surface, self.colors['transparent'],
                                   (int(self.surface_width/2) + self.R1,
                                    (self.axis_center_point )), self.R1 + 4*step, 4*step)

            rect = pygame.Rect(int(self.surface_width/2),
                                    self.axis_center_point - self.R1,
                               2*self.R1, 2*self.R1)
            angle_start_R1 = -math.asin(self.diametr/(2 * self.R1)) + math.pi
            angle_end_R1 = math.asin(self.diametr/(2 * self.R1)) + math.pi
            pygame.draw.arc(self.surface, self.colors['border'], rect, angle_start_R1, angle_end_R1, self.border_size)
            # pygame.draw.arc(self.surface, self.colors['border'], rect, math.pi/2, -math.pi/2, self.border_size)
            key_point_1 = (int(self.surface_width/2), self.axis_center_point)
        if (self.types[0] == 2):
            if (self.show_measure):
                for position_x in range(int(self.surface_width/2)  - self.R1, int(self.surface_width/2) - step//2, hatching_unit_side_size + step):

                    for position_y in range(int(self.axis_center_point - self.diametr / 2) ,
                                            int(self.axis_center_point + self.diametr / 2),
                                            hatching_unit_side_size + step):
                        self.surface.blit(hatching_unit, (position_x, position_y))
                pygame.draw.rect(self.surface, self.colors['transparent'],
                                 pygame.Rect(int(self.surface_width/2) - self.R1 , int(self.axis_center_point + self.diametr/2) - 10, self.R1,
                                             hatching_unit_side_size))


            rect = pygame.Rect(int(self.surface_width/2) - 2*self.R1 ,
                                    self.axis_center_point - self.R1 ,
                               2 * self.R1, 2 * self.R1)
            angle_start_R1 = -math.asin(self.diametr / (2 * self.R1))
            angle_end_R1 = math.asin(self.diametr / (2 * self.R1))
            if (self.show_measure):
                pygame.draw.circle(self.surface, self.colors['transparent'],
                                   (int(self.surface_width/2) - self.R1,
                                    (self.axis_center_point )), self.R1)
            pygame.draw.arc(self.surface, self.colors['border'], rect, angle_start_R1, angle_end_R1, self.border_size)
            # pygame.draw.arc(self.surface, self.colors['border'], rect, math.pi/2, -math.pi/2 ,self.border_size)

            key_point_1 = (int(self.surface_width/2) , self.axis_center_point)
        if (self.types[0] == 3):
            if (self.show_measure):
                pygame.draw.rect(self.surface, self.colors['transparent'],
                                 pygame.Rect( int(self.surface_width/2),
                                              int(self.axis_center_point - self.diametr/2),
                                              self.R1/12, self.diametr) )

            pygame.draw.line(self.surface,self.colors['border'],
                             (int(self.surface_width/2) + self.R1/12, self.axis_center_point - self.diametr/2),
                             (int(self.surface_width/2) + self.R1/12, self.axis_center_point + self.diametr/2), self.border_size )
            angle_start_R1 = -math.asin(self.diametr / (2 * self.R1)) + math.pi
            angle_end_R1 = math.asin(self.diametr / (2 * self.R1)) + math.pi

            key_point_1 = (int(self.surface_width/2) + self.R1/12, self.axis_center_point)


        # Правый
        if (self.types[1] == 1):
            if (self.show_measure):
                pygame.draw.circle(self.surface, self.colors['transparent'],
                                   (int(self.surface_width/2) + self.width - self.R2,
                                    (self.axis_center_point )), self.R2 + 4*step, 4*step)

            rect = pygame.Rect(int(self.surface_width/2) - 2* self.R2 + self.width,
                                    self.axis_center_point - self.R2 ,
                               2*self.R2, 2*self.R2)
            angle_start_R2 = -math.asin(self.diametr / (2 * self.R2))
            angle_end_R2 = math.asin(self.diametr / (2 * self.R2))
            pygame.draw.arc(self.surface, self.colors['border'], rect, angle_start_R2, angle_end_R2, self.border_size)
            # pygame.draw.arc(self.surface, self.colors['border'], rect, math.pi/2, -math.pi/2 ,self.border_size)

            key_point_2 = (int(self.surface_width/2) + self.width,
                               self.axis_center_point)
        if (self.types[1] == 2):
            if (self.show_measure):
                for position_x in range(int(self.surface_width/2) + self.width + 2*step, int(self.surface_width/2) + self.width + self.R2, hatching_unit_side_size + step):

                    for position_y in range(int(self.axis_center_point - self.diametr / 2) + step,
                                            int(self.axis_center_point + self.diametr / 2),
                                            hatching_unit_side_size + step):
                        self.surface.blit(hatching_unit, (position_x, position_y))
                pygame.draw.rect(self.surface, self.colors['transparent'],
                                 pygame.Rect(int(self.surface_width/2) + self.width, int(self.axis_center_point + self.diametr / 2), self.R2,
                                             hatching_unit_side_size))

            rect = pygame.Rect(int(self.surface_width/2) + self.width,
                                    self.axis_center_point - self.R2 ,
                               2*self.R2, 2*self.R2)
            angle_start_R2 = -math.asin(self.diametr / (2 * self.R2)) + math.pi
            angle_end_R2 = math.asin(self.diametr / (2 * self.R2)) + math.pi

            if (self.show_measure):
                pygame.draw.circle(self.surface, self.colors['transparent'],
                                   (int(self.surface_width/2) + self.width + self.R2,
                                    (self.axis_center_point )), self.R2)

            pygame.draw.arc(self.surface, self.colors['border'], rect, angle_start_R2, angle_end_R2, self.border_size)
            # pygame.draw.arc(self.surface, self.colors['border'], rect, math.pi/2, -math.pi/2 ,self.border_size)

            key_point_2 = (int(self.surface_width/2) + self.width,
                               self.axis_center_point)
        if (self.types[1] == 3):
            if (self.show_measure):
                pygame.draw.rect(self.surface, self.colors['transparent'],
                                 pygame.Rect( int(self.surface_width/2) + self.width + self.R2/24,
                                              int(self.axis_center_point - self.diametr/2),
                                              self.R2/12, self.diametr) )


            pygame.draw.line(self.surface,self.colors['border'],
                             (int(self.surface_width/2) + self.width + self.R2/24 ,self.axis_center_point - self.diametr/2),
                             (int(self.surface_width/2) + self.width + self.R2/24,self.axis_center_point + self.diametr/2), self.border_size )
            angle_start_R2 = -math.asin(self.diametr / (2 * self.R2)) + math.pi
            angle_end_R2 = math.asin(self.diametr / (2 * self.R2)) + math.pi

            key_point_2 = (int(self.surface_width/2) + self.width + self.R2/24, self.axis_center_point)


        start_x_R1 = int(self.surface_width/2) + self.R1
        # start_y_R1 =      self.axis_center_point - self.R1

        if (self.types[0] == 2):
            start_x_R1 = int(self.surface_width/2) - self.R1
            start_y_R1 =      self.axis_center_point - self.R1
            angle_start_R1, angle_end_R1 = angle_end_R1, angle_start_R1

        start_x_R2 = int(self.surface_width/2) + self.R2 + self.width
        # start_y_R2 =      self.axis_center_point - self.R2
        if (self.types[1] == 1):
            start_x_R2 = int(self.surface_width/2) - self.R2 + self.width
            # start_y_R2 =      self.axis_center_point - self.R2

            angle_start_R2, angle_end_R2 = angle_end_R2, angle_start_R2


        if (self.types[0] == 3):
            point_1_x = int(self.surface_width/2) + self.R1 / 12
        else:
            point_1_x = start_x_R1 + self.R1 * math.cos(angle_end_R1)
        point_1_y = self.axis_center_point + self.R1 * math.sin(angle_end_R1)
        point_1 = (point_1_x ,point_1_y)

        if (self.types[1] == 3):
            point_2_x = int(self.surface_width/2) + self.R2 / 24  + self.width
        else:
            point_2_x = start_x_R2 + self.R2 * math.cos(angle_end_R2)
        point_2_y = self.axis_center_point + self.R2 * math.sin(angle_end_R2)
        point_2 = (point_2_x,point_2_y)

        if (self.types[0] == 3):
            point_3_x = int(self.surface_width/2) + self.R1 / 12
        else:
            point_3_x = start_x_R1 + self.R1 * math.cos(angle_start_R1)
        point_3_y = self.axis_center_point + self.R1 * math.sin(angle_start_R1)
        point_3 = (point_3_x,point_3_y)


        if (self.types[1] == 3):
            point_4_x = int(self.surface_width/2) + self.R2 / 24  + self.width
        else:
            point_4_x = start_x_R2 + self.R2 * math.cos(angle_start_R2)
        point_4_y = self.axis_center_point + self.R2 * math.sin(angle_start_R2)
        point_4 = (point_4_x,point_4_y
                               )


        pygame.draw.line(self.surface, self.colors['border'], point_1, point_2, self.border_size)
        pygame.draw.line(self.surface, self.colors['border'], point_3, point_4,self.border_size)


        #Фаски
        #Левая
        if (self.left_facet_type != 0 ):
            pygame.draw.rect(self.surface, self.colors['transparent'],
                             pygame.Rect(point_1[0] - self.left_facet_size/2,
                                         point_1[1],
                                         self.left_facet_size,
                                         self.left_facet_size))

            pygame.draw.rect(self.surface, self.colors['transparent'],
                             pygame.Rect(point_3[0] - self.left_facet_size / 2,
                                         point_3[1] - self.left_facet_size + self.border_size,
                                         self.left_facet_size,
                                         self.left_facet_size))

            if (self.types[0] == 1):
                facet_angle_start_R1 = -math.asin((self.diametr - self.left_facet_size * 2) / (2 * self.R1)) + math.pi
                facet_angle_end_R1 = math.asin((self.diametr - self.left_facet_size * 2) / (2 * self.R1)) + math.pi
            else:
                facet_angle_end_R1 = -math.asin((self.diametr - self.left_facet_size * 2) / (2 * self.R1))
                facet_angle_start_R1 = math.asin((self.diametr - self.left_facet_size * 2) / (2 * self.R1))

            if (self.types[0] == 3):
                facet_point_1_x = int(self.surface_width/2) + self.R1 / 12
            else:
                facet_point_1_x = start_x_R1 + self.R1 * math.cos(facet_angle_end_R1)
            facet_point_1_y = self.axis_center_point + self.R1 * math.sin(facet_angle_end_R1)
            facet_point_1 = (facet_point_1_x, facet_point_1_y)

            if (self.types[0] == 3):
                facet_point_3_x = int(self.surface_width/2) + self.R1 / 12
            else:
                facet_point_3_x = start_x_R1 + self.R1 * math.cos(facet_angle_start_R1)
            facet_point_3_y = self.axis_center_point + self.R1 * math.sin(facet_angle_start_R1)
            facet_point_3 = (facet_point_3_x, facet_point_3_y)


            if (self.left_facet_type == 1):
                if (self.types[0] == 2 ):
                    pygame.draw.line(self.surface, self.colors['border'],
                                     (point_1[0] + self.left_facet_size / 2, point_1[1]),
                                     (facet_point_1[0], point_1[1]), self.border_size)
                    pygame.draw.line(self.surface, self.colors['border'],
                                     (facet_point_1[0], point_1[1]),
                                     facet_point_1, self.border_size)

                    pygame.draw.line(self.surface, self.colors['border'],
                                     (point_3[0] + self.left_facet_size / 2, point_3[1]),
                                     (facet_point_3[0], point_3[1]), self.border_size)
                    pygame.draw.line(self.surface, self.colors['border'],
                                     (facet_point_3[0], point_3[1]),
                                     facet_point_3, self.border_size)


            if (self.left_facet_type == 2):

                pygame.draw.line(self.surface, self.colors['border'], (point_1[0] + self.left_facet_size/2, point_1[1]),
                                 facet_point_1, self.border_size)
                pygame.draw.line(self.surface, self.colors['border'],
                                 (point_3[0] + self.left_facet_size / 2, point_3[1]),
                                 facet_point_3, self.border_size)

        #Правая
        if (self.right_facet_type != 0 ):
            pygame.draw.rect(self.surface, self.colors['transparent'],
                             pygame.Rect(point_2[0] - self.right_facet_size/2,
                                         point_2[1] ,
                                         self.right_facet_size,
                                         self.right_facet_size ))

            pygame.draw.rect(self.surface, self.colors['transparent'],
                             pygame.Rect(point_4[0] - self.right_facet_size/2,
                                         point_4[1] - self.right_facet_size + self.border_size,
                                         self.right_facet_size , self.right_facet_size
                                         ))

            if (self.types[1] == 1):
                 facet_angle_end_R2= -math.asin( (self.diametr - self.right_facet_size*2) / (2 * self.R2))
                 facet_angle_start_R2 = math.asin((self.diametr - self.right_facet_size*2) / (2 * self.R2))
            else:
                facet_angle_start_R2 = -math.asin((self.diametr - self.right_facet_size*2) / (2 * self.R2)) + math.pi
                facet_angle_end_R2= math.asin((self.diametr - self.right_facet_size*2) / (2 * self.R2)) + math.pi



            if (self.types[1] == 3):
                facet_point_2_x = int(self.surface_width/2) + self.R2 / 24 + self.width
            else:
                facet_point_2_x = start_x_R2 + self.R2 * math.cos(facet_angle_end_R2)
            facet_point_2_y = self.axis_center_point + self.R2 * math.sin(facet_angle_end_R2)
            facet_point_2 = (facet_point_2_x, facet_point_2_y)

            if (self.types[1] == 3):
                facet_point_4_x = int(self.surface_width/2) + self.R2 / 24 + self.width
            else:
                facet_point_4_x = start_x_R2 + self.R2 * math.cos(facet_angle_start_R2)
            facet_point_4_y = self.axis_center_point + self.R2 * math.sin(facet_angle_start_R2) - 2
            facet_point_4 = (facet_point_4_x,
                       facet_point_4_y)


            if (self.right_facet_type == 1):
                if (self.types[1] == 2):
                    pygame.draw.line(self.surface, self.colors['border'],
                                     (point_2[0] + self.right_facet_size / 2, point_2[1]),
                                     (facet_point_2[0], point_2[1]), self.border_size)
                    pygame.draw.line(self.surface, self.colors['border'],
                                     (facet_point_2[0], point_2[1]),
                                     facet_point_2, self.border_size)

                    pygame.draw.line(self.surface, self.colors['border'],
                                     (point_4[0] + self.right_facet_size / 2, point_4[1]),
                                     (facet_point_4[0], point_4[1]), self.border_size)
                    pygame.draw.line(self.surface, self.colors['border'],
                                     (facet_point_4[0], point_4[1]),
                                     facet_point_4, self.border_size)


            if (self.right_facet_type == 2):

                pygame.draw.line(self.surface, self.colors['border'], (point_2[0] - self.right_facet_size/2, point_2[1]),
                                 facet_point_2, self.border_size)
                pygame.draw.line(self.surface, self.colors['border'],
                                 (point_4[0] - self.right_facet_size/2, point_4[1]),
                                 facet_point_4, self.border_size)

        # #Отображение размеров
        # if (self.show_measure):
        #
        #     self.draw_measure((key_point_1[0], key_point_1[1] ), key_point_2[0] - key_point_1[0] + 5, self.diametr, text=str(self.width))
        #
        #     self.draw_measure((start_x_R1 + self.R1 * math.cos(angle_start_R1),
        #                        self.axis_center_point + self.R1 * math.sin(angle_start_R1) + self.diametr + 10 ),
        #                       self.diametr + 5, self.diametr + 5, angle_rotate= - 90,
        #                       text=str(self.diametr))

        self.screen.blit(self.surface, (self.point_x, self.point_y))


    def __init__(self, screen, colors, start_point, width, diametr, R1, R2,
                 border_size, type, font = None, axis_center_point = 400, show_measure = True,
                 left_facet_type = 0, right_facet_type = 0, left_facet_size = 40, right_facet_size = 40):

        self.font = font

        self.colors = colors
        self.screen = screen
        self.surface = pygame.Surface(( 2*R1 if R1>R2 else 2*R2, 4*R1 if R1>R2 else 4*R2), pygame.SRCALPHA)

        self.point_x = start_point[0]
        self.point_y = start_point[1]
        self.width = width
        self.diametr = diametr
        self.R1 = R1
        self.R2 = R2
        self.border_size = border_size
        self.axis_center_point = axis_center_point
        self.show_measure = show_measure

        self.left_facet_type = left_facet_type
        self.right_facet_type = right_facet_type

        self.left_facet_size = left_facet_size
        self.right_facet_size = right_facet_size

        # self.left_facet_height = left_facet_size
        # self.left_facet_wight = left_facet_size

        # self.right_facet_height = right_facet_size
        # self.right_facet_wight = right_facet_size

        # Фаски
        # 0 - Никакая
        # 1 - Плоская
        # 2 - Диагональная



        # self.lens_type = {
        #     'flat convex': (3, 1),
        #     'convex flat': (1, 3),
        #     'concave flat': (2, 3),
        #     'flat concave': (3, 2),
        #     'biconvex': (1, 1),
        #     'biconcave': (2, 2),
        #     'convex concave': (3, 3),
        #     'concave convex': (3, 3),
        #     'prism': (3, 3),
        #     'meniscus': (1, 2),
        #     'window prism': (3, 3)
        # }

        self.lens_type = {
            1: (3, 1),
            2: (1, 3),
            3: (2, 3),
            4: (3, 2),
            5: (1, 1),
            6: (2, 2),
            7: (3, 3),
            8: (3, 3),
            9: (3, 3),
            10: (1, 2),
            11: (3, 3)
        }


        # Линзы
        # 1 - Выпуклая
        # 2 - Впуклая
        # 3 - Прямая
        self.type = 7

        self.types = self.lens_type[self.type]





