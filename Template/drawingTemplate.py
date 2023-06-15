import pygame
import json
import qrcode
from datetime import date
from Template.cellTemplate import cell
from figure.lens import lens
from GUI.signature import signature
from GUI.image import image
from figure.roughness_measure import roughness_measure


class drawingTemplate:

    def init_draw_cell(self):

        self.mainRect = pygame.Rect(self.reference_point[0],
                                    self.reference_point[1],
                           self.list_size[0]*self.scale,
                           self.list_size[1]*self.scale)
        pygame.draw.rect(self.surface, self.colors['border'], self.mainRect, self.border_size)

        self.cell_dict['document_designation down'] = cell(
            name='document_designation down',
            screen = self.surface,
            colors = self.colors,
            size= (15 + self.border_size/self.scale,120),
            start_point= (
                    self.reference_point[0] + self.list_size[0]*self.scale  - 120 * self.scale ,
                    self.reference_point[1] + self.list_size[1]*self.scale - 55 * self.scale - self.border_size
            ),
            scale = self.scale,
            margin = self.margin,
            border_size= self.border_size,
            text=self.document_designation_text,
            font = self.font,
            font_size= int( self.scale*10))

        self.cell_dict['document_designation up'] = cell(
            name='document_designation up',
            screen = self.surface,
            colors = self.colors,
            size= (14+self.border_size/self.scale ,120),
            start_point= (self.reference_point[0],self.reference_point[1]),
            scale = self.scale,
            margin = self.margin,
            border_size=self.border_size,
            text=self.document_designation_text,
            font = self.font,
            font_size= int( self.scale*10),
            text_rotate = 180)

        self.cell_dict['name'] = cell(
            name='name',
            screen=self.surface,
            colors=self.colors,
            size=(25 + self.border_size / self.scale, 70),
            start_point=(
                self.reference_point[0] + self.list_size[0]*self.scale - 120 * self.scale ,
                self.reference_point[1] + self.list_size[1]*self.scale - 40 * self.scale - self.border_size
            ),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text=self.text_name,
            font=self.font,
            font_size= int( self.scale*12))

        self.cell_dict['material'] = cell(
            name='material',
            screen = self.surface,
            colors = self.colors,
            size= (15 + self.border_size/self.scale,70),
            start_point= (
                    self.reference_point[0] + self.list_size[0]*self.scale- 120* self.scale ,
                    self.reference_point[1] + self.list_size[1]*self.scale- 15 * self.scale - self.border_size
            ),
            scale = self.scale,
            margin = self.margin,
            border_size=self.border_size,
            text=self.material_text,
            font = self.font,
            font_size= int( self.scale* 6) )

        self.cell_dict['author'] = cell(
            name='author',
            screen = self.surface,
            colors = self.colors,
            size= (15 + self.border_size/self.scale ,50+ self.border_size/self.scale),
            start_point= (
                    self.reference_point[0] + self.list_size[0]*self.scale- 50* self.scale - self.border_size ,
                    self.reference_point[1] + self.list_size[1]*self.scale- 15 * self.scale - self.border_size
            ),
            scale = self.scale,
            margin = self.margin,
            border_size=self.border_size,
            text=self.author_text,
            font = self.font,
            font_size= int( self.scale* 12) )

        self.cell_dict['list number'] = cell(
            name='list number',
            screen = self.surface,
            colors = self.colors,
            size= (5 ,20 + 2*self.border_size/self.scale),
            start_point= (
                    self.reference_point[0] + self.list_size[0]*self.scale- 50* self.scale - self.border_size ,
                    self.reference_point[1] + self.list_size[1]*self.scale- 20 * self.scale
            ),
            scale = self.scale,
            margin = self.margin,
            border_size=self.border_size,
            text='Лист ' + self.list_number_text,
            font = self.font,
            font_size= int( self.scale* 5) )

        self.cell_dict['list count'] = cell(
            name='list count',
            screen=self.surface,
            colors=self.colors,
            size=(5 , 30),
            start_point=(
                self.reference_point[0] + self.list_size[0]*self.scale- 30 * self.scale ,
                self.reference_point[1] + self.list_size[1]*self.scale- 20 * self.scale
            ),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text='Листов ' + self.list_count_text,
            font = self.font,
            font_size= int( self.scale* 4) )


        self.cell_dict['Literature title'] = cell(
            name='Literature title',
            screen=self.surface,
            colors=self.colors,
            size=(5, 15 + self.border_size/self.scale),
            start_point=(
                self.reference_point[0] + self.list_size[0]*self.scale- 50 * self.scale - self.border_size ,
                self.reference_point[1] + self.list_size[1]*self.scale- 40 * self.scale - self.border_size
            ),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text='Лит.',
            font = self.font,
            font_size= int( self.scale*4))

        for i in range(1,4):

            self.cell_dict['Literature' + str(i)] = cell(
            name='Literature' + str(i),
                screen=self.surface,
                colors=self.colors,
                size=(15 + 3*self.border_size/self.scale, 5+ self.border_size/self.scale),
                start_point=(
                    self.reference_point[0] + self.list_size[0]*self.scale - (50 - (i-1)*5)  * self.scale - self.border_size ,
                    self.reference_point[1] + self.list_size[1]*self.scale - 35 * self.scale - 2*self.border_size
                ),
                scale=self.scale,
                margin=self.margin,
                border_size=self.border_size,
                text=self.lit_list[i-1],
                font = self.font,
                font_size= int( self.scale*4))

        self.cell_dict['mass title'] = cell(
            name='mass title',
            screen=self.surface,
            colors=self.colors,
            size=(5, 17 + self.border_size / self.scale),
            start_point=(
                self.reference_point[0] + self.list_size[0]*self.scale - 35 * self.scale - self.border_size ,
                self.reference_point[1] + self.list_size[1]*self.scale - 40 * self.scale - self.border_size
            ),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text='масса',
            font=self.font,
            font_size= int( self.scale*4))

        self.cell_dict['mass'] = cell(
            name='mass',
            screen=self.surface,
            colors=self.colors,
            size=(15 + 3 * self.border_size / self.scale, 17 + self.border_size / self.scale),
            start_point=(
                self.reference_point[0] + self.list_size[0]*self.scale - 35 * self.scale - self.border_size ,
                self.reference_point[1] + self.list_size[1]*self.scale - 35 * self.scale - 2 * self.border_size
            ),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text=self.mass_text,
            font=self.font,
            font_size= int( self.scale*4))
        self.cell_dict['scale title'] = cell(
            name='scale title',
            screen=self.surface,
            colors=self.colors,
            size=(5, 18 + self.border_size/self.scale),
            start_point=(
                self.reference_point[0] + self.list_size[0]*self.scale - 18 * self.scale - self.border_size ,
                self.reference_point[1] + self.list_size[1]*self.scale - 40 * self.scale - self.border_size
            ),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text='Масштаб.',
            font = self.font,
            font_size= int( self.scale*4))
        self.cell_dict['scale'] = cell(
            name='scale',
            screen=self.surface,
            colors=self.colors,
            size=(15 + 3*self.border_size/self.scale , 18 + self.border_size/self.scale),
            start_point=(
                self.reference_point[0] + self.list_size[0]*self.scale- 18 * self.scale - self.border_size ,
                self.reference_point[1] + self.list_size[1]*self.scale - 35 * self.scale - 2*self.border_size
            ),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text=self.scale_text,
            font = self.font,
            font_size= int(self.scale*8))
        for i in range(0,11):
            cur_text = self.date_text[i]

            self.cell_dict['date' + str(i)] = cell(
            name='date' + str(i),
                screen=self.surface,
                colors=self.colors,
                size=(5 + self.border_size/self.scale, 15 + self.border_size/self.scale),
                start_point=(
                    self.reference_point[0] + self.list_size[0]*self.scale  - 135 * self.scale ,
                    self.reference_point[1] + self.list_size[1]*self.scale- (55 - 5*(i)) * self.scale - self.border_size
                ),
                scale=self.scale,
                margin=self.margin,
                border_size=self.border_size,
                text=cur_text,
                font = self.font,
                font_size= int( self.scale*4))
        for i in range(0,11):
            cur_text = self.podl_text[i]

            self.cell_dict['podl' + str(i)] = cell(
            name='podl' + str(i),
                screen=self.surface,
                colors=self.colors,
                size=(5 + self.border_size/self.scale, 20 + self.border_size/self.scale),
                start_point=(
                    self.reference_point[0] + self.list_size[0]*self.scale  - 155 * self.scale ,
                    self.reference_point[1] + self.list_size[1]*self.scale- (55 - 5*(i)) * self.scale - self.border_size
                ),
                scale=self.scale,
                margin=self.margin,
                border_size=self.border_size,
                text=cur_text,
                font = self.font,
                font_size= int( self.scale*4))

        for i in range(0,11):
            cur_text = self.N_doc_text[i]

            self.cell_dict['N doc' + str(i)] = cell(
            name='N doc' + str(i),
                screen=self.surface,
                colors=self.colors,
                size=(5 + self.border_size/self.scale, 29 + self.border_size/self.scale),
                start_point=(self.reference_point[0] + self.list_size[0]*self.scale  - 184 * self.scale ,
                    self.reference_point[1] + self.list_size[1]*self.scale- (55 - 5*(i)) * self.scale - self.border_size),
                scale=self.scale,
                margin=self.margin,
                border_size=self.border_size,
                text=cur_text,
                font = self.font,
                font_size= int( self.scale*4))

        for i in range(0,5):
            cur_text = self.change_text[i]

            self.cell_dict['Change' + str(i)] = cell(
            name='Change' + str(i),
                screen=self.surface,
                colors=self.colors,
                size=(5 + self.border_size/self.scale, 13 + self.border_size/self.scale),
                start_point=(
                    self.reference_point[0] + self.list_size[0]*self.scale  - 197 * self.scale ,
                    self.reference_point[1] + self.list_size[1]*self.scale- (55 - 5*(i)) * self.scale - self.border_size
                ),
                scale=self.scale,
                margin=self.margin,
                border_size=self.border_size,
                text=cur_text,
                font = self.font,
                font_size= int( self.scale*4))

        for i in range(0,5):
            cur_text = self.list_text[i]

            self.cell_dict['List' + str(i)] = cell(
            name='List' + str(i),
                screen=self.surface,
                colors=self.colors,
                size=(5 + self.border_size/self.scale, 13 + self.border_size/self.scale),
                start_point=(
                    self.reference_point[0] + self.list_size[0]*self.scale  - 210 * self.scale ,
                    self.reference_point[1] + self.list_size[1]*self.scale- (55 - 5*(i)) * self.scale - self.border_size
                ),
                scale=self.scale,
                margin=self.margin,
                border_size=self.border_size,
                text=cur_text,
                font = self.font,
                font_size= int( self.scale*4))

        #Titles
        for i in range(5,11):
            cur_text = ' '
            if (i == 5):
                cur_text = 'Разраб'
            if (i == 6):
                cur_text = 'Пров'
            if (i == 7):
                cur_text = 'Т.контр'
            if (i == 9):
                cur_text = 'Н.контр'
            if (i == 10):
                cur_text = 'Утв'

            self.cell_dict['info' + str(i)] = cell(
            name='info' + str(i),
                screen=self.surface,
                colors=self.colors,
                size=(5 + self.border_size/self.scale, 26 + self.border_size/self.scale),
                start_point=(
                    self.reference_point[0] + self.list_size[0]*self.scale  - 210 * self.scale ,
                    self.reference_point[1] + self.list_size[1]*self.scale - (55 - 5*(i)) * self.scale - self.border_size
                ),
                scale=self.scale,
                margin=self.margin,
                border_size=self.border_size,
                text=cur_text,
                font = self.font,
                font_size= int( self.scale*4))
        # ГОСТ Клетки из шаблона главно страницыг

        # for i in range(0,5):
        #     cur_text = self.Zona_text[i]
        #
        #     self.cell_dict['Zona' + str(i)] = cell(
        #     name='Zona' + str(i),
        #         screen=self.screen,
        #         colors=self.colors,
        #         size=(5 + self.border_size/self.scale, 25 + self.border_size/self.scale),
        #         start_point=(
        #             self.x - self.margin / 2 - self.margin_right - 210 * self.scale ,
        #             self.y - self.margin / 2 - (55 - 5*(i)) * self.scale - self.border_size
        #         ),
        #         scale=self.scale,
        #         margin=self.margin,
        #         border_size=self.border_size,
        #         text=cur_text,
        #         font = self.font,
        #         font_size= int( self.scale*4))

        # self.cell_dict['inv N podl title'] = cell(
        #     name='inv N podl title',
        #     screen=self.screen,
        #     colors=self.colors,
        #     size=(25 + self.border_size/self.scale, 5 + self.border_size/self.scale),
        #     start_point=(
        #         self.margin / 2  - 12*self.scale + self.margin_left,
        #         self.y - self.margin / 2 - 25*self.scale - 2*self.border_size / self.scale),
        #     scale=self.scale,
        #     margin=self.margin,
        #     border_size=self.border_size,
        #     text='Инв N подл',
        #     font = self.font,
        #     font_size= int( self.scale*4),
        #     text_rotate = 90)
        #
        # self.cell_dict['inv N podl'] = cell(
        #     name='inv N podl',
        #     screen=self.screen,
        #     colors=self.colors,
        #     size=(25 + self.border_size/self.scale, 7 + self.border_size/self.scale),
        #     start_point=(
        #         self.margin / 2 - 7*self.scale + self.margin_left,
        #         self.y - self.margin / 2 - 25*self.scale - 2*self.border_size / self.scale),
        #     scale=self.scale,
        #     margin=self.margin,
        #     border_size=self.border_size,
        #     text=self.inv_N_podl_text,
        #     font = self.font,
        #     font_size= int( self.scale*4),
        #     text_rotate=90)
        #
        # self.cell_dict['Podl and date title'] = cell(
        #     name='Podl and date title',
        #     screen=self.screen,
        #     colors=self.colors,
        #     size=(35 + self.border_size / self.scale, 5 + self.border_size / self.scale),
        #     start_point=(
        #         self.margin / 2 - 12 * self.scale + self.margin_left,
        #         self.y - self.margin / 2 - 60 * self.scale - 2*self.border_size / self.scale),
        #     scale=self.scale,
        #     margin=self.margin,
        #     border_size=self.border_size,
        #     text='Подл и дата',
        #     font = self.font,
        #     font_size= int( self.scale*4),
        #     text_rotate=90)
        #
        # self.cell_dict['Podl and date'] = cell(
        #     name='Podl and date',
        #     screen=self.screen,
        #     colors=self.colors,
        #     size=(35 + self.border_size / self.scale, 7 + self.border_size / self.scale),
        #     start_point=(
        #         self.margin / 2 - 7 * self.scale + self.margin_left,
        #         self.y - self.margin / 2 - 60 * self.scale - 2*self.border_size / self.scale),
        #     scale=self.scale,
        #     margin=self.margin,
        #     border_size=self.border_size,
        #     text=self.Podl_and_date_text,
        #     font = self.font,
        #     font_size= int( self.scale*4),
        #     text_rotate=90)
        #
        # self.cell_dict['Vzam inv title'] = cell(
        #     name='Vzam inv title',
        #     screen=self.screen,
        #     colors=self.colors,
        #     size=(25, 5 + self.border_size / self.scale),
        #     start_point=(
        #         self.margin / 2 - 12 * self.scale + self.margin_left,
        #         self.y - self.margin / 2 - 85 * self.scale ),
        #     scale=self.scale,
        #     margin=self.margin,
        #     border_size=self.border_size,
        #     text='Взам инв',
        #     font = self.font,
        #     font_size= int( self.scale*4),
        #     text_rotate=90)
        #
        # self.cell_dict['Vzam inv'] = cell(
        #     name='Vzam inv',
        #     screen=self.screen,
        #     colors=self.colors,
        #     size=(25, 7 + self.border_size / self.scale),
        #     start_point=(
        #         self.margin / 2 - 7 * self.scale + self.margin_left,
        #         self.y - self.margin / 2 - 85 * self.scale),
        #     scale=self.scale,
        #     margin=self.margin,
        #     border_size=self.border_size,
        #     text=self.Vzam_inv_text,
        #     font = self.font,
        #     font_size= int( self.scale*4),
        #     text_rotate=90)
        #
        # self.cell_dict['inv dubble title'] = cell(
        #     name='inv dubble title',
        #     screen=self.screen,
        #     colors=self.colors,
        #     size=(25 + self.border_size / self.scale, 5 + self.border_size / self.scale),
        #     start_point=(
        #         self.margin / 2 - 12 * self.scale + self.margin_left,
        #         self.y - self.margin / 2 - 110 * self.scale ),
        #     scale=self.scale,
        #     margin=self.margin,
        #     border_size=self.border_size,
        #     text='Инв N дубл',
        #     font = self.font,
        #     font_size= int( self.scale*4),
        #     text_rotate=90)
        #
        # self.cell_dict['inv dubble podl'] = cell(
        #     name='inv dubble podl',
        #     screen=self.screen,
        #     colors=self.colors,
        #     size=(25 + self.border_size / self.scale, 7 + self.border_size / self.scale),
        #     start_point=(
        #         self.margin / 2 - 7 * self.scale + self.margin_left,
        #         self.y - self.margin / 2 - 110 * self.scale),
        #     scale=self.scale,
        #     margin=self.margin,
        #     border_size=self.border_size,
        #     text=self.inv_dubble_text,
        #     font = self.font,
        #     font_size= int( self.scale*4),
        #     text_rotate=90)
        #
        # self.cell_dict['podl and date 2 title'] = cell(
        #     name='podl and date 2 title',
        #     screen=self.screen,
        #     colors=self.colors,
        #     size=(35 + self.border_size / self.scale, 5 + self.border_size / self.scale),
        #     start_point=(
        #         self.margin / 2 - 12 * self.scale + self.margin_left,
        #         self.y - self.margin / 2 - 145 * self.scale ),
        #     scale=self.scale,
        #     margin=self.margin,
        #     border_size=self.border_size,
        #     text='Подл и дата',
        #     font = self.font,
        #     font_size= int( self.scale*4),
        #     text_rotate=90)
        #
        # self.cell_dict['podl and date 2'] = cell(
        #     name='podl and date 2',
        #     screen=self.screen,
        #     colors=self.colors,
        #     size=(35 + self.border_size / self.scale, 7 + self.border_size / self.scale),
        #     start_point=(
        #         self.margin / 2 - 7 * self.scale + self.margin_left,
        #         self.y - self.margin / 2 - 145 * self.scale),
        #     scale=self.scale,
        #     margin=self.margin,
        #     border_size=self.border_size,
        #     text=self.podl_and_date_2,
        #     font = self.font,
        #     font_size= int( self.scale*4),
        #     text_rotate=90)
        #
        # self.cell_dict['First use title'] = cell(
        #     name='First use title',
        #     screen=self.screen,
        #     colors=self.colors,
        #     size=(60 + self.border_size / self.scale, 5 + self.border_size / self.scale),
        #     start_point=(
        #         self.margin / 2 - 12 * self.scale + self.margin_left,
        #         self.margin / 2 ),
        #     scale=self.scale,
        #     margin=self.margin,
        #     border_size=self.border_size,
        #     text='Перв прим',
        #     font = self.font,
        #     font_size= int( self.scale*4),
        #     text_rotate=90)
        #
        # self.cell_dict['First use'] = cell(
        #     name='First use',
        #     screen= self.screen,
        #     colors= self.colors,
        #     size=(60 + self.border_size / self.scale, 7 + self.border_size / self.scale),
        #     start_point=(
        #         self.margin / 2 - 7 * self.scale + self.margin_left,
        #         self.margin / 2 ),
        #     scale=self.scale,
        #     margin=self.margin,
        #     border_size=self.border_size,
        #     text=self.First_use_text,
        #     font = self.font,
        #     font_size= int(self.scale*4),
        #     text_rotate=90)
        #
        # self.cell_dict['Help N title'] = \
        #     cell(
        #     name='Help N title',
        #     screen=self.screen,
        #     colors=self.colors,
        #     size=(60 + self.border_size / self.scale, 5 + self.border_size / self.scale),
        #     start_point=(
        #         self.margin / 2 - 12 * self.scale + self.margin_left,
        #         self.margin / 2 + 60 * self.scale),
        #     scale=self.scale,
        #     margin=self.margin,
        #     border_size=self.border_size,
        #     text='Справ N',
        #     font = self.font,
        #     font_size= int( self.scale*4),
        #     text_rotate=90)
        #
        # self.cell_dict['Help N'] = cell(
        #     name='Help N',
        #     screen=self.screen,
        #     colors=self.colors,
        #     size=(60 + self.border_size / self.scale, 7 + self.border_size / self.scale),
        #     start_point=(
        #         self.margin / 2 - 7 * self.scale + self.margin_left,
        #         self.margin / 2 + 60 * self.scale),
        #     scale=self.scale,
        #     margin=self.margin,
        #     border_size=self.border_size,
        #     text=self.Help_N_text,
        #     font = self.font,
        #     font_size= int( self.scale*4),
        #     text_rotate=90)
    def set_base_text(self):

        # Открываем файл с данными
        with open(self.save_file, encoding='utf-8') as f:
            # Читаем данные из файла
            data = json.load(f)
        # Обозначение документа
        self.document_designation_text = data['document_designation']
        # Наименование изделия
        self.text_name = data['name']
        # Материал
        self.material_text = data['material']
        # Автор
        self.author_text = data['author']
        # Номер листа
        self.list_number_text = 'N'
        # Количество листов
        self.list_count_text = 'N'
        # Литера
        self.lit_list = ['', '', '']
        # Масса
        self.mass_text = ''
        # Масштаб
        self.scale_text = self.scale_text_list[self.current_scale]
        # Дата
        self.date_text = [''] * 4
        self.date_text.append('Дата')
        self.date_text.extend([str(date.today().strftime("%d.%m.%Y"))] * 6)
        self.date_text[4] = 'Дата'
        # Подл
        self.podl_text = [''] * 11
        self.podl_text[4] = 'Подл'
        # Номер документа
        self.N_doc_text = [''] * 11
        self.N_doc_text[4] = 'N докум.'
        self.N_doc_text[5] = data['Developer']

        # Лист
        self.list_text = [''] * 5
        self.list_text[4] = 'Лист'

        # Изменения
        self.change_text = [''] * 5
        self.change_text[4] = 'Изм'

        # Зона
        self.Zona_text = [''] * 5
        self.Zona_text[4] = 'Изм'

        # inv N podl
        self.inv_N_podl_text = ''

        # Podl and date
        self.Podl_and_date_text = ''

        # Vzam inv
        self.Vzam_inv_text = ''
        # inv dubble
        self.inv_dubble_text = ''
        # podl and date 2
        self.podl_and_date_2 = ''
        # First use
        self.First_use_text = ''
        # Help N
        self.Help_N_text = ''
    def check_curren_cell(self, x, y):
        current_cell = 'None'
        for cellName in self.cell_dict.keys():

            if (self.cell_dict[cellName].check_coord(x,y)):


                self.cell_dict[cellName].set_selected_border_color()
                current_cell = cellName

            else:
                self.cell_dict[cellName].set_base_border_color()
        return current_cell
    def set_selected_cell(self, name):
        if name in self.cell_dict.keys():
            self.selected_cell = self.cell_dict[name]
        else:
            self.selected_cell = None
            print('Not Valid cell name')
    def draw_param_table(self):
        param_height = 7
        param_wight = 15
        param_wight_title = 30

        param_list = ['Δn_D',
                      'Δ(n_F - n_C)',
                      'Однородн',
                      'Дв.лучепр',
                      'Светопогл',
                      'Бессвильн',
                      'Пузырность',
                      'N_A',
                      'ΔN',
                      'c',
                      'P',
                      'ΔR',
                      'p',
                      'S\'_F\'',
                      'св.',
                      ]
        common_roughness_size = (30*self.scale,30*self.scale)
        self.figure_dict['common_roughness'] = \
            roughness_measure(self.surface, self.colors,
            (self.reference_point[0] + self.list_size[0]*self.scale - common_roughness_size[0] - self.border_size*2,
            self.reference_point[1] + common_roughness_size[1] - common_roughness_size[1]*1.5), size = common_roughness_size,
            font=self.font, text_designation = 'R20()')

        for i in range(0,12):
            self.cell_dict['param ' + str(i)] = cell(
                name='param ' + str(i),
                screen=self.surface,
                colors=self.colors,
                size=(param_height + self.border_size / self.scale,param_wight  ),
                start_point=(
                    self.reference_point[0] + self.list_size[0]*self.scale - param_wight  * self.scale,
                    self.reference_point[1] + 8*self.scale * self.scale - self.border_size + (param_height*self.scale + self.border_size)*i
                ),
                scale=self.scale,
                margin=self.margin,
                border_size=self.border_size,
                text='',
                font=self.font,
                font_size= int( self.scale*5))

            self.cell_dict['param title ' + str(i)] = cell(
                name='param title ' + str(i),
                screen=self.surface,
                colors=self.colors,
                size=( param_height + self.border_size / self.scale, param_wight_title),
                start_point=(
                    self.reference_point[0] + self.list_size[0]*self.scale - param_wight_title  * self.scale - param_wight*self.scale + self.border_size ,
                    self.reference_point[1] +8*self.scale * self.scale - self.border_size + (param_height*self.scale + self.border_size)*i
                ),
                scale=self.scale,
                margin=self.margin,
                border_size=self.border_size,
                text=param_list[i],
                font=self.font,
                font_size= int( self.scale*5))
            for i in range(12, 15):
                self.cell_dict['param ' + str(i)] = cell(
                    name='param ' + str(i),
                    screen=self.surface,
                    colors=self.colors,
                    size=(param_height + self.border_size / self.scale, param_wight_title),
                    start_point=(
                        self.reference_point[0] + self.list_size[0]*self.scale - param_wight_title * self.scale,
                        self.reference_point[1] + 8*self.scale * self.scale - self.border_size + (param_height *self.scale + self.border_size) * i
                    ),
                    scale=self.scale,
                    margin=self.margin,
                    border_size=self.border_size,
                    text='',
                    font=self.font,
                    font_size= int( self.scale*5) )

                self.cell_dict['param title ' + str(i)] = cell(
                    name='param title ' + str(i),
                    screen=self.surface,
                    colors=self.colors,
                    size=(param_height + self.border_size / self.scale, param_wight),
                    start_point=(
                        self.reference_point[0] + self.list_size[0]*self.scale - param_wight_title * self.scale - param_wight * self.scale + self.border_size,
                        self.reference_point[1] +8*self.scale * self.scale - self.border_size + (param_height *self.scale + self.border_size) * i
                    ),
                    scale=self.scale,
                    margin=self.margin,
                    border_size=self.border_size,
                    text=param_list[i],
                    font=self.font,
                    font_size= int( self.scale*5))
    def qr_genrate(self):
        img = qrcode.make(f'lens_width:{self.lens_width}'
                          f'lens_diametr:{self.lens_diametr}'
                          f'lens_R1:{self.lens_R1}'
                          f'lens_R2:{self.lens_R2}'
                          f'current_type:{self.current_type}')
        img.save('QR.png')
        image = pygame.image.load('QR.png')
        image = pygame.transform.scale(image, self.qr_code)
        self.surface.blit(image, self.qr_place)
    def change_reference_point(self):
        try:
            for l in self.lens:
                l.blit_point = \
                (l.original_blit_point[0] + self.reference_point[0],
                 l.original_blit_point[1] + self.reference_point[1])
            self.init_draw_cell()
            self.draw_param_table()

            for key in self.figure_dict.keys():
                self.figure_dict[key].blit_point = \
                    (self.figure_dict[key].original_blit_point[0] + self.reference_point[0],
                     self.figure_dict[key].original_blit_point[1] + self.reference_point[1])
        except Exception as e:
            print(e)
            print('Что-то пошло не так во время отрисовки линзы, если одна из клеток пуста, то все ок')
    def total_draw(self, scale = 1):

        self.surface = pygame.Surface((self.list_size[0] * self.scale, self.list_size[1] * self.scale), pygame.SRCALPHA)
        # self.init_draw_cell()
        # self.draw_param_table()
        self.surface.fill(self.colors['background'])
        # print(self.cell_dict)


        try:
            for l in self.lens:
                l.screen = self.surface
                l.drawLens(scale)
        except Exception as e:
            print(e)
            print('Что-то пошло не так во время отрисовки линзы, если одна из клеток пуста, то все ок')
        # for l in self.lens:
        #     l.screen = self.surface
        #     l.drawLens(scale)
        # pygame.draw.circle(self.surface, (128, 0, 0), self.click_point, 20)

        rect = pygame.Rect(self.reference_point[0],
                           self.reference_point[1] ,
                           self.list_size[0]*self.scale,
                           self.list_size[1]*self.scale)
        pygame.draw.rect(self.surface, self.colors['border'], rect, self.border_size)
        self.cell_dict['document_designation up'].text = self.cell_dict['document_designation down'].text


        for key in self.cell_dict.keys():
            self.cell_dict[key].screen = self.surface
            self.cell_dict[key].draw()

        for key in self.figure_dict.keys():
            self.figure_dict[key].draw()
            self.surface.blit(self.figure_dict[key].surface, self.figure_dict[key].blit_point)
        for i in self.imgList:
            i.draw()
        if self.selected_cell:
            self.selected_cell.draw()


        self.screen.blit(self.surface, self.blit_point)

    def checkSelectFigure(self, click_pos):
        self.click_point = click_pos


        for l in self.lens:
            print('self.scale ',self.scale)
            # surface_offset = (l.blit_point[0]* self.scale/2.5, l.blit_point[1]*self.scale/2.5)
            surface_offset = (l.blit_point[0], l.blit_point[1])

            print('surface_offset ', surface_offset)
            # Получаем координаты нажатия мыши относительно главного окна
            click_pos_absolute = (click_pos[0] - surface_offset[0], click_pos[1] - surface_offset[1])
            # Выводим координаты нажатия мыши относительно главного окна
            if l.check_click(click_pos_absolute):
                self.current_figure = l
                return l
    def checkSelectImg(self, click_pos):
        for l in self.imgList:
            if l.check_click(click_pos):
                self.selected_img = l
                return l

        return False
    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Получение координат клика
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_x, mouse_y = mouse_x - self.blit_point[0], mouse_y - self.blit_point[1]

            checkRes =  self.checkSelectFigure((mouse_x, mouse_y))
            if (checkRes):
                return checkRes

            checkRes = self.checkSelectImg((mouse_x, mouse_y))
            if (checkRes):
                return checkRes

            checkRes = self.check_curren_cell(mouse_x, mouse_y)

            if (checkRes):
                print('CellRes', checkRes)
                self.set_selected_cell(checkRes)
                return self.selected_cell

        return None
    def add_lens(self, start_point = False, width = False,
                diametr = False, R1 = False, R2 = False,
                border_size = False, type = False ):
        if not (start_point): start_point = (0, 0)
        if not (width): width = self.lens_width
        if not (diametr): diametr = self.lens_diametr
        if not (R1): R1 = self.lens_R1
        if not (R2): R2 = self.lens_R2
        if not (border_size): border_size = self.border_size
        if not (type): type = self.current_type

        print('NEW LENS')

        self.lens.append(lens(self.surface, self.colors, start_point,
                         width, diametr, R1, R2,
                              border_size, type,
                         font = self.font ))
    def delete_element(self, element):

        if element in self.lens:
            self.lens.remove(element)
        if element in self.imgList:
            self.imgList.remove(element)
        self.current_figure = None
    def add_img(self):
        new_img = image((50, 50), self.surface)
        self.imgList.append(new_img)
    def delete_signature(self):

        try:
            del self.cell_dict['sign ' + str(self.number_signature)]
        except KeyError:
            print('Нет полей для удаления')


        self.number_signature -= 1
        self.step_signature -= 30 + 2*self.border_size / self.scale
    def add_signature(self):

        self.number_signature += 1
        self.step_signature += 30 + 2*self.border_size / self.scale
        print('number_signature', self.number_signature)
        print('step_signature', self.step_signature)

        self.cell_dict['sign ' + str(self.number_signature)] = signature(
            name='sign ' + str(self.number_signature),
            screen=self.surface,
            colors=self.colors,
            size=(15 + self.border_size / self.scale, 120),
            start_point=(
                self.x - self.margin / 2 - 180 * self.scale  ,
                self.y - self.margin / 2 - 120 * self.scale - self.border_size + self.step_signature
            ),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text= str(self.number_signature) + '. ',
            font=self.font,
            font_size= int( self.scale*10))
    def draw_signature(self):

        self.number_signature = 1
        self.step_signature = 15 + self.border_size / self.scale


        self.cell_dict['sign 1'] = signature(
            name='sign 1',
            screen=self.surface,
            colors=self.colors,
            size=(15 + self.border_size / self.scale, 120),
            start_point=(
                self.x - self.margin / 2 - 180 * self.scale ,
                self.y - self.margin / 2 - 120 * self.scale - self.border_size
            ),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text='1. ',
            font=self.font,
            font_size= int( self.scale*10))
    def __init__(self, screen,
                 colors,
                 list_size,
                 scale,
                 margin,
                 margin_left = 0 ,
                 margin_up = 0,
                 margin_right = 0,
                 margin_text_coef = 1.02,
                 border_size = 2,
                 font = None,
                 save_file = 'config.json'):

        # Создание экрана
        self.list_size = list_size
        self.colors = colors
        self.margin = margin
        self.scale = scale
        self.margin_text_coef = margin_text_coef
        self.screen = screen
        self.font = font
        self.border_size = border_size
        self.x, self.y = self.screen.get_size()
        self.selected_cell = None
        self.margin_left = margin_left
        self.margin_up = margin_up
        self.margin_right = margin_right

        self.surface = pygame.Surface((self.list_size[0]*self.scale,self.list_size[1]*self.scale ),  pygame.SRCALPHA)

        self.blit_point = (self.margin/2 + self.margin_left,
                           self.margin/2 + self.margin_up)
        self.original_blit_point = self.blit_point
        self.reference_point = (0,0)

        self.lens_width = int(60*self.scale)
        self.lens_diametr = int(100*self.scale)
        self.lens_R1 = int(96*self.scale)
        self.lens_R2 = int(80*self.scale)
        self.current_type = 2

        self.left_facet_type = int(0)
        self.right_facet_type = int(0)
        self.left_facet_size = int(16*self.scale)
        self.right_facet_size = int(16*self.scale)

        self.save_file = save_file

        self.scale_text_list = ['10:1', '5:1', '4:1', '2.5:1', '2:1', '1:1', '1:2', '1:2.5', '1:4', '1:5', '1:10']
        self.scale_list = [10, 5, 4, 2.5, 2, 1, 0.5, 0.4, 0.2, 0.1 ]
        self.current_scale = 5

        self.qr_code = (200, 200)
        self.qr_place = (450, 550)
        self.lens = []
        self.start_point = (-self.lens_width/4, self.lens_diametr/4)
        self.lens.append(lens(self.surface, self.colors, self.start_point,
                         self.lens_width, self.lens_diametr, self.lens_R1,
                         self.lens_R2, self.border_size, self.current_type,
                         font = self.font))

        self.current_figure = self.lens[0]

        self.imgList = []
        self.selected_img = None


        self.number_signature = 0
        self.step_signature = 0

        self.cell_dict = {}
        self.figure_dict = {}

        self.set_base_text()
        self.init_draw_cell()
        # self.draw_signature()
        self.draw_param_table()
        self.click_point = (0, 0)