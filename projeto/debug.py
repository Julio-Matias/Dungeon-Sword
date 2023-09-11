import pygame
from settings import *

pygame.init()
fonte_debug = pygame.font.Font(None, 35)

def debug(info, descricao, y = 5, x = 5):
    sup_debug = fonte_debug.render(f"{descricao}: {str(info)}", True, 'White')
    rect_debug = sup_debug.get_rect(topleft = (x, y))
    pygame.draw.rect(TELA, 'Black', rect_debug)
    TELA.blit(sup_debug, rect_debug)
