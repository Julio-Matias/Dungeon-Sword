# Caracteristicas da programação dos inimigos
from settings import *
import pygame
pygame.init()

class Enemy:
    def __init__(self):
        self.imagem = pygame.Surface((TAMANHO_TILE, TAMANHO_TILE))
        self.imagem.fill(Cor.BRANCO)
        self.hitbox = self.imagem.get_rect(topleft=(100, 100))