import pygame
from figure.lens import lens




def initLensTypeImageSurface(screen, colors, start_point, border_size = 3, type = 1, font = None, scale = 1, left_facet_type = None, right_facet_type = None):
    lens_width = 70
    lens_diametr = 250
    lens_R1 = 240
    lens_R2 = 200

    l = lens(screen, colors, start_point,
         lens_width, lens_diametr, lens_R1,
         lens_R2, border_size, type,
         font=font)
    if (left_facet_type):
        l.left_facet_type = left_facet_type
        l.left_facet_size = 40
    if (right_facet_type):
        l.right_facet_type = right_facet_type
        l.right_facet_size = 40

    l.drawLens()

    surface = pygame.transform.scale(l.surface, (l.surface.get_width()*scale, l.surface.get_height()*scale))
    return surface
