from settings import *
from graphics import Superficie
import pygame

pygame.init()
#classe deteminando a imagem da tela de morte
class Tela_morte:
    tela_morte = pygame.image.load('projeto/assets/frase.png') 
    img_inimigo = pygame.image.load('projeto\sprites_folder\sprite_07.png')
    img_inimigo = pygame.transform.scale(img_inimigo, (40, 40))
    def exibir_tela_morte(self, hud, jogador):
        sup_inimigos = hud.fonte2.render(f': {jogador.pontuacao}', False, 'White')
        TELA.blit(Superficie.im_jogo, (LARGURA_TELA/2 - Superficie.im_jogo.get_width()/2, ALTURA_TELA/2 - Superficie.im_jogo.get_height()/2))
        TELA.blit(Tela_morte.tela_morte, (1,1))
        TELA.blit(self.img_inimigo, (545, 385))
        TELA.blit(hud.img_nivel, (545, 440))
        TELA.blit(sup_inimigos, (580, 400))
        TELA.blit(hud.sup_nivel, (580, 450))