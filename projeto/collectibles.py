from settings import *
import pygame

pygame.init()

class Espada:
    def __init__(self):
        self.sword = pygame.image.load('projeto/assets/espada.png') 
        self.sword = pygame.transform.scale(self.sword, (25, 50))
        self.hitbox = self.sword.get_rect(topleft=(900, 100))
        self.coletado = False

    def coletar(self, jogador):
        if self.hitbox.colliderect(jogador.hitbox):
            self.hitbox = pygame.Rect((0,0), (0,0))
            self.coletado = True
            jogador.dano += 1
class Escudo:

    def __init__(self):
        self.shield = pygame.image.load('projeto/assets/escudo.png')
        self.shield = pygame.transform.scale(self.shield, (80,50))
        self.hitbox = self.shield.get_rect(topleft=(150, 200))
        self.coletado = False

    def coletar(self, jogador):
        if self.hitbox.colliderect(jogador.hitbox):
            self.hitbox = pygame.Rect((0,0), (0,0))
            self.coletado = True
            jogador.vida += 1
class Portal:
    tamanho_porta = TAMANHO_TILE * 1.5
    def __init__(self):
        self.imagem = pygame.image.load('projeto/assets/porta.png')
        self.imagem = pygame.transform.scale(self.imagem, (self.tamanho_porta, self.tamanho_porta))
        self.hitbox = self.imagem.get_rect(topleft=((LARGURA_TELA- self.tamanho_porta)/2, (ALTURA_TELA - self.tamanho_porta)/2))
        self.coletado = False
