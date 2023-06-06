import pygame
import roughness_class


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
roughness = roughness_class.RoughnessMeasure(surface, (20, 20), colors, 20, 1, 200, 0, text_base_len="Ra3.44", text_method="", text_designation="")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            roughness.check_click(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                roughness.move_angle(pygame.mouse.get_pos())

    # отрисовка элементов
    surface.fill((0, 0, 0))
    roughness.draw()
    screen.blit(surface, (0, 0))
    pygame.display.update()

pygame.quit()