import pygame
import picture_class


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
picture = picture_class.Picture(surface, (20, 20), (100, 100), colors, 1, 2)
# pictures = []
# for i in range(1, 28):
#     pictures.append(picture_class.Picture(surface, (((i-1) % 5)*90, ((i-1)//5)*90), (80, 80), colors, i, 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if picture.picture_type > 1:
                    picture.picture_type -= 1
            if event.key == pygame.K_BACKSPACE:
                if picture.picture_type < 27:
                    picture.picture_type += 1

    # отрисовка элементов
    surface.fill((0, 0, 0))
    picture.draw()
    screen.blit(surface, (0, 0))
    pygame.display.update()

pygame.quit()