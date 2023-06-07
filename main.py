import pygame
import pyperclip
from reportlab.pdfgen import canvas
import math
import json
from GUI.inputBox import inputBox
from figure.lens import lens
from figure.line_measure import line_measure
from figure.cover_measure import cover_measure
from figure.roughness_measure import roughness_measure
from figure.arrow import arrow
from Template.drawingTemplate import drawingTemplate
from GUI.initImageSurface import initLensTypeImageSurface
import GUI.init_buttoms as initBtn
from GUI.userInterfce import controlPanel
from GUI.userInterfce import controlPanelGroup
from GUI.image import image
from GUI.signature import signature
from Template.cellTemplate import cell
from figure.roughness_measure import roughness_measure
from figure.figure_new.tasks_may.radius_class import Radius

global_x = 'SOS'

# COLORS
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0,0,0)
RED = (255,0,0)
transparent = (0,0,0,0)
colors = {
    'border':WHITE,
    'text':WHITE,
    'selected': RED,
    'background': BLACK,
    'test': RED,
    'transparent': transparent,
    'active': RED
}
save_file = 'config.json'
with open(save_file, encoding='utf-8') as f:
    # Читаем данные из файла
    data = json.load(f)
scale_screen = 1
coef = float(data['Coef'])
size = (210, 297)

pygame.init()

# Создание основного экрана экрана
margin = 120
margin_side_right = 700
margin_side_left = 200
margin_side_top = 0
screen_size = [x * coef + margin for x in size]
screen_size[0] += margin_side_right + margin_side_left
screen = pygame.display.set_mode(tuple(screen_size))
screen.fill(colors['background'])
dt = drawingTemplate(screen, colors, font= 'fonts-GOST\\GOST_AU.TTF',
                 list_size = size,
                 scale = coef,
                 margin = margin,
                 margin_left = margin_side_left,
                margin_right = margin_side_right)

interfacePosX = 10
interfacePosY = margin/2
interfaceBorderSize = 3

ControlPanels = []

leftControlPanel = controlPanel(dt, screen,
                          interfacePosX,
                          interfacePosY, size[0] * 0.8, size[1] * coef, colors, interfaceBorderSize,
                          font= 'fonts-GOST\\GOST_AU.TTF')
leftControlPanel.inputBoxDict, leftControlPanel.buttonDict = \
    initBtn.initLeftPanel(dt, leftControlPanel.surface, colors,
                          border_size=interfaceBorderSize, font = 'fonts-GOST\\GOST_AU.TTF', scale=3  )
ControlPanels.append(leftControlPanel)


#Конец создания основного экрана


commonControlPanelGroup_blit_point = (screen_size[0] - margin_side_right, margin/2 + (screen_size[1] - margin)/2 + margin/8)
commonControlPanelGroup_size =  (margin_side_right - margin/2, (screen_size[1] - margin)/2 - 1*margin/8 )
commonControlPanelGroup = controlPanelGroup(screen, colors,
                                            commonControlPanelGroup_blit_point,
                                           commonControlPanelGroup_size)

controlPanelDict = {}

controlPanelDict['Surface A'] = controlPanel(dt, commonControlPanelGroup.surface, margin/4, margin/8,
                                             commonControlPanelGroup_size[0]*0.45, commonControlPanelGroup_size[1]*0.6,
                                             colors, interfaceBorderSize)
controlPanelDict['Surface A'].inputBoxDict, controlPanelDict['Surface A'].buttonDict = \
    initBtn.initSurfaceA(dt, controlPanelDict['Surface A'].surface, colors,
                         border_size=interfaceBorderSize, font = 'fonts-GOST\\GOST_AU.TTF', scale=coef  )



controlPanelDict['Surface B'] = controlPanel(dt,
                                             commonControlPanelGroup.surface, margin/4 + commonControlPanelGroup_size[0]*0.47, margin/8,
                                             commonControlPanelGroup_size[0]*0.45, commonControlPanelGroup_size[1]*0.6,
                                             colors, interfaceBorderSize)

controlPanelDict['Surface B'].inputBoxDict, controlPanelDict['Surface B'].buttonDict = \
    initBtn.initSurfaceB(dt, controlPanelDict['Surface B'].surface, colors,
                         border_size=interfaceBorderSize, font = 'fonts-GOST\\GOST_AU.TTF', scale=coef  )

