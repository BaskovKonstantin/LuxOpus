import pygame
import numpy as np
import choosingtable_class

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

def test_function(option):
    print(option)

tables = {
    'таблица 1': (('ФИО', 'Математика', 'Русский', 'Английский', 'Информатика', 'Биология'),
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