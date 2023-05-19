import pygame
import radius_class


colors = {
    'border': (255, 255, 255),
    'text': (255, 255, 255),
    'selected': (255, 255, 255),
    'background': (0, 0, 0),
    'test': (255, 0, 0),
    'transparent': (0, 0, 0, 0)
}

pygame.init()
screen = pygame.display.set_mode((600, 600))
surface = pygame.Surface((400, 400), pygame.SRCALPHA)
radius = radius_class.Radius(surface, (0, 0), colors, 50, 40, 2, 180, "text", 1, None, 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            radius.check_click(event.pos)
            radius.move_angle(pygame.mouse.get_pos())



    # отрисовка элементов
    surface.fill((0, 0, 0))
    radius.draw()
    screen.blit(surface, (0, 0))
    pygame.display.update()

pygame.quit()

