from graphics import Superficie
from settings import *
from level import Mapa
import pygame
pygame.init()



# Posição do jogador
x_jogador = 300
y_jogador = 200
pos_jogador = [x_jogador, y_jogador]
# Criando uma class de player que vai conter as caracteristicas do personagem do jogador
class Player: 
    distancia_movida = 10
    def __init__(self):
        self.imagem = pygame.Surface((LARGURA_JOGADOR, ALTURA_JOGADOR))
        self.imagem.fill(Cor.VERMELHO)
        self.hitbox = pygame.Rect((pos_jogador), (LARGURA_JOGADOR+2, ALTURA_JOGADOR+2))
        self.velocidade_x = 0
        self.velocidade_y = 0
    def movimento_jogador(self):
        # Checa quais as teclas que estão sendo pressionadas e baseado nisso faz o personagem se mover
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:
            self.velocidade_y -= Player.distancia_movida
        if teclas[pygame.K_DOWN]:
            self.velocidade_y += Player.distancia_movida
        if teclas[pygame.K_LEFT]:
            self.velocidade_x -= Player.distancia_movida
        if teclas[pygame.K_RIGHT]:
            self.velocidade_x += Player.distancia_movida
        pos_jogador[0] += self.velocidade_x
        pos_jogador[1] += self.velocidade_y
        return pos_jogador
    def checando_colisao(self, mapa):
        colidiu = False
        for tile in mapa.mapa_tiles:
            if tile.tipo == 'parede' and self.hitbox.colliderect(tile.hitbox):
                colidiu = True
        return colidiu
