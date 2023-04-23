import pygame


class cover_measure:

    def __init__(self, screen, colors, blit_point,
                 width, angle_position, size=(50, 50)):
        self.screen = screen
        self.blit_point = blit_point
        self.width, self.height = size
        self.angle_position = angle_position

        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        # Рисуем крестик на поверхности
        pygame.draw.line(self.surface, colors['border'],
                         (self.width // 2, 0),
                         (self.width // 2, self.height), width)

        pygame.draw.line(self.surface, colors['border'],
                         (0, self.height // 2),
                         (self.width, self.height // 2), width)

        # Рисуем круг на поверхности
        pygame.draw.circle(self.surface, colors['border'], (self.width // 2, self.height // 2), self.width // 2, width)


    def check_click(self, clickpos):

        if (clickpos[0] > 0 and clickpos[1] > 0
                and clickpos[0] < self.width and clickpos[1] < self.height ):
            print('YOU CLICK ON COVER measure')
            return True


    def draw(self):
        ...
