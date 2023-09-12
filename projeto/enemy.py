# Caracteristicas da programação dos inimigos
from settings import *
import pygame
pygame.init()

class Enemy:
    def __init__(self):
        self.vida = 3
        self.imagem = pygame.Surface((TAMANHO_TILE, TAMANHO_TILE))
        self.imagem.fill(Cor.VERMELHO)
        self.hitbox = self.imagem.get_rect(topleft=(100, 100))
    def atualizar(self, jogador):
        self.acertado_ataque(jogador)
        TELA.blit(self.imagem, self.hitbox)
    def acertado_ataque(self, jogador):
        if jogador.ataque_hitbox.colliderect(self.hitbox):
            self.vida -= 1
            if self.vida < 0:
                self.hitbox == pygame.Rect((0,0), (0,0))
        return jogador.ataque_hitbox.colliderect(self.hitbox)
        