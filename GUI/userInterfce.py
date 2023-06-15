import pygame
import math
from GUI.button import button
from GUI.inputBox import inputBox

class controlPanel:

    def draw(self):
        self.surface.fill(self.colors['background'])
        for key in self.inputBoxDict.keys():
            if key not in self.DisabledInputBox:
                self.inputBoxDict[key].draw()

        for key in self.dropDownDict.keys():
            if key not in self.DisabledButtons:
                self.dropDownDict[key].draw()

        for key in self.buttonDict.keys():
            self.buttonDict[key].draw()
        for key in self.imageSurfaceDict.keys():
            self.surface.blit(self.imageSurfaceDict[key][0], self.imageSurfaceDict[key][1])

        self.mainRect = pygame.Rect(0, 0, self.size[0], self.size[1])
        pygame.draw.rect(self.surface, self.colors['border'], self.mainRect, self.border_size)

        self.screen.blit(self.surface, (self.posX, self.posY))

    def initDraw(self):
        self.mainRect = pygame.Rect(0,0,self.size[0], self.size[1])

        pygame.draw.rect(self.surface, self.colors['border'],self.mainRect ,self.border_size)
    def checkBtn(self, event, mouseX, mouseY):

        for key in self.dropDownDict.keys():
            # if (mouseX > (self.posX + self.buttonDict[key].pos[0]) and mouseX < (
            #         self.posX + self.buttonDict[key].pos[0] + self.buttonDict[key].size[0])
            #         and (mouseY > (self.posY + self.buttonDict[key].pos[1]) and mouseY < (
            #                 self.posY + self.buttonDict[key].pos[1] + self.buttonDict[key].size[1]))):
                self.dropDownDict[key].handle_event(event, mouseX-self.posX, mouseY-self.posY)


        for key in self.buttonDict.keys():
            if (mouseX > (self.posX + self.buttonDict[key].pos[0]) and mouseX < (
                    self.posX + self.buttonDict[key].pos[0] + self.buttonDict[key].size[0])
                    and (mouseY > (self.posY + self.buttonDict[key].pos[1]) and mouseY < (
                            self.posY + self.buttonDict[key].pos[1] + self.buttonDict[key].size[1]))):
                self.buttonDict[key].click()

        for key in self.inputBoxDict.keys():
            if (mouseX > (self.posX + self.inputBoxDict[key].pos[0]) and mouseX < (
                    self.posX + self.inputBoxDict[key].pos[0] + self.inputBoxDict[key].size[0])
                    and (mouseY > (self.posY + self.inputBoxDict[key].pos[1]) and mouseY < (
                            self.posY + self.inputBoxDict[key].pos[1] + self.inputBoxDict[key].size[1]))):
                self.inputBoxDict[key].active = True
                self.inputBoxDict[key].clear()
                self.seletedInputBox = self.inputBoxDict[key]
            else:
                self.inputBoxDict[key].active = False
    def handle_event(self, event, offsetX = 0, offsetY = 0):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Получение координат клика
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.checkBtn(event ,mouse_x - offsetX, mouse_y - offsetY)
            if self.seletedInputBox:
                ...
            return self.seletedInputBox
        return None


    def __init__(self,
                 drawingTemplate, screen,
                 posX, posY,
                 width, heidth, colors,
                 border_size, font = None,
                 buttonDict = {},
                 inputBoxDict = {},
                 imageSurfaceDict = {},
                 dropDownDict = {}):
        self.drawingTemplate = drawingTemplate
        self.posX = posX
        self.posY = posY

        self.buttonDict = buttonDict
        self.inputBoxDict = inputBoxDict
        self.dropDownDict = dropDownDict
        self.imageSurfaceDict = imageSurfaceDict

        self.screen = screen
        self.colors = colors
        self.border_size = border_size

        self.size = (width, heidth)
        self.font = font
        self.surface = pygame.Surface(self.size, pygame.SRCALPHA)

        self.initDraw()

        # self.draw()
        self.seletedInputBox = None
        self.DisabledInputBox = []
        self.DisabledButtons = []


class controlPanelGroup:

    def __init__(self, screen, colors, blitPoint, size, controlPanelsDict = {}, imageSurfaceDict = {}, is_visible = True):
        self.screen = screen
        self.colors = colors
        self.controlPanelsDict = controlPanelsDict
        self.imageSurfaceDict = imageSurfaceDict
        self.blitPoint = blitPoint
        self.size = size
        self.is_visible = is_visible

        self.surface = pygame.Surface(self.size, pygame.SRCALPHA)
        self.surface.fill(self.colors['background'])

    def handle_event(self, event):

        for key in self.controlPanelsDict.keys():

            inpBox = self.controlPanelsDict[key].handle_event(event,
                                                     offsetX=self.blitPoint[0],
                                                     offsetY=self.blitPoint[1])

            if inpBox:

                return inpBox


    def draw(self):
        if (self.is_visible):
            pygame.draw.rect(self.surface, self.colors['border'], (0, 0,
                                                             self.size[0], self.size[1]), 3)
            for key in self.controlPanelsDict.keys():
                self.controlPanelsDict[key].draw()
            for key in self.imageSurfaceDict.keys():
                self.surface.blit(self.imageSurfaceDict[key][0], self.imageSurfaceDict[key][1])


            self.screen.blit(self.surface, self.blitPoint)








