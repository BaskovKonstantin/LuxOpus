import pygame
from GUI.button import button
from GUI.inputBox import inputBox

class userInterface:


    def redraw(self):
        self.interfceSurfce.fill(self.colors['background'])



        for key in self.inputBoxDict.keys():
                self.inputBoxDict[key].redraw()
        for key in self.buttonDict.keys():

                self.buttonDict[key].redraw()

        self.mainRect = pygame.Rect(0, 0, self.size[0], self.size[1])
        pygame.draw.rect(self.interfceSurfce, self.colors['border'], self.mainRect, self.border_size)

        self.screen.blit(self.interfceSurfce, (self.posX, self.posY))

    def initDraw(self):
        self.mainRect = pygame.Rect(0,0,self.size[0], self.size[1])

        pygame.draw.rect(self.interfceSurfce, self.colors['border'],self.mainRect ,self.border_size)

    def checkBtn(self, mouseX, mouseY):
        print(self.buttonDict.keys())
        for key in self.buttonDict.keys():

            if (mouseX > (self.posX + self.buttonDict[key].pos[0]) and mouseX < (self.posX + self.buttonDict[key].pos[0] + self.buttonDict[key].size[0])
                    and (mouseY > (self.posY + self.buttonDict[key].pos[1]) and mouseY < (self.posY + self.buttonDict[key].pos[1] + self.buttonDict[key].size[1]))):
                print(key)
                self.buttonDict[key].click()

        for key in self.inputBoxDict.keys():
            if (mouseX > (self.posX + self.inputBoxDict[key].pos[0]) and mouseX < (self.posX + self.inputBoxDict[key].pos[0] + self.inputBoxDict[key].size[0])
                    and (mouseY > (self.posY + self.inputBoxDict[key].pos[1]) and mouseY < (self.posY + self.inputBoxDict[key].pos[1] + self.inputBoxDict[key].size[1]))):
                print(key)
                self.inputBoxDict[key].active = True
                self.inputBoxDict[key].clear()
                self.seletedInputBox = self.inputBoxDict[key]
            else:
                self.inputBoxDict[key].active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Получение координат клика
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.checkBtn(mouse_x, mouse_y)
            # print(self.seletedInputBox)
            # print(self.seletedInputBox.text)
            return self.seletedInputBox
        return None


    def initButton(self):

        self.buttonDict = dict()

        button_size = (80,40)

        for i in range(1, 11):
            def buff(i=i):  # передача i в качестве аргумента по умолчанию
                self.drawingTemplate.current_figure.type = int(i)
                print(i)

            self.buttonDict[f'set type {i}'] = button(self.interfceSurfce, (0, button_size[1] * (i - 1) ), button_size,
                                                      self.colors, lambda i=i: buff(i), f'type {i}', self.font, border_size = self.border_size)

        for i in range(0, 3):
            def lf_buff(i=i):  # передача i в качестве аргумента по умолчанию
                self.drawingTemplate.current_figure.left_facet_type = int(i)
                print(i)

            self.buttonDict[f'set left facet type {i}'] = button(self.interfceSurfce, (button_size[0] + 5, button_size[1] * (i)), button_size,
                                                      self.colors, lambda i=i: lf_buff(i), f'left_facet_type {i}', self.font, font_size=9,
                                                      border_size=self.border_size)
        for i in range(0, 3):
            def rf_buff(i=i):  # передача i в качестве аргумента по умолчанию
                self.drawingTemplate.current_figure.right_facet_type = int(i)
                print(i)

            self.buttonDict[f'set right facet type {i}'] = button(self.interfceSurfce, (2*button_size[0] + 2*5, button_size[1] * (i)), button_size,
                                                      self.colors, lambda i=i: rf_buff(i), f'right_facet_type {i}', self.font, font_size=9,
                                                      border_size=self.border_size)

        def add_lens():  # передача i в качестве аргумента по умолчанию
            self.drawingTemplate.add_lens()
            print(i)



        self.buttonDict[f'add_lens'] = button(self.interfceSurfce, (170, 200), button_size,
                                                  self.colors, lambda : add_lens(), 'add lens', self.font,
                                                  border_size=self.border_size)



        self.inputBoxDict = dict()


        def lfs_buff(text):  # передача i в качестве аргумента по умолчанию
            try:
                self.drawingTemplate.current_figure.left_facet_size = int(text)
            except:
                print('Some kind of shit lfc')


        self.inputBoxDict['left_facet_type_inpBox'] = inputBox(self.interfceSurfce, (button_size[0] + 5, button_size[1] * (3)), button_size, self.colors, text='30', font = self.font,
                                                               onChangeAction = lambda text: lfs_buff(text))
        def rfs_buff(text):  # передача i в качестве аргумента по умолчанию
            try:
                self.drawingTemplate.current_figure.right_facet_size = int(text)
            except:
                print('Some kind of shit rfc' )

        self.inputBoxDict['right_facet_type_inpBox'] = inputBox(self.interfceSurfce, (2*button_size[0] + 2*5, button_size[1] * (3)), button_size, self.colors, text='30', font = self.font,
                                                                onChangeAction = lambda text: rfs_buff(text))

        def R1_buff(text):  # передача i в качестве аргумента по умолчанию
            try:
                self.drawingTemplate.current_figure.R1 = int(text)
            except:
                print('Some kind of shit r1')

        self.inputBoxDict['R1_inpBox'] = inputBox(self.interfceSurfce, (3*button_size[0] + 3*5, button_size[1] * (0)), button_size, self.colors, text='R1', font = self.font,
                                                                onChangeAction = lambda text: R1_buff(text))
        def R2_buff(text):  # передача i в качестве аргумента по умолчанию
            try:
                self.drawingTemplate.current_figure.R2 = int(text)
            except:
                print('Some kind of shit r2')

        self.inputBoxDict['R2_inpBox'] = inputBox(self.interfceSurfce, (3*button_size[0] + 3*5, button_size[1] * (1)), button_size, self.colors, text='R2', font = self.font,
                                                                onChangeAction = lambda text: R2_buff(text))

        def diametr_buff(text):  # передача i в качестве аргумента по умолчанию
            try:
                self.drawingTemplate.current_figure.diametr = int(text)
            except:
                print('Some kind of shit diametr')

        self.inputBoxDict['diametr_inpBox'] = inputBox(self.interfceSurfce, (3*button_size[0] + 3*5, button_size[1] * (2)), button_size, self.colors, text='diametr', font = self.font,
                                                                onChangeAction = lambda text: diametr_buff(text))
        def width_buff(text):  # передача i в качестве аргумента по умолчанию
            try:
                self.drawingTemplate.current_figure.width = int(text)
            except:
                print('Some kind of shit width')

        self.inputBoxDict['width_inpBox'] = inputBox(self.interfceSurfce, (3*button_size[0] + 3*5, button_size[1] * (3)), button_size, self.colors, text='width', font = self.font,
                                                                onChangeAction = lambda text: width_buff(text))






    def __init__(self, drawingTemplate, screen, posX, posY, width, heidth, colors, border_size, font = None):
        self.drawingTemplate = drawingTemplate
        self.posX = posX
        self.posY = posY


        self.screen = screen
        self.colors = colors
        self.border_size = border_size

        self.size = (width, heidth)
        self.font = font
        self.interfceSurfce = pygame.Surface(self.size, pygame.SRCALPHA)

        self.initDraw()
        self.initButton()

        self.redraw()
        self.seletedInputBox = None








