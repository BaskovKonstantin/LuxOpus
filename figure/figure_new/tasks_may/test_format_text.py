import pygame
import format_text_function


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
text = format_text_function.format_text("Test:<10", colors, 40, 'arial.ttf')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # отрисовка элементов
    surface.fill((0, 0, 0))
    pygame.draw.rect(screen, colors['test'], (10, 10, text.get_width(), text.get_height()), 1)
    screen.blit(text, (10, 10))
    pygame.display.update()

pygame.quit()