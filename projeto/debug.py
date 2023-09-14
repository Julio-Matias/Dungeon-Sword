import pygame
from settings import *

pygame.init()
fonte_debug = pygame.font.Font(None, 35)
# Criei uma função de debug
# Para usar ela é só colocar a variavel que você quer analisar como primeiro parametro
def debug(info, descricao = '', y = 5, x = 5):
    # Se quiser ter uma descrição melhor na tela pode passar um texto para acompanhar a variavel como segundo parametro
    sup_debug = fonte_debug.render(f"{descricao} {str(info)}", True, 'White')
    # Por fim, se for usada mais de uma vez, as informações vão ficar uma em cima da outra na tela, então para resolver esse problema, é só passar um valor maior para a coordenada x e y
    # Coloquei a coordenada y como terceiro parametro e a x como quarto porque é mais comum querer as informações uma embaixo da outra, e assim fica mais facil mexer no y
    rect_debug = sup_debug.get_rect(topleft = (x, y))
    pygame.draw.rect(TELA, 'Black', rect_debug)
    TELA.blit(sup_debug, rect_debug)