controlPanelDict['Focus'] = controlPanel(dt,
                                             commonControlPanelGroup.surface, margin/4 , commonControlPanelGroup_size[1]*0.7,
                                             commonControlPanelGroup_size[0]*0.92, commonControlPanelGroup_size[1]*0.1,
                                             colors, interfaceBorderSize)
controlPanelDict['Focus'].inputBoxDict, controlPanelDict['Focus'].buttonDict = initBtn.initFocusBtn(dt,
                        controlPanelDict['Focus'].surface, colors,
                         border_size=interfaceBorderSize, font = 'fonts-GOST\\GOST_AU.TTF', scale=coef  )


controlPanelDict['Document Info'] = controlPanel(dt,
                                             commonControlPanelGroup.surface, margin/4 , commonControlPanelGroup_size[1]*0.83,
                                             commonControlPanelGroup_size[0]*0.92, commonControlPanelGroup_size[1]*0.14,
                                             colors, interfaceBorderSize)

controlPanelDict['Document Info'].inputBoxDict, controlPanelDict['Document Info'].buttonDict = \
    initBtn.initCustomerBtn(dt,
                        controlPanelDict['Document Info'].surface, colors,
                         border_size=interfaceBorderSize, font = 'fonts-GOST\\GOST_AU.TTF', scale=coef  )

commonControlPanelGroup.controlPanelsDict = controlPanelDict

typeControlPanelGroup_blit_point = (screen_size[0] - margin_side_right, margin/2 )
typeControlPanelGroup_size =  (margin_side_right - margin/2, (screen_size[1] - margin)/2)
typeControlPanelGroup = controlPanelGroup(screen, colors,
                                          typeControlPanelGroup_blit_point,
                                          typeControlPanelGroup_size  )
controlPanelDict = {}
imgSurfaceDict = {}
controlPanelDict['parametr lens'] = controlPanel(dt,
                                             typeControlPanelGroup.surface, margin/4, margin/4,
                                             typeControlPanelGroup_size[0]*0.55, typeControlPanelGroup_size[1]*0.7,
                                             colors, interfaceBorderSize)

controlPanelDict['parametr lens'].inputBoxDict, controlPanelDict['parametr lens'].buttonDict = \
                        initBtn.initLensParamBtn(dt,
                        controlPanelDict['parametr lens'].surface, colors,
                        border_size=interfaceBorderSize, font = 'fonts-GOST\\GOST_AU.TTF', scale=coef)
imgSurfaceDict['lens_image'] = [initLensTypeImageSurface(
    controlPanelDict['parametr lens'].surface, colors, (-10,-10),
    type = 1, font = 'fonts-GOST\\GOST_AU.TTF', scale=coef ), (-10,-10)]
controlPanelDict['parametr lens'].imageSurfaceDict = imgSurfaceDict




controlPanelDict['allowance'] = controlPanel(dt,
                                             typeControlPanelGroup.surface, margin/4 + typeControlPanelGroup_size[0]*0.57, margin/4,
                                             typeControlPanelGroup_size[0]*0.23, typeControlPanelGroup_size[1]*0.7,
                                             colors, interfaceBorderSize)


controlPanelDict['allowance'].inputBoxDict, controlPanelDict['allowance'].buttonDict = \
                        initBtn.initAllowanceBtn(dt,
                        controlPanelDict['allowance'].surface, colors,
                        border_size=interfaceBorderSize, font = 'fonts-GOST\\GOST_AU.TTF', scale=coef)



controlPanelDict['scale'] = controlPanel(dt,
                                             typeControlPanelGroup.surface, margin/4 + typeControlPanelGroup_size[0]*0.83, margin/4,
                                             typeControlPanelGroup_size[0]*0.1, typeControlPanelGroup_size[1]*0.9,
                                             colors, interfaceBorderSize)
controlPanelDict['scale'].inputBoxDict, controlPanelDict['scale'].buttonDict = \
                        initBtn.initScaleBtn(dt,
                        controlPanelDict['scale'].surface, colors,
                        border_size=interfaceBorderSize, font = 'fonts-GOST\\GOST_AU.TTF', scale=coef)

