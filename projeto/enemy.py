# Caracteristicas da programação dos inimigos
from settings import *
import pygame
import random
pygame.init()

class Enemy:
    evento_intervalo_dano = pygame.USEREVENT + 2
    intervalo_dano = 2000
    def __init__(self, mapa):
        self.vida = 1 
        self.imagem = pygame.Surface((TAMANHO_TILE, TAMANHO_TILE)) 
        self.imagem.fill(Cor.VERMELHO)
        self.levou_ataque = False 
        # Já nasce em um lugar aleatorio
        local_spawn = mapa.tipo_tiles['Chão'][random.randint(0, len(mapa.tipo_tiles['Chão']) - 1)].hitbox
        self.y, self.x = local_spawn.top, local_spawn.left
        self.velocidade = 5
        self.hitbox = self.imagem.get_rect(topleft=(self.x, self.y)) 
    def acertado_ataque(self, jogador):
        if jogador.ataque_hitbox.colliderect(self.hitbox) and not self.levou_ataque:
            self.vida -= 1
            self.levou_ataque = True
            if self.vida < 0:
                self.hitbox == pygame.Rect((0,0), (0,0))
        elif not jogador.ataque_hitbox.colliderect(self.hitbox):
            self.levou_ataque = False
    def causou_dano(self, jogador):
        if self.hitbox.colliderect(jogador.hitbox) and not jogador.sofreu_dano:
            jogador.sofreu_dano = True
            pygame.time.set_timer(self.evento_intervalo_dano, self.intervalo_dano)
            jogador.vida -= 1
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
        if self.colisao_obstaculos(mapa):
            self.x -= direcao_x * self.velocidade 
            self.y -= direcao_y * self.velocidade 
    def renascer(self, mapa): 
        self.vida = 1 
        # Renasce em um lugar aleatorio do mapa
        local_spawn = mapa.tipo_tiles['Chão'][random.randint(0, len(mapa.tipo_tiles['Chão']) - 1)].hitbox
        self.y, self.x = local_spawn.top, local_spawn.left
        # Quando renascer o hitbox vai ficar no lugar certo 
        self.hitbox = self.imagem.get_rect(topleft=(self.x, self.y)) 
        # Certificando que o inimigo não vai renascer dentro de uma parede
    def colisao_obstaculos(self, mapa):
        colidiu = False
        for tile in mapa.tipo_tiles['Parede']:
            if self.hitbox.colliderect(tile.hitbox):
                colidiu = True
        return colidiu
    def atualizar(self, jogador, mapa): 
        self.causou_dano(jogador)
        self.hitbox = self.imagem.get_rect(topleft=(self.x, self.y))
        TELA.blit(self.imagem, self.hitbox)
        self.acertado_ataque(jogador) 
        if self.vida <= 0: 
            self.renascer(mapa) 
            jogador.pontuacao += 100
        else: 
            self.seguir_jogador(jogador, mapa) 
        
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