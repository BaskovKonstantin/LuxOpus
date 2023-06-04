import json
from GUI.button import button
from GUI.inputBox import inputBox
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from tkinter import filedialog
import pygame
import math
import sys
from figure.figure_new.tasks_may.dropdownlist_class import DropdownList
import win32api
import win32ui
import win32gui
import win32com

def initFlatFacetMeasureTypeBtn(drawingTemplate , interfceSurfce, colors, border_size, font = None, scale = 1):
    buttonDict = {}
    inputBoxDict = {}
    dropDownDict = {}
    button_size = (int(25*scale), int(15*scale))

    def facet_measure_type_1():  # передача i в качестве аргумента по умолчанию
        print('KAAAAAAAAAK 111')
        drawingTemplate.current_figure.right_facet_measure_type = 1


    buttonDict['facet_type_1'] = \
        button(interfceSurfce,
                (int(10*scale), int(5*scale)),
                button_size, colors, action=lambda text: facet_measure_type_1(), text='type_1',
               font=font, font_size= int(4*scale), sign = '')

    def facet_measure_type_2():  # передача i в качестве аргумента по умолчанию
        print('KAAAAAAAAAK 222')
        drawingTemplate.current_figure.right_facet_measure_type = 2


    buttonDict['facet_type_2'] = \
        button(interfceSurfce,
                (int(10*scale) + 1*button_size[0] + 10, int(5*scale)),
                button_size, colors, text='type_2', font=font,
                action=lambda text: facet_measure_type_2(),
                sign = '',
                font_size= int(4*scale))

    def facet_measure_type_3():  # передача i в качестве аргумента по умолчанию
        print('KAAAAAAAAAK 333')
        drawingTemplate.current_figure.right_facet_measure_type = 3


    buttonDict['facet_type_3'] = \
        button(interfceSurfce,
                (int(10*scale) + 2*button_size[0] + int(scale*9), int(5*scale)),
                button_size, colors, text='type_3', font=font,
                action=lambda text: facet_measure_type_3(),
                sign = '',
                font_size= int(4*scale))

    return inputBoxDict, buttonDict
def initFlatFacetParamTypeBtn(drawingTemplate ,interfceSurfce, colors, border_size, font = None, scale = 1):
    buttonDict = {}
    inputBoxDict = {}
    dropDownDict = {}
    button_size = (int(25*scale), int(10*scale))

    def light_diametr(text):
        drawingTemplate.current_figure.right_facet_type = 1
        drawingTemplate.current_figure.right_facet_measure_type = 1
        try:
            drawingTemplate.current_figure.right_facet_size = drawingTemplate.current_figure.diametr - int(text)
            drawingTemplate.current_figure.measureDict['facet_right_side_measure'].text = text

        except:
            print()

    inputBoxDict['light_diametr'] = \
        inputBox(interfceSurfce,
                (int(120*scale), int(5*scale)),
                button_size, colors, text='**', font=font,
                onChangeAction=lambda text: light_diametr(text),
                sign = 'Свет.диаметр D2',
                font_size= int(4*scale))

    def deflection_arrow(text):
        print('kkkkkdfskdfjlsdkf')
        drawingTemplate.current_figure.right_facet_type = 1
        drawingTemplate.current_figure.right_facet_measure_type = 3
        try:
            res = drawingTemplate.current_figure.width / 10 + \
                (drawingTemplate.current_figure.R2 - math.sqrt(
                    (drawingTemplate.current_figure.R2) ** 2 - (
                            (drawingTemplate.current_figure.R2 - int(text)) / 2) ** 2))
            drawingTemplate.current_figure.right_facet_size = res

        except Exception as e:
            print(e)
            # drawingTemplate.current_figure.right_facet_size = 0
            print('Some kind of shit rfc')




    inputBoxDict['deflection_arrow'] = \
        inputBox(interfceSurfce,
                (int(120*scale) , int(5*scale) + 1*button_size[0] + 10),
                button_size, colors, text='**', font=font,
                onChangeAction=lambda text: deflection_arrow(text),
                sign = 'Стрелка прогиба l2',
                font_size= int(4*scale))

    def overall_thickness(text):
        drawingTemplate.current_figure.right_facet_type = 1
        drawingTemplate.current_figure.right_facet_measure_type = 2
        try:
            drawingTemplate.current_figure.right_facet_size = drawingTemplate.current_figure.R1 - int(text)
            drawingTemplate.current_figure.measureDict['facet_right_big_measure'].text = text

        except:
            print('Some kind of shit lfc')

    inputBoxDict['overall thickness'] = \
        inputBox(interfceSurfce,
                (int(120*scale) , int(5*scale) + 2*button_size[0] + 10),
                button_size, colors, text='**', font=font,
                onChangeAction=lambda text: overall_thickness(text),
                sign = 'Общая толщина',
                font_size= int(4*scale))

    return inputBoxDict, buttonDict
