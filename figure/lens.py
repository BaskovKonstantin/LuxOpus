import pygame
import math
from figure.facet_measure import facet_measure
from figure.cover_measure import cover_measure
from figure.roughness_measure import roughness_measure
from figure.line_measure import line_measure
from figure.dash_line import dashed_line
from figure.figure_new.tasks_may.covers_class import CoversMeasure
from figure.figure_new.tasks_may.chamfers_class import Chamfers
from figure.arrow import arrow
from figure.figure_new.tasks_may.covers_class import CoversMeasure
from figure.figure_new.tasks_may.chamfers_class import Chamfers
from figure.figure_new.tasks_may.radius_class import Radius
from figure.figure_new.tasks_may.roughness_class import RoughnessMeasure

class lens:


    def check_click(self, click_pos):
        width = self.width*self.scale
        left_point = (int(self.surface_width/2 - width/2) + self.R1/12, self.axis_center_point - self.diametr/2)
        right_point = (int(self.surface_width/2 - width/2) + self.width + self.R2/24,self.axis_center_point + self.diametr/2)

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
        image_surface.fill(self.colors['transparent'])
        pygame.draw.line(image_surface, self.colors['border'], (0, side_size), (side_size, 0), width)
        pygame.draw.line(image_surface, self.colors['border'], (0, side_size/2), (side_size/2, 0), width)
        pygame.draw.line(image_surface, self.colors['border'], (side_size, side_size/2), (side_size/2, side_size), width)

        return image_surface
    def drawLens(self, scale = 1):
        self.types = self.lens_type[self.type]

        R1 = int(self.R1*self.scale)
        R2 = int(self.R2*self.scale)
        width = int(self.width*self.scale)
        diametr = int(self.diametr*self.scale)
        x_diff = 2 * R1 if R1 > R2 else 2 * R2 - 2 * self.R1 if self.R1 > self.R2 else 2 * self.R2
        y_diff = 2 * R1 if R1 > R2 else 2 * R2 - 2 * self.R1 if self.R1 > self.R2 else 2 * self.R2


        self.surface = pygame.Surface(
            (2 * (R1+100) if R1 > R2 else 2 * (R2+100), 2*(R1+100) if R1 >R2 else 2*(R2+100)), pygame.SRCALPHA)
        # self.surface.fill(self.colors['test'])

        self.surface_width = self.surface.get_width()
        self.axis_center_point = self.surface.get_height()/2

        arrow_height = 15
        angle_start_R1 = 0
        angle_start_R2 = 0
        angle_end_R1 = 0
        angle_end_R2 = 0

        #Отображение размеров
        if (self.show_streak):

            hatching_unit_side_size = int(30*self.scale)
            step = int(15*self.scale)
            hatching_unit = self.get_hatching_unit(side_size = hatching_unit_side_size)

            for position_x in range( int(self.surface_width/2 - width/2) , int(self.surface_width/2 - width/2) + width, hatching_unit_side_size + step):

                for position_y in range(int(self.axis_center_point - diametr/2), int(self.axis_center_point + diametr/2), hatching_unit_side_size + step):
                    self.surface.blit(hatching_unit, (position_x, position_y))
            pygame.draw.rect(self.surface, self.colors['transparent'], pygame.Rect( int(self.surface_width/2 - width/2), int(self.axis_center_point + diametr/2), width, hatching_unit_side_size) )

        #Левый
        if (self.types[0] == 1):
            if (self.show_streak):
                pygame.draw.circle(self.surface, self.colors['transparent'],
                                   (int(self.surface_width/2 - width/2) + R1,
                                    (self.axis_center_point )), R1 + 4*step, 4*step)

            rect = pygame.Rect(int(self.surface_width/2 - width/2),
                                    self.axis_center_point - R1,
                               2*R1, 2*R1)
            angle_start_R1 = -math.asin(diametr/(2 * R1)) + math.pi
            angle_end_R1 = math.asin(diametr/(2 * R1)) + math.pi
            pygame.draw.arc(self.surface, self.colors['border'], rect, angle_start_R1, angle_end_R1, self.border_size)
            # pygame.draw.arc(self.surface, self.colors['border'], rect, math.pi/2, -math.pi/2, self.border_size)
            self.key_point_1 = (int(self.surface_width/2 - width/2), self.axis_center_point)
        if (self.types[0] == 2):
            if (self.show_streak):
                for position_x in range(int(self.surface_width/2 - width/2)  - R1, int(self.surface_width/2 - width/2) - step//2, hatching_unit_side_size + step):

                    for position_y in range(int(self.axis_center_point - diametr / 2) ,
                                            int(self.axis_center_point + diametr / 2),
                                            hatching_unit_side_size + step):
                        self.surface.blit(hatching_unit, (position_x, position_y))
                pygame.draw.rect(self.surface, self.colors['transparent'],
                                 pygame.Rect(int(self.surface_width/2 - width/2) - R1 , int(self.axis_center_point + diametr/2) - 10, R1,
                                             hatching_unit_side_size))


            rect = pygame.Rect(int(self.surface_width/2 - width/2) - 2*R1 ,
                                    self.axis_center_point - R1 ,
                               2 * R1, 2 * R1)
            angle_start_R1 = -math.asin(diametr / (2 * R1))
            angle_end_R1 = math.asin(diametr / (2 * R1))
            if (self.show_streak):
                pygame.draw.circle(self.surface, self.colors['transparent'],
                                   (int(self.surface_width/2 - width/2) - R1,
                                    (self.axis_center_point )), R1)
            pygame.draw.arc(self.surface, self.colors['border'], rect, angle_start_R1, angle_end_R1, self.border_size)
            # pygame.draw.arc(self.surface, self.colors['border'], rect, math.pi/2, -math.pi/2 ,self.border_size)

            self.key_point_1 = (int(self.surface_width/2 - width/2) , self.axis_center_point)
        if (self.types[0] == 3):
            if (self.show_streak):
                pygame.draw.rect(self.surface, self.colors['transparent'],
                                 pygame.Rect( int(self.surface_width/2 - width/2),
                                              int(self.axis_center_point - diametr/2),
                                              R1/12, diametr) )

            pygame.draw.line(self.surface,self.colors['border'],
                             (int(self.surface_width/2 - width/2) + R1/12, self.axis_center_point - diametr/2),
                             (int(self.surface_width/2 - width/2) + R1/12, self.axis_center_point + diametr/2), self.border_size )
            angle_start_R1 = -math.asin(diametr / (2 * R1)) + math.pi
            angle_end_R1 = math.asin(diametr / (2 * R1)) + math.pi

            self.key_point_1 = (int(self.surface_width/2 - width/2) + R1/12, self.axis_center_point)


        # Правый
        if (self.types[1] == 1):
            if (self.show_streak):
                pygame.draw.circle(self.surface, self.colors['transparent'],
                                   (int(self.surface_width/2 - width/2) + width - R2,
                                    (self.axis_center_point )), R2 + 4*step, 4*step)

            rect = pygame.Rect(int(self.surface_width/2 - width/2) - 2* R2 + width,
                                    self.axis_center_point - R2 ,
                               2*R2, 2*R2)
            angle_start_R2 = -math.asin(diametr / (2 * R2))
            angle_end_R2 = math.asin(diametr / (2 * R2))
            pygame.draw.arc(self.surface, self.colors['border'], rect, angle_start_R2, angle_end_R2, self.border_size)
            # pygame.draw.arc(self.surface, self.colors['border'], rect, math.pi/2, -math.pi/2 ,self.border_size)

            self.key_point_2 = (int(self.surface_width/2 - width/2) + width,
                               self.axis_center_point)
        if (self.types[1] == 2):
            if (self.show_streak):
                for position_x in range(int(self.surface_width/2 - width/2) + width + 2*step, int(self.surface_width/2 - width/2) + width + R2, hatching_unit_side_size + step):

                    for position_y in range(int(self.axis_center_point - diametr / 2) + step,
                                            int(self.axis_center_point + diametr / 2),
                                            hatching_unit_side_size + step):
                        self.surface.blit(hatching_unit, (position_x, position_y))
                pygame.draw.rect(self.surface, self.colors['transparent'],
                                 pygame.Rect(int(self.surface_width/2 - width/2) + width, int(self.axis_center_point + diametr / 2), R2,
                                             hatching_unit_side_size))

            rect = pygame.Rect(int(self.surface_width/2 - width/2) + width,
                                    self.axis_center_point - R2 ,
                               2*R2, 2*R2)
            angle_start_R2 = -math.asin(diametr / (2 * R2)) + math.pi
            angle_end_R2 = math.asin(diametr / (2 * R2)) + math.pi

            if (self.show_streak):
                pygame.draw.circle(self.surface, self.colors['transparent'],
                                   (int(self.surface_width/2 - width/2) + width + R2,
                                    (self.axis_center_point )), R2)

            pygame.draw.arc(self.surface, self.colors['border'], rect, angle_start_R2, angle_end_R2, self.border_size)
            # pygame.draw.arc(self.surface, self.colors['border'], rect, math.pi/2, -math.pi/2 ,self.border_size)

            self.key_point_2 = (int(self.surface_width/2 - width/2) + width,
                               self.axis_center_point)
        if (self.types[1] == 3):
            if (self.show_streak):
                pygame.draw.rect(self.surface, self.colors['transparent'],
                                 pygame.Rect( int(self.surface_width/2 - width/2) + width + R2/24,
                                              int(self.axis_center_point - diametr/2),
                                              R2/12, diametr) )


            pygame.draw.line(self.surface,self.colors['border'],
                             (int(self.surface_width/2 - width/2) + width + R2/24 ,self.axis_center_point - diametr/2),
                             (int(self.surface_width/2 - width/2) + width + R2/24,self.axis_center_point + diametr/2), self.border_size )
            angle_start_R2 = -math.asin(diametr / (2 * R2)) + math.pi
            angle_end_R2 = math.asin(diametr / (2 * R2)) + math.pi

            self.key_point_2 = (int(self.surface_width/2 - width/2) + width + R2/24, self.axis_center_point)

        start_x_R1 = int(self.surface_width/2 - width/2) + R1
        # start_y_R1 =      self.axis_center_point - R1

        if (self.types[0] == 2):
            start_x_R1 = int(self.surface_width/2 - width/2) - R1
            start_y_R1 =      self.axis_center_point - R1
            angle_start_R1, angle_end_R1 = angle_end_R1, angle_start_R1

        start_x_R2 = int(self.surface_width/2 - width/2) + R2 + width
        # start_y_R2 =      self.axis_center_point - R2
        if (self.types[1] == 1):
            start_x_R2 = int(self.surface_width/2 - width/2) - R2 + width
            # start_y_R2 =      self.axis_center_point - R2

            angle_start_R2, angle_end_R2 = angle_end_R2, angle_start_R2

        if (self.types[0] == 3):
            point_1_x = int(self.surface_width/2 - width/2) + R1 / 12
        else:
            point_1_x = start_x_R1 + R1 * math.cos(angle_end_R1)
        point_1_y = self.axis_center_point + R1 * math.sin(angle_end_R1)
        self.point_1 = (point_1_x ,point_1_y)

        if (self.types[1] == 3):
            point_2_x = int(self.surface_width/2 - width/2) + R2 / 24  + width
        else:
            point_2_x = start_x_R2 + R2 * math.cos(angle_end_R2)
        point_2_y = self.axis_center_point + R2 * math.sin(angle_end_R2)
        self.point_2 = (point_2_x,point_2_y)

        if (self.types[0] == 3):
            point_3_x = int(self.surface_width/2 - width/2) + R1 / 12
        else:
            point_3_x = start_x_R1 + R1 * math.cos(angle_start_R1)
        point_3_y = self.axis_center_point + R1 * math.sin(angle_start_R1)
        self.point_3 = (point_3_x,point_3_y)

        if (self.types[1] == 3):
            point_4_x = int(self.surface_width/2 - width/2) + R2 / 24  + width
        else:
            point_4_x = start_x_R2 + R2 * math.cos(angle_start_R2)
        point_4_y = self.axis_center_point + R2 * math.sin(angle_start_R2)
        self.point_4 = (point_4_x,point_4_y)


        pygame.draw.line(self.surface, self.colors['border'], self.point_1, self.point_2, self.border_size)
        pygame.draw.line(self.surface, self.colors['border'], self.point_3, self.point_4,self.border_size)


        #Фаски
        #Левая
        if (self.left_facet_type != 0 ):

            if (self.types[0] == 1):

                facet_angle_start_R1 = -math.asin(
                    (diametr - self.left_facet_size * 2) / (2 * R1)) + math.pi
                facet_angle_end_R1 = math.asin(
                    (diametr - self.left_facet_size * 2) / (2 * R1)) + math.pi
            else:
                facet_angle_end_R1 = -math.asin((diametr - self.left_facet_size * 2) / (2 * R1))
                facet_angle_start_R1 = math.asin((diametr - self.left_facet_size * 2) / (2 * R1))

            if (self.types[0] == 3):
                facet_point_1_x = int(self.surface_width / 2) + R1 / 12
            else:
                facet_point_1_x = start_x_R1 + R1 * math.cos(facet_angle_end_R1)
            facet_point_1_y = self.axis_center_point + R1 * math.sin(facet_angle_end_R1)
            self.facet_point_1 = (facet_point_1_x, facet_point_1_y)

            if (self.types[0] == 3):
                facet_point_3_x = int(self.surface_width / 2) + R1 / 12
            else:
                facet_point_3_x = start_x_R1 + R1 * math.cos(facet_angle_start_R1)
            facet_point_3_y = self.axis_center_point + R1 * math.sin(facet_angle_start_R1)
            self.facet_point_3 = (facet_point_3_x, facet_point_3_y)

            if (self.left_facet_type == 1):
                if (self.types[0] == 2 ):
                    pygame.draw.rect(self.surface, self.colors['transparent'],
                                     pygame.Rect(self.point_1[0] - self.left_facet_size / 2,
                                                 self.point_1[1] - 2 * self.border_size,
                                                 self.left_facet_size,
                                                 self.left_facet_size + 2 * self.border_size))

                    pygame.draw.rect(self.surface, self.colors['transparent'],
                                     pygame.Rect(self.point_3[0] - self.left_facet_size / 2,
                                                 self.point_3[1] - self.left_facet_size + self.border_size,
                                                 self.left_facet_size,
                                                 self.left_facet_size))




                    pygame.draw.line(self.surface, self.colors['border'],
                                     (self.point_1[0] + self.left_facet_size / 2, self.point_1[1]),
                                     (self.facet_point_1[0], self.point_1[1]), self.border_size)
                    pygame.draw.line(self.surface, self.colors['border'],
                                     (self.facet_point_1[0], self.point_1[1]),
                                     self.facet_point_1, self.border_size)

                    pygame.draw.line(self.surface, self.colors['border'],
                                     (self.point_3[0] + self.left_facet_size / 2, self.point_3[1]),
                                     (self.facet_point_3[0], self.point_3[1]), self.border_size)
                    pygame.draw.line(self.surface, self.colors['border'],
                                     (self.facet_point_3[0], self.point_3[1]),
                                     self.facet_point_3, self.border_size)

        #Правая
        if (self.right_facet_type != 0  or True):

            if (self.types[1] == 1):
                facet_angle_end_R2 = -math.asin((diametr - self.right_facet_size * 2) / (2 * R2))
                facet_angle_start_R2 = math.asin((diametr - self.right_facet_size * 2) / (2 * R2))
            else:
                facet_angle_start_R2 = -math.asin(
                    (diametr - self.right_facet_size * 2) / (2 * R2)) + math.pi
                facet_angle_end_R2 = math.asin(
                    (diametr - self.right_facet_size * 2) / (2 * R2)) + math.pi

            if (self.types[1] == 3):
                facet_point_2_x = int(self.surface_width / 2) + R2 / 24 + width
            else:
                facet_point_2_x = start_x_R2 + R2 * math.cos(facet_angle_end_R2)
            facet_point_2_y = self.axis_center_point + R2 * math.sin(facet_angle_end_R2)
            self.facet_point_2 = (facet_point_2_x, facet_point_2_y)

            if (self.types[1] == 3):
                facet_point_4_x = int(self.surface_width / 2) + R2 / 24 + width
            else:
                facet_point_4_x = start_x_R2 + R2 * math.cos(facet_angle_start_R2)
            facet_point_4_y = self.axis_center_point + R2 * math.sin(facet_angle_start_R2) - 2
            self.facet_point_4 = (facet_point_4_x,
                                  facet_point_4_y)

            if (self.right_facet_type == 1):

                if (self.types[1] == 2):
                    pygame.draw.rect(self.surface, self.colors['transparent'],
                                     pygame.Rect(self.point_2[0] - self.right_facet_size / 2 - 2 * self.border_size,
                                                 self.point_2[1] - 2 * self.border_size,
                                                 self.right_facet_size + 2 * self.border_size,
                                                 self.right_facet_size + 2 * self.border_size))

                    pygame.draw.rect(self.surface, self.colors['transparent'],
                                     pygame.Rect(self.point_4[0] - self.right_facet_size / 2 - 2 * self.border_size,
                                                 self.point_4[1] - self.right_facet_size + self.border_size,
                                                 self.right_facet_size + 2 * self.border_size,
                                                 self.right_facet_size + 2 * self.border_size))



                    pygame.draw.line(self.surface, self.colors['border'],
                                     (self.facet_point_2[0], self.point_2[1]),
                                     self.facet_point_2, self.border_size)


                    pygame.draw.line(self.surface, self.colors['border'],
                                     (self.facet_point_4[0], self.point_4[1]),
                                     self.facet_point_4, self.border_size)

        # #Отображение размеров
        if (self.show_measure):
            dash_length = 10
            dashed_line(self.surface, self.colors['border'],
                        (int(self.surface_width/2 - width), self.axis_center_point),
                        (int(self.surface_width/2 + width), self.axis_center_point), width=self.border_size-1,
                        dash_length=dash_length, dotted=True)

            self.draw_faset_measure()
            self.draw_base_measure()


        self.screen.blit(
            self.surface,
            (self.blit_point[0]*self.scale, self.blit_point[1]*self.scale) )
    def draw_faset_measure(self):

        width = self.width*self.scale
        diametr = self.diametr*self.scale

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
                    self.measureDict['facet_right_side_measure'].measure_shift = self.width*0.45
                else:
                    try:
                        self.measureDict['facet_right_side_measure'].start_point = self.facet_point_4
                        self.measureDict['facet_right_side_measure'].end_point = self.facet_point_2
                        self.measureDict['facet_right_side_measure'].width = int(self.facet_point_4[1] - self.facet_point_2[1] + 4*self.border_size)
                        # self.measureDict['facet_right_side_measure'].text = str(self.measureDict['facet_right_side_measure'].width)

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
                                     (self.key_point_1[0],self.key_point_1[1] - diametr/2),
                                     (self.key_point_1[0], self.key_point_1[1] - diametr),
                                     self.colors, width, text=str(width), font=self.font)
                else:

                    self.measureDict['facet_right_up_big_measure'].start_point = (self.key_point_1[0],self.key_point_1[1] - diametr/2)
                    self.measureDict['facet_right_up_big_measure'].end_point = (self.key_point_1[0], self.key_point_1[1] - diametr)
                    self.measureDict['facet_right_up_big_measure'].width = width
                    # self.measureDict['facet_right_up_big_measure'].text = str(self.measureDict['facet_right_up_big_measure'].width)

                    self.measureDict['facet_right_up_big_measure'].draw()
                    self.surface.blit(self.measureDict['facet_right_up_big_measure'].measure_surface,
                                      self.measureDict['facet_right_up_big_measure'].blit_point)
            if (self.right_facet_measure_type == 3):
                width = self.facet_point_2[0] - ( self.key_point_1[0] + width + 2*self.border_size)
                if not ('facet_right_up_small_measure' in self.measureDict.keys()):

                    self.measureDict['facet_right_up_small_measure'] = \
                        line_measure(self.surface,
                                     (self.key_point_1[0] + width ,self.key_point_1[1] - diametr/2),
                                     (self.key_point_1[0]  + width - width,self.key_point_1[1], self.key_point_1[1] - diametr),
                                     self.colors, width, arrow_height= 4, text=str(2), font_size= 15, font=self.font)

                    self.measureDict['facet_right_up_small_measure'].measure_shift = self.diametr*0.45
                else:
                    try:
                        self.measureDict['facet_right_up_small_measure'].start_point =(self.key_point_1[0] + width ,self.key_point_1[1] - diametr/2)
                        self.measureDict['facet_right_up_small_measure'].end_point = (self.key_point_1[0] + width - width , self.key_point_1[1] - diametr)
                        self.measureDict['facet_right_up_small_measure'].width = 2*width
                        # self.measureDict['facet_right_up_measure'].text = str(width)

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
                    self.measureDict['facet_left_side_measure'].measure_shift = self.width*0.45
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
                                     (self.facet_point_1[0],self.key_point_1[1] - diametr/2),
                                     (self.facet_point_1[0], self.key_point_1[1] - diametr),
                                     self.colors, width, text=str(self.width), font=self.font)
                else:

                    self.measureDict['facet_left_up_big_measure'].start_point = (self.facet_point_1[0],self.key_point_1[1] - diametr/2)
                    self.measureDict['facet_left_up_big_measure'].end_point = (self.facet_point_1[0], self.key_point_1[1] - diametr)
                    self.measureDict['facet_left_up_big_measure'].width = width

                    self.measureDict['facet_left_up_big_measure'].draw()
                    self.surface.blit(self.measureDict['facet_left_up_big_measure'].measure_surface,
                                      self.measureDict['facet_left_up_big_measure'].blit_point)
            if (self.left_facet_measure_type == 3):
                width = ( self.key_point_1[0] ) - self.facet_point_1[0] + self.border_size*2
                if not ('facet_left_up_small_measure' in self.measureDict.keys()):

                    self.measureDict['facet_left_up_small_measure'] = \
                        line_measure(self.surface,
                                     (self.facet_point_1[0] ,self.key_point_1[1] - diametr/2),
                                     (self.facet_point_1[0]  ,self.key_point_1[1], self.key_point_1[1] - diametr),
                                     self.colors, width, arrow_height= 4, text=str(2), font_size= 15, font=self.font)

                    self.measureDict['facet_left_up_small_measure'].measure_shift = self.diametr * 0.45
                else:
                    self.measureDict['facet_left_up_small_measure'].start_point =(self.facet_point_1[0] ,self.key_point_1[1] - diametr/2)
                    self.measureDict['facet_left_up_small_measure'].end_point = (self.facet_point_1[0] , self.key_point_1[1] - diametr)
                    self.measureDict['facet_left_up_small_measure'].width = width
                    # self.measureDict['facet_left_up_measure'].text = str(self.width)

                    self.measureDict['facet_left_up_small_measure'].draw()
                    self.surface.blit(self.measureDict['facet_left_up_small_measure'].measure_surface,
                                      self.measureDict['facet_left_up_small_measure'].blit_point)

