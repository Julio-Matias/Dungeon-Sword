from settings import *
from graphics import Superficie
import pygame

pygame.init()
#classe deteminando a imagem da tela de morte
class Tela_morte:
    tela_morte = pygame.image.load('projeto/assets/frase.png') 
    def exibir_tela_morte(self, hud):
        TELA.blit(Superficie.im_jogo, (LARGURA_TELA/2 - Superficie.im_jogo.get_width()/2, ALTURA_TELA/2 - Superficie.im_jogo.get_height()/2))
        TELA.blit(Tela_morte.tela_morte, (1,1))
        TELA.blit(hud.sup_pontuacao, (600,400))
        TELA.blit(hud.sup_nivel, ( 550,450))
