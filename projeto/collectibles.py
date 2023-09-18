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
        self.hitbox = self.shield.get_rect(topleft=(200, 200))
        self.coletado = False

    def coletar(self, jogador):
        if self.hitbox.colliderect(jogador.hitbox):
            self.hitbox = pygame.Rect((0,0), (0,0))
            self.coletado = True
            jogador.vida += 1
