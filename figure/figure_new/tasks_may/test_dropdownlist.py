import pygame
import dropdownlist_class
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Dropdown List Example")
colors = {
    'border': (255, 255, 255),
    'text': (255, 255, 255),
    'selected': (255, 255, 255),
    'background': (0, 0, 0),
    'test': (255, 0, 0),
    'transparent': (0, 0, 0, 0)
}
font = pygame.font.Font(None, 24)

def test_function(option):
    print(option)

dropdown_list = dropdownlist_class.DropdownList(
    window, (10, 10), colors,
    (150, 30),
    ("Option 1", "Option 2", "Option 3", "Option 4", "Option 5", "Option 6", "Option 7"),
    3, test_function,default_value='', scale=1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEMOTION:
            dropdown_list.handle_event(event, pygame.mouse)

    window.fill(BLACK)
    dropdown_list.draw()
    pygame.display.flip()

pygame.quit()