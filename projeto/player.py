from graphics import Superficie
from settings import *
from level import Mapa
import pygame
pygame.init()

# Posição do jogador
# Criando uma class de player que vai conter as caracteristicas do personagem do jogador
class Player: 
    # Caracteristicas do jogador
    pontuacao = 0
    vida = 3
    # Movimento
    x_jogador = 300
    y_jogador = 200
    velocidade = 10
    olhando_direcao = 'baixo'
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
            self.imagem = pygame.image.load('projeto/assets\playerback-placeholder.png')
            self.imagem = pygame.transform.scale(self.imagem, (LARGURA_JOGADOR, ALTURA_JOGADOR))
        elif teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
            self.direcao.y = 1
            self.olhando_direcao = 'baixo'
            self.imagem = pygame.image.load('projeto/assets\playerfront-placeholder.png')
            self.imagem = pygame.transform.scale(self.imagem, (LARGURA_JOGADOR, ALTURA_JOGADOR))
        else:
            self.direcao.y = 0
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            self.direcao.x = -1
            self.olhando_direcao = 'esquerda'
            self.imagem = pygame.image.load('projeto/assets\playerleft-placeholder.png')
            self.imagem = pygame.transform.scale(self.imagem, (LARGURA_JOGADOR, ALTURA_JOGADOR))
        elif teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            self.direcao.x = +1
            self.olhando_direcao = 'direita'
            self.imagem = pygame.image.load('projeto/assets\playerright-placeholder.png')
            self.imagem = pygame.transform.scale(self.imagem, (LARGURA_JOGADOR, ALTURA_JOGADOR))
        else:
            self.direcao.x = 0
        # Caso o jogador pressione espaço ele ataca
        if teclas[pygame.K_SPACE]:
            self.ataque()
    def movimento(self, velocidade, mapa):
        # Impede que o vetor de direção fique com uma resultade maior que 1, senão o jogador conseguiria se mover mais rápido que o normal quando fosse na diagonal 
        if self.direcao.magnitude() != 0:
            self.direcao = self.direcao.normalize()
        # Move as coordenadas do jogador baseado na direção e velocidade
        self.x_jogador += self.direcao.x * velocidade
        self.y_jogador += self.direcao.y * velocidade
        # Atualiza a caixa de colisão para as novas coordenadas
        self.hitbox = self.imagem.get_rect(topleft=(self.x_jogador, self.y_jogador))
        # Vê se após esse movimento o jogador estaria dentro de um obstaculo, caso sim, ele volta. Isso impede que ele atravesse paredes
        if self.colisao_obstaculos(mapa):
            self.x_jogador -= self.direcao.x * velocidade 
            self.y_jogador -= self.direcao.y * velocidade 
    def colisao_obstaculos(self, mapa):
        # Checa se, para todos os obstaculos da fase há ou não colisão com o jogador
        colidiu = False
        for tile in mapa.tipo_tiles['Parede']:
            if self.hitbox.colliderect(tile.hitbox):
                colidiu = True
        return colidiu
    def ataque(self):
        # Checa se o jogador está no intervalo de tempo em que não pode atacar
        if self.pode_atacar:
            # Caso possa atacar ele ataca, mas entra em um intervalo de alguns milisegundos em que ele não pode atacar 
            self.pode_atacar = False
            pygame.time.set_timer(EVENTO_INTERVALO_ATAQUE, INTERVALO_ATAQUE)
            # Checa a ultima direção em que o personagem se moveu para definir onde a caixa de colisão do ataque irá aparecer e rotaciona a imagem do ataque para ficar de acordo
            if self.olhando_direcao == 'direita':
                self.ataque_hitbox = pygame.Rect((self.hitbox.right, self.hitbox.centery - ALTURA_ATAQUE/2), (LARGURA_ATAQUE, ALTURA_ATAQUE))
                im_ataque_direcionado = pygame.transform.flip(Superficie.im_ataque, False, False)
            elif self.olhando_direcao == 'esquerda':
                self.ataque_hitbox = pygame.Rect((self.hitbox.left - LARGURA_ATAQUE, self.hitbox.centery - ALTURA_ATAQUE/2), (LARGURA_ATAQUE, ALTURA_ATAQUE))
                im_ataque_direcionado = pygame.transform.flip(Superficie.im_ataque, True, False)
            elif self.olhando_direcao == 'baixo':
                self.ataque_hitbox = pygame.Rect((self.hitbox.centerx - LARGURA_ATAQUE/2, self.hitbox.bottom), (LARGURA_ATAQUE, ALTURA_ATAQUE))
                im_ataque_direcionado = pygame.transform.rotate(Superficie.im_ataque, 270)
            elif self.olhando_direcao == 'cima':
                self.ataque_hitbox = pygame.Rect((self.hitbox.centerx - LARGURA_ATAQUE/2, self.hitbox.top - ALTURA_ATAQUE), (LARGURA_ATAQUE, ALTURA_ATAQUE))
                im_ataque_direcionado = pygame.transform.rotate(Superficie.im_ataque, 90)
            # Coloca o ataque na tela
            TELA.blit(im_ataque_direcionado, self.ataque_hitbox)
    def morte(self):
        # Se o jogador chegar a 0 de Vida o jogo acaba
        if self.vida <= 0:
            self.morreu = True
    def atualizar(self, mapa):
        self.morte()
        if not self.morreu:
            # Isso vai atualizar o jogador, vendo se o ele fez algum input, sofreu dano, se movimentou ou atacou, e após isso tudo, coloca sua superficies na tela
            self.ataque_hitbox = pygame.Rect((0,0), (0,0))
            self.hitbox = self.imagem.get_rect(topleft=(self.x_jogador, self.y_jogador))
            TELA.blit(self.imagem, self.hitbox)
            self.movimento(self.velocidade, mapa)
            self.input()
        else:
            # Se o personagem morrer ele não aparece na tela porque ele morreu :(
            self.ataque_hitbox = pygame.Rect((0,0), (0,0))
            self.hitbox = self.imagem.get_rect(topleft=(0, 0))
        
        