controlPanelDict['facet_type'] = controlPanel(dt,
                                             typeControlPanelGroup.surface, margin/4 , margin/4 + typeControlPanelGroup_size[1]*0.75,
                                             typeControlPanelGroup_size[0]*0.8, typeControlPanelGroup_size[1]*0.15,
                                             colors, interfaceBorderSize)
controlPanelDict['facet_type'].inputBoxDict, controlPanelDict['facet_type'].buttonDict = \
                        initBtn.initFacetTypeBtn(dt,
                        controlPanelDict['facet_type'].surface, colors,
                        border_size=interfaceBorderSize, font = 'fonts-GOST\\GOST_AU.TTF', scale=coef)

typeControlPanelGroup.controlPanelsDict = controlPanelDict

flatFacetControlPanelGroup_blit_point = (screen_size[0] - margin_side_right, margin )
flatFacetControlPanelGroup_size =  (margin_side_right - margin/2, (screen_size[1] - 2*margin)/2)
flatFacetControlPanelGroup = controlPanelGroup(screen, colors,
                                          flatFacetControlPanelGroup_blit_point,
                                          flatFacetControlPanelGroup_size,
                                        is_visible=False)


controlFacetPanelDict = {}
imgFacetSurfaceDict = {}
controlFacetPanelDict['parametr flat facet'] = controlPanel(dt,
                                             flatFacetControlPanelGroup.surface, margin/4, margin/8,
                                             flatFacetControlPanelGroup_size[0]*0.6, flatFacetControlPanelGroup_size[1]*0.7,
                                             colors, interfaceBorderSize)
controlFacetPanelDict['parametr flat facet'].inputBoxDict, controlFacetPanelDict['parametr flat facet'].buttonDict = \
                        initBtn.initFlatFacetParamTypeBtn(dt,
                        controlFacetPanelDict['parametr flat facet'].surface, colors,
                        border_size=interfaceBorderSize, font = 'fonts-GOST\\GOST_AU.TTF', scale=coef)
imgFacetSurfaceDict['lens_image FACET'] = [initLensTypeImageSurface(
    controlFacetPanelDict['parametr flat facet'].surface, colors, (0,0),
    type = 3, font = 'fonts-GOST\\GOST_AU.TTF', scale=coef ), (-10,-10)]

controlFacetPanelDict['parametr flat facet'].imageSurfaceDict = imgFacetSurfaceDict

controlFacetPanelDict['allowance']= controlPanel(dt,
                                             flatFacetControlPanelGroup.surface, margin/2 + flatFacetControlPanelGroup_size[0]*0.6, margin/8,
                                             flatFacetControlPanelGroup_size[0]*0.25, flatFacetControlPanelGroup_size[1]*0.7,
                                             colors, interfaceBorderSize)
controlFacetPanelDict['allowance'].inputBoxDict, controlFacetPanelDict['allowance'].buttonDict = \
                        initBtn.initAllowanceBtn(dt,
                        controlFacetPanelDict['allowance'].surface, colors,
                        border_size=interfaceBorderSize, font = 'fonts-GOST\\GOST_AU.TTF', scale=coef)


controlFacetPanelDict['measure type']= controlPanel(dt,
                                             flatFacetControlPanelGroup.surface, margin/4, margin/5 + flatFacetControlPanelGroup_size[1]*0.7,
                                             flatFacetControlPanelGroup_size[0]*0.9, flatFacetControlPanelGroup_size[1]*0.18,
                                             colors, interfaceBorderSize)
controlFacetPanelDict['measure type'].inputBoxDict, controlFacetPanelDict['measure type'].buttonDict = \
                        initBtn.initFlatFacetMeasureTypeBtn(dt,
                        controlFacetPanelDict['measure type'].surface, colors,
                        border_size=interfaceBorderSize, font = 'fonts-GOST\\GOST_AU.TTF', scale=coef)

flatFacetControlPanelGroup.controlPanelsDict = controlFacetPanelDict


interfacePosX = 10
interfacePosY = 5

topControlPanel = controlPanel(dt, screen,
                          interfacePosX,
                          interfacePosY, screen_size[0] - margin/2 - interfacePosX, 50, colors, interfaceBorderSize,
                          font= 'fonts-GOST\\GOST_AU.TTF')
