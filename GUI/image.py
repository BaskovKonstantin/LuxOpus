import easygui
import pygame

class image:

    def __init__(self, startPos, screen, file_path = None, resize_margin = 20):

        self.point_x = startPos[0]
        self.point_y = startPos[1]

        if (file_path == None):
            self.file_path = easygui.fileopenbox()
        else:
            self.file_path = file_path
        print(file_path)
        self.image = pygame.image.load(self.file_path)
        self.screen = screen
        self.resize_margin = resize_margin
        self.resize_mode = False

        self.scale = 1
        self.width = self.image.get_width()
        self.height = self.image.get_height()


    def check_click(self, click_pos):
        width, height = self.image.get_size()

        key_points = list()
        key_points.append((self.point_x, self.point_y))
        key_points.append((self.point_x + self.width, self.point_y))
        key_points.append((self.point_x + self.width, self.point_y + self.height))
        key_points.append((self.point_x, self.point_y + self.height))

        if (click_pos[0] > key_points[0][0] and click_pos[0] < key_points[2][0] and
                click_pos[1] > key_points[0][1] and click_pos[1] < key_points[2][1]):
            print('Click on img')

            for point in key_points:
                if (click_pos[0] > point[0] - self.resize_margin  and click_pos[0] < point[0] + self.resize_margin and
                        click_pos[1] > point[1] - self.resize_margin and click_pos[1] < point[1] + self.resize_margin):
                    self.resize_mode = True
                    if (point == key_points[0]):
                        self.resize_mode = 1
                        print('Левый верхний угол')
                    if (point == key_points[1]):
                        self.resize_mode = 2
                        print('Правый верхний угол')
                    if (point == key_points[2]):
                        self.resize_mode = 3
                        print('Правый нижний угол')
                    if (point == key_points[3]):
                        self.resize_mode = 4
                        print('Левый нижний угол')
                    break
                else:
                    self.resize_mode = False
            return True

        return False

    def draw(self):

        img = pygame.transform.scale(self.image, (self.width , self.height ))
        self.screen.blit(img, (self.point_x, self.point_y))

    # def resize(self, scale):
    #     self.width = self.image.get_width()
    #     self.height = self.image.get_height()