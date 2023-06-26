import pygame
import numpy as np
import choosingtable_class

from picture_class import Picture

colors = {
    'border': (255, 255, 255),
    'text': (255, 255, 255),
    'selected': (255, 255, 255),
    'background': (0, 0, 0),
    'test': (255, 0, 0),
    'transparent': (0, 0, 0, 0)
}

pygame.init()
screen = pygame.display.set_mode((800, 800))
surface = pygame.Surface((800, 800), pygame.SRCALPHA)

picture_1 = (Picture(screen, (0,0), (100, 100), colors, 1, 2, 1), "test_text_picture_1")
picture_2 = (Picture(screen, (0,0), (100, 100), colors, 2, 2, 1), "test_text_picture_2")
picture_3 = (Picture(screen, (0,0), (100, 100), colors, 3, 2, 1), "test_text_picture_3")
picture_4 = (Picture(screen, (0,0), (100, 100), colors, 4, 2, 1), "test_text_picture_4")
picture_5 = (Picture(screen, (0,0), (100, 100), colors, 5, 2, 1), "test_text_picture_5")
picture_6 = (Picture(screen, (0,0), (100, 100), colors, 6, 2, 1), "test_text_picture_6")
picture_7 = (Picture(screen, (0,0), (100, 100), colors, 7, 2, 1), "test_text_picture_7")
picture_8 = (Picture(screen, (0,0), (100, 100), colors, 8, 2, 1), "test_text_picture_8")
picture_9 = (Picture(screen, (0,0), (100, 100), colors, 9, 2, 1), "test_text_picture_9")
picture_10 = (Picture(screen, (0,0), (100, 100), colors, 10, 2, 1), "test_text_picture_10")
picture_11 = (Picture(screen, (0,0), (100, 100), colors, 11, 2, 1), "test_text_picture_11")
picture_12 = (Picture(screen, (0,0), (100, 100), colors, 12, 2, 1), "test_text_picture_12")
picture_13 = (Picture(screen, (0,0), (100, 100), colors, 13, 2, 1), "test_text_picture_13")
picture_14 = (Picture(screen, (0,0), (100, 100), colors, 14, 2, 1), "test_text_picture_14")
picture_15 = (Picture(screen, (0,0), (100, 100), colors, 15, 2, 1), "test_text_picture_15")
picture_16 = (Picture(screen, (0,0), (100, 100), colors, 16, 2, 1), "test_text_picture_16")

def test_function(option):
    print(option)

tables = {
    'таблица 1': (('ФИО', 'Математика', 'Русский', 'Английский', 'Информатика', 'Биология'),
                  ('Пупкин В.В.', picture_1, np.random.randint(2, 6), np.random.randint(2, 6),
                   np.random.randint(2, 6), picture_2),
                  ('Машнов В.К.', np.random.randint(2, 6), picture_3, np.random.randint(2, 6),
                   picture_5, picture_4),
                  ('Замай А.А.', picture_6, picture_7, np.random.randint(2, 6),
                   picture_8, picture_9),
                  ('Аухадыев Р.Р.', picture_10, picture_11, picture_12,
                   np.random.randint(2, 6), picture_13),
                  ('Шунин М.Д.', picture_14, np.random.randint(2, 6), picture_15,
                   np.random.randint(2, 6), picture_16)),
    'table 1': (('ФИО', 'Математика', 'Русский', 'Английский', 'Информатика', 'Биология'),
                ('Пупкин В.В.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6)),
                ('Машнов В.К.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6)),
                ('Замай А.А.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6)),
                ('Аухадыев Р.Р.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6)),
                ('Шунин М.Д.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6))),
    'table 2': (('ФИО', 'Математика', 'Русский', 'Английский', 'Информатика', 'Биология'),
                ('Пупкин В.В.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6)),
                ('Машнов В.К.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6)),
                ('Замай А.А.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6)),
                ('Аухадыев Р.Р.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6)),
                ('Шунин М.Д.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6))),
    'table 3': (('ФИО', 'Математика', 'Русский', 'Английский', 'Информатика', 'Биология'),
                ('Пупкин В.В.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6)),
                ('Машнов В.К.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6)),
                ('Замай А.А.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6)),
                ('Аухадыев Р.Р.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6)),
                ('Шунин М.Д.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6))),
    'table 4': (('ФИО', 'Математика', 'Русский', 'Английский', 'Информатика', 'Биология'),
                ('Пупкин В.В.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6)),
                ('Машнов В.К.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6)),
                ('Замай А.А.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6)),
                ('Аухадыев Р.Р.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6)),
                ('Шунин М.Д.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6))),
    'table 5': (('ФИО', 'Математика', 'Русский', 'Английский', 'Информатика', 'Биология'),
                ('Пупкин В.В.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6)),
                ('Машнов В.К.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6)),
                ('Замай А.А.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6)),
                ('Аухадыев Р.Р.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6)),
                ('Шунин М.Д.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6))),
    'table 6': (('ФИО', 'Математика', 'Русский', 'Английский', 'Информатика', 'Биология'),
                ('Пупкин В.В.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6)),
                ('Машнов В.К.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6)),
                ('Замай А.А.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6)),
                ('Аухадыев Р.Р.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6)),
                ('Шунин М.Д.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                 np.random.randint(2, 6), np.random.randint(2, 6))),
    'таблица N': (('ФИО', 'Математика', 'Русский', 'Английский', 'Информатика', 'Биология'),
                  ('Пупкин В.В.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                   np.random.randint(2, 6), np.random.randint(2, 6)),
                  ('Машнов В.К.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                   np.random.randint(2, 6), np.random.randint(2, 6)),
                  ('Замай А.А.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                   np.random.randint(2, 6), np.random.randint(2, 6)),
                  ('Аухадыев Р.Р.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                   np.random.randint(2, 6), np.random.randint(2, 6)),
                  ('Шунин М.Д.', np.random.randint(2, 6), np.random.randint(2, 6), np.random.randint(2, 6),
                   np.random.randint(2, 6), np.random.randint(2, 6))),
    'таблица 2': (('угол', 'sin', 'cos', 'tg', 'arctg'),
                  (0, 0.0, 1.0, 0.0, 0.0),
                  (30, 0.5, np.sqrt(3) / 2, np.sqrt(3) / 3, np.pi / 6),
                  (45, np.sqrt(2) / 2, np.sqrt(2) / 2, 1.0, np.pi / 4),
                  (60, np.sqrt(3) / 2, 0.5, np.sqrt(3), np.pi / 3),
                  (90, 1.0, 0.0, np.inf, np.pi / 2)),
    'таблица маленькая': (('Группы', 'Фактор 1', 'Фактор 2'),
                          ('Группа 1', np.random.randint(1, 1001), np.random.randint(1, 1001)),
                          ('Группа 2', np.random.randint(1, 1001), np.random.randint(1, 1001)))
}

tables = choosingtable_class.ChoosingTable(screen, (0, 0), colors, (400, 400), tables, test_function, font_size=16, scale=2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            tables.check_click(pygame.mouse.get_pos())

    screen.fill(colors['background'])
    tables.draw()
    pygame.display.flip()

pygame.quit()