topControlPanel.inputBoxDict, topControlPanel.buttonDict = \
    initBtn.initTopPanel(dt,
                         topControlPanel.surface, colors, border_size=interfaceBorderSize,
                         font = 'fonts-GOST\\GOST_AU.TTF', FlatFacetPanelControlGroup= flatFacetControlPanelGroup, typeFacetPanelGroup = typeControlPanelGroup, scale=3  )
ControlPanels.append(topControlPanel)

def handleControlPanelevent(event):
    for ControlPanel in ControlPanels:
        inpBox = ControlPanel.handle_event(event)
        if inpBox: return inpBox
    if commonControlPanelGroup.handle_event(event):
        inpBox = commonControlPanelGroup.handle_event(event)
    elif typeControlPanelGroup.handle_event(event):
        inpBox = typeControlPanelGroup.handle_event(event)
    else :
        inpBox = flatFacetControlPanelGroup.handle_event(event)

    if inpBox: return inpBox

# Ожидание выхода из приложения
running = True
is_mouse_down = False
current_input = 0

right_button_down = False

while running:
    screen.fill(BLACK)
    dt.total_draw(scale=scale_screen)
    for ControlPanel in ControlPanels:
        ControlPanel.draw()
    commonControlPanelGroup.draw()
    if (dt.current_figure):
        if dt.current_figure.type > 5:
            typeControlPanelGroup.controlPanelsDict['parametr lens'].DisabledInputBox = ['Радиус 1', 'Радиус 2']
        elif dt.current_figure.type == 2 or dt.current_figure.type == 1:
            typeControlPanelGroup.controlPanelsDict['parametr lens'].DisabledInputBox = ['Радиус 1']
        else:
            typeControlPanelGroup.controlPanelsDict['parametr lens'].DisabledInputBox = []

    typeControlPanelGroup.draw()
    flatFacetControlPanelGroup.draw()

    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # колесо мыши вверх
                print("Колесо мыши вверх")
                dt.scale += 0.1
                dt.current_figure.scale += 0.1
                dt.init_draw_cell()
                dt.draw_param_table()
            elif event.button == 5:  # колесо мыши вниз
                print("Колесо мыши вниз")
                dt.scale += -0.1
                dt.current_figure.scale += -0.1
                dt.init_draw_cell()
                dt.draw_param_table()
        elif event.type == pygame.VIDEORESIZE:
            size = (event.w, event.h)
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RETURN:  # если нажали Enter
                # сохраняем верхнюю половину экрана как изображение
                pygame.image.save(screen.subsurface(pygame.Rect(margin_side_left + margin/2 - interfaceBorderSize/2, margin_side_top + margin/2 - interfaceBorderSize, size[0]*coef + 2*interfaceBorderSize, size[1]*coef + 2*interfaceBorderSize )),
                                  "screenshot.png")

        #########################################################
        # НАЧАЛО СОБЫТИЙ ПРОИСХОДЯЩИХ ПРИ НАЖАТИИ ЛЕВОЙ КНОПКИ МЫШИ
        #######################################################
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('Mouse Down')
            is_mouse_down = True
            if (event.button == 3):
                right_button_down = True
                prev_point_x = dt.reference_point[0]
                prev_point_y = dt.reference_point[1]

            start_pos = pygame.mouse.get_pos()
            prev_pos = start_pos
            current_input =  dt.handle_event(event) if dt.handle_event(event) else handleControlPanelevent(event)

            print('current_input_1',current_input)

            if (isinstance(current_input, lens)) and current_input.select_measure:
                print('CURREN INPUT', current_input.selected_measure)
                if (current_input.select_measure ):
                    if (isinstance(current_input.selected_measure, line_measure )):
                        prev_measure_shift = current_input.selected_measure.measure_shift
                    if (isinstance(current_input.selected_measure, cover_measure ) or
                            isinstance(current_input.selected_measure, roughness_measure)
                    or isinstance(current_input.selected_measure, arrow)):
                        prev_blit_point = current_input.selected_measure.blit_point
                    if (isinstance(current_input.selected_measure, Radius)):
                        pass

            if (isinstance(current_input, image)) and current_input.resize_mode:
                prev_point_x = current_input.point_x
                prev_point_y = current_input.point_y
                prev_height = current_input.height
                prev_width = current_input.width
        #########################################################
        # КОНЕЦ СОБЫТИЙ ПРОИСХОДЯЩИХ ПРИ НАЖАТИИ ЛЕВОЙ КНОПКИ МЫШИ
        #######################################################




        if event.type == pygame.MOUSEBUTTONUP:
            print('Mouse UP')
            right_button_down = False
            is_mouse_down = False
            end_pos = pygame.mouse.get_pos()


        if event.type == pygame.KEYDOWN:
            print('curren_input_2', current_input)
            if (isinstance(current_input, cell) ) or (isinstance(current_input, signature) )or (isinstance(current_input, inputBox)) :

                if event.unicode.isalpha() or event.unicode.isspace() or event.unicode.isdigit():
                    print('current_input.text', current_input.text)
                    current_input.text = current_input.text + event.unicode
                    # Удаление последнего символа из текста
                elif event.key == pygame.K_BACKSPACE:
                    current_input.text = current_input.text[:-1]
                    pass
            if event.key == pygame.K_UP:
                dt.current_scale += 1
                dt.current_figure.scale = dt.scale_list[dt.current_scale]
                dt.cell_dict['scale'].text = dt.scale_text_list[dt.current_scale]
                print("UP")
            elif event.key == pygame.K_DOWN:
                dt\
                    .current_scale += -1
                dt.current_figure.scale = dt.scale_list[dt.current_scale]
                dt.cell_dict['scale'].text = dt.scale_text_list[dt.current_scale]
                print("DOWN")
            elif event.key == pygame.K_LEFT:
                print("LEFT")
                dt.scale += -0.1
                dt.current_figure.scale += -0.04
                dt.init_draw_cell()
                dt.draw_param_table()
                # dt.rescale_cell()
            elif event.key == pygame.K_RIGHT:
                print("RIGHT")
                dt.scale += 0.1
                dt.current_figure.scale += 0.04
                dt.init_draw_cell()
                dt.draw_param_table()
                # dt.rescale_cell()
