from graphics import Superficie
from settings import *
import pygame
pygame.init()



# Posição do jogador
x_jogador = 300
y_jogador = 200
# Criando uma class de player que vai conter as caracteristicas do personagem do jogador
class Player: 
    def __init__(self):
        self.imagem = pygame.Surface((LARGURA_JOGADOR, ALTURA_JOGADOR))
        self.imagem.fill(Cor.VERMELHO)
        self.hitbox = self.imagem.get_rect(topleft=(x_jogador, y_jogador))
    def movimento_jogador(evento):
        global x_jogador
        global y_jogador
        # Checa quais as teclas que estão sendo pressionadas e baseado nisso faz o personagem se mover
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:
            y_jogador -= 10
        if teclas[pygame.K_DOWN]:
            y_jogador += 10
        if teclas[pygame.K_LEFT]:
            x_jogador -= 10
        if teclas[pygame.K_RIGHT]:
            x_jogador += 10
        return (x_jogador, y_jogador)