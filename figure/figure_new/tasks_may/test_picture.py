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
picture = picture_class.Picture(surface, (20, 20), (100, 100), colors, 1, 4)
pictures = []
for i in range(1, 17):
    pictures.append(picture_class.Picture(surface, (((i-1) % 4)*90, ((i-1)//4)*90), (80, 80), colors, i, 4))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                picture.scale += 0.5
            if event.key == pygame.K_BACKSPACE:
                picture.scale -= 0.5

    # отрисовка элементов
    surface.fill((0, 0, 0))
    for i in pictures:
        i.draw()
    screen.blit(surface, (0, 0))
    pygame.display.update()

pygame.quit()