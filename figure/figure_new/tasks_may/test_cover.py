import pygame
import covers_class


colors = {
    'border': (255, 255, 255),
    'text': (255, 255, 255),
    'selected': (255, 255, 255),
    'background': (0, 0, 0),
    'test': (255, 0, 0),
    'transparent': (0, 0, 0, 0)
}

pygame.init()
screen = pygame.display.set_mode((700, 700))
surface = pygame.Surface((700, 700), pygame.SRCALPHA)
cover = covers_class.CoversMeasure(surface, (20, 20), colors, 120, (30, 30), 0, 6, 1, None, 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            cover.check_click(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                cover.move_angle(pygame.mouse.get_pos())

    # отрисовка элементов
    surface.fill((0, 0, 0))
    cover.draw()
    screen.blit(surface, (0, 0))
    pygame.display.update()

pygame.quit()