#########################################################
#НАЧАЛО СОБЫТИЙ ПРОИСХОДЯЩИХ ПРИ ЗАЖАТОЙ КНОПКИ МЫШИ
#######################################################
        if (is_mouse_down):

            cur_pos = pygame.mouse.get_pos()
            x_diff = prev_pos[0] - cur_pos[0]
            y_diff = prev_pos[1] - cur_pos[1]

            if (right_button_down):
                dt.reference_point = (prev_point_x - x_diff, prev_point_y - y_diff)
                dt.change_reference_point()
            elif ( isinstance(current_input,image)):
                if (isinstance(current_input, image)) and current_input.resize_mode:
                    if (current_input.resize_mode == 1):
                        current_input.point_x = prev_point_x - x_diff
                        current_input.point_y = prev_point_y - y_diff
                        current_input.height = prev_height + y_diff
                        current_input.width = prev_width + x_diff
                    if (current_input.resize_mode == 2):
                        current_input.point_y = prev_point_y - y_diff
                        current_input.height = prev_height + y_diff
                        current_input.width = prev_width - x_diff
                    if (current_input.resize_mode == 3):
                        current_input.height = prev_height - y_diff
                        current_input.width = prev_width - x_diff
                    if (current_input.resize_mode == 4):
                        current_input.point_x = prev_point_x - x_diff
                        current_input.height = prev_height - y_diff
                        current_input.width = prev_width + x_diff
                else:
                    current_input.point_x += -x_diff
                    current_input.point_y += -y_diff
            elif isinstance(current_input, lens) :

                if (current_input.select_measure):

                    if (isinstance(current_input.selected_measure, line_measure )):
                        if (current_input.selected_measure.angle_rotate == 0):
                            current_input.selected_measure.measure_shift = prev_measure_shift + y_diff
                        if (current_input.selected_measure.angle_rotate == -90):
                            current_input.selected_measure.measure_shift = prev_measure_shift - x_diff
                    if (isinstance(current_input.selected_measure, cover_measure)
                            or isinstance(current_input.selected_measure, roughness_measure)
                            or isinstance(current_input.selected_measure, arrow)):

                        current_input.selected_measure.blit_point = (prev_blit_point[0] - x_diff ,prev_blit_point[1] - y_diff)

                # События вызываемое если был нажат радису ########
                    if (isinstance(current_input.selected_measure, Radius)):
                        current_input.selected_measure.move_angle(start_pos,(x_diff, y_diff))
                # По этому примеру можно вставлять и другие типы фигур

                else:
                    current_input.blit_point = (current_input.blit_point[0] -x_diff, current_input.blit_point[1]-y_diff)
                    current_input.original_blit_point = current_input.blit_point
                    prev_pos = cur_pos
                    prev_pos = cur_pos

            elif( isinstance(current_input, signature)):
                    current_input.point_x += -x_diff
                    current_input.point_y += -y_diff

                    prev_pos = cur_pos
                    prev_pos = cur_pos

