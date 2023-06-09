import pygame
import math
from figure.facet_measure import facet_measure
from figure.cover_measure import cover_measure
from figure.roughness_measure import roughness_measure
from figure.line_measure import line_measure
from figure.dash_line import dashed_line
from figure_new.tasks_may.covers_class import CoversMeasure
from figure_new.tasks_may.chamfers_class import Chamfers
from figure_new.tasks_may.covers_class import CoversMeasure
from figure_new.tasks_may.chamfers_class import Chamfers
from figure_new.tasks_may.radius_class import Radius

class lens:


    def check_click(self, click_pos):
        R1 = int(self.R1*(self.scale + self.super_scale) )
        R2 = int(self.R2*(self.scale + self.super_scale) )
        width = int(self.width*(self.scale + self.super_scale))
        diametr = int(self.diametr*(self.scale + self.super_scale))
        click_pos = (click_pos[0] , click_pos[1] )
        self.click_point = click_pos


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
        if (click_pos[0] > self.left_point[0] and click_pos[0] < self.right_point[0] and
                click_pos[1] > self.left_point[1] and click_pos[1] < self.right_point[1]):
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

        R1 = int(self.R1*(self.scale + self.super_scale))
        R2 = int(self.R2*(self.scale + self.super_scale))
        width = int(self.width*(self.scale + self.super_scale))
        diametr = int(self.diametr*(self.scale + self.super_scale))
        x_diff = 2 * R1 if R1 > R2 else 2 * R2 - 2 * self.R1 if self.R1 > self.R2 else 2 * self.R2
        y_diff = 2 * R1 if R1 > R2 else 2 * R2 - 2 * self.R1 if self.R1 > self.R2 else 2 * self.R2


        self.surface = pygame.Surface(
            (2 * R1 if R1 > R2 else 2 * R2,
             2*R1 if R1 >R2 else 2*R2),
            pygame.SRCALPHA)
        self.left_point = (self.surface.get_width()/2 - width/2, self.surface.get_height()/2 - diametr/2)
        self.right_point = (self.surface.get_width()/2 + width/2, self.surface.get_height()/2 + diametr/2)


        # self.surface.fill(self.colors['test'])
        # pygame.draw.rect(self.surface, self.colors['test'], (self.surface.get_width()/2 - width/2, self.surface.get_height()/2 - diametr/2, width, diametr))
        # pygame.draw.circle(self.surface, self.colors['test'], (self.surface.get_height()/2,self.surface.get_width()/2), width/2)


        self.surface_width = self.surface.get_width()
        self.axis_center_height = self.surface.get_height()/2

        arrow_height = 15
        self.angle_start_R1 = 0
        self.angle_start_R2 = 0
        self.angle_end_R1 = 0
        self.angle_end_R2 = 0

        #Отображение размеров
        if (self.show_streak):

            hatching_unit_side_size = int(30*(self.scale + self.super_scale))
            step = int(15*(self.scale + self.super_scale))
            hatching_unit = self.get_hatching_unit(side_size = hatching_unit_side_size)

            for position_x in range( int(self.surface_width/2 - width/2) , int(self.surface_width/2 - width/2) + width, hatching_unit_side_size + step):

                for position_y in range(int(self.axis_center_height - diametr/2), int(self.axis_center_height + diametr/2), hatching_unit_side_size + step):
                    self.surface.blit(hatching_unit, (position_x, position_y))
            pygame.draw.rect(self.surface, self.colors['transparent'], pygame.Rect( int(self.surface_width/2 - width/2), int(self.axis_center_height + diametr/2), width, hatching_unit_side_size) )

        #Левый
        if (self.types[0] == 1):
            if (self.show_streak):
                pygame.draw.circle(self.surface, self.colors['transparent'],
                                   (int(self.surface_width/2 - width/2) + R1,
                                    (self.axis_center_height )), R1 + 4*step, 4*step)

            rect = pygame.Rect(int(self.surface_width/2 - width/2),
                                    self.axis_center_height - R1,
                               2*R1, 2*R1)
            self.angle_start_R1 = -math.asin(diametr/(2 * R1)) + math.pi
            self.angle_end_R1 = math.asin(diametr/(2 * R1)) + math.pi
            pygame.draw.arc(self.surface, self.colors['border'], rect, self.angle_start_R1, self.angle_end_R1, self.border_size)
            # pygame.draw.arc(self.surface, self.colors['border'], rect, math.pi/2, -math.pi/2, self.border_size)
            self.key_point_1 = (int(self.surface_width/2 - width/2), self.axis_center_height)
        if (self.types[0] == 2):
            if (self.show_streak):
                for position_x in range(int(self.surface_width/2 - width/2)  - R1, int(self.surface_width/2 - width/2) - step//2, hatching_unit_side_size + step):

                    for position_y in range(int(self.axis_center_height - diametr / 2) ,
                                            int(self.axis_center_height + diametr / 2),
                                            hatching_unit_side_size + step):
                        self.surface.blit(hatching_unit, (position_x, position_y))
                pygame.draw.rect(self.surface, self.colors['transparent'],
                                 pygame.Rect(int(self.surface_width/2 - width/2) - R1 , int(self.axis_center_height + diametr/2) - 10, R1,
                                             hatching_unit_side_size))


            rect = pygame.Rect(int(self.surface_width/2 - width/2) - 2*R1 ,
                                    self.axis_center_height - R1 ,
                               2 * R1, 2 * R1)
            self.angle_start_R1 = -math.asin(diametr / (2 * R1))
            self.angle_end_R1 = math.asin(diametr / (2 * R1))
            if (self.show_streak):
                pygame.draw.circle(self.surface, self.colors['transparent'],
                                   (int(self.surface_width/2 - width/2) - R1,
                                    (self.axis_center_height )), R1)
            pygame.draw.arc(self.surface, self.colors['border'], rect, self.angle_start_R1, self.angle_end_R1, self.border_size)
            # pygame.draw.arc(self.surface, self.colors['border'], rect, math.pi/2, -math.pi/2 ,self.border_size)

            self.key_point_1 = (int(self.surface_width/2 - width/2) , self.axis_center_height)
        if (self.types[0] == 3):
            if (self.show_streak):
                pygame.draw.rect(self.surface, self.colors['transparent'],
                                 pygame.Rect( int(self.surface_width/2 - width/2),
                                              int(self.axis_center_height - diametr/2),
                                              R1/12, diametr) )

            pygame.draw.line(self.surface,self.colors['border'],
                             (int(self.surface_width/2 - width/2) + R1/12, self.axis_center_height - diametr/2),
                             (int(self.surface_width/2 - width/2) + R1/12, self.axis_center_height + diametr/2), self.border_size )
            self.angle_start_R1 = -math.asin(diametr / (2 * R1)) + math.pi
            self.angle_end_R1 = math.asin(diametr / (2 * R1)) + math.pi

            self.key_point_1 = (int(self.surface_width/2 - width/2) + R1/12, self.axis_center_height)


        # Правый
        if (self.types[1] == 1):
            if (self.show_streak):
                pygame.draw.circle(self.surface, self.colors['transparent'],
                                   (int(self.surface_width/2 - width/2) + width - R2,
                                    (self.axis_center_height )), R2 + 4*step, 4*step)

            rect = pygame.Rect(int(self.surface_width/2 - width/2) - 2* R2 + width,
                                    self.axis_center_height - R2 ,
                               2*R2, 2*R2)
            self.angle_start_R2 = -math.asin(diametr / (2 * R2))
            self.angle_end_R2 = math.asin(diametr / (2 * R2))
            pygame.draw.arc(self.surface, self.colors['border'], rect, self.angle_start_R2, self.angle_end_R2, self.border_size)
            # pygame.draw.arc(self.surface, self.colors['border'], rect, math.pi/2, -math.pi/2 ,self.border_size)

            self.key_point_2 = (int(self.surface_width/2 - width/2) + width,
                               self.axis_center_height)
        if (self.types[1] == 2):
            if (self.show_streak):
                for position_x in range(int(self.surface_width/2 - width/2) + width + 2*step, int(self.surface_width/2 - width/2) + width + R2, hatching_unit_side_size + step):

                    for position_y in range(int(self.axis_center_height - diametr / 2) + step,
                                            int(self.axis_center_height + diametr / 2),
                                            hatching_unit_side_size + step):
                        self.surface.blit(hatching_unit, (position_x, position_y))
                pygame.draw.rect(self.surface, self.colors['transparent'],
                                 pygame.Rect(int(self.surface_width/2 - width/2) + width, int(self.axis_center_height + diametr / 2), R2,
                                             hatching_unit_side_size))

            rect = pygame.Rect(int(self.surface_width/2 - width/2) + width,
                                    self.axis_center_height - R2 ,
                               2*R2, 2*R2)
            self.angle_start_R2 = -math.asin(diametr / (2 * R2)) + math.pi
            self.angle_end_R2 = math.asin(diametr / (2 * R2)) + math.pi

            if (self.show_streak):
                pygame.draw.circle(self.surface, self.colors['transparent'],
                                   (int(self.surface_width/2 - width/2) + width + R2,
                                    (self.axis_center_height )), R2)

            pygame.draw.arc(self.surface, self.colors['border'], rect, self.angle_start_R2, self.angle_end_R2, self.border_size)
            # pygame.draw.arc(self.surface, self.colors['border'], rect, math.pi/2, -math.pi/2 ,self.border_size)

            self.key_point_2 = (int(self.surface_width/2 - width/2) + width,
                               self.axis_center_height)
        if (self.types[1] == 3):
            if (self.show_streak):
                pygame.draw.rect(self.surface, self.colors['transparent'],
                                 pygame.Rect( int(self.surface_width/2 - width/2) + width + R2/24,
                                              int(self.axis_center_height - diametr/2),
                                              R2/12, diametr) )


            pygame.draw.line(self.surface,self.colors['border'],
                             (int(self.surface_width/2 - width/2) + width + R2/24 ,self.axis_center_height - diametr/2),
                             (int(self.surface_width/2 - width/2) + width + R2/24,self.axis_center_height + diametr/2), self.border_size )
            self.angle_start_R2 = -math.asin(diametr / (2 * R2)) + math.pi
            self.angle_end_R2 = math.asin(diametr / (2 * R2)) + math.pi

            self.key_point_2 = (int(self.surface_width/2 - width/2) + width + R2/24, self.axis_center_height)

        start_x_R1 = int(self.surface_width/2 - width/2) + R1
        # start_y_R1 =      self.axis_center_height - R1

        if (self.types[0] == 2):
            start_x_R1 = int(self.surface_width/2 - width/2) - R1
            start_y_R1 =      self.axis_center_height - R1
            self.angle_start_R1, self.angle_end_R1 = self.angle_end_R1, self.angle_start_R1

        start_x_R2 = int(self.surface_width/2 - width/2) + R2 + width
        # start_y_R2 =      self.axis_center_height - R2
        if (self.types[1] == 1):
            start_x_R2 = int(self.surface_width/2 - width/2) - R2 + width
            # start_y_R2 =      self.axis_center_height - R2

            self.angle_start_R2, self.angle_end_R2 = self.angle_end_R2, self.angle_start_R2

        if (self.types[0] == 3):
            point_1_x = int(self.surface_width/2 - width/2) + R1 / 12
        else:
            point_1_x = start_x_R1 + R1 * math.cos(self.angle_end_R1)
        point_1_y = self.axis_center_height + R1 * math.sin(self.angle_end_R1)
        point_1 = (point_1_x ,point_1_y)

        if (self.types[1] == 3):
            point_2_x = int(self.surface_width/2 - width/2) + R2 / 24  + width
        else:
            point_2_x = start_x_R2 + R2 * math.cos(self.angle_end_R2)
        point_2_y = self.axis_center_height + R2 * math.sin(self.angle_end_R2)
        point_2 = (point_2_x,point_2_y)

        if (self.types[0] == 3):
            point_3_x = int(self.surface_width/2 - width/2) + R1 / 12
        else:
            point_3_x = start_x_R1 + R1 * math.cos(self.angle_start_R1)
        point_3_y = self.axis_center_height + R1 * math.sin(self.angle_start_R1)
        point_3 = (point_3_x,point_3_y)

        if (self.types[1] == 3):
            point_4_x = int(self.surface_width/2 - width/2) + R2 / 24  + width
        else:
            point_4_x = start_x_R2 + R2 * math.cos(self.angle_start_R2)
        point_4_y = self.axis_center_height + R2 * math.sin(self.angle_start_R2)
        point_4 = (point_4_x,point_4_y)


        pygame.draw.line(self.surface, self.colors['border'], point_1, point_2, self.border_size)
        pygame.draw.line(self.surface, self.colors['border'], point_3, point_4,self.border_size)


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
            facet_point_1_y = self.axis_center_height + R1 * math.sin(facet_angle_end_R1)
            self.facet_point_1 = (facet_point_1_x, facet_point_1_y)

            if (self.types[0] == 3):
                facet_point_3_x = int(self.surface_width / 2) + R1 / 12
            else:
                facet_point_3_x = start_x_R1 + R1 * math.cos(facet_angle_start_R1)
            facet_point_3_y = self.axis_center_height + R1 * math.sin(facet_angle_start_R1)
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
            facet_point_2_y = self.axis_center_height + R2 * math.sin(facet_angle_end_R2)
            self.facet_point_2 = (facet_point_2_x, facet_point_2_y)

            if (self.types[1] == 3):
                facet_point_4_x = int(self.surface_width / 2) + R2 / 24 + width
            else:
                facet_point_4_x = start_x_R2 + R2 * math.cos(facet_angle_start_R2)
            facet_point_4_y = self.axis_center_height + R2 * math.sin(facet_angle_start_R2) - 2
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
            dash_length = 10
            dashed_line(self.surface, self.colors['border'],
                        (int(self.surface_width/2 - width), self.axis_center_height),
                        (int(self.surface_width/2 + width), self.axis_center_height), width=self.border_size-1,
                        dash_length=dash_length, dotted=True)

            # self.draw_faset_measure()
            self.draw_base_measure()

        # pygame.draw.circle(self.surface, self.colors['test'], self.left_point, width/2)
        # pygame.draw.circle(self.surface, self.colors['test'], self.right_point, width/2)
        # pygame.draw.circle(self.surface, (255,0,255), self.click_point, 10)


        self.screen.blit(
            self.surface,
            (self.blit_point[0], self.blit_point[1]) )
    def draw_faset_measure(self):

        width = self.width**(self.scale + self.super_scale)
        diametr = self.diametr**(self.scale + self.super_scale)

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

        size = (60,80)
        if (self.right_facet_type == 2 or True):
            if not ('facet_right_measure' in self.measureDict.keys()):
                self.measureDict['facet_right_measure'] =\
                    Chamfers(
                        screen = self.surface,
                        colors = self.colors,
                        line_length= 40,
                        line_width= self.border_size,
                        pointer_length= 40,
                        text = '45',
                        chamfer_type = 3,
                        font=self.font,
                        first_point= (100, 100))

            else:
                self.measureDict['facet_right_measure'].blit_point = self.facet_point_2
                self.measureDict['facet_right_measure'].draw()
                self.surface.blit(self.measureDict['facet_right_measure'].surface,
                                      self.measureDict['facet_right_measure'].blit_point)

        size = (60,80)
        if (self.left_facet_type == 2):
            if not ('facet_left_measure' in self.measureDict.keys()):
                self.measureDict['facet_left_measure'] =\
                    facet_measure(
                                self.surface,
                                self.colors,
                        (self.facet_point_1[0] + size[0]/3,self.facet_point_1[1] - diametr/2 ),
                        size = size,
                                 text=str('Upp'), font=self.font,)

            else:
                try:
                    self.measureDict['facet_left_measure'].blit_point = (self.facet_point_1[0] - size[0]/2,self.facet_point_1[1] - diametr/2 )
                    self.measureDict['facet_left_measure'].draw()
                    self.surface.blit(self.measureDict['facet_left_measure'].surface,
                                      self.measureDict['facet_left_measure'].blit_point)
                except:
                    pass
    def draw_base_measure(self):
        R1 = int(self.R1*(self.scale + self.super_scale))
        R2 = int(self.R2*(self.scale + self.super_scale))
        width = int(self.width*(self.scale + self.super_scale))
        diametr = int(self.diametr*(self.scale + self.super_scale))

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
            self.measureDict['up_measure'].scale = (self.scale + self.super_scale)
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
            self.measureDict['side_measure'].scale = (self.scale + self.super_scale)
            self.measureDict['side_measure'].draw()
            self.surface.blit(self.measureDict['side_measure'].measure_surface, self.measureDict['side_measure'].blit_point)

        if (self.types[0] != 3):
            radius_width = 150
            if not ('R1_measure' in self.measureDict.keys()):

                self.measureDict['R1_measure'] = Radius(self.surface,
                                                        (int(self.surface_width / 2 - 2 * width - R1 - 25 + diametr),
                                                         0 - diametr + 10),
                                                        self.colors,
                                                        surface_radius=R1,
                                                        radius_length=R1 / 2,
                                                        radius_width=1,
                                                        triangle_length=30,
                                                        triangle_width=30,
                                                        angle=180,
                                                        text='R1',
                                                        radius_type=0,
                                                        # limit=(self.angle_start_R1, self.angle_end_R1),
                                                        font=self.font)

            else:
                self.measureDict['R1_measure'].scale = self.scale
                self.measureDict['R1_measure'].draw()
                self.surface.blit(self.measureDict['R1_measure'].surface,
                                  self.measureDict['R1_measure'].blit_point)
        if (self.types[1] != 3):
            radius_width = 150
            if not ('R2_measure' in self.measureDict.keys()):
                # print((-math.asin(diametr / (2 * R2)) + math.pi, math.asin(diametr / (2 * R2)) + math.pi))

                self.measureDict['R2_measure'] = Radius(self.surface,
                                                        (int(self.surface_width / 2 - R2 - 13 - diametr - 61),
                                                         0 - diametr / 2 - 36),
                                                        self.colors,
                                                        surface_radius=R2,
                                                        radius_length=R2 / 2,
                                                        radius_width=1,
                                                        triangle_length=30,
                                                        triangle_width=30,
                                                        angle=0,
                                                        text='R2',
                                                        radius_type=0,
                                                        # limit=(-math.asin(diametr / (2 * R2)) + math.pi, math.asin(diametr / (2 * R2)) + math.pi),
                                                        font=self.font)

            else:
                self.measureDict['R2_measure'].scale = self.scale
                self.measureDict['R2_measure'].draw()
                self.surface.blit(self.measureDict['R2_measure'].surface,
                                  self.measureDict['R2_measure'].blit_point)

        if (self.types[0] != 3):
            cover_measure_size = (30, 30)
            if not ('cover_measure_1' in self.measureDict.keys()):

                point = (0, 0)

                self.measureDict['cover_measure_1'] = \
                    CoversMeasure(
                        screen=self.surface,
                        blit_point=point,
                        colors=self.colors,
                        surface_radius=self.R1,
                        cover_size=cover_measure_size,
                        angle=200,
                        line_width=2,
                        limit=(149, 211),
                        cover_type=0)
            else:
                if (self.types[0] == 2):
                    self.circle_center_cover_measure_1 = (int(self.surface_width / 2 - width / 2) - 2 * R1,
                                                          (self.axis_center_height - R1))

                    point = (self.circle_center_cover_measure_1[0],
                             self.circle_center_cover_measure_1[1])
                    self.measureDict['cover_measure_1'].cover_type = 0
                    self.measureDict['cover_measure_1'].angle = 0
                    self.measureDict['cover_measure_1'].blit_point = point

                if (self.types[0] == 1):
                    # self.circle_center_cover_measure_1 = (int(self.surface_width/2 - width/2) - 2*R1,
                    #                (self.axis_center_height - R1))
                    # подставил значения наугад
                    self.circle_center_cover_measure_1 = (int(self.surface_width / 2 - width / 2) - 2 * R1 + 450,
                                                          (self.axis_center_height - R1 - 30))
                    point = (self.circle_center_cover_measure_1[0],
                             self.circle_center_cover_measure_1[1])

                    self.measureDict['cover_measure_1'].cover_type = 0
                    # закоментил эту строку потому-что из-за неё cover встаёт в позицию 200 в каждой итерации
                    # self.measureDict['cover_measure_1'].angle = 200
                    self.measureDict['cover_measure_1'].blit_point = point

                self.measureDict['cover_measure_1'].draw()
                self.surface.blit(self.measureDict['cover_measure_1'].surface,
                                  (self.measureDict['cover_measure_1'].blit_point[0],
                                   self.measureDict['cover_measure_1'].blit_point[1]))
        if (self.types[1] != 3):
            cover_measure_size = (30, 30)
            if not ('cover_measure_2' in self.measureDict.keys()):

                if (self.types[1] == 2):
                    self.circle_center_cover_measure_2 = (int(self.surface_width / 2 - width / 2) + width + R2,
                                                          0)
                    angle = -15

                    point = (self.circle_center_cover_measure_2[0] - R2 * math.cos(math.radians(angle)),
                             self.circle_center_cover_measure_2[1] - R2 * math.sin(math.radians(angle)))
                    angle = -20
                if (self.types[1] == 1):
                    self.circle_center_cover_measure_2 = (int(self.surface_width / 2) + width - R2,
                                                          0)
                    angle = 20

                    point = (self.circle_center_cover_measure_2[0] + R2 * math.cos(math.radians(angle)),
                             self.circle_center_cover_measure_2[1] + R2 * math.sin(math.radians(angle)))
                    angle = 15

                self.measureDict['cover_measure_2'] = CoversMeasure(
                    screen=self.surface,
                    blit_point=point,
                    colors=self.colors,
                    surface_radius=self.R2,
                    cover_size=cover_measure_size,
                    angle=-20,
                    line_width=2,
                    cover_type=0,
                    limit=(-38, 38))

            else:
                if (self.types[1] == 2):
                    self.circle_center_cover_measure_2 = \
                        (int(self.surface_width / 2 - width / 2) + width,
                         (self.axis_center_height - R2))

                    point = (self.circle_center_cover_measure_2[0],
                             self.circle_center_cover_measure_2[1])
                    self.measureDict['cover_measure_2'].cover_type = 1
                    self.measureDict['cover_measure_2'].angle = 180

                if (self.types[1] == 1):
                    # self.circle_center_cover_measure_2 = \
                    #     (int(self.surface_width/2 )  - 2*R2 + width/2,
                    #                 (self.axis_center_height - R2))
                    # подставил значения наугад
                    self.circle_center_cover_measure_2 = \
                        (int(self.surface_width / 2) - 2 * R2 + width / 2 - 35,
                         (self.axis_center_height - R2 - 30))

                    point = (self.circle_center_cover_measure_2[0] + 5,
                             self.circle_center_cover_measure_2[1])
                    self.measureDict['cover_measure_2'].cover_type = 0
                    # закоментил эту строку потому-что из-за неё cover встаёт в позицию -20 в каждой итерации
                    # self.measureDict['cover_measure_2'].angle = -20

                self.measureDict['cover_measure_2'].blit_point = point
                self.measureDict['cover_measure_2'].surface_radius = R2

                self.measureDict['cover_measure_2'].draw()
                self.surface.blit(self.measureDict['cover_measure_2'].surface,
                                  (self.measureDict['cover_measure_2'].blit_point[0],
                                   self.measureDict['cover_measure_2'].blit_point[1]))




    def __init__(self, screen, colors, start_point, width, diametr, R1, R2,
                 border_size, type, font = None, axis_center_point = 400, show_measure = True, show_streak = True,
                 left_facet_type = 0, right_facet_type = 0, left_facet_size = 40, right_facet_size = 40, scale = 1):

        self.font = font
        self.scale = scale
        self.super_scale = 0

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
        self.axis_center_height = axis_center_point
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
        self.click_point = (0,0)








