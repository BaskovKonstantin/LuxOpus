import pygame
import math
from figure.facet_measure import facet_measure
from figure.cover_measure import cover_measure
from figure.roughness_measure import roughness_measure
from figure.arrow import arrow
from figure.measure import line_measure
from figure.dash_line import dashed_line

class lens:


    def check_click(self, click_pos):

        left_point = (int(self.surface_width/2) + self.R1/12, self.axis_center_point - self.diametr/2)
        right_point = (int(self.surface_width/2) + self.width + self.R2/24,self.axis_center_point + self.diametr/2)

        if (self.show_measure):
            for key in self.measureDict.keys():
                offset_pos = (
                    click_pos[0] - self.measureDict[key].blit_point[0],
                    click_pos[1] - self.measureDict[key].blit_point[1]
                )
                if (self.measureDict[key].check_click(offset_pos)):
                    self.select_measure = True
                    self.selected_measure = self.measureDict[key]
                    return True

        self.select_measure = False
        self.selected_measure = None
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

    def drawLens(self, scale = 1):
        self.types = self.lens_type[self.type]

        self.surface = pygame.Surface(
            (3 * self.R1 if self.R1 > self.R2 else 3 * self.R2, 3 * self.R1 if self.R1 >self. R2 else 3 * self.R2), pygame.SRCALPHA)

        self.surface_width = self.surface.get_width()
        dash_length = 10
        dash_gap = 5


        arrow_height = 15
        angle_start_R1 = 0
        angle_start_R2 = 0
        angle_end_R1 = 0
        angle_end_R2 = 0

        #Отображение размеров
        if (self.show_streak):

            hatching_unit_side_size = 30
            step = 15
            hatching_unit = self.get_hatching_unit(side_size = hatching_unit_side_size)

            for position_x in range( int(self.surface_width/2) , int(self.surface_width/2) + self.width, hatching_unit_side_size + step):

                for position_y in range(int(self.axis_center_point - self.diametr/2), int(self.axis_center_point + self.diametr/2), hatching_unit_side_size + step):
                    self.surface.blit(hatching_unit, (position_x, position_y))
            pygame.draw.rect(self.surface, self.colors['transparent'], pygame.Rect( int(self.surface_width/2), int(self.axis_center_point + self.diametr/2), self.width, hatching_unit_side_size) )

        #Левый
        if (self.types[0] == 1):
            if (self.show_streak):
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
            self.key_point_1 = (int(self.surface_width/2), self.axis_center_point)
        if (self.types[0] == 2):
            if (self.show_streak):
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
            if (self.show_streak):
                pygame.draw.circle(self.surface, self.colors['transparent'],
                                   (int(self.surface_width/2) - self.R1,
                                    (self.axis_center_point )), self.R1)
            pygame.draw.arc(self.surface, self.colors['border'], rect, angle_start_R1, angle_end_R1, self.border_size)
            # pygame.draw.arc(self.surface, self.colors['border'], rect, math.pi/2, -math.pi/2 ,self.border_size)

            self.key_point_1 = (int(self.surface_width/2) , self.axis_center_point)
        if (self.types[0] == 3):
            if (self.show_streak):
                pygame.draw.rect(self.surface, self.colors['transparent'],
                                 pygame.Rect( int(self.surface_width/2),
                                              int(self.axis_center_point - self.diametr/2),
                                              self.R1/12, self.diametr) )

            pygame.draw.line(self.surface,self.colors['border'],
                             (int(self.surface_width/2) + self.R1/12, self.axis_center_point - self.diametr/2),
                             (int(self.surface_width/2) + self.R1/12, self.axis_center_point + self.diametr/2), self.border_size )
            angle_start_R1 = -math.asin(self.diametr / (2 * self.R1)) + math.pi
            angle_end_R1 = math.asin(self.diametr / (2 * self.R1)) + math.pi

            self.key_point_1 = (int(self.surface_width/2) + self.R1/12, self.axis_center_point)


        # Правый
        if (self.types[1] == 1):
            if (self.show_streak):
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

            self.key_point_2 = (int(self.surface_width/2) + self.width,
                               self.axis_center_point)
        if (self.types[1] == 2):
            if (self.show_streak):
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

            if (self.show_streak):
                pygame.draw.circle(self.surface, self.colors['transparent'],
                                   (int(self.surface_width/2) + self.width + self.R2,
                                    (self.axis_center_point )), self.R2)

            pygame.draw.arc(self.surface, self.colors['border'], rect, angle_start_R2, angle_end_R2, self.border_size)
            # pygame.draw.arc(self.surface, self.colors['border'], rect, math.pi/2, -math.pi/2 ,self.border_size)

            self.key_point_2 = (int(self.surface_width/2) + self.width,
                               self.axis_center_point)
        if (self.types[1] == 3):
            if (self.show_streak):
                pygame.draw.rect(self.surface, self.colors['transparent'],
                                 pygame.Rect( int(self.surface_width/2) + self.width + self.R2/24,
                                              int(self.axis_center_point - self.diametr/2),
                                              self.R2/12, self.diametr) )


            pygame.draw.line(self.surface,self.colors['border'],
                             (int(self.surface_width/2) + self.width + self.R2/24 ,self.axis_center_point - self.diametr/2),
                             (int(self.surface_width/2) + self.width + self.R2/24,self.axis_center_point + self.diametr/2), self.border_size )
            angle_start_R2 = -math.asin(self.diametr / (2 * self.R2)) + math.pi
            angle_end_R2 = math.asin(self.diametr / (2 * self.R2)) + math.pi

            self.key_point_2 = (int(self.surface_width/2) + self.width + self.R2/24, self.axis_center_point)

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
        point_4 = (point_4_x,point_4_y)


        pygame.draw.line(self.surface, self.colors['border'], point_1, point_2, self.border_size)
        pygame.draw.line(self.surface, self.colors['border'], point_3, point_4,self.border_size)


        #Фаски
        #Левая
        if (self.left_facet_type != 0 ):

            if (self.types[0] == 1):

                facet_angle_start_R1 = -math.asin(
                    (self.diametr - self.left_facet_size * 2) / (2 * self.R1)) + math.pi
                facet_angle_end_R1 = math.asin(
                    (self.diametr - self.left_facet_size * 2) / (2 * self.R1)) + math.pi
            else:
                facet_angle_end_R1 = -math.asin((self.diametr - self.left_facet_size * 2) / (2 * self.R1))
                facet_angle_start_R1 = math.asin((self.diametr - self.left_facet_size * 2) / (2 * self.R1))

            if (self.types[0] == 3):
                facet_point_1_x = int(self.surface_width / 2) + self.R1 / 12
            else:
                facet_point_1_x = start_x_R1 + self.R1 * math.cos(facet_angle_end_R1)
            facet_point_1_y = self.axis_center_point + self.R1 * math.sin(facet_angle_end_R1)
            self.facet_point_1 = (facet_point_1_x, facet_point_1_y)

            if (self.types[0] == 3):
                facet_point_3_x = int(self.surface_width / 2) + self.R1 / 12
            else:
                facet_point_3_x = start_x_R1 + self.R1 * math.cos(facet_angle_start_R1)
            facet_point_3_y = self.axis_center_point + self.R1 * math.sin(facet_angle_start_R1)
            self.facet_point_3 = (facet_point_3_x, facet_point_3_y)

            if (self.left_facet_type == 1):
                if (self.types[0] == 2 ):
                    pygame.draw.rect(self.surface, self.colors['transparent'],
                                     pygame.Rect(point_1[0] - self.left_facet_size / 2,
                                                 point_1[1] - 2 * self.border_size,
                                                 self.left_facet_size,
                                                 self.left_facet_size + 2 * self.border_size))

                    pygame.draw.rect(self.surface, self.colors['transparent'],
                                     pygame.Rect(point_3[0] - self.left_facet_size / 2,
                                                 point_3[1] - self.left_facet_size + self.border_size,
                                                 self.left_facet_size,
                                                 self.left_facet_size))




                    pygame.draw.line(self.surface, self.colors['border'],
                                     (point_1[0] + self.left_facet_size / 2, point_1[1]),
                                     (self.facet_point_1[0], point_1[1]), self.border_size)
                    pygame.draw.line(self.surface, self.colors['border'],
                                     (self.facet_point_1[0], point_1[1]),
                                     self.facet_point_1, self.border_size)

                    pygame.draw.line(self.surface, self.colors['border'],
                                     (point_3[0] + self.left_facet_size / 2, point_3[1]),
                                     (self.facet_point_3[0], point_3[1]), self.border_size)
                    pygame.draw.line(self.surface, self.colors['border'],
                                     (self.facet_point_3[0], point_3[1]),
                                     self.facet_point_3, self.border_size)

        #Правая
        if (self.right_facet_type != 0 ):

            if (self.types[1] == 1):
                facet_angle_end_R2 = -math.asin((self.diametr - self.right_facet_size * 2) / (2 * self.R2))
                facet_angle_start_R2 = math.asin((self.diametr - self.right_facet_size * 2) / (2 * self.R2))
            else:
                facet_angle_start_R2 = -math.asin(
                    (self.diametr - self.right_facet_size * 2) / (2 * self.R2)) + math.pi
                facet_angle_end_R2 = math.asin(
                    (self.diametr - self.right_facet_size * 2) / (2 * self.R2)) + math.pi

            if (self.types[1] == 3):
                facet_point_2_x = int(self.surface_width / 2) + self.R2 / 24 + self.width
            else:
                facet_point_2_x = start_x_R2 + self.R2 * math.cos(facet_angle_end_R2)
            facet_point_2_y = self.axis_center_point + self.R2 * math.sin(facet_angle_end_R2)
            self.facet_point_2 = (facet_point_2_x, facet_point_2_y)

            if (self.types[1] == 3):
                facet_point_4_x = int(self.surface_width / 2) + self.R2 / 24 + self.width
            else:
                facet_point_4_x = start_x_R2 + self.R2 * math.cos(facet_angle_start_R2)
            facet_point_4_y = self.axis_center_point + self.R2 * math.sin(facet_angle_start_R2) - 2
            self.facet_point_4 = (facet_point_4_x,
                                  facet_point_4_y)

            if (self.right_facet_type == 1):

                if (self.types[1] == 2):
                    pygame.draw.rect(self.surface, self.colors['transparent'],
                                     pygame.Rect(point_2[0] - self.right_facet_size / 2 - 2 * self.border_size,
                                                 point_2[1] - 2 * self.border_size,
                                                 self.right_facet_size + 2 * self.border_size,
                                                 self.right_facet_size + 2 * self.border_size))

                    pygame.draw.rect(self.surface, self.colors['transparent'],
                                     pygame.Rect(point_4[0] - self.right_facet_size / 2 - 2 * self.border_size,
                                                 point_4[1] - self.right_facet_size + self.border_size,
                                                 self.right_facet_size + 2 * self.border_size,
                                                 self.right_facet_size + 2 * self.border_size))



                    pygame.draw.line(self.surface, self.colors['border'],
                                     (self.facet_point_2[0], point_2[1]),
                                     self.facet_point_2, self.border_size)


                    pygame.draw.line(self.surface, self.colors['border'],
                                     (self.facet_point_4[0], point_4[1]),
                                     self.facet_point_4, self.border_size)

        # #Отображение размеров
        if (self.show_measure):
            ...
            dashed_line(self.surface, self.colors['border'],
                        (int(self.surface.get_width() * 0.4), self.axis_center_point),
                        (int(self.surface.get_width() * 0.9), self.axis_center_point), width=self.border_size,
                        dash_length=dash_length)

            self.draw_faset_measure()
            self.draw_base_measure()



        # print('self.axis_center_point', self.axis_center_point)


        # self.screen.blit(
        #     pygame.transform.scale(self.surface,
        #                            (self.surface.get_width()*scale, self.surface.get_height()*scale) ),
        #     (self.point_x, self.point_y))

        self.screen.blit(
            self.surface,
            (self.point_x, self.point_y))


    def draw_faset_measure(self):

        if (self.right_facet_type == 1):
            if (self.right_facet_measure_type == 1):
                if not ('facet_right_side_measure' in self.measureDict.keys()):
                    self.measureDict['facet_right_side_measure'] = \
                        line_measure(self.surface,
                                     self.facet_point_4,
                                     self.facet_point_2,
                                     self.colors,
                                     int(self.facet_point_4[1] - self.facet_point_2[1] + 4*self.border_size),
                                     text=str(self.diametr), font=self.font,
                                     angle_rotate=-90)
                    self.measureDict['facet_right_side_measure'].measure_shift = 100
                else:
                    try:
                        self.measureDict['facet_right_side_measure'].start_point = self.facet_point_4
                        self.measureDict['facet_right_side_measure'].end_point = self.facet_point_2
                        self.measureDict['facet_right_side_measure'].width = int(self.facet_point_4[1] - self.facet_point_2[1] + 4*self.border_size)

                        self.measureDict['facet_right_side_measure'].draw()
                        self.surface.blit(self.measureDict['facet_right_side_measure'].measure_surface,
                                          self.measureDict['facet_right_side_measure'].blit_point)
                    except:
                        pass

            if (self.right_facet_measure_type == 2):
                width = self.facet_point_2[0] - self.key_point_1[0] + self.border_size*2
                if not ('facet_right_up_big_measure' in self.measureDict.keys()):

                    self.measureDict['facet_right_up_big_measure'] = \
                        line_measure(self.surface,
                                     (self.key_point_1[0],self.key_point_1[1] - self.diametr/2),
                                     (self.key_point_1[0], self.key_point_1[1] - self.diametr),
                                     self.colors, width, text=str(self.width), font=self.font)
                else:

                    self.measureDict['facet_right_up_big_measure'].start_point = (self.key_point_1[0],self.key_point_1[1] - self.diametr/2)
                    self.measureDict['facet_right_up_big_measure'].end_point = (self.key_point_1[0], self.key_point_1[1] - self.diametr)
                    self.measureDict['facet_right_up_big_measure'].width = width
                    # self.measureDict['facet_right_up_measure'].text = str(self.width)

                    self.measureDict['facet_right_up_big_measure'].draw()
                    self.surface.blit(self.measureDict['facet_right_up_big_measure'].measure_surface,
                                      self.measureDict['facet_right_up_big_measure'].blit_point)

            if (self.right_facet_measure_type == 3):
                width = self.facet_point_2[0] - ( self.key_point_1[0] + self.width) + self.border_size*2
                if not ('facet_right_up_small_measure' in self.measureDict.keys()):

                    self.measureDict['facet_right_up_small_measure'] = \
                        line_measure(self.surface,
                                     (self.key_point_1[0] + self.width,self.key_point_1[1] - self.diametr/2),
                                     (self.key_point_1[0]  + self.width,self.key_point_1[1], self.key_point_1[1] - self.diametr),
                                     self.colors, width, arrow_height= 4, text=str(2), font_size= 15, font=self.font)

                    self.measureDict['facet_right_up_small_measure'].measure_shift = 50
                else:
                    try:
                        self.measureDict['facet_right_up_small_measure'].start_point =(self.key_point_1[0] + self.width,self.key_point_1[1] - self.diametr/2)
                        self.measureDict['facet_right_up_small_measure'].end_point = (self.key_point_1[0] + self.width, self.key_point_1[1] - self.diametr)
                        self.measureDict['facet_right_up_small_measure'].width = width
                        # self.measureDict['facet_right_up_measure'].text = str(self.width)

                        self.measureDict['facet_right_up_small_measure'].draw()
                        self.surface.blit(self.measureDict['facet_right_up_small_measure'].measure_surface,
                                          self.measureDict['facet_right_up_small_measure'].blit_point)
                    except:
                        pass

        if (self.left_facet_type == 1):

            if (self.left_facet_measure_type == 1):
                if not ('facet_left_side_measure' in self.measureDict.keys()):
                    self.measureDict['facet_left_side_measure'] = \
                        line_measure(self.surface,
                                     (self.facet_point_3[0] - 100, self.facet_point_3[1] - self.border_size),
                                     (self.facet_point_1[0] - 100, self.facet_point_1[1] - self.border_size) ,
                                     self.colors, int(self.facet_point_3[1] - self.facet_point_1[1] - 2*self.border_size), text=str(self.diametr), font=self.font,
                                     angle_rotate= 90)
                    self.measureDict['facet_left_side_measure'].measure_shift = 100
                else:
                    try:
                        self.measureDict['facet_left_side_measure'].start_point = (self.facet_point_3[0] - 100, self.facet_point_3[1] - self.border_size)
                        self.measureDict['facet_left_side_measure'].end_point = (self.facet_point_1[0] - 100, self.facet_point_1[1] - self.border_size)
                        self.measureDict['facet_left_side_measure'].width = int(self.facet_point_3[1] - self.facet_point_1[1] + 2*self.border_size)


                        self.measureDict['facet_left_side_measure'].draw()
                        self.surface.blit(self.measureDict['facet_left_side_measure'].measure_surface,
                                          self.measureDict['facet_left_side_measure'].blit_point)
                    except:
                        pass

            if (self.left_facet_measure_type == 2):
                width = self.key_point_2[0] - self.facet_point_1[0]  + 2*self.border_size*2
                if not ('facet_left_up_big_measure' in self.measureDict.keys()):

                    self.measureDict['facet_left_up_big_measure'] = \
                        line_measure(self.surface,
                                     (self.facet_point_1[0],self.key_point_1[1] - self.diametr/2),
                                     (self.facet_point_1[0], self.key_point_1[1] - self.diametr),
                                     self.colors, width, text=str(self.width), font=self.font)
                else:

                    self.measureDict['facet_left_up_big_measure'].start_point = (self.facet_point_1[0],self.key_point_1[1] - self.diametr/2)
                    self.measureDict['facet_left_up_big_measure'].end_point = (self.facet_point_1[0], self.key_point_1[1] - self.diametr)
                    self.measureDict['facet_left_up_big_measure'].width = width

                    self.measureDict['facet_left_up_big_measure'].draw()
                    self.surface.blit(self.measureDict['facet_left_up_big_measure'].measure_surface,
                                      self.measureDict['facet_left_up_big_measure'].blit_point)

            if (self.left_facet_measure_type == 3):
                width = ( self.key_point_1[0] ) - self.facet_point_1[0] + self.border_size*2
                if not ('facet_left_up_small_measure' in self.measureDict.keys()):

                    self.measureDict['facet_left_up_small_measure'] = \
                        line_measure(self.surface,
                                     (self.facet_point_1[0] ,self.key_point_1[1] - self.diametr/2),
                                     (self.facet_point_1[0]  ,self.key_point_1[1], self.key_point_1[1] - self.diametr),
                                     self.colors, width, arrow_height= 4, text=str(2), font_size= 15, font=self.font)

                    self.measureDict['facet_left_up_small_measure'].measure_shift = 50
                else:
                    self.measureDict['facet_left_up_small_measure'].start_point =(self.facet_point_1[0] ,self.key_point_1[1] - self.diametr/2)
                    self.measureDict['facet_left_up_small_measure'].end_point = (self.facet_point_1[0] , self.key_point_1[1] - self.diametr)
                    self.measureDict['facet_left_up_small_measure'].width = width
                    # self.measureDict['facet_left_up_measure'].text = str(self.width)

                    self.measureDict['facet_left_up_small_measure'].draw()
                    self.surface.blit(self.measureDict['facet_left_up_small_measure'].measure_surface,
                                      self.measureDict['facet_left_up_small_measure'].blit_point)

        size = (60,80)
        if (self.right_facet_type == 2):
            if not ('facet_right_measure' in self.measureDict.keys()):
                self.measureDict['facet_right_measure'] =\
                    facet_measure(
                                self.surface,
                                self.colors,
                        (self.facet_point_2[0] + size[0]/3,self.facet_point_2[1] - self.diametr/2 ),
                        size = size,
                                 text=str('Upp'), font=self.font,)

            else:
                try:
                    self.measureDict['facet_right_measure'].blit_point = (self.facet_point_2[0] + size[0]/3,self.facet_point_2[1] - self.diametr/2 )
                    self.measureDict['facet_right_measure'].draw()
                    self.surface.blit(self.measureDict['facet_right_measure'].surface,
                                      self.measureDict['facet_right_measure'].blit_point)
                except:
                    pass

        size = (60,80)
        if (self.left_facet_type == 2):
            if not ('facet_left_measure' in self.measureDict.keys()):
                self.measureDict['facet_left_measure'] =\
                    facet_measure(
                                self.surface,
                                self.colors,
                        (self.facet_point_1[0] + size[0]/3,self.facet_point_1[1] - self.diametr/2 ),
                        size = size,
                                 text=str('Upp'), font=self.font,)

            else:
                try:
                    self.measureDict['facet_left_measure'].blit_point = (self.facet_point_1[0] - size[0]/2,self.facet_point_1[1] - self.diametr/2 )
                    self.measureDict['facet_left_measure'].draw()
                    self.surface.blit(self.measureDict['facet_left_measure'].surface,
                                      self.measureDict['facet_left_measure'].blit_point)
                except:
                    pass
    def draw_base_measure(self):


        measure_width = self.key_point_2[0] - self.key_point_1[0] + 5

        if not ('up_measure' in self.measureDict.keys()):
            self.measureDict['up_measure'] = \
                line_measure(self.surface,
                                          self.key_point_1,
                                        (self.key_point_1[0], self.key_point_1[1] - self.diametr),
                                          self.colors, measure_width, text=str(self.width), font=self.font)
        else:
            self.measureDict['up_measure'].start_point = self.key_point_1
            self.measureDict['up_measure'].end_point = (self.key_point_1[0], self.key_point_1[1] - self.diametr)
            self.measureDict['up_measure'].width = measure_width
            self.measureDict['up_measure'].text = str(self.width)

            self.measureDict['up_measure'].draw()
            self.surface.blit(self.measureDict['up_measure'].measure_surface, self.measureDict['up_measure'].blit_point)

        if not ('side_measure' in self.measureDict.keys()):
            self.measureDict['side_measure'] = \
                line_measure(self.surface,
                             (self.key_point_1[0], self.key_point_1[1] - 20 + self.diametr/2),
                                        (self.key_point_1[0] , self.key_point_1[1] - self.diametr/2),
                                          self.colors, self.diametr + self.border_size*2, text=str(self.diametr), font=self.font,
                             angle_rotate=-90)
            self.measureDict['side_measure'].measure_shift = 250
        else:
            self.measureDict['side_measure'].start_point = (self.key_point_1[0], self.key_point_1[1] - 20 + self.diametr/2)
            self.measureDict['side_measure'].end_point = (self.key_point_1[0] , self.key_point_1[1] - self.diametr/2)
            self.measureDict['side_measure'].width = self.diametr + self.border_size*2
            self.measureDict['side_measure'].text = '' + str(self.diametr)
            self.measureDict['side_measure'].draw()
            self.surface.blit(self.measureDict['side_measure'].measure_surface, self.measureDict['side_measure'].blit_point)
        if (self.types[0] !=3):
            if not ('R1_measure' in self.measureDict.keys()):

                radius_width = 150
                self.measureDict['R1_measure'] = arrow(
                    (int(self.surface_width/2 - radius_width - radius_width),
                     self.axis_center_point ), self.surface,
                                        self.colors, size = (radius_width, 10), font = self.font,
                                        text = f'R{self.R1}', angle_rotate=0)
            else:

                # self.measureDict['R1_measure'].angle_rotate += 1

                self.measureDict['R1_measure'].draw()
                self.surface.blit(self.measureDict['R1_measure'].arrow_surface,
                                  self.measureDict['R1_measure'].blit_point)
        if (self.types[1] !=3):
            if not ('R2_measure' in self.measureDict.keys()):


                radius_width = 150
                self.measureDict['R2_measure'] = arrow((int(self.surface_width/2 + self.width - radius_width),
                                                        self.axis_center_point ), self.surface,
                                        self.colors, size = (radius_width, 10), font = self.font,
                                        text = f'R{self.R1}', opposite=True)
            else:

                self.measureDict['R2_measure'].draw()
                self.surface.blit(self.measureDict['R2_measure'].arrow_surface,
                                  self.measureDict['R2_measure'].blit_point)

        if (self.types[0] !=3):
            if not ('roughness_measure_1' in self.measureDict.keys()):

                roughness_measure_size = (60,60)

                if (self.types[0] == 2):
                    self.circle_center_roughness_measure_1 = (int(self.surface_width/2) - self.R1,
                                        self.axis_center_point )
                    angle = 25


                    point = (self.circle_center_roughness_measure_1[0] + self.R1*math.cos( math.radians(angle) ) ,
                             self.circle_center_roughness_measure_1[1] + self.R1*math.sin( math.radians(angle) ) )
                    angle = -90
                if (self.types[0] == 1):
                    self.circle_center_roughness_measure_1 = (int(self.surface_width / 2) + self.R1,
                                          self.axis_center_point)
                    angle = 20


                    point = (self.circle_center_roughness_measure_1[0] - self.R1 * math.cos(math.radians(angle) ) - 1.3*roughness_measure_size[0],
                             self.circle_center_roughness_measure_1[1] - self.R1 * math.sin(math.radians(angle)))
                    angle = -90

                self.measureDict['roughness_measure_1'] = \
                    roughness_measure(self.surface, self.colors,
                                    point,
                                    size = roughness_measure_size,
                                    angle_rotate=-angle,
                                    font = self.font,
                                    text_method = 'T1',
                                    text_base_len = 'B1',
                                    text_designation = 'D1')
            else:
                if (self.types[0] == 2):
                    self.circle_center_roughness_measure_1 = (int(self.surface_width/2) - self.R1,
                                        self.axis_center_point )
                    angle = 5

                    # self.measureDict['roughness_measure_1'].blit_point = \
                    #     (self.circle_center_roughness_measure_1[0] + self.R1*math.cos( math.radians(angle) )
                    #      - 1.2*self.measureDict['roughness_measure_1'].height,
                    #          self.circle_center_roughness_measure_1[1] + self.R1*math.sin( math.radians(angle) ) )

                if (self.types[0] == 1):
                    self.circle_center_roughness_measure_1 = (int(self.surface_width / 2) + self.R1,
                                          self.axis_center_point)
                    angle = 20


                    # self.measureDict['roughness_measure_1'].blit_point = \
                    #     (self.circle_center_roughness_measure_1[0] - self.R1 * math.cos(math.radians(angle)) -
                    #      1.2*self.measureDict['roughness_measure_1'].height,
                    #          self.circle_center_roughness_measure_1[1] - self.R1 * math.sin(math.radians(angle)))


                self.measureDict['roughness_measure_1'].draw()
                self.surface.blit(self.measureDict['roughness_measure_1'].surface,
                                  (self.measureDict['roughness_measure_1'].blit_point[0] ,
                                   self.measureDict['roughness_measure_1'].blit_point[1] ))
        if (self.types[1] !=3):
            if not ('roughness_measure_2' in self.measureDict.keys()):

                roughness_measure_size = (60,60)

                if (self.types[1] == 2):
                    self.circle_center_roughness_measure_2 = (int(self.surface_width/2) + self.width + self.R2,
                                        self.axis_center_point )
                    angle = 25

                    point = (self.circle_center_roughness_measure_2[0] - self.R2*math.cos( math.radians(angle) ) ,
                             self.circle_center_roughness_measure_2[1] - self.R2*math.sin( math.radians(angle) ) )
                    angle = 90
                if (self.types[1] == 1):
                    self.circle_center_roughness_measure_2 = (int(self.surface_width / 2) + self.width - self.R2,
                                          self.axis_center_point)
                    angle = 25


                    point = (self.circle_center_roughness_measure_2[0] + self.R2 * math.cos(math.radians(angle)),
                             self.circle_center_roughness_measure_2[1] + self.R2 * math.sin(math.radians(angle)))
                    angle = 90

                self.measureDict['roughness_measure_2'] = \
                    roughness_measure(self.surface, self.colors,
                                    point,
                                    size = roughness_measure_size,
                                    angle_rotate=-angle,
                                    font = self.font,
                                    text_method = 'T1',
                                    text_base_len = 'B1',
                                    text_designation = 'D1')
            else:
                if (self.types[1] == 2):
                    self.circle_center_roughness_measure_2 = (int(self.surface_width/2) + self.width + self.R2,
                                        self.axis_center_point )
                    angle = 25

                    # self.measureDict['roughness_measure_2'].blit_point = (self.circle_center_roughness_measure_2[0]
                    #                                                       - self.R2*math.cos( math.radians(angle) ) ,
                    #          self.circle_center_roughness_measure_2[1] -
                    #                                                       self.R2*math.sin( math.radians(angle) ) )

                if (self.types[1] == 1):
                    self.circle_center_roughness_measure_2 = (int(self.surface_width / 2) + self.width - self.R2,
                                          self.axis_center_point)
                    angle = 15


                self.measureDict['roughness_measure_2'].draw()
                self.surface.blit(self.measureDict['roughness_measure_2'].surface,
                                  (self.measureDict['roughness_measure_2'].blit_point[0] ,
                                   self.measureDict['roughness_measure_2'].blit_point[1] ))

        if (self.types[0] !=3):
            if not ('cover_measure_1' in self.measureDict.keys()):

                cover_measure_size = (30,30)

                if (self.types[0] == 2):
                    self.circle_center_cover_measure_1 = (int(self.surface_width/2) - self.R1,
                                        self.axis_center_point )
                    angle = 20


                    point = (self.circle_center_cover_measure_1[0] + self.R1*math.cos( math.radians(angle) ) ,
                             self.circle_center_cover_measure_1[1] + self.R1*math.sin( math.radians(angle) ) )
                if (self.types[0] == 1):
                    self.circle_center_cover_measure_1 = (int(self.surface_width / 2) + self.R1,
                                          self.axis_center_point)
                    angle = -20


                    point = (self.circle_center_cover_measure_1[0] - self.R1 * math.cos(math.radians(angle)),
                             self.circle_center_cover_measure_1[1] - self.R1 * math.sin(math.radians(angle)))

                self.measureDict['cover_measure_1'] = \
                    cover_measure(  self.surface,
                                    self.colors,
                                    point, 3,
                                    angle_position= angle,
                                    size = cover_measure_size)
            else:
                if (self.types[0] == 2):
                    self.circle_center_cover_measure_1 = (int(self.surface_width/2) - self.R1,
                                        self.axis_center_point )
                    # angle = -10

                    # self.measureDict['cover_measure_1'].blit_point = \
                    #     (self.circle_center_cover_measure_1[0] + self.R1*math.cos( math.radians(self.measureDict['cover_measure_1'].angle_position) )
                    #      - self.measureDict['cover_measure_1'].height,
                    #          self.circle_center_cover_measure_1[1] + self.R1*math.sin( math.radians(self.measureDict['cover_measure_1'].angle_position) ) )

                if (self.types[0] == 1):
                    self.circle_center_cover_measure_1 = (int(self.surface_width / 2) + self.R1,
                                          self.axis_center_point)
                    # angle = -20
                    # self.measureDict['cover_measure_1'].blit_point = \
                    #     (self.circle_center_cover_measure_1[0] - self.R1 * math.cos(math.radians(self.measureDict['cover_measure_1'].angle_position)) -
                    #      self.measureDict['cover_measure_1'].height,
                    #          self.circle_center_cover_measure_1[1] - self.R1 * math.sin(math.radians(self.measureDict['cover_measure_1'].angle_position)))


                self.measureDict['cover_measure_1'].draw()
                self.surface.blit(self.measureDict['cover_measure_1'].surface,
                                  (self.measureDict['cover_measure_1'].blit_point[0] ,
                                   self.measureDict['cover_measure_1'].blit_point[1] ))
        if (self.types[1] !=3):
            if not ('cover_measure_2' in self.measureDict.keys()):

                cover_measure_size = (30,30)

                if (self.types[1] == 2):
                    self.circle_center_cover_measure_2 = (int(self.surface_width/2) + self.width + self.R2,
                                        self.axis_center_point )
                    angle = -15


                    point = (self.circle_center_cover_measure_2[0] - self.R2*math.cos( math.radians(angle) ) ,
                             self.circle_center_cover_measure_2[1] - self.R2*math.sin( math.radians(angle) ) )
                    angle = -20
                if (self.types[1] == 1):
                    self.circle_center_cover_measure_2 = (int(self.surface_width / 2) + self.width - self.R2,
                                          self.axis_center_point)
                    angle = 20


                    point = (self.circle_center_cover_measure_2[0] + self.R2 * math.cos(math.radians(angle)),
                             self.circle_center_cover_measure_2[1] + self.R2 * math.sin(math.radians(angle)))
                    angle = 15

                self.measureDict['cover_measure_2'] = \
                    cover_measure(self.surface,
                                  self.colors,
                                  point, 3,
                                  angle_position=angle,
                                  size=cover_measure_size)
            else:
                if (self.types[1] == 2):
                    self.circle_center_cover_measure_2 = (int(self.surface_width/2) + self.width + self.R2,
                                        self.axis_center_point )
                    # angle = -15

                    # self.measureDict['cover_measure_2'].blit_point = \
                    #     (self.circle_center_cover_measure_2[0]- self.R2*math.cos( math.radians(self.measureDict['cover_measure_2'].angle_position))
                    #      + + self.measureDict['cover_measure_2'].width/2,
                    #          self.circle_center_cover_measure_2[1] - self.R2*math.sin( math.radians(self.measureDict['cover_measure_2'].angle_position) ) )

                if (self.types[1] == 1):
                    self.circle_center_cover_measure_2 = (int(self.surface_width / 2) + self.width - self.R2,
                                          self.axis_center_point)



                self.measureDict['cover_measure_2'].draw()
                self.surface.blit(self.measureDict['cover_measure_2'].surface,
                                  (self.measureDict['cover_measure_2'].blit_point[0] ,
                                   self.measureDict['cover_measure_2'].blit_point[1] ))


    def __init__(self, screen, colors, start_point, width, diametr, R1, R2,
                 border_size, type, font = None, axis_center_point = 400, show_measure = True, show_streak = True,
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
        self.show_streak =show_streak

        self.left_facet_type = left_facet_type
        self.right_facet_type = right_facet_type

        self.left_facet_measure_type = 0
        self.right_facet_measure_type = 0

        self.left_facet_size = left_facet_size
        self.right_facet_size = right_facet_size

        self.lens_type = {
            1: (3, 1),
            2: (3, 2),
            3: (1, 1),
            4: (2, 2),
            5: (1, 2),
            6: (2, 2),
            7: (1, 2),
            8: (3, 3),
            9: (3, 3),
            10: (3, 3),
            11: (3, 3)
        }

        # Линзы
        # 1 - Выпуклая
        # 2 - Впуклая
        # 3 - Прямая
        self.type = type

        self.types = self.lens_type[self.type]
        self.measureDict = dict()
        self.select_measure = False
        self.selected_measure = None