#########################################################
# КОНЕЦ СОБЫТИЙ ПРОИСХОДЯЩИХ ПРИ ЗАЖАТОЙ КНОПКИ МЫШИ
#######################################################
        # # Считываем нажатия клавиш
        keys = pygame.key.get_pressed()
        try:
            if (isinstance(dt.current_figure, lens)):
                imgFacetSurfaceDict['lens_image FACET'] =  [initLensTypeImageSurface(
                    controlPanelDict['parametr lens'].surface, colors, (0, 0),
                    type=2, font='fonts-GOST\\GOST_AU.TTF', scale=0.5,  right_facet_type=1), (-10, -10)]
                imgSurfaceDict['lens_image'] = [initLensTypeImageSurface(
                    controlPanelDict['parametr lens'].surface, colors, (0, 0),
                    type= dt.current_figure.type, font='fonts-GOST\\GOST_AU.TTF', scale=0.5), (-10, -10)]

                controlPanelDict['parametr lens'].imageSurfaceDict = imgSurfaceDict
                typeControlPanelGroup.controlPanelsDict = controlPanelDict

                controlFacetPanelDict['parametr flat facet'].imageSurfaceDict = imgFacetSurfaceDict
                flatFacetControlPanelGroup.controlPanelsDict = controlFacetPanelDict

        except:
            pass

        if keys[pygame.K_LCTRL] and keys[pygame.K_p]:
            dt.add_signature()
        if keys[pygame.K_LCTRL] and keys[pygame.K_m]:
                dt.reference_point = (0,0)
                dt.scale = coef
                dt.current_figure.scale = 1
                dt.init_draw_cell()
                dt.draw_param_table()
                dt.change_reference_point()
        if keys[pygame.K_LCTRL] and keys[pygame.K_o]:
            dt.delete_signature()
        if keys[pygame.K_LCTRL] and keys[pygame.K_DELETE]:
            dt.delete_element(current_input)

        if keys[pygame.K_LCTRL] and keys[pygame.K_v]:
            buff_dict = json.loads(pyperclip.paste())
            if (buff_dict['object_type'] == 'lens'):
                dt.add_lens(
                    (pygame.mouse.get_pos()[0] - 2*buff_dict['width'] ,pygame.mouse.get_pos()[1] - 2*buff_dict['diametr']),
                    buff_dict['width'],
                    buff_dict['diametr'],
                    buff_dict['R1'],
                    buff_dict['R2'],
                    buff_dict['border_size'],
                    buff_dict['type'],
                )
        if keys[pygame.K_LCTRL] and keys[pygame.K_c]:
            if (isinstance(current_input, lens)):
                dict_to_copy = {
                    'object_type': 'lens',
                    'R1':current_input.R1,
                    'R2': current_input.R2,
                    'width': current_input.width,
                    'diametr': current_input.diametr,
                    'border_size' : current_input.border_size,
                    'axis_center_point' : current_input.axis_center_point,
                    'show_measure' : current_input.show_measure,
                    'left_facet_type': current_input.left_facet_type,
                    'right_facet_type': current_input.right_facet_type,
                    'left_facet_size': current_input.left_facet_size,
                    'right_facet_size': current_input.right_facet_size,
                    'type': current_input.type
                }
                pyperclip.copy(json.dumps(dict_to_copy))

# Завершение работы Pygame
pygame.quit()