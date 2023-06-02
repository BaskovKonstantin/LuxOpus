import pygame
import chamfers_class

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
chamfer = chamfers_class.Chamfers(surface, colors, 50, 2, 40, "fx45", 3, (200, 200), 30, (300, 200), 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            chamfer.check_click(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # chamfer.move_angle(pygame.mouse.get_pos())
                pass

    # отрисовка элементов
    surface.fill((0, 0, 0))
    pygame.draw.circle(surface, (255, 0, 0), (200, 200), 2)
    pygame.draw.circle(surface, (255, 0, 0), (300, 200), 2)
    chamfer.draw()
    screen.blit(surface, (0, 0))
    pygame.display.update()

pygame.quit()
