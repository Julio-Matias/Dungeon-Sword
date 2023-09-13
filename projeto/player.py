from graphics import Superficie
from settings import *
from level import Mapa
import pygame
pygame.init()

# Posição do jogador
# Criando uma class de player que vai conter as caracteristicas do personagem do jogador
class Player: 
    pontuacao = 0
    vida = 3
    x_jogador = 300
    y_jogador = 200
    velocidade = 10
    olhando_direcao = 'baixo'
    intervalo_ataque = 500
    evento_intervalo_ataque = pygame.USEREVENT + 1
    pisca = False
    def __init__(self):
        self.imagem = pygame.image.load('projeto/assets\playerfront-placeholder.png')
        self.hitbox = self.imagem.get_rect(topleft=(self.x_jogador, self.y_jogador))
        self.imagem = pygame.transform.scale(self.imagem, (LARGURA_JOGADOR, ALTURA_JOGADOR))
        self.direcao = pygame.math.Vector2()
        self.ataque_hitbox = pygame.Rect((0,0), (0,0))
        self.pode_atacar = True
        self.sofreu_dano = False
        self.morreu = False
    def input(self):
        # Checa quais as teclas que estão sendo pressionadas e baseado nisso faz o personagem se mover
        teclas = pygame.key.get_pressed()
        # Defini uma vetor que decidira a direção e orientação em que o personagem irá se mover para 'salvar' qual foi a ultima direção em que o personagem se moveu
        if teclas[pygame.K_w] or teclas[pygame.K_UP]:
            self.direcao.y = -1
            self.olhando_direcao = 'cima'
        elif teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
            self.direcao.y = 1
            self.olhando_direcao = 'baixo'
        else:
            self.direcao.y = 0
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            self.direcao.x = -1
            self.olhando_direcao = 'esquerda'
        elif teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            self.direcao.x = +1
            self.olhando_direcao = 'direita'
        else:
            self.direcao.x = 0
        if teclas[pygame.K_SPACE]:
            self.ataque()
    def movimento(self, velocidade, mapa):
        if self.direcao.magnitude() != 0:
            self.direcao = self.direcao.normalize()
        self.x_jogador += self.direcao.x * velocidade
        self.y_jogador += self.direcao.y * velocidade
        self.hitbox = self.imagem.get_rect(topleft=(self.x_jogador, self.y_jogador))
        if self.colisao_obstaculos(mapa):
            self.x_jogador -= self.direcao.x * velocidade 
            self.y_jogador -= self.direcao.y * velocidade 
    def colisao_obstaculos(self, mapa):
        colidiu = False
        for tile in mapa.tipo_tiles['Parede']:
            if self.hitbox.colliderect(tile.hitbox):
                colidiu = True
        return colidiu
    def ataque(self):
        if self.pode_atacar:
            self.pode_atacar = False
            largura_ataque, altura_ataque = TAMANHO_TILE*2, TAMANHO_TILE*2
            pygame.time.set_timer(self.evento_intervalo_ataque, self.intervalo_ataque)
            if self.olhando_direcao == 'direita':
                self.ataque_hitbox = pygame.Rect((self.hitbox.right, self.hitbox.centery - altura_ataque/2), (largura_ataque, altura_ataque))
                pygame.draw.rect(TELA, 'White', self.ataque_hitbox)
            elif self.olhando_direcao == 'esquerda':
                self.ataque_hitbox = pygame.Rect((self.hitbox.left - largura_ataque, self.hitbox.centery - altura_ataque/2), (largura_ataque, altura_ataque))
                pygame.draw.rect(TELA, 'White', self.ataque_hitbox)
            elif self.olhando_direcao == 'baixo':
                self.ataque_hitbox = pygame.Rect((self.hitbox.centerx - largura_ataque/2, self.hitbox.bottom), (largura_ataque, altura_ataque))
                pygame.draw.rect(TELA, 'White', self.ataque_hitbox)
            elif self.olhando_direcao == 'cima':
                self.ataque_hitbox = pygame.Rect((self.hitbox.centerx - largura_ataque/2, self.hitbox.top - altura_ataque), (largura_ataque, altura_ataque))
                pygame.draw.rect(TELA, 'White', self.ataque_hitbox)
    def morte(self):
        if self.vida <= 0:
            self.morreu = True
    def atualizar(self, mapa):
        self.morte()
        if not self.morreu:
            self.ataque_hitbox = pygame.Rect((0,0), (0,0))
            self.hitbox = self.imagem.get_rect(topleft=(self.x_jogador, self.y_jogador))
            TELA.blit(self.imagem, self.hitbox)
            self.movimento(self.velocidade, mapa)
            self.input()
        else:
            self.ataque_hitbox = pygame.Rect((0,0), (0,0))
            self.hitbox = self.imagem.get_rect(topleft=(0, 0))
        
        
