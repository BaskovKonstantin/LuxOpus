import pygame
from Template.cellTemplate import cell
from figure.lens import lens
from GUI.signature import signature


class drawingTemplate:

    def init_draw_cell(self):
        print(self.margin)
        self.mainRect = pygame.Rect(self.margin,
                           self.margin,
                           self.list_size[0],
                           self.list_size[1])
        pygame.draw.rect(self.screen, self.colors['border'], self.mainRect, self.border_size)

        self.cell_dict['document_designation down'] = cell(
            name='document_designation down',
            screen = self.screen,
            colors = self.colors,
            cell_size= (15 + self.border_size/self.scale,120),
            cell_start_point= (
                    self.x - self.margin / 2 - 120 * self.scale - self.margin_side,
                    self.y - self.margin / 2 - 55 * self.scale - self.border_size
            ),
            scale = self.scale,
            margin = self.margin,
            border_size= self.border_size,
            text=self.document_designation_text,
            font = self.font,
            font_size= 32)

        self.cell_dict['document_designation up'] = cell(
            name='document_designation up',
            screen = self.screen,
            colors = self.colors,
            cell_size= (14+self.border_size/self.scale ,120),
            cell_start_point= (
                    self.margin / 2 ,
                    self.margin / 2
            ),
            scale = self.scale,
            margin = self.margin,
            border_size=self.border_size,
            text=self.document_designation_text,
            font = self.font,
            font_size= 32,
            text_rotate = 180)

        self.cell_dict['name'] = cell(
            name='name',
            screen=self.screen,
            colors=self.colors,
            cell_size=(25 + self.border_size / self.scale, 70),
            cell_start_point=(
                self.x - self.margin / 2 - 120 * self.scale - self.margin_side,
                self.y - self.margin / 2 - 40 * self.scale - self.border_size
            ),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text=self.text_name,
            font=self.font,
            font_size=36)

        self.cell_dict['material'] = cell(
            name='material',
            screen = self.screen,
            colors = self.colors,
            cell_size= (15 + self.border_size/self.scale,70),
            cell_start_point= (
                    self.x - self.margin / 2 - 120* self.scale - self.margin_side,
                    self.y - self.margin / 2 - 15 * self.scale - self.border_size
            ),
            scale = self.scale,
            margin = self.margin,
            border_size=self.border_size,
            text=self.material_text,
            font = self.font,
            font_size= 36)
        self.cell_dict['author'] = cell(
            name='author',
            screen = self.screen,
            colors = self.colors,
            cell_size= (15 + self.border_size/self.scale ,50+ self.border_size/self.scale),
            cell_start_point= (
                    self.x - self.margin / 2 - 50* self.scale - self.border_size - self.margin_side,
                    self.y - self.margin / 2 - 15 * self.scale - self.border_size
            ),
            scale = self.scale,
            margin = self.margin,
            border_size=self.border_size,
            text=self.author_text,
            font = self.font,
            font_size= 36)

        self.cell_dict['list number'] = cell(
            name='list number',
            screen = self.screen,
            colors = self.colors,
            cell_size= (5 ,20 + 2*self.border_size/self.scale),
            cell_start_point= (
                    self.x - self.margin / 2 - 50* self.scale - self.border_size - self.margin_side,
                    self.y - self.margin / 2 - 20 * self.scale
            ),
            scale = self.scale,
            margin = self.margin,
            border_size=self.border_size,
            text='Лист ' + self.list_number_text,
            font = self.font,
            font_size= 16)

        self.cell_dict['list count'] = cell(
            name='list count',
            screen=self.screen,
            colors=self.colors,
            cell_size=(5 , 30),
            cell_start_point=(
                self.x - self.margin / 2 - 30 * self.scale - self.margin_side,
                self.y - self.margin / 2 - 20 * self.scale
            ),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text='Листов ' + self.list_count_text,
            font = self.font,
            font_size=14)


        self.cell_dict['Literature title'] = cell(
            name='Literature title',
            screen=self.screen,
            colors=self.colors,
            cell_size=(5, 15 + self.border_size/self.scale),
            cell_start_point=(
                self.x - self.margin / 2 - 50 * self.scale - self.border_size - self.margin_side,
                self.y - self.margin / 2 - 40 * self.scale - self.border_size
            ),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text='Лит.',
            font = self.font,
            font_size=14)

        for i in range(1,4):

            self.cell_dict['Literature' + str(i)] = cell(
            name='Literature' + str(i),
                screen=self.screen,
                colors=self.colors,
                cell_size=(15 + 3*self.border_size/self.scale, 5+ self.border_size/self.scale),
                cell_start_point=(
                    self.x - self.margin / 2 - (50 - (i-1)*5)  * self.scale - self.border_size - self.margin_side,
                    self.y - self.margin / 2 - 35 * self.scale - 2*self.border_size
                ),
                scale=self.scale,
                margin=self.margin,
                border_size=self.border_size,
                text=self.lit_list[i-1],
                font = self.font,
                font_size=14)

        self.cell_dict['mass title'] = cell(
            name='mass title',
            screen=self.screen,
            colors=self.colors,
            cell_size=(5, 17 + self.border_size / self.scale),
            cell_start_point=(
                self.x - self.margin / 2 - 35 * self.scale - self.border_size - self.margin_side,
                self.y - self.margin / 2 - 40 * self.scale - self.border_size
            ),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text='масса',
            font=self.font,
            font_size=14)

        self.cell_dict['mass'] = cell(
            name='mass',
            screen=self.screen,
            colors=self.colors,
            cell_size=(15 + 3 * self.border_size / self.scale, 17 + self.border_size / self.scale),
            cell_start_point=(
                self.x - self.margin / 2 - 35 * self.scale - self.border_size - self.margin_side,
                self.y - self.margin / 2 - 35 * self.scale - 2 * self.border_size
            ),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text=self.mass_text,
            font=self.font,
            font_size=14)
        self.cell_dict['scale title'] = cell(
            name='scale title',
            screen=self.screen,
            colors=self.colors,
            cell_size=(5, 18 + self.border_size/self.scale),
            cell_start_point=(
                self.x - self.margin / 2 - 18 * self.scale - self.border_size - self.margin_side,
                self.y - self.margin / 2 - 40 * self.scale - self.border_size
            ),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text='Масштаб.',
            font = self.font,
            font_size=14)
        self.cell_dict['scale'] = cell(
            name='scale',
            screen=self.screen,
            colors=self.colors,
            cell_size=(15 + 3*self.border_size/self.scale , 18 + self.border_size/self.scale),
            cell_start_point=(
                self.x - self.margin / 2 - 18 * self.scale - self.border_size - self.margin_side,
                self.y - self.margin / 2 - 35 * self.scale - 2*self.border_size
            ),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text=self.scale_text,
            font = self.font,
            font_size=14)
        for i in range(0,11):
            cur_text = self.date_text[i]

            self.cell_dict['date' + str(i)] = cell(
            name='date' + str(i),
                screen=self.screen,
                colors=self.colors,
                cell_size=(5 + self.border_size/self.scale, 10 + self.border_size/self.scale),
                cell_start_point=(
                    self.x - self.margin / 2 - 130 * self.scale - self.margin_side,
                    self.y - self.margin / 2 - (55 - 5*(i)) * self.scale - self.border_size
                ),
                scale=self.scale,
                margin=self.margin,
                border_size=self.border_size,
                text=cur_text,
                font = self.font,
                font_size=14)
        for i in range(0,11):
            cur_text = self.podl_text[i]

            self.cell_dict['podl' + str(i)] = cell(
            name='podl' + str(i),
                screen=self.screen,
                colors=self.colors,
                cell_size=(5 + self.border_size/self.scale, 15 + self.border_size/self.scale),
                cell_start_point=(
                    self.x - self.margin / 2 - 145 * self.scale - self.margin_side,
                    self.y - self.margin / 2 - (55 - 5*(i)) * self.scale - self.border_size
                ),
                scale=self.scale,
                margin=self.margin,
                border_size=self.border_size,
                text=cur_text,
                font = self.font,
                font_size=14)

        for i in range(0,11):
            cur_text = self.N_doc_text[i]

            self.cell_dict['N doc' + str(i)] = cell(
            name='N doc' + str(i),
                screen=self.screen,
                colors=self.colors,
                cell_size=(5 + self.border_size/self.scale, 23 + self.border_size/self.scale),
                cell_start_point=(
                    self.x - self.margin / 2 - 168 * self.scale - self.margin_side,
                    self.y - self.margin / 2 - (55 - 5*(i)) * self.scale - self.border_size
                ),
                scale=self.scale,
                margin=self.margin,
                border_size=self.border_size,
                text=cur_text,
                font = self.font,
                font_size=14)

        for i in range(0,5):
            cur_text = self.change_text[i]

            self.cell_dict['Change' + str(i)] = cell(
            name='Change' + str(i),
                screen=self.screen,
                colors=self.colors,
                cell_size=(5 + self.border_size/self.scale, 7 + self.border_size/self.scale),
                cell_start_point=(
                    self.x - self.margin / 2 - 185 * self.scale - self.margin_side,
                    self.y - self.margin / 2 - (55 - 5*(i)) * self.scale - self.border_size
                ),
                scale=self.scale,
                margin=self.margin,
                border_size=self.border_size,
                text=cur_text,
                font = self.font,
                font_size=14)

        for i in range(0,5):
            cur_text = self.list_text[i]

            self.cell_dict['List' + str(i)] = cell(
            name='List' + str(i),
                screen=self.screen,
                colors=self.colors,
                cell_size=(5 + self.border_size/self.scale, 10 + self.border_size/self.scale),
                cell_start_point=(
                    self.x - self.margin / 2 - 178 * self.scale - self.margin_side,
                    self.y - self.margin / 2 - (55 - 5*(i)) * self.scale - self.border_size
                ),
                scale=self.scale,
                margin=self.margin,
                border_size=self.border_size,
                text=cur_text,
                font = self.font,
                font_size=14)

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
                screen=self.screen,
                colors=self.colors,
                cell_size=(5 + self.border_size/self.scale, 17 + self.border_size/self.scale),
                cell_start_point=(
                    self.x - self.margin / 2 - 185 * self.scale - self.margin_side,
                    self.y - self.margin / 2 - (55 - 5*(i)) * self.scale - self.border_size
                ),
                scale=self.scale,
                margin=self.margin,
                border_size=self.border_size,
                text=cur_text,
                font = self.font,
                font_size=14)
        # ГОСТ Клетки из шаблона главно страницыг

        for i in range(0,5):
            cur_text = self.Zona_text[i]

            self.cell_dict['Zona' + str(i)] = cell(
            name='Zona' + str(i),
                screen=self.screen,
                colors=self.colors,
                cell_size=(5 + self.border_size/self.scale, 25 + self.border_size/self.scale),
                cell_start_point=(
                    self.x - self.margin / 2 - 210 * self.scale - self.margin_side,
                    self.y - self.margin / 2 - (55 - 5*(i)) * self.scale - self.border_size
                ),
                scale=self.scale,
                margin=self.margin,
                border_size=self.border_size,
                text=cur_text,
                font = self.font,
                font_size=14)

        self.cell_dict['inv N podl title'] = cell(
            name='inv N podl title',
            screen=self.screen,
            colors=self.colors,
            cell_size=(25 + self.border_size/self.scale, 5 + self.border_size/self.scale),
            cell_start_point=(
                self.margin / 2 - 12*self.scale ,
                self.y - self.margin / 2 - 25*self.scale - 2*self.border_size / self.scale),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text='Инв N подл',
            font = self.font,
            font_size=14,
            text_rotate = 90)

        self.cell_dict['inv N podl'] = cell(
            name='inv N podl',
            screen=self.screen,
            colors=self.colors,
            cell_size=(25 + self.border_size/self.scale, 7 + self.border_size/self.scale),
            cell_start_point=(
                self.margin / 2 - 7*self.scale ,
                self.y - self.margin / 2 - 25*self.scale - 2*self.border_size / self.scale),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text=self.inv_N_podl_text,
            font = self.font,
            font_size=14,
            text_rotate=90)

        self.cell_dict['Podl and date title'] = cell(
            name='Podl and date title',
            screen=self.screen,
            colors=self.colors,
            cell_size=(35 + self.border_size / self.scale, 5 + self.border_size / self.scale),
            cell_start_point=(
                self.margin / 2 - 12 * self.scale,
                self.y - self.margin / 2 - 60 * self.scale - 2*self.border_size / self.scale),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text='Подл и дата',
            font = self.font,
            font_size=14,
            text_rotate=90)

        self.cell_dict['Podl and date'] = cell(
            name='Podl and date',
            screen=self.screen,
            colors=self.colors,
            cell_size=(35 + self.border_size / self.scale, 7 + self.border_size / self.scale),
            cell_start_point=(
                self.margin / 2 - 7 * self.scale,
                self.y - self.margin / 2 - 60 * self.scale - 2*self.border_size / self.scale),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text=self.Podl_and_date_text,
            font = self.font,
            font_size=14,
            text_rotate=90)

        self.cell_dict['Vzam inv title'] = cell(
            name='Vzam inv title',
            screen=self.screen,
            colors=self.colors,
            cell_size=(25, 5 + self.border_size / self.scale),
            cell_start_point=(
                self.margin / 2 - 12 * self.scale,
                self.y - self.margin / 2 - 85 * self.scale ),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text='Взам инв',
            font = self.font,
            font_size=14,
            text_rotate=90)

        self.cell_dict['Vzam inv'] = cell(
            name='Vzam inv',
            screen=self.screen,
            colors=self.colors,
            cell_size=(25, 7 + self.border_size / self.scale),
            cell_start_point=(
                self.margin / 2 - 7 * self.scale,
                self.y - self.margin / 2 - 85 * self.scale),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text=self.Vzam_inv_text,
            font = self.font,
            font_size=14,
            text_rotate=90)

        self.cell_dict['inv dubble title'] = cell(
            name='inv dubble title',
            screen=self.screen,
            colors=self.colors,
            cell_size=(25 + self.border_size / self.scale, 5 + self.border_size / self.scale),
            cell_start_point=(
                self.margin / 2 - 12 * self.scale,
                self.y - self.margin / 2 - 110 * self.scale ),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text='Инв N дубл',
            font = self.font,
            font_size=14,
            text_rotate=90)

        self.cell_dict['inv dubble podl'] = cell(
            name='inv dubble podl',
            screen=self.screen,
            colors=self.colors,
            cell_size=(25 + self.border_size / self.scale, 7 + self.border_size / self.scale),
            cell_start_point=(
                self.margin / 2 - 7 * self.scale,
                self.y - self.margin / 2 - 110 * self.scale),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text=self.inv_dubble_text,
            font = self.font,
            font_size=14,
            text_rotate=90)

        self.cell_dict['podl and date 2 title'] = cell(
            name='podl and date 2 title',
            screen=self.screen,
            colors=self.colors,
            cell_size=(35 + self.border_size / self.scale, 5 + self.border_size / self.scale),
            cell_start_point=(
                self.margin / 2 - 12 * self.scale,
                self.y - self.margin / 2 - 145 * self.scale ),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text='Подл и дата',
            font = self.font,
            font_size=14,
            text_rotate=90)

        self.cell_dict['podl and date 2'] = cell(
            name='podl and date 2',
            screen=self.screen,
            colors=self.colors,
            cell_size=(35 + self.border_size / self.scale, 7 + self.border_size / self.scale),
            cell_start_point=(
                self.margin / 2 - 7 * self.scale,
                self.y - self.margin / 2 - 145 * self.scale),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text=self.podl_and_date_2,
            font = self.font,
            font_size=14,
            text_rotate=90)

        self.cell_dict['First use title'] = cell(
            name='First use title',
            screen=self.screen,
            colors=self.colors,
            cell_size=(60 + self.border_size / self.scale, 5 + self.border_size / self.scale),
            cell_start_point=(
                self.margin / 2 - 12 * self.scale,
                self.margin / 2 ),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text='Перв прим',
            font = self.font,
            font_size=14,
            text_rotate=90)

        self.cell_dict['First use'] = cell(
            name='First use',
            screen=self.screen,
            colors=self.colors,
            cell_size=(60 + self.border_size / self.scale, 7 + self.border_size / self.scale),
            cell_start_point=(
                self.margin / 2 - 7 * self.scale,
                self.margin / 2 ),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text=self.First_use_text,
            font = self.font,
            font_size=14,
            text_rotate=90)

        self.cell_dict['Help N title'] = cell(
            name='Help N title',
            screen=self.screen,
            colors=self.colors,
            cell_size=(60 + self.border_size / self.scale, 5 + self.border_size / self.scale),
            cell_start_point=(
                self.margin / 2 - 12 * self.scale,
                self.margin / 2 + 60 * self.scale),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text='Справ N',
            font = self.font,
            font_size=14,
            text_rotate=90)

        self.cell_dict['Help N'] = cell(
            name='Help N',
            screen=self.screen,
            colors=self.colors,
            cell_size=(60 + self.border_size / self.scale, 7 + self.border_size / self.scale),
            cell_start_point=(
                self.margin / 2 - 7 * self.scale,
                self.margin / 2 + 60 * self.scale),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text=self.Help_N_text,
            font = self.font,
            font_size=14,
            text_rotate=90)
    def set_base_text(self):
        # Обозначение документа
        self.document_designation_text = 'Обозначение документа'

        # Наименование изделия
        self.text_name = 'Имя изделия'

        # Материал
        self.material_text = 'Материал'

        # Автор
        self.author_text = 'Изготов.'

        # Номер листа
        self.list_number_text = 'N'

        # Количество листов
        self.list_count_text = 'N'

        # Литера
        self.lit_list = ['', '', '']

        # Масса
        self.mass_text = ''

        # Масштаб
        self.scale_text = ''

        # Дата
        self.date_text = [''] * 11
        self.date_text[4] = 'Дата'

        # Подл
        self.podl_text = [''] * 11
        self.podl_text[4] = 'Подл'

        # Номер документа
        self.N_doc_text = [''] * 11
        self.N_doc_text[4] = 'N докум.'

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
                # print(self.cell_dict[cellName].text)
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
    # def draw_param_table(self):
    #
    #     self.cell_dict['lens width'] = cell(
    #         name='lens width',
    #         screen = self.screen,
    #         colors = self.colors,
    #         cell_size= (10 + self.border_size/self.scale,20),
    #         cell_start_point= (
    #                 self.x - self.margin / 2 - 20 * self.scale - self.margin_side,
    #                 self.margin / 2 + 20 * self.scale - self.border_size
    #         ),
    #         scale = self.scale,
    #         margin = self.margin,
    #         border_size= self.border_size,
    #         text= str(self.lens_width),
    #         font = self.font,
    #         font_size= 16)
    #
    #     self.cell_dict['lens width title'] = cell(
    #         name='lens width title',
    #         screen = self.screen,
    #         colors = self.colors,
    #         cell_size= (10 + self.border_size/self.scale,20),
    #         cell_start_point= (
    #                 self.x - self.margin / 2 - 20 * self.scale - 60 + self.border_size - self.margin_side,
    #                 self.margin / 2 + 20 * self.scale - self.border_size
    #         ),
    #         scale = self.scale,
    #         margin = self.margin,
    #         border_size= self.border_size,
    #         text= 'Шир.',
    #         font = self.font,
    #         font_size= 16)
    #
    #     self.cell_dict['lens diametr'] = cell(
    #         name='lens diametr',
    #         screen = self.screen,
    #         colors = self.colors,
    #         cell_size= (10 + self.border_size/self.scale,20),
    #         cell_start_point= (
    #                 self.x - self.margin / 2 - 20 * self.scale - self.margin_side,
    #                 self.margin / 2 + 30 * self.scale - self.border_size
    #         ),
    #         scale = self.scale,
    #         margin = self.margin,
    #         border_size= self.border_size,
    #         text= str(self.lens_diametr),
    #         font = self.font,
    #         font_size= 16)
    #
    #     self.cell_dict['lens diametr title'] = cell(
    #         name='lens diametr title',
    #         screen = self.screen,
    #         colors = self.colors,
    #         cell_size= (10 + self.border_size/self.scale,20),
    #         cell_start_point= (
    #                 self.x - self.margin / 2 - 20 * self.scale - 60 + self.border_size - self.margin_side,
    #                 self.margin / 2 + 30 * self.scale - self.border_size
    #         ),
    #         scale = self.scale,
    #         margin = self.margin,
    #         border_size= self.border_size,
    #         text= 'D',
    #         font = self.font,
    #         font_size= 16)
    #
    #     self.cell_dict['lens R1'] = cell(
    #         name='lens R1',
    #         screen = self.screen,
    #         colors = self.colors,
    #         cell_size= (10 + self.border_size/self.scale,20),
    #         cell_start_point= (
    #                 self.x - self.margin / 2 - 20 * self.scale - self.margin_side,
    #                 self.margin / 2 + 40 * self.scale - self.border_size
    #         ),
    #         scale = self.scale,
    #         margin = self.margin,
    #         border_size= self.border_size,
    #         text= str(self.lens_R1),
    #         font = self.font,
    #         font_size= 16)
    #
    #     self.cell_dict['lens R1 title'] = cell(
    #         name='lens R1 title',
    #         screen = self.screen,
    #         colors = self.colors,
    #         cell_size= (10 + self.border_size/self.scale,20),
    #         cell_start_point= (
    #                 self.x - self.margin / 2 - 20 * self.scale - 60 + self.border_size - self.margin_side,
    #                 self.margin / 2 + 40 * self.scale - self.border_size
    #         ),
    #         scale = self.scale,
    #         margin = self.margin,
    #         border_size= self.border_size,
    #         text= 'R1',
    #         font = self.font,
    #         font_size= 16)
    #
    #     self.cell_dict['lens R2'] = cell(
    #         name='lens R1',
    #         screen = self.screen,
    #         colors = self.colors,
    #         cell_size= (10 + self.border_size/self.scale,20),
    #         cell_start_point= (
    #                 self.x - self.margin / 2 - 20 * self.scale - self.margin_side,
    #                 self.margin / 2 + 50 * self.scale - self.border_size
    #         ),
    #         scale = self.scale,
    #         margin = self.margin,
    #         border_size= self.border_size,
    #         text= str(self.lens_R2),
    #         font = self.font,
    #         font_size= 16)
    #     self.cell_dict['lens R2 title'] = cell(
    #         name='lens R2 title',
    #         screen = self.screen,
    #         colors = self.colors,
    #         cell_size= (10 + self.border_size/self.scale,20),
    #         cell_start_point= (
    #                 self.x - self.margin / 2 - 20 * self.scale - 60 + self.border_size - self.margin_side,
    #                 self.margin / 2 + 50 * self.scale - self.border_size
    #         ),
    #         scale = self.scale,
    #         margin = self.margin,
    #         border_size= self.border_size,
    #         text= 'R2',
    #         font = self.font,
    #         font_size= 16)
    #
    #     self.cell_dict['type title'] = cell(
    #         name='type title',
    #         screen = self.screen,
    #         colors = self.colors,
    #         cell_size= (10 + self.border_size/self.scale,20),
    #         cell_start_point= (
    #                 self.x - self.margin / 2 - 20 * self.scale - 60 + self.border_size - self.margin_side,
    #                 self.margin / 2 + 60 * self.scale - self.border_size
    #         ),
    #         scale = self.scale,
    #         margin = self.margin,
    #         border_size= self.border_size,
    #         text= 'type',
    #         font = self.font,
    #         font_size= 16)
    #
    #     self.cell_dict['type'] = cell(
    #         name='type',
    #         screen = self.screen,
    #         colors = self.colors,
    #         cell_size= (10 + self.border_size/self.scale,20),
    #         cell_start_point= (
    #                 self.x - self.margin / 2 - 20 * self.scale - self.margin_side,
    #                 self.margin / 2 + 60 * self.scale - self.border_size
    #         ),
    #         scale = self.scale,
    #         margin = self.margin,
    #         border_size= self.border_size,
    #         text= str(self.current_type),
    #         font = self.font,
    #         font_size= 16)
    #
    #     self.cell_dict['facet type title'] = cell(
    #         name='facet type title',
    #         screen = self.screen,
    #         colors = self.colors,
    #         cell_size= (10 + self.border_size/self.scale,26),
    #         cell_start_point= (
    #                 self.x - self.margin / 2 - 66 * self.scale - self.margin_side,
    #                 self.margin / 2 + 100 * self.scale - self.border_size
    #         ),
    #         scale = self.scale,
    #         margin = self.margin,
    #         border_size= self.border_size,
    #         text= 'facet type',
    #         font = self.font,
    #         font_size= 16)
    #
    #     self.cell_dict['facet type left'] = cell(
    #         name='facet type left',
    #         screen = self.screen,
    #         colors = self.colors,
    #         cell_size= (10 + self.border_size/self.scale,20),
    #         cell_start_point= (
    #                 self.x - self.margin / 2 - 40 * self.scale - self.margin_side,
    #                 self.margin / 2 + 100 * self.scale - self.border_size
    #         ),
    #         scale = self.scale,
    #         margin = self.margin,
    #         border_size= self.border_size,
    #         text= str(self.left_facet_type),
    #         font = self.font,
    #         font_size= 16)
    #
    #     self.cell_dict['facet type right'] = cell(
    #         name='facet type right',
    #         screen = self.screen,
    #         colors = self.colors,
    #         cell_size= (10 + self.border_size/self.scale,20),
    #         cell_start_point= (
    #                 self.x - self.margin / 2 - 20 * self.scale - self.margin_side,
    #                 self.margin / 2 + 100 * self.scale - self.border_size
    #         ),
    #         scale = self.scale,
    #         margin = self.margin,
    #         border_size= self.border_size,
    #         text= str(self.right_facet_type),
    #         font = self.font,
    #         font_size= 16)
    #
    #     self.cell_dict['facet size title'] = cell(
    #         name='facet size title',
    #         screen=self.screen,
    #         colors=self.colors,
    #         cell_size=(10 + self.border_size / self.scale, 26),
    #         cell_start_point=(
    #             self.x - self.margin / 2 - 66 * self.scale - self.margin_side,
    #             self.margin / 2 + 110 * self.scale - self.border_size
    #         ),
    #         scale=self.scale,
    #         margin=self.margin,
    #         border_size=self.border_size,
    #         text='facet size',
    #         font=self.font,
    #         font_size=16)
    #
    #     self.cell_dict['facet size left'] = cell(
    #         name='facet size left',
    #         screen=self.screen,
    #         colors=self.colors,
    #         cell_size=(10 + self.border_size / self.scale, 20),
    #         cell_start_point=(
    #             self.x - self.margin / 2 - 40 * self.scale - self.margin_side,
    #             self.margin / 2 + 110 * self.scale - self.border_size
    #         ),
    #         scale=self.scale,
    #         margin=self.margin,
    #         border_size=self.border_size,
    #         text=str(self.left_facet_size),
    #         font=self.font,
    #         font_size=16)
    #
    #     self.cell_dict['facet size right'] = cell(
    #         name='facet size right',
    #         screen=self.screen,
    #         colors=self.colors,
    #         cell_size=(10 + self.border_size / self.scale, 20),
    #         cell_start_point=(
    #             self.x - self.margin / 2 - 20 * self.scale - self.margin_side,
    #             self.margin / 2 + 110 * self.scale - self.border_size
    #         ),
    #         scale=self.scale,
    #         margin=self.margin,
    #         border_size=self.border_size,
    #         text=str(self.right_facet_size),
    #         font=self.font,
    #         font_size=16)
    # def qr_genrate(self):
    #
    #
    #     img = qrcode.make(f'lens_width:{self.lens_width}'
    #                       f'lens_diametr:{self.lens_diametr}'
    #                       f'lens_R1:{self.lens_R1}'
    #                       f'lens_R2:{self.lens_R2}'
    #                       f'current_type:{self.current_type}')
    #     img.save('QR.png')
    #     image = pygame.image.load('QR.png')
    #     image = pygame.transform.scale(image, self.qr_code)
    #     self.screen.blit(image, self.qr_place)
    def total_redraw(self):
        # self.lens.width = int(self.cell_dict['lens width'].text) if  len(self.cell_dict['lens width'].text) > 0 else self.lens.width
        # self.lens.diametr = int(self.cell_dict['lens diametr'].text) if  len(self.cell_dict['lens diametr'].text) > 0 else self.lens.diametr
        # self.lens.R1 = int(self.cell_dict['lens R1'].text) if  len(self.cell_dict['lens R1'].text) > 0 else self.lens.R1
        # self.lens.R2 = int(self.cell_dict['lens R2'].text) if  len(self.cell_dict['lens R2'].text) > 0 else self.lens.R2
        # self.current_type = int(self.cell_dict['type'].text) if self.cell_dict['type'].text else self.current_type



        # self.lens.left_facet_type = int(self.cell_dict['facet type left'].text) if  len(self.cell_dict['facet type left'].text) > 0 else self.left_facet_type
        # self.lens.right_facet_type = int(self.cell_dict['facet type right'].text) if  len(self.cell_dict['facet type right'].text) > 0 else self.right_facet_type

        # self.lens.left_facet_size = int(self.cell_dict['facet size left'].text) if  len(self.cell_dict['facet size left'].text) > 0 else self.right_facet_size
        # self.lens.right_facet_size = int(self.cell_dict['facet size right'].text) if  len(self.cell_dict['facet size right'].text) > 0 else self.right_facet_size
        # print(self.lens.R1)
        # print(self.lens.R2)

        # self.current_figure.types = self.current_figure.lens_type[self.current_type if (self.current_type > 0
        #                                             and self.current_type < 12) else self.current_type]
        try:
            for l in self.lens:
                l.drawLens()
        except Exception as e:
            print(e)
            print('Что-то пошло не так во время отрисовки линзы, если одна из клеток пуста, то все ок')

        rect = pygame.Rect(self.margin / 2,
                           self.margin / 2,
                           self.list_size[0]*self.scale,
                           self.list_size[1]*self.scale)
        pygame.draw.rect(self.screen, self.colors['border'], rect, self.border_size)
        # self.qr_genrate()

        for key in self.cell_dict.keys():
            self.cell_dict[key].redraw()

    def checkSelectFigure(self, click_pos):

        for l in self.lens:

            surface_offset = (l.point_x,l.point_y)
            print(surface_offset)
            # Получаем координаты нажатия мыши относительно главного окна
            click_pos_absolute = (click_pos[0] - surface_offset[0], click_pos[1] - surface_offset[1])
            # Выводим координаты нажатия мыши относительно главного окна
            # print("Кнопка мыши нажата в точке", click_pos_absolute)
            if l.check_click(click_pos_absolute):
                self.current_figure = l
                return l

        return False

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Получение координат клика
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (self.checkSelectFigure((mouse_x, mouse_y))):
                return self.checkSelectFigure((mouse_x, mouse_y))
            self.set_selected_cell(self.check_curren_cell(mouse_x, mouse_y))
            print(self.selected_cell)
            return self.selected_cell

        return None

    def add_lens(self):
        self.start_point = (0, 0)
        print('NEW LENS')
        self.lens.append(lens(self.screen, self.colors, self.start_point,
                         self.lens_width, self.lens_diametr, self.lens_R1,
                         self.lens_R2, self.border_size, self.current_type,
                         font = self.font ))

    def delete_signature(self):

        del self.cell_dict['sign ' + str(self.number_signature)]

        self.number_signature -= 1
        self.step_signature -= 30 + 2*self.border_size / self.scale





    def add_signature(self):

        self.number_signature += 1
        self.step_signature += 30 + 2*self.border_size / self.scale
        print('number_signature', self.number_signature)
        print('step_signature', self.step_signature)

        self.cell_dict['sign ' + str(self.number_signature)] = signature(
            name='sign ' + str(self.number_signature),
            screen=self.screen,
            colors=self.colors,
            cell_size=(15 + self.border_size / self.scale, 120),
            cell_start_point=(
                self.x - self.margin / 2 - 180 * self.scale - self.margin_side ,
                self.y - self.margin / 2 - 120 * self.scale - self.border_size + self.step_signature
            ),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text= str(self.number_signature) + '. ',
            font=self.font,
            font_size=32)


        self.cell_dict['sign 1'] = signature(
            name='sign 1',
            screen=self.screen,
            colors=self.colors,
            cell_size=(15 + self.border_size / self.scale, 120),
            cell_start_point=(
                self.x - self.margin / 2 - 180 * self.scale - self.margin_side,
                self.y - self.margin / 2 - 120 * self.scale - self.border_size
            ),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text='1. ',
            font=self.font,
            font_size=32)


    def draw_signature(self):

        self.number_signature = 1
        self.step_signature = 15 + self.border_size / self.scale


        self.cell_dict['sign 1'] = signature(
            name='sign 1',
            screen=self.screen,
            colors=self.colors,
            cell_size=(15 + self.border_size / self.scale, 120),
            cell_start_point=(
                self.x - self.margin / 2 - 180 * self.scale - self.margin_side,
                self.y - self.margin / 2 - 120 * self.scale - self.border_size
            ),
            scale=self.scale,
            margin=self.margin,
            border_size=self.border_size,
            text='1. ',
            font=self.font,
            font_size=32)

    def __init__(self, screen,
                 colors,
                 list_size ,
                 scale ,
                 margin,
                 margin_side = 0 ,
                 margin_up = 0,
                 margin_text_coef = 1.02,
                 border_size = 2,
                 font = None):

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
        self.margin_side = margin_side
        self.margin_up = margin_up


        self.lens_width = 150
        self.lens_diametr = 250
        self.lens_R1 = 240
        self.lens_R2 = 200
        self.current_type = 7

        self.left_facet_type = 0
        self.right_facet_type = 0
        self.left_facet_size = 40
        self.right_facet_size = 40

        # self.lensTypeDict = {
        #     1:'flat convex',
        #     2:'convex flat',
        #     3:'concave flat',
        #     4:'flat concave',
        #     5:'biconvex',
        #     6:'biconcave',
        #     7:'convex concave',
        #     8:'concave convex',
        #     9:'prism',
        #     10:'meniscus',
        #     11:'window prism'
        # }

        self.qr_code = (200, 200)
        self.qr_place = (450, 550)
        self.lens = []
        self.start_point = (0, 0)
        self.lens.append(lens(self.screen, self.colors, self.start_point,
                         self.lens_width, self.lens_diametr, self.lens_R1,
                         self.lens_R2, self.border_size, self.current_type,
                         font = self.font ))

        # self.start_point = (120, 0)
        # self.lens.append(lens(self.screen, self.colors, self.start_point,
        #                       self.lens_width, self.lens_diametr, self.lens_R1,
        #                       self.lens_R2, self.border_size, self.current_type,
        #                       font=self.font))

        self.current_figure = self.lens[0]



        self.cell_dict = {}

        self.set_base_text()
        self.init_draw_cell()
        self.draw_signature()
        # self.draw_param_table()









