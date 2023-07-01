import pygame
import base_class


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
surface = pygame.Surface((600, 600), pygame.SRCALPHA)
base = base_class.Base(surface, (0, 0), colors, 50, 10, 10, (10, 10), 180, "A", 0, None, scale=2)
last_click = None
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            last_click = None
        if event.type == pygame.MOUSEBUTTONDOWN:
            if base.check_click(event.pos):
                last_click = event.pos
        if event.type == pygame.MOUSEMOTION:
            if last_click is not None:
                base.move_angle((last_click[0]-pygame.mouse.get_pos()[0], last_click[1]-pygame.mouse.get_pos()[1]))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                base.move_angle(pygame.mouse.get_pos())
            if event.key == pygame.K_BACKSPACE:
                base.scale += 0.5

    # отрисовка элементов
    surface.fill((0, 0, 0))
    base.draw()
    screen.blit(surface, (0, 0))
    pygame.display.update()

pygame.quit()