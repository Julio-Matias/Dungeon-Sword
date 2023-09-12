# Caracteristicas da programação dos inimigos
from settings import *
import pygame
import random
from level import Mapa 
pygame.init()

class Enemy:
    def __init__(self):
        self.vida = 3 
        self.imagem = pygame.Surface((TAMANHO_TILE, TAMANHO_TILE)) 
        self.imagem.fill(Cor.VERMELHO) 
        # Já nasce em um lugar aleatorio
        self.x = random.randint(0, LARGURA_TELA - TAMANHO_TILE) 
        self.y = random.randint(0, ALTURA_TELA - TAMANHO_TILE) 
        self.velocidade = 1 
        self.hitbox = self.imagem.get_rect(topleft=(self.x, self.y)) 
    def acertado_ataque(self, jogador):
        if jogador.ataque_hitbox.colliderect(self.hitbox):
            self.vida -= 1
            if self.vida < 0:
                self.hitbox == pygame.Rect((0,0), (0,0))
        return jogador.ataque_hitbox.colliderect(self.hitbox)
    def seguir_jogador(self, jogador, Mapa): 
        self.velocidade = 1 
        # Faz o calculo da direção do inimigo pro player
        direcao_x = jogador.x_jogador - self.x 
        direcao_y = jogador.y_jogador - self.y 
        # Faz o calculo do vetor 
        comprimento = pygame.math.Vector2(direcao_x, direcao_y).length() 
        # Normaliza a direção e faz o inimigo se mexer em uma constante 
        if comprimento != 0:
            direcao_x /= comprimento 
            direcao_y /= comprimento 
        # Vai atualizando as posições 
        self.x += direcao_x * self.velocidade 
        self.y += direcao_y * self.velocidade 
        # Muda a posição do hitbox pra ficar onde o inimigo vai estar 
        self.hitbox = self.imagem.get_rect(topleft=(self.x, self.y)) 
    def renascer(self): 
        self.vida = 3 
        # Renasce em um lugar aleatorio do mapa (falta ele determinar oq é e n é parede) 
        self.x = random.randint(0, LARGURA_TELA - TAMANHO_TILE) 
        self.y = random.randint(0, ALTURA_TELA - TAMANHO_TILE)
        # Quando renascer o hitbox vai ficar no lugar certo 
        self.hitbox = self.imagem.get_rect(topleft=(self.x, self.y)) 
    def atualizar(self, jogador): 
        self.acertado_ataque(jogador) 
        if self.vida <= 0: 
            self.renascer() 
        else: 
            self.seguir_jogador(jogador, Mapa) 
        TELA.blit(self.imagem, self.hitbox)
        
"""# Caracteristicas da programação dos inimigos
from settings import * 
import pygame 
import random 
from level import Mapa 
pygame.init() 
class Enemy: 
    def _init_(self): 
        self.vida = 3 
        self.imagem = pygame.Surface((TAMANHO_TILE, TAMANHO_TILE)) 
        self.imagem.fill(Cor.VERMELHO) 
        # Já nasce em um lugar aleatorio
        self.x = random.randint(0, LARGURA_TELA - TAMANHO_TILE) 
        self.y = random.randint(0, ALTURA_TELA - TAMANHO_TILE) 
        self.velocidade = 1 
        self.hitbox = self.imagem.get_rect(topleft=(self.x, self.y)) 
    def atualizar(self, jogador): 
        self.acertado_ataque(jogador) 
        TELA.blit(self.imagem, self.hitbox) 
    def acertado_ataque(self, jogador): 
        
        if jogador.ataque_hitbox.colliderect(self.hitbox): 
            self.vida -= 1 
            if self.vida < 0: 
                self.hitbox == pygame.Rect((0,0), (0,0)) 
        return jogador.ataque_hitbox.colliderect(self.hitbox) 
    def seguir_jogador(self, jogador, mapa): 
        self.velocidade = 1 
        # Faz o calculo da direção do inimigo pro player
        direcao_x = jogador.x_jogador - self.x 
        direcao_y = jogador.y_jogador - self.y 
        # Faz o calculo do vetor 
        comprimento = pygame.math.Vector2(direcao_x, direcao_y).length() 
        # Normaliza a direção e faz o inimigo se mexer em uma constante 
        if comprimento != 0:
            direcao_x /= comprimento 
            direcao_y /= comprimento 
        # Vai atualizando as posições 
        self.x += direcao_x * self.velocidade 
        self.y += direcao_y * self.velocidade 
        # Muda a posição do hitbox pra ficar onde o inimigo vai estar 
        self.hitbox = self.imagem.get_rect(topleft=(self.x, self.y)) 
    def renascer(self): 
        self.vida = 3 
        # Renasce em um lugar aleatorio do mapa (falta ele determinar oq é e n é parede) 
        self.x = random.randint(0, LARGURA_TELA - TAMANHO_TILE) 
        self.y = random.randint(0, ALTURA_TELA - TAMANHO_TILE)
        # Quando renascer o hitbox vai ficar no lugar certo 
        self.hitbox = self.imagem.get_rect(topleft=(self.x, self.y)) 
    def atualizar(self, jogador): 
        self.acertado_ataque(jogador) 
        if self.vida <= 0: 
            self.renascer() 
        else: 
            self.seguir_jogador(jogador, Mapa) 
        TELA.blit(self.imagem, self.hitbox)"""