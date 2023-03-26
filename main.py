import pygame
from figure.lens import lens
from Template.drawingTemplate import drawingTemplate
from GUI.userInterfce import userInterface

# COLORS
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0,0,0)
RED = (255,0,0)
transparent = (0,0,0,0)
colors = {
    'border':WHITE,
    'text':WHITE,
    'selected': WHITE,
    'background': BLACK,
    'test': RED,
    'transparent': transparent
}

coef = 3
size = (210, 297)

pygame.init()

# Создание экрана
margin = 100
margin_side = 400
screen_size = [x * coef + margin for x in size]
screen_size[0] += margin_side
screen = pygame.display.set_mode(tuple(screen_size))
screen.fill(colors['background'])
dt = drawingTemplate(screen, colors, font= 'fonts-GOST\\ГОСТ тип А наклонный.ttf',
                 list_size = size,
                 scale = coef,
                 margin = margin,
                 margin_side = margin_side)

interfacePosX = margin + size[0]*coef
interfacePosY = margin/2
interfaceBorderSize = 3

Interface = userInterface(dt, screen,
                          interfacePosX,
                          interfacePosY, size[0] * 1.75, size[1] * coef, colors, interfaceBorderSize,
                          font= 'fonts-GOST\\ГОСТ тип А наклонный.ttf')

# Ожидание выхода из приложения
running = True
is_mouse_down = False
while running:
    screen.fill(BLACK)
    dt.total_redraw()
    Interface.redraw()
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RETURN:  # если нажали Enter
                # сохраняем верхнюю половину экрана как изображение
                pygame.image.save(screen.subsurface(pygame.Rect(0, 0, screen_size[0], screen_size[1])),
                                  "screenshot.png")
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('Mouse Down')
            is_mouse_down = True
            start_pos = pygame.mouse.get_pos()
            prev_pos = start_pos
            current_input =  dt.handle_event(event) if dt.handle_event(event) else Interface.handle_event(event)


        if event.type == pygame.MOUSEBUTTONUP:
            print('Mouse UP')
            is_mouse_down = False
            end_pos = pygame.mouse.get_pos()

        if event.type == pygame.KEYDOWN:

            if event.unicode.isalpha() or event.unicode.isspace() or event.unicode.isdigit():
                current_input.text = current_input.text + event.unicode
                pass
                # Удаление последнего символа из текста
            elif event.key == pygame.K_BACKSPACE:
                current_input.text = current_input.text[:-1]
                pass
            # elif event.unicode.isalpha() or event.unicode.isspace() or event.unicode.isdigit():
            #     dt.selected_cell.change_text(dt.selected_cell.text + event.unicode)
            #     Interface.seletedInputBox.text = (dt.selected_cell.text + event.unicode)
            #
            #     pass
            # # Удаление последнего символа из текста
            # elif event.key == pygame.K_BACKSPACE:
            #     dt.selected_cell.change_text(dt.selected_cell.text[:-1])
            #     Interface.seletedInputBox.text = (dt.selected_cell.text[:-1])
            #     pass

        # elif event.type == pygame.MOUSEBUTTONUP:
        #     # Получение координат клика
        #     mouse_x, mouse_y = pygame.mouse.get_pos()
        #     dt.set_selected_cell(dt.check_curren_cell(mouse_x, mouse_y))
        #     Interface.checkBtn(mouse_x, mouse_y)
        #     print(dt.selected_cell)
        if (is_mouse_down):

            cur_pos = pygame.mouse.get_pos()
            x_diff = prev_pos[0] - cur_pos[0]
            y_diff = prev_pos[1] - cur_pos[1]
            if isinstance(current_input, lens):
                current_input.point_x += -x_diff
                current_input.point_y += -y_diff
                print('X_diff', x_diff, 'Y_diff', y_diff)
                prev_pos = cur_pos


        # Считываем нажатия клавиш
        step = 10
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            dt.lens.point_y += -step
        if keys[pygame.K_DOWN]:
            dt.lens.point_y += step
        if keys[pygame.K_LEFT]:
            dt.lens.point_x += -step
        if keys[pygame.K_RIGHT]:
            dt.lens.point_x += step

        if keys[pygame.K_LCTRL] and keys[pygame.K_p]:
            dt.add_signature()
        if keys[pygame.K_LCTRL] and keys[pygame.K_o]:
            dt.delete_signature()


# Завершение работы Pygame
pygame.quit()