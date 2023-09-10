from graphics import Superficie
from settings import *
from level import Mapa
import pygame
pygame.init()

# Posição do jogador
x_jogador = 300
y_jogador = 200
# Criando uma class de player que vai conter as caracteristicas do personagem do jogador
class Player: 
    distancia_movida = 10
    def __init__(self):
        self.imagem = pygame.transform.scale(pygame.image.load('projeto/assets\player-placeholder1.png'), (LARGURA_JOGADOR, ALTURA_JOGADOR))
        self.imagem.fill(Cor.VERMELHO)
        self.hitbox = self.imagem.get_rect(topleft=(x_jogador, y_jogador))
        self.direcao = pygame.math.Vector2()
        self.velocidade = 10
    def input(self):
        # Checa quais as teclas que estão sendo pressionadas e baseado nisso faz o personagem se mover
        teclas = pygame.key.get_pressed()
        # Defini uma vetor que decidira a direção e orientação em que o personagem irá se mover para 'salvar' qual foi a ultima direção em que o personagem se moveu
        if teclas[pygame.K_UP]:
            self.direcao.y = -1
        elif teclas[pygame.K_DOWN]:
            self.direcao.y = 1
        else:
            self.direcao.y = 0
        if teclas[pygame.K_LEFT]:
            self.direcao.x = -1
        elif teclas[pygame.K_RIGHT]:
            self.direcao.x += 1
        else:
            self.direcao.x = 0
    def movimento(self, velocidade):
        global x_jogador, y_jogador
        if self.direcao.magnitude() != 0:
            self.direcao = self.direcao.normalize()
        x_jogador += self.direcao.x * velocidade
        y_jogador += self.direcao.y * self.velocidade
        return x_jogador, y_jogador
    def atualizar(self):
        self.input()
        self.movimento(self.velocidade)
    def checando_colisao(self, mapa):
        colidiu = False
        for tile in mapa.mapa_tiles:
            if tile.tipo == 'parede' and self.hitbox.colliderect(tile.hitbox):
                colidiu = True
        return colidiu
