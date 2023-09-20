from settings import *
import pygame

pygame.init()

class Coletaveis:
    lista_coletaveis = []
    def __init__(self, posicao, tipo):
        if tipo == 'espada':
            self.tipo = 'espada'
            self.imagem = pygame.image.load('projeto/assets/espada.png') 
            self.imagem = pygame.transform.scale(self.imagem, (25, 50))
        elif tipo == 'escudo':
            self.tipo = 'escudo'
            self.imagem = pygame.image.load('projeto/assets/escudo.png')
            self.imagem = pygame.transform.scale(self.imagem, (80,50))
        self.hitbox = self.imagem.get_rect(topleft=(posicao))
        self.coletado = False

    def coletar(self, jogador):
        if self.hitbox.colliderect(jogador.hitbox):
            self.hitbox = pygame.Rect((0,0), (0,0))
            self.coletado = True
            Coletaveis.lista_coletaveis.remove(self)
            if self.tipo == 'espada':
                jogador.nivel_espada += 1
            elif self.tipo == 'escudo':
                jogador.vida += 1
            
class Portal:
    tamanho_porta = TAMANHO_TILE * 1.5
    def __init__(self):
        self.imagem = pygame.image.load('projeto/assets/porta.png')
        self.imagem = pygame.transform.scale(self.imagem, (self.tamanho_porta, self.tamanho_porta))
        self.hitbox = self.imagem.get_rect(topleft=((LARGURA_TELA- self.tamanho_porta)/2, (ALTURA_TELA - self.tamanho_porta)/2))
        self.coletado = False