def initFacetTypeBtn(drawingTemplate , interfceSurfce, colors, border_size, font = None, scale = 1):
    buttonDict = {}
    inputBoxDict = {}
    dropDownDict = {}
    button_size = (int(25*scale), int(15*scale))

    def facet_type_1(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT 555555', text)
    buttonDict['facet_type_1'] = \
        button(interfceSurfce,
                (int(10*scale), int(5*scale)),
                button_size, colors, text='type_1', font=font,
                action=lambda text: facet_type_1(text),
                sign = '',
                font_size= int(4*scale))
    def facet_type_2(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT 9999999', text)
    buttonDict['facet_type_2'] = \
        button(interfceSurfce,
                (int(10*scale) + 1*button_size[0] + 10, int(5*scale)),
                button_size, colors, text='type_2', font=font,
                action=lambda text: facet_type_2(text),
                sign = '',
                font_size= int(4*scale))
    def facet_type_3(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT 11111111', text)
    buttonDict['facet_type_3'] = \
        button(interfceSurfce,
                (int(10*scale) + 2*button_size[0] + int(scale*9), int(5*scale)),
                button_size, colors, text='type_3', font=font,
                action=lambda text: facet_type_3(text),
                sign = '',
                font_size= int(4*scale))
    def facet_type_4(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT 77777777', text)
    buttonDict['facet_type_4'] = \
        button(interfceSurfce,
                (int(10*scale) + 3*button_size[0] + 30,int(5*scale)),
                button_size, colors, text='type_4', font=font,
                action=lambda text: facet_type_1(text),
                sign = '',
                font_size= int(4*scale))


    return inputBoxDict, buttonDict
def initAllowanceBtn(drawingTemplate , interfceSurfce, colors, border_size, font = None, scale = 1):
    buttonDict = {}
    inputBoxDict = {}
    dropDownDict = {}
    button_size = (int(23*scale), int(8*scale))
    button_size_small = (int(12*scale), int(8*scale))

    #Первая пятерка
    def Allowance_1_1(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['Allowance_1_1'] = \
        inputBox(interfceSurfce,
                (int(3*scale),int(3*scale)),
                button_size, colors, text='', font=font,
                onChangeAction=lambda text: Allowance_1_1(text),
                sign = '',
                 font_size=int(scale*4))
    def Allowance_1_2(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['Allowance_1_2'] = \
        inputBox(interfceSurfce,
                (int(28*scale),int(3*scale)),
                button_size_small, colors, text='', font=font,
                onChangeAction=lambda text: Allowance_1_2(text),
                sign = '',
                 font_size=int(scale*4))
    def Allowance_1_3(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['Allowance_1_3'] = \
        inputBox(interfceSurfce,
                (int(41*scale),int(3*scale)),
                button_size_small, colors, text='', font=font,
                onChangeAction=lambda text: Allowance_1_3(text),
                sign = '',
                 font_size=int(scale*4))

    def Allowance_1_4(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['Allowance_1_4'] = \
        inputBox(interfceSurfce,
                (int(27*scale),int(13*scale)),
                button_size_small, colors, text='', font=font,
                onChangeAction=lambda text: Allowance_1_4(text),
                sign = '',
                 font_size=int(scale*4))
    def Allowance_1_5(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['Allowance_1_5'] = \
        inputBox(interfceSurfce,
                (int(41*scale),int(13*scale)),
                button_size_small, colors, text='', font=font,
                onChangeAction=lambda text: Allowance_1_5(text),
                sign = '',
                 font_size=int(scale*4))

    # Вторая пятерка
    def Allowance_2_1(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)

    inputBoxDict['Allowance_2_1'] = \
        inputBox(interfceSurfce,
                 (int(3*scale), int(27*scale)),
                 button_size, colors, text='', font=font,
                 onChangeAction=lambda text: Allowance_2_1(text),
                 sign='',
                 font_size=int(scale*4))

    def Allowance_2_2(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)

    inputBoxDict['Allowance_2_2'] = \
        inputBox(interfceSurfce,
                 (int(scale*28), int(scale*28)),
                 button_size_small, colors, text='', font=font,
                 onChangeAction=lambda text: Allowance_2_2(text),
                 sign='',
                 font_size=int(scale*4))

    def Allowance_2_3(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)

    inputBoxDict['Allowance_2_3'] = \
        inputBox(interfceSurfce,
                 (int(scale*41), int(scale*28)),
                 button_size_small, colors, text='', font=font,
                 onChangeAction=lambda text: Allowance_2_3(text),
                 sign='',
                 font_size=int(scale*4))

    def Allowance_2_4(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)

    inputBoxDict['Allowance_2_4'] = \
        inputBox(interfceSurfce,
                 (int(scale*28), int(scale*37)),
                 button_size_small, colors, text='', font=font,
                 onChangeAction=lambda text: Allowance_2_4(text),
                 sign='',
                 font_size=int(scale*4))

    def Allowance_2_5(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)

    inputBoxDict['Allowance_2_5'] = \
        inputBox(interfceSurfce,
                 (int(scale*41), int(scale*37)),
                 button_size_small, colors, text='', font=font,
                 onChangeAction=lambda text: Allowance_2_5(text),
                 sign='',
                 font_size=int(scale*4))

    # Третья пятерка
    def Allowance_3_1(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)

    inputBoxDict['Allowance_3_1'] = \
        inputBox(interfceSurfce,
                 (int(scale*3), int(scale*51)),
                 button_size, colors, text='', font=font,
                 onChangeAction=lambda text: Allowance_3_1(text),
                 sign='',
                 font_size=int(scale*4))

    def Allowance_3_2(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)

    inputBoxDict['Allowance_3_2'] = \
        inputBox(interfceSurfce,
                 (int(scale*28), int(scale*51)),
                 button_size_small, colors, text='', font=font,
                 onChangeAction=lambda text: Allowance_3_2(text),
                 sign='',
                 font_size=int(scale*4))

    def Allowance_3_3(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)

    inputBoxDict['Allowance_3_3'] = \
        inputBox(interfceSurfce,
                 (int(scale*41), int(scale*51)),
                 button_size_small, colors, text='', font=font,
                 onChangeAction=lambda text: Allowance_3_3(text),
                 sign='',
                 font_size=int(scale*4))

    def Allowance_3_4(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)

    inputBoxDict['Allowance_3_4'] = \
        inputBox(interfceSurfce,
                 (int(scale*28), int(scale*61)),
                 button_size_small, colors, text='', font=font,
                 onChangeAction=lambda text: Allowance_3_4(text),
                 sign='',
                 font_size=int(scale*4))

    def Allowance_3_5(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)

    inputBoxDict['Allowance_3_5'] = \
        inputBox(interfceSurfce,
                 (int(scale*41), int(scale*61)),
                 button_size_small, colors, text='', font=font,
                 onChangeAction=lambda text: Allowance_3_5(text),
                 sign='',
                 font_size=int(scale*4))


    return inputBoxDict, buttonDict
def initLensParamBtn(drawingTemplate , interfceSurfce, colors, border_size, font = None, scale = 1):
    buttonDict = {}
    inputBoxDict = {}
    dropDownDict = {}
    button_size = (int(scale*20), int(scale*10))

    def diametr(text):  # передача i в качестве аргумента по умолчанию
        if (text.isnumeric()): drawingTemplate.current_figure.diametr = int(text)
    inputBoxDict['Диаметр'] = \
        inputBox(interfceSurfce,
                (int(scale*90),int(scale*3)),
                button_size, colors, text='*', font=font,
                onChangeAction=lambda text: diametr(text),
                sign = 'Диаметр',
                 font_size=int(scale*5))
    def diametr_2(text):  # передача i в качестве аргумента по умолчанию
        print('', text)
    inputBoxDict['Диаметр 2'] = \
        inputBox(interfceSurfce,
                (int(scale*90) + button_size[0] + 5, int(scale*3)),
                button_size, colors, text='', font=font,
                onChangeAction=lambda text: diametr_2(text),
                sign = '',
                 font_size=int(scale*5))

    def width(text):  # передача i в качестве аргумента по умолчанию
        if (text.isnumeric()): drawingTemplate.current_figure.width = int(text)
    inputBoxDict['Толщина'] = \
        inputBox(interfceSurfce,
                (int(scale*90), int(scale*19)),
                button_size, colors, text='*', font=font,
                onChangeAction=lambda text: width(text),
                sign = 'Толщина',
                 font_size=int(scale*5))

    def facet(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['Фаска'] = \
        inputBox(interfceSurfce,
                (int(scale*90), int(scale*30)),
                button_size, colors, text='', font=font,
                onChangeAction=lambda text: facet(text),
                sign = 'Фаска',
                 font_size=int(scale*5))
    def facet_2(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['Фаска 2'] = \
        inputBox(interfceSurfce,
                (int(scale*90) + button_size[0] + 5,int(scale*30)),
                button_size, colors, text='', font=font,
                onChangeAction=lambda text: facet_2(text),
                sign = '',
                 font_size=int(scale*5))

    def Radius_1(text):  # передача i в качестве аргумента по умолчанию
        if (text.isnumeric()): drawingTemplate.current_figure.R1 = int(text)

    inputBoxDict['Радиус 1'] = \
        inputBox(interfceSurfce,
                (int(scale*90), int(scale*43)),
                button_size, colors, text='*', font=font,
                onChangeAction=lambda text: Radius_1(text),
                sign = 'Радиус 1',
                 font_size=int(scale*5))

    def Radius_2(text):  # передача i в качестве аргумента по умолчанию
        if (text.isnumeric()): drawingTemplate.current_figure.R2 = int(text)

    inputBoxDict['Радиус 2'] = \
        inputBox(interfceSurfce,
                (int(scale*90), int(scale*57)),
                button_size, colors, text='*', font=font,
                onChangeAction=lambda text: Radius_2(text),
                sign = 'Радиус 2',
                 font_size=int(scale*5))



    return inputBoxDict, buttonDict
def initCustomerBtn(drawingTemplate , interfceSurfce, colors, border_size, font = None, scale = 1):
    buttonDict = {}
    inputBoxDict = {}
    dropDownDict = {}
    button_size = (int(scale*40), int(scale*8))

    def order_number(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['order number'] = \
        inputBox(interfceSurfce,
                (int(scale*57),int(int(scale*2))),
                button_size, colors, text='', font=font,
                onChangeAction=lambda text: order_number(text),
                sign = 'Номер заказа')

    def catalog_number(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['Focus lenses for the visible spectrum'] = \
        inputBox(interfceSurfce,
                (int(scale*57), int(scale*10)),
                button_size, colors, text='', font=font,
                onChangeAction=lambda text: catalog_number(text),
                sign = 'Каталожный номер')

    def material_detail(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['material detail'] = \
        inputBox(interfceSurfce,
                (int(scale*50) + button_size[0] + int(scale*50),int(int(scale*2))),
                button_size, colors, text='', font=font,
                onChangeAction=lambda text: material_detail(text),
                sign = 'Номер заказа')

    def PN_number(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['PN number'] = \
        inputBox(interfceSurfce,
                (int(scale*50) + button_size[0] + int(scale*50), int(scale*10)),
                button_size, colors, text='', font=font,
                onChangeAction=lambda text: catalog_number(text),
                sign = 'PN номер')

    return inputBoxDict, buttonDict
def initFocusBtn(drawingTemplate , interfceSurfce, colors, border_size, font = None, scale = 1):
    buttonDict = {}
    inputBoxDict = {}
    dropDownDict = {}
    button_size = (int(scale*40), int(scale*9))

    def focus_lens(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['focus_lens'] = \
        inputBox(interfceSurfce,
                (int(scale*50),5),
                button_size, colors, text='', font=font,
                onChangeAction=lambda text: focus_lens(text),
                sign = 'Фокус линзы')

    def focus_lenses_for_the_visible_spectrum(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['Focus lenses for the visible spectrum'] = \
        inputBox(interfceSurfce,
                (int(scale*57) + button_size[0] + 260, 5),
                button_size, colors, text='', font=font,
                onChangeAction=lambda text: focus_lenses_for_the_visible_spectrum(text),
                sign = 'Фокус линзы для видимого спектра')

    return inputBoxDict, buttonDict
def initSurfaceA(drawingTemplate , interfceSurfce, colors, border_size, font = None, scale = 1):
    buttonDict = {}
    inputBoxDict = {}
    dropDownDict = {}
    button_size = (int(scale*40), int(scale*10))
    button_size_small = (int(scale*10), int(scale*10))

    def roughness(text):  # передача i в качестве аргумента по умолчанию
        drawingTemplate.current_figure.measureDict['roughness_measure_1'].text_base_len = str(text)
        print('INPUT BOX TEXT', text)
    inputBoxDict['roughness'] = \
        inputBox(interfceSurfce,
                (int(scale*57),int(scale*3)),
                button_size, colors, text='12', font=font,
                onChangeAction=lambda text: roughness(text),
                sign = 'Шероховатость')

    def general_error(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['general error'] = \
        inputBox(interfceSurfce,
                 (int(scale*57), int(scale*15)),
                 button_size, colors, text='', font=font,
                 onChangeAction=lambda text: general_error(text),
                 sign='Общая ошибка')

    def general_error_2(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['general error 2'] = \
        inputBox(interfceSurfce,
                 (int(scale*57) + button_size[0]  + 5, int(scale*15)),
                 button_size_small, colors, text='', font=font,
                 onChangeAction=lambda text: general_error_2(text),
                 sign='')

    def Local_error(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['Local error'] = \
        inputBox(interfceSurfce,
                 (int(scale*57), int(scale*27)),
                 button_size, colors, text='', font=font,
                 onChangeAction=lambda text: Local_error(text),
                 sign='Местная ошибка')

    def Purity(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['Purity'] = \
        inputBox(interfceSurfce,
                 (int(scale*57), int(scale*39)),
                 button_size, colors, text='', font=font,
                 onChangeAction=lambda text: Purity(text),
                 sign='Чистота')

    def Light_diameter(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['Light diameter'] = \
        inputBox(interfceSurfce,
                 (int(scale*57), int(scale*51)),
                 button_size, colors, text='', font=font,
                 onChangeAction=lambda text: Light_diameter(text),
                 sign='Световой диаметр')

    def light_diameter_2(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['light diameter 2'] = \
        inputBox(interfceSurfce,
                 (int(scale*57) + button_size[0]  + 5, int(scale*51)),
                 button_size_small, colors, text='', font=font,
                 onChangeAction=lambda text: light_diameter_2(text),
                 sign='')

    def customer_radius(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['customer radius'] = \
        inputBox(interfceSurfce,
                 (int(scale*57), int(scale*63)),
                 button_size, colors, text='', font=font,
                 onChangeAction=lambda text: customer_radius(text),
                 sign='Радиус заказчика')


    return inputBoxDict, buttonDict
def initSurfaceB(drawingTemplate , interfceSurfce, colors, border_size, font = None, scale = 1):
    buttonDict = {}
    inputBoxDict = {}
    dropDownDict = {}
    button_size = (int(scale*40), int(scale*10))
    button_size_small = (int(scale*10), int(scale*10))

    def roughness(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['roughness'] = \
        inputBox(interfceSurfce,
                (int(scale*57),int(scale*3)),
                button_size, colors, text='', font=font,
                onChangeAction=lambda text: roughness(text),
                sign = 'Шероховатость')

    def general_error(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['general error'] = \
        inputBox(interfceSurfce,
                 (int(scale*57), int(scale*15)),
                 button_size, colors, text='', font=font,
                 onChangeAction=lambda text: general_error(text),
                 sign='Общая ошибка')

    def general_error_2(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['general error 2'] = \
        inputBox(interfceSurfce,
                 (int(scale*57) + button_size[0]  + 5, int(scale*15)),
                 button_size_small, colors, text='', font=font,
                 onChangeAction=lambda text: general_error_2(text),
                 sign='')

    def Local_error(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['Local error'] = \
        inputBox(interfceSurfce,
                 (int(scale*57), int(scale*27)),
                 button_size, colors, text='', font=font,
                 onChangeAction=lambda text: Local_error(text),
                 sign='Местная ошибка')

    def Purity(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['Purity'] = \
        inputBox(interfceSurfce,
                 (int(scale*57), int(scale*39)),
                 button_size, colors, text='', font=font,
                 onChangeAction=lambda text: Purity(text),
                 sign='Чистота')

    def Light_diameter(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['Light diameter'] = \
        inputBox(interfceSurfce,
                 (int(scale*57), int(scale*51)),
                 button_size, colors, text='', font=font,
                 onChangeAction=lambda text: Light_diameter(text),
                 sign='Световой диаметр')

    def light_diameter_2(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['light diameter 2'] = \
        inputBox(interfceSurfce,
                 (int(scale*57) + button_size[0]  + 5, int(scale*51)),
                 button_size_small, colors, text='', font=font,
                 onChangeAction=lambda text: light_diameter_2(text),
                 sign='')

    def customer_radius(text):  # передача i в качестве аргумента по умолчанию
        print('INPUT BOX TEXT', text)
    inputBoxDict['customer radius'] = \
        inputBox(interfceSurfce,
                 (int(scale*57), int(scale*63)),
                 button_size, colors, text='', font=font,
                 onChangeAction=lambda text: customer_radius(text),
                 sign='Радиус заказчика')


    return inputBoxDict, buttonDict
def initTopPanel(drawingTemplate, interfceSurfce,  colors, border_size, font, FlatFacetPanelControlGroup,typeFacetPanelGroup, scale = 1):
    buttonDict = {}
    inputBoxDict = {}
    dropDownDict = {}
    button_size = (int(scale*13), int(scale*20))
    button_size_big = (int(scale * 30), int(scale * 20))

    def end():  # передача i в качестве аргумента по умолчанию
        sys.exit()

    buttonDict[f'END'] = button(interfceSurfce, (0, 0), button_size,
                                         colors, lambda : end(), 'END', font,
                                         border_size=border_size)

    def save_file():  # передача i в качестве аргумента по умолчанию
        dlg = win32ui.CreateFileDialog(1)  # 1 - режим открытия файла
        dlg.DoModal()

        # Получаем путь к выбранному файлу
        file_path = dlg.GetPathName()
        drawingTemplate.save_file = file_path
        drawingTemplate.set_base_text()
        drawingTemplate.init_draw_cell()

    buttonDict[f'save_file'] = button(interfceSurfce, (int(scale*15), 0), button_size,
                                         colors, lambda : save_file(), 'load', font,
                                         border_size=border_size)

    def swith_measure():  # передача i в качестве аргумента по умолчанию
        drawingTemplate.current_figure.show_measure = not drawingTemplate.current_figure.show_measure


    buttonDict[f'Measure'] = button(interfceSurfce, (2*int(scale*15), 0), button_size_big,
                                         colors, lambda : swith_measure(), 'Measure', font,
                                         border_size=border_size)

    def swith_FlatFacetControlPanelGroup():  # передача i в качестве аргумента по умолчанию
        FlatFacetPanelControlGroup.is_visible = not FlatFacetPanelControlGroup.is_visible
        typeFacetPanelGroup.is_visible = not typeFacetPanelGroup.is_visible

    buttonDict[f'FlatFacetControlPanelGroup'] = button(interfceSurfce, (3*int(scale*20), 0), button_size_big,
                                         colors, lambda : swith_FlatFacetControlPanelGroup(), 'FlatFacet', font,
                                         border_size=border_size)


    def PDF():  # передача i в качестве аргумента по умолчанию
        save_file = 'config.json'
        with open(save_file, encoding='utf-8') as f:
            # Читаем данные из файла
            data = json.load(f)
        scale = 5
        drawingTemplate.scale = scale
        drawingTemplate.current_figure.scale = scale/2.5
        drawingTemplate.reference_point = (0,0)
        drawingTemplate.init_draw_cell()
        drawingTemplate.draw_param_table()
        drawingTemplate.total_redraw()


        image_filename = filedialog.asksaveasfilename(defaultextension='.pdf')

        # Создание PDF-документа
        pygame.image.save(drawingTemplate.surface,image_filename[:-4]+".jpg")


        # Создание PDF-документа
        pdf_filename = image_filename + ".pdf"
        pdf_canvas = canvas.Canvas(pdf_filename, pagesize= (int(drawingTemplate.surface.get_width()), int(drawingTemplate.surface.get_height())))

        # Рисование изображения на PDF-документе
        with open(image_filename[:-4]+".jpg", "rb") as f:
            image_reader = ImageReader(f)
            pdf_canvas.drawImage(image_reader, 0, 0, width=int(drawingTemplate.surface.get_width()), height=int(drawingTemplate.surface.get_height()))

        # Завершение PDF-документа
        pdf_canvas.showPage()
        pdf_canvas.save()
        print('MAKE image')
        scale = float(data['Coef'])
        drawingTemplate.scale = scale
        drawingTemplate.current_figure.scale = scale/2.5
        drawingTemplate.reference_point = (0,0)
        drawingTemplate.init_draw_cell()
        drawingTemplate.draw_param_table()
        drawingTemplate.total_redraw()

    buttonDict[f'PDF'] = button(interfceSurfce, (5*int(scale*20), 0), button_size_big,
                                         colors, lambda : PDF(), 'PDF', font,
                                         border_size=border_size)

    return inputBoxDict, buttonDict
def initLeftPanel(drawingTemplate, interfceSurfce,  colors, border_size, font, scale = 1):
    buttonDict = {}
    inputBoxDict = {}
    dropDownDict = {}

    button_size = (int(scale*55), int(scale*13))

    def test_function(option):
        print(option)

    dropDownDict['dropDownList_Type'] = DropdownList(
        interfceSurfce,
        (0, 0),
        colors,
        button_size,
        ("Type 1", "Type 2", "Type 3", "Type 4", "Type 5"),
        3, test_function, default_value='', scale=1, font = font
    )

    # for i in range(1, 6):
    #     def buff(i=i):  # передача i в качестве аргумента по умолчанию
    #         drawingTemplate.current_figure.type = int(i)
    #         print('TYPE ',i)
    #
    #     buttonDict[f'set type {i}'] = button(interfceSurfce, (0, button_size[1] * (i - 1)), button_size,
    #                                          colors, lambda i=i: buff(i), f'type {i}', font,
    #                                          border_size=border_size)
    def add_lens():  # передача i в качестве аргумента по умолчанию
        drawingTemplate.add_lens()

    buttonDict[f'add_lens'] = button(interfceSurfce, (0, button_size[1] * 12), button_size,
                                          colors, lambda: add_lens(), 'add lens', font,
                                          border_size=border_size)

    def add_img():  # передача i в качестве аргумента по умолчанию
        drawingTemplate.add_img()

    buttonDict[f'add_img'] = button(interfceSurfce, (0, button_size[1] * 13), button_size,
                                         colors, lambda: add_img(), 'add img', font,
                                         border_size=border_size)

    return inputBoxDict, buttonDict

# def initButton(drawingTemplate, interfceSurfce,  colors, border_size, font, scale = 1):
#     buttonDict = dict()
#
#     button_size = (int(scale*29), int(scale*13))
#
#     for i in range(1, 11):
#         def buff(i=i):  # передача i в качестве аргумента по умолчанию
#             drawingTemplate.current_figure.type = int(i)
#
#         buttonDict[f'set type {i}'] = button(interfceSurfce, (0, button_size[1] * (i - 1)), button_size,
#                                                   colors, lambda i=i: buff(i), f'type {i}', font,
#                                                   border_size=border_size)
#
#     for i in range(0, 3):
#         def lf_buff(i=i):  # передача i в качестве аргумента по умолчанию
#             drawingTemplate.current_figure.left_facet_type = int(i)
#
#         buttonDict[f'set left facet type {i}'] = button(interfceSurfce,
#                                                              (button_size[0] + 5, button_size[1] * (i)), button_size,
#                                                              colors, lambda i=i: lf_buff(i),
#                                                              f'left_facet_type {i}', font, font_size=9,
#                                                              border_size=border_size)
#     for i in range(0, 3):
#         def rf_buff(i=i):  # передача i в качестве аргумента по умолчанию
#             drawingTemplate.current_figure.right_facet_type = int(i)
#
#
#         buttonDict[f'set right facet type {i}'] = button(interfceSurfce,
#                                                               (2 * button_size[0] + 2 * 5, button_size[1] * (i)),
#                                                               button_size,
#                                                               colors, lambda i=i: rf_buff(i),
#                                                               f'right_facet_type {i}', font, font_size=9,
#                                                               border_size=border_size)
#
#     def add_lens():  # передача i в качестве аргумента по умолчанию
#         drawingTemplate.add_lens()
#
#
#     buttonDict[f'add_lens'] = button(interfceSurfce, (int(scale*57), int(scale*93)), button_size,
#                                           colors, lambda: add_lens(), 'add lens', font,
#                                           border_size=border_size)
#
#     def add_img():  # передача i в качестве аргумента по умолчанию
#         drawingTemplate.add_img()
#
#
#     buttonDict[f'add_img'] = button(interfceSurfce, (int(scale*57), 320), button_size,
#                                          colors, lambda: add_img(), 'add img', font,
#                                          border_size=border_size)
#     inputBoxDict = dict()
#
#     def lfs_flat_1(text):  # передача i в качестве аргумента по умолчанию
#         try:
#             drawingTemplate.current_figure.left_facet_size = drawingTemplate.current_figure.R1 - int(text)
#             drawingTemplate.current_figure.left_facet_measure_type = 2
#             drawingTemplate.current_figure.measureDict['facet_left_big_measure'].text = text
#         except:
#             print('Some kind of shit lfc')
#
#     inputBoxDict['left_facet_flat_1_inpBox'] = inputBox(interfceSurfce,
#                                                              (button_size[0] + 5, button_size[1] * (3)),
#                                                              button_size, colors, text='150', font=font,
#                                                              onChangeAction=lambda text: lfs_flat_1(text))
#
#     def lfs_flat_2(text):  # передача i в качестве аргумента по умолчанию
#         try:
#             drawingTemplate.current_figure.left_facet_size = int(
#                 drawingTemplate.current_figure.R1 - (int(text) + drawingTemplate.current_figure.width))
#             drawingTemplate.current_figure.left_facet_measure_type = 3
#             drawingTemplate.current_figure.measureDict['facet_left_up_small_measure'].text = text
#         except:
#             print('Some kind of shit lfc')
#
#     inputBoxDict['left_facet_flat_2_inpBox'] = inputBox(interfceSurfce,
#                                                              (button_size[0] + 5, button_size[1] * (4)),
#                                                              button_size, colors, text='0', font=font,
#                                                              onChangeAction=lambda text: lfs_flat_2(text))
#
#     def lfs_flat_3(text):  # передача i в качестве аргумента по умолчанию
#         try:
#             drawingTemplate.current_figure.left_facet_size = drawingTemplate.current_figure.width / 10 + \
#                                                                   (drawingTemplate.current_figure.R1 - math.sqrt(
#                                                                       (drawingTemplate.current_figure.R1) ** 2 -
#                                                                       ((drawingTemplate.current_figure.R1 - int(text)) / 2) ** 2))
#             drawingTemplate.current_figure.left_facet_measure_type = 1
#             drawingTemplate.current_figure.measureDict['facet_left_side_measure'].text = text
#         except:
#             print('Some kind of shit lfc')
#
#     inputBoxDict['left_facet_flat_3_inpBox'] = inputBox(interfceSurfce,
#                                                              (button_size[0] + 5, button_size[1] * (5)),
#                                                              button_size, colors, text='0', font=font,
#                                                              onChangeAction=lambda text: lfs_flat_3(text))
#
#     def rfs_flat_1(text):  # передача i в качестве аргумента по умолчанию
#         try:
#             drawingTemplate.current_figure.right_facet_size = drawingTemplate.current_figure.R2 - int(text)
#             drawingTemplate.current_figure.right_facet_measure_type = 2
#             drawingTemplate.current_figure.measureDict['facet_right_up_big_measure'].text = text
#         except Exception as e:
#             print(e)
#             print('Some kind of shit rfc')
#
#     inputBoxDict['right_facet_flat_1_inpBox'] = inputBox(interfceSurfce,
#                                                               (2 * button_size[0] + 2 * 5, button_size[1] * (3)),
#                                                               button_size, colors, text='150', font=font,
#                                                               onChangeAction=lambda text: rfs_flat_1(text))
#
#     def rfs_flat_2(text):  # передача i в качестве аргумента по умолчанию
#         try:
#             drawingTemplate.current_figure.right_facet_size = \
#                 int(drawingTemplate.current_figure.R2 - (int(text) + drawingTemplate.current_figure.width))
#             drawingTemplate.current_figure.right_facet_measure_type = 3
#             drawingTemplate.current_figure.measureDict['facet_right_up_small_measure'].text = text
#         except:
#             print('Some kind of shit rfc')
#
#     inputBoxDict['right_facet_flat_2_inpBox'] = inputBox(interfceSurfce,
#                                                               (2 * button_size[0] + 2 * 5, button_size[1] * (4)),
#                                                               button_size, colors, text='0', font=font,
#                                                               onChangeAction=lambda text: rfs_flat_2(text))
#
#     def rfs_flat_3(text):  # передача i в качестве аргумента по умолчанию
#         try:
#             res = drawingTemplate.current_figure.width / 10 + \
#                   (drawingTemplate.current_figure.R2 - math.sqrt(
#                       (drawingTemplate.current_figure.R2) ** 2 - (
#                                   (drawingTemplate.current_figure.R2 - int(text)) / 2) ** 2))
#             drawingTemplate.current_figure.right_facet_measure_type = 1
#             drawingTemplate.current_figure.measureDict['facet_right_side_measure'].text = text
#
#         except Exception as e:
#             print(e)
#             pass
#
#         try:
#             drawingTemplate.current_figure.right_facet_size = res
#         except Exception as e:
#             print(e)
#             drawingTemplate.current_figure.right_facet_size = 0
#             print('Some kind of shit rfc')
#         # drawingTemplate.current_figure.right_facet_size = drawingTemplate.current_figure.width/10 +\
#         #                                                     int( drawingTemplate.current_figure.R2/10 -
#         #                                                     math.sqrt((drawingTemplate.current_figure.R2/10) **2 - (int(text)/2)**2))
#
#     inputBoxDict['right_facet_flat_3_inpBox'] = inputBox(interfceSurfce,
#                                                               (2 * button_size[0] + 2 * 5, button_size[1] * (5)),
#                                                               button_size, colors, text='0', font=font,
#                                                               onChangeAction=lambda text: rfs_flat_3(text))
#
#     def R1_buff(text):  # передача i в качестве аргумента по умолчанию
#         try:
#             drawingTemplate.current_figure.R1 = int(text)
#         except:
#             print('Some kind of shit r1')
#
#     inputBoxDict['R1_inpBox'] = inputBox(interfceSurfce, (3 * button_size[0] + 3 * 5, button_size[1] * (0)),
#                                               button_size, colors, text='R1', font=font,
#                                               onChangeAction=lambda text: R1_buff(text))
#
#     def R2_buff(text):  # передача i в качестве аргумента по умолчанию
#         try:
#             drawingTemplate.current_figure.R2 = int(text)
#         except:
#             print('Some kind of shit r2')
#
#     inputBoxDict['R2_inpBox'] = inputBox(interfceSurfce, (3 * button_size[0] + 3 * 5, button_size[1] * (1)),
#                                               button_size, colors, text='R2', font=font,
#                                               onChangeAction=lambda text: R2_buff(text))
#
#     def diametr_buff(text):  # передача i в качестве аргумента по умолчанию
#         try:
#             drawingTemplate.current_figure.diametr = int(text)
#         except:
#             print('Some kind of shit diametr')
#
#     inputBoxDict['diametr_inpBox'] = inputBox(interfceSurfce,
#                                                    (3 * button_size[0] + 3 * 5, button_size[1] * (2)), button_size,
#                                                    colors, text='diametr', font=font,
#                                                    onChangeAction=lambda text: diametr_buff(text))
#
#     def width_buff(text):  # передача i в качестве аргумента по умолчанию
#         try:
#             drawingTemplate.current_figure.width = int(text)
#         except:
#             print('Some kind of shit width')
#
#     inputBoxDict['width_inpBox'] = inputBox(interfceSurfce,
#                                                  (3 * button_size[0] + 3 * 5, button_size[1] * (3)), button_size,
#                                                  colors, text='width', font=font,
#                                                  onChangeAction=lambda text: width_buff(text))
#
#     return inputBoxDict, buttonDict




