# Caracteristicas da programação dos inimigos
from settings import *
import pygame
import random
pygame.init()

class Enemy:
    def __init__(self, mapa):
        # Caracteristicas do jogador
        self.vida = VIDA_INIMIGO 
        self.imagem = pygame.Surface((LARGURA_INIMIGO, ALTURA_INIMIGO)) 
        self.imagem.fill('Red')
        # Já nasce em um lugar aleatorio que não seja um obstaculo
        local_spawn = mapa.tipo_tiles['Chão'][random.randint(0, len(mapa.tipo_tiles['Chão']) - 1)].hitbox
        self.y, self.x = local_spawn.top, local_spawn.left
        self.velocidade = 5
        self.hitbox = self.imagem.get_rect(topleft=(self.x, self.y)) 
    def acertado_por_ataque(self, jogador):
        # Checa se a caixa de colisão do ataque do jogador encostou nele e faz o inimgo sofrer dano. 
        if jogador.ataque_hitbox.colliderect(self.hitbox):
            self.vida -= 1
    def causou_dano(self, jogador):
        # Checa se o inimigo encostou no jogador e faz o jogador sofrer dano
        if self.hitbox.colliderect(jogador.hitbox) and not jogador.sofreu_dano:
            jogador.sofreu_dano = True
            # Após sofrer dano o jogador se torna invulneravel por alguns segundos
            pygame.time.set_timer(EVENTO_INTERVALO_DANO, INTERVALO_DANO)
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
        # Vê se após esse movimento o inimigo estaria dentro de um obstaculo, caso sim, ele volta. Isso impede que ele atravesse paredes
        if self.colisao_obstaculos(mapa):
            self.x -= direcao_x * self.velocidade 
            self.y -= direcao_y * self.velocidade 
    def renascer(self, mapa): 
        self.vida = VIDA_INIMIGO
        # Renasce em um lugar aleatorio do mapa que não seja um obstaculo
        local_spawn = mapa.tipo_tiles['Chão'][random.randint(0, len(mapa.tipo_tiles['Chão']) - 1)].hitbox
        self.y, self.x = local_spawn.top, local_spawn.left
        # Quando renascer o hitbox vai ficar no lugar certo 
        self.hitbox = self.imagem.get_rect(topleft=(self.x, self.y)) 
    def colisao_obstaculos(self, mapa):
        # Checa se, para todos os obstaculos da fase há ou não colisão com o jogador
        colidiu = False
        for tile in mapa.tipo_tiles['Parede']:
            if self.hitbox.colliderect(tile.hitbox):
                colidiu = True
        return colidiu
    def atualizar(self, jogador, mapa): 
        # Isso vai atualizar o inimigo, checando se ele sofreu um ataque do jogador ou causou dano no mesmo, e após isso coloca sua superficie na tela
        self.causou_dano(jogador)
        self.hitbox = self.imagem.get_rect(topleft=(self.x, self.y))
        TELA.blit(self.imagem, self.hitbox)
        self.acertado_por_ataque(jogador) 
        # Se o inimigo estiver morto ele renasce e aumenta a pontuação do jogador
        if self.vida <= 0: 
            self.renascer(mapa) 
            jogador.pontuacao += 1
        # Caso contrario ele segue o jogador
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