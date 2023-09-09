from graphics import Superficie
from settings import *
from level import hitbox_tilemap
import pygame
pygame.init()



# Posição do jogador
x_jogador = 300
y_jogador = 200
pos_jogador = [x_jogador, y_jogador]
# Criando uma class de player que vai conter as caracteristicas do personagem do jogador
class Player: 
    def __init__(self):
        self.imagem = pygame.Surface((LARGURA_JOGADOR, ALTURA_JOGADOR))
        self.imagem.fill(Cor.VERMELHO)
        self.hitbox = self.imagem.get_rect(topleft=(pos_jogador))
    def movimento_jogador(colisao):
        # Checa quais as teclas que estão sendo pressionadas e baseado nisso faz o personagem se mover
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:
            pos_jogador[1] -= 10
        if teclas[pygame.K_DOWN]:
            pos_jogador[1] += 10
        if teclas[pygame.K_LEFT]:
            pos_jogador[0] -= 10
        if teclas[pygame.K_RIGHT]:
            pos_jogador[0] += 10
        return pos_jogador
    def checando_colisao(self):
        colidiu = False
        for tile in hitbox_tilemap:
            if self.hitbox.colliderect(tile):
                colidiu = True
        return colidiu
