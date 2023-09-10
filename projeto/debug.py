import pygame
from settings import *

pygame.init()
fonte_debug = pygame.font.Font(None, 50)

def debug(info, y = 10, x = 10):
    sup_debug = fonte_debug.render(str(info), True, 'White')
    rect_debug = sup_debug.get_rect(topleft = (x, y))
    pygame.draw.rect(TELA, 'Black', rect_debug)
    TELA.blit(sup_debug, rect_debug)