#######################################################################
        # Здесь задается фаски#
        # Справа
        size = (60,80)
        if (self.right_facet_type == 2 and self.left_facet_type != 2):
            if not ('facet_right_measure' in self.measureDict.keys()):
                self.measureDict['facet_right_measure'] =\
                    Chamfers(
                        screen = self.surface,
                        colors = self.colors,
                        line_length= 40,
                        line_width= self.border_size,
                        pointer_length= 40,
                        text = '45',
                        chamfer_type = 1,
                        font=self.font,
                        first_point= self.point_2)
            else:
                #self.measureDict['facet_right_measure'].first_point = self.facet_point_2
                self.measureDict['facet_right_measure'].line_length = 40
                self.measureDict['facet_right_measure'].triangle_part = 0.5
                self.measureDict['facet_right_measure'].pointer_length = 40
                self.measureDict['facet_right_measure'].first_point = self.point_2
                self.measureDict['facet_right_measure'].second_point = None
                self.measureDict['facet_right_measure'].text = '45'
                self.measureDict['facet_right_measure'].chamfer_type = 1
                self.measureDict['facet_right_measure'].scale = self.scale
                self.measureDict['facet_right_measure'].draw()
                self.surface.blit(self.measureDict['facet_right_measure'].surface,
                                      self.measureDict['facet_right_measure'].blit_point)
        # и справа
        size = (60,80)
        if (self.right_facet_type != 2 and self.left_facet_type == 2):
            if not ('facet_left_measure' in self.measureDict.keys()):
                self.measureDict['facet_left_measure'] = \
                    Chamfers(
                        screen=self.surface,
                        colors=self.colors,
                        line_length=40,
                        line_width=self.border_size,
                        pointer_length=40,
                        text='UP',
                        chamfer_type=3,
                        font=self.font,
                        first_point=self.point_1)
                # self.measureDict['facet_left_measure'] =\
                #     facet_measure(
                #                 self.surface,
                #                 self.colors,
                #         (self.facet_point_1[0] + size[0]/3,self.facet_point_1[1] - diametr/2 ),
                #         size = size,
                #                  text=str('Upp'), font=self.font,)

            else:
                try:
                    self.measureDict['facet_left_measure'].line_length = 40
                    self.measureDict['facet_left_measure'].triangle_part = 0.5
                    self.measureDict['facet_left_measure'].pointer_length = 40
                    self.measureDict['facet_left_measure'].first_point = self.point_1
                    self.measureDict['facet_left_measure'].second_point = None
                    self.measureDict['facet_left_measure'].text = 'UP'
                    self.measureDict['facet_left_measure'].chamfer_type = 3
                    self.measureDict['facet_left_measure'].scale = self.scale
                    self.measureDict['facet_left_measure'].blit_point = (self.facet_point_1[0] - size[0]/2,self.facet_point_1[1] - diametr/2 )
                    self.measureDict['facet_left_measure'].draw()
                    self.surface.blit(self.measureDict['facet_left_measure'].surface,
                                      self.measureDict['facet_left_measure'].blit_point)
                except:
                    pass
        if (self.right_facet_type == 2 and self.left_facet_type == 2):
            if not ('facet_left_measure' in self.measureDict.keys()):
                self.measureDict['facet_left_measure'] =\
                    Chamfers(
                        screen = self.surface,
                        colors = self.colors,
                        line_length= 100,
                        triangle_part=0.3,
                        line_width= self.border_size,
                        pointer_length= 100,
                        text = '45',
                        chamfer_type = 2,
                        font=self.font,
                        first_point= self.point_1,
                        second_point=self.point_2)
            else:
                #self.measureDict['facet_right_measure'].first_point = self.facet_point_24
                self.measureDict['facet_left_measure'].line_length = 100
                self.measureDict['facet_left_measure'].triangle_part = 0.3
                self.measureDict['facet_left_measure'].pointer_length = 100
                self.measureDict['facet_left_measure'].first_point = self.point_1
                self.measureDict['facet_left_measure'].second_point = self.point_2
                self.measureDict['facet_left_measure'].text = '45'
                self.measureDict['facet_left_measure'].chamfer_type = 2
                self.measureDict['facet_left_measure'].scale = self.scale
                self.measureDict['facet_left_measure'].draw()
                self.surface.blit(self.measureDict['facet_left_measure'].surface,
                                      self.measureDict['facet_left_measure'].blit_point)

    def draw_base_measure(self):
        R1 = int(self.R1*self.scale)
        R2 = int(self.R2*self.scale)
        width = int(self.width*self.scale)
        diametr = int(self.diametr * self.scale)

        measure_width = self.key_point_2[0] - self.key_point_1[0] + 5

        if not ('up_measure' in self.measureDict.keys()):
            self.measureDict['up_measure'] = \
                line_measure(self.surface,
                                          self.key_point_1,
                                        (self.key_point_1[0], self.key_point_1[1] - diametr),
                                          self.colors, measure_width, text=str(self.width), font=self.font)
        else:
            self.measureDict['up_measure'].start_point = self.key_point_1
            self.measureDict['up_measure'].end_point = (self.key_point_1[0], self.key_point_1[1] - diametr)
            self.measureDict['up_measure'].width = measure_width
            self.measureDict['up_measure'].scale = self.scale
            self.measureDict['up_measure'].text = str(self.width)

            self.measureDict['up_measure'].draw()
            self.surface.blit(self.measureDict['up_measure'].measure_surface, self.measureDict['up_measure'].blit_point)

        if not ('side_measure' in self.measureDict.keys()):
            self.measureDict['side_measure'] = \
                line_measure(self.surface,
                             (self.key_point_1[0] + width/2, self.key_point_1[1] - 20 + diametr/2),
                                        (self.key_point_1[0] + width/2, self.key_point_1[1] - diametr/2),
                                          self.colors, diametr + self.border_size*3, text=str(self.diametr), font=self.font,
                             angle_rotate=-90)
            self.measureDict['side_measure'].measure_shift = self.width*1.2
        else:
            self.measureDict['side_measure'].start_point = (self.key_point_1[0] + width/2, self.key_point_1[1] - 20 + diametr/2)
            self.measureDict['side_measure'].end_point = (self.key_point_1[0] + width/2, self.key_point_1[1] - diametr/2)
            self.measureDict['side_measure'].width = diametr + self.border_size*3
            self.measureDict['side_measure'].text = '' + str(self.diametr)
            self.measureDict['side_measure'].scale = self.scale
            self.measureDict['side_measure'].draw()
            self.surface.blit(self.measureDict['side_measure'].measure_surface, self.measureDict['side_measure'].blit_point)

        if (self.types[0] !=3):

            if not ('R1_measure' in self.measureDict.keys()):

                if self.types[0] == 1:
                    angle = 180
                    limit = (180-math.degrees(math.asin(diametr/2/R1)), 180+math.degrees(math.asin(diametr/2/R1)))
                if self.types[0] == 2:
                    angle = 0
                    limit = (0 - math.degrees(math.asin(diametr / 2 / R1)), 0 + math.degrees(math.asin(diametr / 2 / R1)))

                self.measureDict['R1_measure'] = Radius(self.surface,
                                                        (int(self.surface_width/2 -2*width - R1 - 25 +diametr),0-diametr+10),
                                                        self.colors,
                                                        surface_radius = R1,
                                                        radius_length = R1/2,
                                                        radius_width = 1,
                                                        triangle_length=30,
                                                        triangle_width=30,
                                                        angle = angle,
                                                        text = 'R1',
                                                        radius_type = self.types[0]-1,
                                                        limit=limit,
                                                        font = self.font)
            else:

                if self.measureDict['R1_measure'].radius_type != self.types[0]-1:
                    self.measureDict['R1_measure'].radius_type = self.types[0]-1
                    self.measureDict['R1_measure'].moved_once = False
                    self.measureDict['R1_measure'].create_surface()
                    if self.types[0] == 1:
                        self.measureDict['R1_measure'].start_angle = 180
                    if self.types[0] == 2:
                        self.measureDict['R1_measure'].start_angle = 0

                self.measureDict['R1_measure'].surface_radius = R1
                self.measureDict['R1_measure'].radius_length = R1/2
                self.measureDict['R1_measure'].line_length = int(R1 * 0.95)
                self.measureDict['R1_measure'].create_surface()
                self.measureDict['R1_measure'].scale = self.scale
                self.measureDict['R1_measure'].draw()
                if self.types[0] == 1:
                    self.measureDict['R1_measure'].limit = (180 - math.degrees(math.asin(diametr / 2 / R1)),
                                                            180 + math.degrees(math.asin(diametr / 2 / R1)))
                    self.measureDict['R1_measure'].blit_point = (self.point_1[0]-R1-(R1-math.sqrt(R1**2-(diametr/2)**2)),
                                                                 self.point_1[1]-(R1*4-diametr)/2)
                    # self.measureDict['R1_measure'].blit_point = (self.surface_width/2 - R1 - width/2,
                    #                                              R1 - self.measureDict['R1_measure'].surface.get_height()/2)
                elif self.types[0] == 2:
                    self.measureDict['R1_measure'].limit = (0 - math.degrees(math.asin(diametr / 2 / R1)),
                                                            0 + math.degrees(math.asin(diametr / 2 / R1)))
                    self.measureDict['R1_measure'].blit_point = (self.point_1[0]-R1*2+(R1-math.sqrt(R1**2-(diametr/2)**2)),
                                                                 self.point_1[1]-(R1*2-diametr)/2)
                    # self.measureDict['R1_measure'].blit_point = (self.surface_width / 2 - R1*2 - width/2,
                    #                                              0)
                #print(self.point_1, self.point_2)

                self.surface.blit(self.measureDict['R1_measure'].surface,
                                  self.measureDict['R1_measure'].blit_point)

        if (self.types[1] !=3):
            radius_width = 150

            if not ('R2_measure' in self.measureDict.keys()):
                #print(self.types[1])
                if self.types[1] == 2:
                    angle = 180
                    limit = (180 - math.degrees(math.asin(diametr / 2 / R2)), 180 + math.degrees(math.asin(diametr / 2 / R2)))
                if self.types[1] == 1:
                    angle = 0
                    limit = (0 - math.degrees(math.asin(diametr / 2 / R2)), 0 + math.degrees(math.asin(diametr / 2 / R2)))

                self.measureDict['R2_measure'] = Radius(self.surface,
                                                        (int(self.surface_width/2 - R2 - 13 - diametr - 61),
                                                         0-diametr/2-36),
                                                        self.colors,
                                                        surface_radius = R2,
                                                        radius_length = R2/2,
                                                        radius_width = 1,
                                                        triangle_length= 30,
                                                        triangle_width=30,
                                                        angle = angle,
                                                        text = 'R2',
                                                        radius_type = self.types[1]-1,
                                                        limit=limit,
                                                        font = self.font)

                # не знаю что это но на всякий случай комментил
                # self.measureDict['R2_measure'] = arrow((int(self.surface_width / 2 - width / 2 + width - radius_width),
                #                                         self.axis_center_point), self.surface,
                #                                        self.colors, size=(radius_width, 10), font=self.font,
                #                                        text=f'R{R1}', opposite=True, angle_rotate=8)

            else:
                self.measureDict['R2_measure'].surface_radius = R2
                self.measureDict['R2_measure'].radius_length = R2 / 2
                self.measureDict['R2_measure'].line_length = int(R2 * 0.95)
                self.measureDict['R2_measure'].create_surface()
                if self.measureDict['R2_measure'].radius_type != self.types[1]-1:
                    self.measureDict['R2_measure'].radius_type = self.types[1]-1
                    self.measureDict['R2_measure'].moved_once = False
                    self.measureDict['R2_measure'].create_surface()
                    if self.types[1] == 2:
                        self.measureDict['R2_measure'].start_angle = 180
                    if self.types[1] == 1:
                        self.measureDict['R2_measure'].start_angle = 0
                self.measureDict['R2_measure'].scale = self.scale
                self.measureDict['R2_measure'].draw()
                if self.types[1] == 2:
                    self.measureDict['R2_measure'].limit = (180 - math.degrees(math.asin(diametr / 2 / R2)),
                                                            180 + math.degrees(math.asin(diametr / 2 / R2)))
                    self.measureDict['R2_measure'].blit_point = (self.point_2[0]-(R2-math.sqrt(R2**2-(diametr/2)**2)),
                                                                 self.point_2[1]-(R2*2-diametr)/2)
                    # self.measureDict['R2_measure'].blit_point = (self.surface_width/2 + width/2,
                    #                                              self.surface.get_height()/2-R2)
                elif self.types[1] == 1:
                    self.measureDict['R2_measure'].limit = (0 - math.degrees(math.asin(diametr / 2 / R2)),
                                                            0 + math.degrees(math.asin(diametr / 2 / R2)))
                    self.measureDict['R2_measure'].blit_point = (self.point_2[0]-R2*3+(R2-math.sqrt(R2**2-(diametr/2)**2)),
                                                                 self.point_2[1]-(R2*4-diametr)/2)
                    # self.measureDict['R2_measure'].blit_point = (self.surface.get_width()/2-R2*3+width/2,
                    #                                              self.surface.get_height()/2 - R2*2)

                self.surface.blit(self.measureDict['R2_measure'].surface,
                                  self.measureDict['R2_measure'].blit_point)

            #else:
            #    self.measureDict['R2_measure'].text = f'R{R2}'
            #    self.measureDict['R2_measure'].blit_point = (int(self.surface_width/2 - width/2 + width - radius_width),
            #                                            self.axis_center_point )
            #
            #    self.measureDict['R2_measure'].draw()
            #    self.surface.blit(self.measureDict['R2_measure'].surface,
            #                      self.measureDict['R2_measure'].blit_point)
        if (self.types[0] !=3):

            roughness_measure_size = (60, 60)

            if not ('roughness_measure_1' in self.measureDict.keys()):

                if self.types[0] == 1:
                    angle = 180
                    limit = (180 - math.degrees(math.asin(diametr / 2 / R1)), 180 + math.degrees(math.asin(diametr / 2 / R1)))
                if self.types[0] == 2:
                    angle = 0
                    limit = (0 - math.degrees(math.asin(diametr / 2 / R1)), 0 + math.degrees(math.asin(diametr / 2 / R1)))

                self.measureDict['roughness_measure_1'] = \
                    RoughnessMeasure(self.surface,
                                     colors=self.colors,
                                     blit_point=(0, 0),
                                     surface_radius=R1,
                                     size = roughness_measure_size,
                                     angle=angle,
                                     line_width=2,
                                     font = self.font,
                                     limit=limit,
                                     text_method = 'T1',
                                     text_base_len = 'B1',
                                     text_designation = 'D1',
                                     roughness_type=self.types[0]-1)
            else:
                if self.measureDict['roughness_measure_1'].roughness_type != self.types[0]-1:
                    self.measureDict['roughness_measure_1'].roughness_type = self.types[0]-1
                    self.measureDict['roughness_measure_1'].moved_once = False
                    self.measureDict['roughness_measure_1'].create_surface()
                    if self.types[0] == 1:
                        self.measureDict['roughness_measure_1'].start_angle = 180
                    if self.types[0] == 2:
                        self.measureDict['roughness_measure_1'].start_angle = 0
                self.measureDict['roughness_measure_1'].surface_radius = R1
                self.measureDict['roughness_measure_1'].create_surface()
                self.measureDict['roughness_measure_1'].scale = self.scale
                self.measureDict['roughness_measure_1'].draw()

                if self.types[0] == 1:
                    self.measureDict['roughness_measure_1'].limit = limit = (
                        180 - math.degrees(math.asin(diametr / 2 / R1)),
                        180 + math.degrees(math.asin(diametr / 2 / R1)))
                    self.measureDict['roughness_measure_1'].blit_point = (self.point_1[0]-(R1-math.sqrt(R1**2-(diametr/2)**2))-self.measureDict['roughness_measure_1'].width,
                                                                          self.point_1[1]-(R1*2-diametr)/2-self.measureDict['roughness_measure_1'].width)
                    # self.measureDict['roughness_measure_1'].blit_point = (
                    #     self.surface_width - R1 - width/2 - (self.measureDict['roughness_measure_1'].surface.get_width()/2 - R1),
                    #     R1 - self.measureDict['roughness_measure_1'].surface.get_height()/2)

                elif self.types[0] == 2:
                    self.measureDict['roughness_measure_1'].limit = limit = (
                        0 - math.degrees(math.asin(diametr / 2 / R1)),
                        0 + math.degrees(math.asin(diametr / 2 / R1)))
                    self.measureDict['roughness_measure_1'].blit_point = (self.point_1[0]-R1*2+(R1-math.sqrt(R1**2-(diametr/2)**2)),
                                                                          self.point_1[1]-(R1*2-diametr)/2)
                    # self.measureDict['roughness_measure_1'].blit_point = (
                    #     self.surface_width / 2 - R1*2 - width/2,
                    #     R1 - self.measureDict['roughness_measure_1'].surface.get_height() / 2)

                self.surface.blit(self.measureDict['roughness_measure_1'].surface,
                                  self.measureDict['roughness_measure_1'].blit_point)
                #print(self.measureDict['roughness_measure_1'].angle)

                # if (self.types[0] == 2):
                #     angle = 25
                #     self.measureDict['roughness_measure_1'].scale = self.scale
                #     self.measureDict['roughness_measure_1'].draw()
                #     point = (self.circle_center_roughness_measure_1[0] + R1 * math.cos(math.radians(angle)) - 1*roughness_measure_size[0],
                #              self.circle_center_roughness_measure_1[1] + R1 * math.sin(math.radians(angle)) - 1.3*roughness_measure_size[1])
                #     self.measureDict['roughness_measure_1'].blit_point = point
                #     self.circle_center_roughness_measure_1 = (int(self.surface_width/2 - width/2) - R1,
                #                         self.axis_center_point )
                #     angle = 5
                # if (self.types[0] == 1):
                #     angle = 20
                #     # point = (self.circle_center_roughness_measure_1[0] - R1 * math.cos(math.radians(angle) ) - width,
                #     #          self.circle_center_roughness_measure_1[1] - R1 * math.sin(math.radians(angle)) )
                #     self.measureDict['roughness_measure_1'].scale = self.scale
                #     self.measureDict['roughness_measure_1'].draw()
                #     point = (self.surface_width - R1 - width/2 - (self.measureDict['roughness_measure_1'].surface.get_width()/2 - R1),
                #              R1 - self.measureDict['roughness_measure_1'].surface.get_height()/2)
                #     self.measureDict['roughness_measure_1'].blit_point = point
                #     self.circle_center_roughness_measure_1 = (int(self.surface_width / 2) + R1,
                #                           self.axis_center_point)
                #     angle = 20
                # self.measureDict['roughness_measure_1'].scale = self.scale
                # self.measureDict['roughness_measure_1'].draw()
                # self.surface.blit(self.measureDict['roughness_measure_1'].surface,
                #                   (self.measureDict['roughness_measure_1'].blit_point[0] ,
                #                    self.measureDict['roughness_measure_1'].blit_point[1] ))

        if (self.types[1] !=3):
            if not ('roughness_measure_2' in self.measureDict.keys()):
                roughness_measure_size = (60,60)

                if self.types[1] == 2:
                    angle = 180
                    limit = (180 - math.degrees(math.asin(diametr / 2 / R2)), 180 + math.degrees(math.asin(diametr / 2 / R2)))
                if self.types[1] == 1:
                    angle = 0
                    limit = (0 - math.degrees(math.asin(diametr / 2 / R2)), 0 + math.degrees(math.asin(diametr / 2 / R2)))

                self.measureDict['roughness_measure_2'] = RoughnessMeasure(self.surface,
                                                                           (0,0),
                                                                           self.colors,
                                                                           line_width=2,
                                                                           surface_radius=R2,
                                                                           roughness_type=self.types[1]-1,
                                                                           size = roughness_measure_size,
                                                                           angle=angle,
                                                                           font = self.font,
                                                                           limit=limit,
                                                                           text_method = 'T1',
                                                                           text_base_len = 'B1',
                                                                           text_designation = 'D1')
            else:

                if self.measureDict['roughness_measure_2'].roughness_type != self.types[1]-1:
                    self.measureDict['roughness_measure_2'].roughness_type = self.types[1]-1
                    self.measureDict['roughness_measure_2'].moved_once = False
                    self.measureDict['roughness_measure_2'].create_surface()
                    if self.types[1] == 2:
                        self.measureDict['roughness_measure_2'].start_angle = 180
                    if self.types[1] == 1:
                        self.measureDict['roughness_measure_2'].start_angle = 0
                self.measureDict['roughness_measure_2'].surface_radius = R2
                self.measureDict['roughness_measure_2'].create_surface()
                self.measureDict['roughness_measure_2'].scale = self.scale
                self.measureDict['roughness_measure_2'].draw()

                if self.types[1] == 1:
                    self.measureDict['roughness_measure_2'].limit = (
                        0 - math.degrees(math.asin(diametr / 2 / R2)),
                        0 + math.degrees(math.asin(diametr / 2 / R2)))
                    self.measureDict['roughness_measure_2'].blit_point = (self.point_2[0]-R2*2-self.measureDict['roughness_measure_2'].width+(R2-math.sqrt(R2**2-(diametr/2)**2)),
                                                                          self.point_2[1]-(R2*2-diametr)/2-self.measureDict['roughness_measure_2'].width)
                    # self.measureDict['roughness_measure_2'].blit_point = (
                    #     self.surface.get_width()/2-R2-self.measureDict['roughness_measure_2'].surface.get_width()/2+width/2,
                    #     self.surface.get_height()/2 - self.measureDict['roughness_measure_2'].surface.get_height()/2)

                elif self.types[1] == 2:
                    self.measureDict['roughness_measure_2'].limit = (
                        180 - math.degrees(math.asin(diametr / 2 / R2)),
                        180 + math.degrees(math.asin(diametr / 2 / R2)))
                    self.measureDict['roughness_measure_2'].blit_point = (self.point_2[0]-(R2-math.sqrt(R2**2-(diametr/2)**2)),
                                                                          self.point_2[1]-(R2*2-diametr)/2)
                    # self.measureDict['roughness_measure_2'].blit_point = (
                    #     self.surface_width / 2+width/2,
                    #     self.surface.get_height()/2-R2)

                self.surface.blit(self.measureDict['roughness_measure_2'].surface,
                                  self.measureDict['roughness_measure_2'].blit_point)

                # if (self.types[1] == 2):
                #     angle = 25
                #     self.measureDict['roughness_measure_2'].scale = self.scale
                #     self.measureDict['roughness_measure_2'].draw()
                #     point = (self.circle_center_roughness_measure_2[0] - R2*math.cos( math.radians(angle) ) ,
                #              self.circle_center_roughness_measure_2[1] - R2*math.sin( math.radians(angle) ) )
                #     self.measureDict['roughness_measure_2'].blit_point = point
                #
                #
                #     self.circle_center_roughness_measure_2 = (int(self.surface_width/2 - width/2) + width + R2,
                #                         self.axis_center_point )
                #     angle = 25
                #
                # if (self.types[1] == 1):
                #     angle = 25
                #
                #     # point = (self.circle_center_roughness_measure_2[0] + R2 * math.cos(math.radians(angle)),
                #     #          self.circle_center_roughness_measure_2[1] + R2 * math.sin(math.radians(angle)))
                #     self.measureDict['roughness_measure_2'].scale = self.scale
                #     self.measureDict['roughness_measure_2'].draw()
                #     point = (self.surface_width/2 - R2 - diametr/2 - (self.measureDict['roughness_measure_2'].surface.get_width()/2 - R2),
                #              R2 - self.measureDict['roughness_measure_2'].surface.get_height()/2+(R1-R2))
                #     self.measureDict['roughness_measure_2'].blit_point = point
                #
                #
                #     self.circle_center_roughness_measure_2 = (int(self.surface_width / 2) + width - R2,
                #                           self.axis_center_point)
                #     angle = 15
                #
                #
                # # self.measureDict['roughness_measure_2'].draw()
                # self.surface.blit(self.measureDict['roughness_measure_2'].surface,
                #                   (self.measureDict['roughness_measure_2'].blit_point[0] ,
                #                    self.measureDict['roughness_measure_2'].blit_point[1] ))
        if (self.types[0] !=3):
            cover_measure_size = (30, 30)
            if not ('cover_measure_1' in self.measureDict.keys()):

                if self.types[0] == 1:
                    angle = 180
                    limit = (180 - math.degrees(math.asin(diametr / 2 / R1)), 180 + math.degrees(math.asin(diametr / 2 / R1)))
                if self.types[0] == 2:
                    angle = 0
                    limit = (0 - math.degrees(math.asin(diametr / 2 / R1)), 0 + math.degrees(math.asin(diametr / 2 / R1)))

                self.measureDict['cover_measure_1'] = \
                    CoversMeasure(
                        screen=self.surface,
                        blit_point=(0,0),
                        colors=self.colors,
                        surface_radius=self.R1,
                        cover_size=cover_measure_size,
                        angle=angle,
                        line_width=1,
                        limit=limit,
                        cover_type=self.types[0]-1,
                        font=self.font)
            else:

                if self.measureDict['cover_measure_1'].cover_type != self.types[0]-1:
                    self.measureDict['cover_measure_1'].cover_type = self.types[0]-1
                    self.measureDict['cover_measure_1'].moved_once = False
                    self.measureDict['cover_measure_1'].create_surface()
                    if self.types[0] == 1:
                        self.measureDict['cover_measure_1'].start_angle = 180
                        self.measureDict['cover_measure_1'].limit = (149, 211)
                    if self.types[0] == 2:
                        self.measureDict['cover_measure_1'].start_angle = 0
                        self.measureDict['cover_measure_1'].limit = (-31, 31)
                self.measureDict['cover_measure_1'].surface_radius = R1
                self.measureDict['cover_measure_1'].create_surface()
                self.measureDict['cover_measure_1'].scale = self.scale
                self.measureDict['cover_measure_1'].draw()
                if self.types[0] == 1:
                    self.measureDict['cover_measure_1'].limit = (
                        180 - math.degrees(math.asin(diametr / 2 / R1)),
                        180 + math.degrees(math.asin(diametr / 2 / R1)))
                    self.measureDict['cover_measure_1'].blit_point = (self.point_1[0]-(R1-math.sqrt(R1**2-(diametr/2)**2))-self.measureDict['cover_measure_1'].width,
                                                                      self.point_1[1] - (R1 * 2 - diametr) / 2 - self.measureDict['cover_measure_1'].height)
                    # self.measureDict['cover_measure_1'].blit_point = (
                    #     self.surface_width - R1 - width/2 - (self.measureDict['cover_measure_1'].surface.get_width()/2 - R1),
                    #     R1 - self.measureDict['cover_measure_1'].surface.get_height()/2)

                elif self.types[0] == 2:
                    self.measureDict['cover_measure_1'].limit = (
                        0 - math.degrees(math.asin(diametr / 2 / R1)),
                        0 + math.degrees(math.asin(diametr / 2 / R1)))
                    self.measureDict['cover_measure_1'].blit_point = (self.point_1[0]-R1*2+(R1-math.sqrt(R1**2-(diametr/2)**2)),
                                                                      self.point_1[1] - (R1 * 2 - diametr) / 2)
                    # self.measureDict['cover_measure_1'].blit_point = (
                    #     self.surface_width / 2 - R1*2 - width/2,
                    #     0)
                self.surface.blit(self.measureDict['cover_measure_1'].surface,
                                  self.measureDict['cover_measure_1'].blit_point)

                # if (self.types[0] == 2):
                #     self.circle_center_cover_measure_1 = (int(self.surface_width/2 - width/2) - 2*R1,
                #                     (self.axis_center_point - R1))
                #
                #     point = (self.circle_center_cover_measure_1[0],
                #              self.circle_center_cover_measure_1[1])
                #     self.measureDict['cover_measure_1'].cover_type = 0
                #     self.measureDict['cover_measure_1'].angle = 0
                #     self.measureDict['cover_measure_1'].blit_point = point
                #
                #
                # if (self.types[0] == 1):
                #     # self.circle_center_cover_measure_1 = (int(self.surface_width/2 - width/2) - 2*R1,
                #     #                (self.axis_center_point - R1))
                #     # подставил значения наугад
                #     self.measureDict['cover_measure_1'].scale = self.scale
                #     self.measureDict['cover_measure_1'].draw()
                #     self.circle_center_cover_measure_1 = (self.surface_width/2 - width/2 - self.measureDict['cover_measure_1'].width,
                #                                              R1 - self.measureDict['cover_measure_1'].surface.get_height()/2)
                #     point = (self.circle_center_cover_measure_1[0],
                #              self.circle_center_cover_measure_1[1] )
                #
                #     self.measureDict['cover_measure_1'].cover_type = 0
                #     # закоментил эту строку потому-что из-за неё cover встаёт в позицию 200 в каждой итерации
                #     #self.measureDict['cover_measure_1'].angle = 200
                #     self.measureDict['cover_measure_1'].blit_point = point
                #
                # # self.measureDict['cover_measure_1'].draw()
                # self.surface.blit(self.measureDict['cover_measure_1'].surface,
                #                   (self.measureDict['cover_measure_1'].blit_point[0] ,
                #                    self.measureDict['cover_measure_1'].blit_point[1] ))
        if (self.types[1] !=3):
            cover_measure_size = (30, 30)
            if not ('cover_measure_2' in self.measureDict.keys()):

                if self.types[1] == 2:
                    angle = 180
                    limit = (180 - math.degrees(math.asin(diametr / 2 / R2)), 180 + math.degrees(math.asin(diametr / 2 / R2)))
                if self.types[1] == 1:
                    angle = 0
                    limit = (0 - math.degrees(math.asin(diametr / 2 / R2)), 0 + math.degrees(math.asin(diametr / 2 / R2)))

                self.measureDict['cover_measure_2'] = CoversMeasure(
                    screen = self.surface,
                    blit_point = (0, 0),
                    colors = self.colors,
                    surface_radius = self.R2,
                    cover_size=cover_measure_size,
                    angle = angle,
                    line_width= 2,
                    cover_type = 0,
                    limit=limit,
                    font = self.font)

            else:

                if self.measureDict['cover_measure_2'].cover_type != self.types[1]-1:
                    self.measureDict['cover_measure_2'].cover_type = self.types[1]-1
                    self.measureDict['cover_measure_2'].moved_once = False
                    self.measureDict['cover_measure_2'].create_surface()
                    if self.types[1] == 2:
                        self.measureDict['cover_measure_2'].start_angle = 180
                        self.measureDict['cover_measure_2'].limit = (142, 218)
                    if self.types[1] == 1:
                        self.measureDict['cover_measure_2'].start_angle = 0
                        self.measureDict['cover_measure_2'].limit = (-38, 38)
                self.measureDict['cover_measure_2'].surface_radius = R2
                self.measureDict['cover_measure_2'].create_surface()
                self.measureDict['cover_measure_2'].scale = self.scale
                self.measureDict['cover_measure_2'].draw()
                if self.types[1] == 1:
                    self.measureDict['cover_measure_2'].limit = (
                        0 - math.degrees(math.asin(diametr / 2 / R2)),
                        0 + math.degrees(math.asin(diametr / 2 / R2)))
                    self.measureDict['cover_measure_2'].blit_point = (
                        self.point_2[0] - R2 * 2 + (R2 - math.sqrt(R2 ** 2 - (diametr / 2) ** 2)) - self.measureDict['cover_measure_2'].width,
                        self.point_2[1] - (R2 * 2 - diametr) / 2 - self.measureDict['cover_measure_2'].height)
                    # self.measureDict['cover_measure_2'].blit_point = (
                    #     self.surface.get_width()/2-R2-self.measureDict['cover_measure_2'].surface.get_width()/2+width/2,
                    #     self.surface.get_height()/2 - self.measureDict['cover_measure_2'].surface.get_height()/2)

                elif self.types[1] == 2:
                    self.measureDict['cover_measure_2'].limit = (
                        180 - math.degrees(math.asin(diametr / 2 / R2)),
                        180 + math.degrees(math.asin(diametr / 2 / R2)))
                    self.measureDict['cover_measure_2'].blit_point = (
                        self.point_2[0] - (R2 - math.sqrt(R2 ** 2 - (diametr / 2) ** 2)),
                        self.point_2[1] - (R2 * 2 - diametr) / 2)
                    # self.measureDict['cover_measure_2'].blit_point = (
                    #     self.surface_width / 2+width/2,
                    #     self.surface.get_height()/2-R2)
                self.surface.blit(self.measureDict['cover_measure_2'].surface,
                                  self.measureDict['cover_measure_2'].blit_point)
                # if (self.types[1] == 2):
                #     self.circle_center_cover_measure_2 = \
                #         (int(self.surface_width / 2 - width / 2) + width ,
                #          (self.axis_center_point - R2))
                #
                #
                #     point = (self.circle_center_cover_measure_2[0],
                #              self.circle_center_cover_measure_2[1])
                #     self.measureDict['cover_measure_2'].cover_type = 1
                #     self.measureDict['cover_measure_2'].angle = 180
                #
                #
                # if (self.types[1] == 1):
                #     # self.circle_center_cover_measure_2 = \
                #     #     (int(self.surface_width/2 )  - 2*R2 + width/2,
                #     #                 (self.axis_center_point - R2))
                #     # подставил значения наугад
                #     self.measureDict['cover_measure_2'].scale = self.scale
                #     self.measureDict['cover_measure_2'].draw()
                #     self.circle_center_cover_measure_2 = \
                #         (self.surface_width / 2 - self.measureDict['cover_measure_2'].width-R2-diametr/2,
                #          R2 - self.measureDict['cover_measure_2'].surface.get_height() / 2 + (R1 - R2))
                #     point = (self.circle_center_cover_measure_2[0],
                #              self.circle_center_cover_measure_2[1] )
                #     self.measureDict['cover_measure_2'].cover_type = 0
                #     # закоментил эту строку потому-что из-за неё cover встаёт в позицию -20 в каждой итерации
                #     #self.measureDict['cover_measure_2'].angle = -20
                #
                # self.measureDict['cover_measure_2'].blit_point = point
                # self.measureDict['cover_measure_2'].surface_radius = R2
                #
                #
                #
                # #self.measureDict['cover_measure_2'].draw()
                # self.surface.blit(self.measureDict['cover_measure_2'].surface,
                #                   (self.measureDict['cover_measure_2'].blit_point[0] ,
                #                    self.measureDict['cover_measure_2'].blit_point[1] ))

    def __init__(self, screen, colors, start_point, width, diametr, R1, R2,
                 border_size, type, font = None, axis_center_point = 400, show_measure = True, show_streak = True,
                 left_facet_type = 0, right_facet_type = 0, left_facet_size = 40, right_facet_size = 40, scale = 1):

        self.font = font
        self.scale = scale

        self.colors = colors
        self.screen = screen
        self.surface = pygame.Surface(( 2*R1 if R1>R2 else 2*R2, 4*R1 if R1>R2 else 4*R2), pygame.SRCALPHA)

        # self.point_x = start_point[0]
        # self.point_y = start_point[1]
        self.blit_point = start_point
        self.width = width
        self.diametr = diametr
        self.R1 = R1
        self.R2 = R2
        self.border_size = border_size
        self.axis_center_point = axis_center_point
        self.show_measure = show_measure
        self.show_streak =show_streak


        self.original_blit_point = self.blit_point

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
            6: (3, 3),
            7: (3, 3),
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








