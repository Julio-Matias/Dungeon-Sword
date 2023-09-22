from graphics import Superficie
from settings import *
from audios import Audios
import pygame
pygame.init()

# Posição do jogador
# Criando uma class de player que vai conter as caracteristicas do personagem do jogador
class Player: 
    # Constantes do jogador
    velocidade = 7.5
    def __init__(self):
        # Caracteristicas iniciais do jogador
        self.pontuacao = 0
        self.vida = 3
        # Posição e movimento inicial do jogador
        self.x_jogador = (LARGURA_TELA - LARGURA_JOGADOR)/2
        self.y_jogador = (ALTURA_TELA - ALTURA_JOGADOR)/2
        self.direcao = pygame.math.Vector2()
        self.olhando_direcao = 'baixo'
        # sprite inicial do jogador
        self.imagem = pygame.image.load('projeto/assets\playerfront-placeholder.png')
        self.imagem = pygame.transform.scale(self.imagem, (LARGURA_JOGADOR, ALTURA_JOGADOR))
        self.hitbox = self.imagem.get_rect(topleft=(self.x_jogador, self.y_jogador))
        self.ataque_hitbox = pygame.Rect((0,0), (0,0))
        # transparencia inicial
        self.alfa = 255
        self.ataque_alfa = 255
        self.nivel_espada = 0
        # Outros
        self.pode_atacar = True
        self.sofreu_dano = False
        self.morreu = False
        self.andando = False
        
    def input(self):
        # Checa quais as teclas que estão sendo pressionadas e baseado nisso faz o personagem se mover
        teclas = pygame.key.get_pressed()
        # Defini uma vetor que decidira a direção e orientação em que o personagem irá se mover para 'salvar' qual foi a ultima direção em que o personagem se moveu
        if teclas[pygame.K_w] or teclas[pygame.K_UP]:
            self.direcao.y = -1
            self.olhando_direcao = 'cima'
            self.imagem = pygame.image.load('projeto/assets\playerback-placeholder.png')
            self.imagem = pygame.transform.scale(self.imagem, (LARGURA_JOGADOR, ALTURA_JOGADOR))
            self.andando = True
            
        elif teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
            self.direcao.y = 1
            self.olhando_direcao = 'baixo'
            self.imagem = pygame.image.load('projeto/assets\playerfront-placeholder.png')
            self.imagem = pygame.transform.scale(self.imagem, (LARGURA_JOGADOR, ALTURA_JOGADOR))
            self.andando = True
            
        else:
            self.direcao.y = 0
            self.andando = False
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            self.direcao.x = -1
            self.olhando_direcao = 'esquerda'
            self.imagem = pygame.image.load('projeto/assets\playerleft-placeholder.png')
            self.imagem = pygame.transform.scale(self.imagem, (LARGURA_JOGADOR, ALTURA_JOGADOR))
            self.andando = True
            
        elif teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            self.direcao.x = +1
            self.olhando_direcao = 'direita'
            self.imagem = pygame.image.load('projeto/assets\playerright-placeholder.png')
            self.imagem = pygame.transform.scale(self.imagem, (LARGURA_JOGADOR, ALTURA_JOGADOR))
            self.andando = True
            
        else:
            self.direcao.x = 0
            self.andando = False
        # Caso o jogador pressione espaço ele ataca
        # Quando o jogador pressionar o espaço, agora tem o som :)
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
            if not Audios.audio_playing:
                Audios.ataque_sem_espada.play()
                Audios.audio_playing = True
            pygame.time.set_timer(EVENTO_INTERVALO_ATAQUE, self.intervalo_ataque)
            # Checa a ultima direção em que o personagem se moveu para definir onde a caixa de colisão do ataque irá aparecer e rotaciona a imagem do ataque para ficar de acordo
            if self.olhando_direcao == 'direita':
                self.ataque_hitbox = pygame.Rect((self.hitbox.right, self.hitbox.centery - ALTURA_ATAQUE/2), (LARGURA_ATAQUE, ALTURA_ATAQUE))
                self.im_ataque = pygame.transform.flip(Superficie.im_ataque, False, False)
            elif self.olhando_direcao == 'esquerda':
                self.ataque_hitbox = pygame.Rect((self.hitbox.left - LARGURA_ATAQUE, self.hitbox.centery - ALTURA_ATAQUE/2), (LARGURA_ATAQUE, ALTURA_ATAQUE))
                self.im_ataque = pygame.transform.flip(Superficie.im_ataque, True, False)
            elif self.olhando_direcao == 'baixo':
                self.ataque_hitbox = pygame.Rect((self.hitbox.centerx - LARGURA_ATAQUE/2, self.hitbox.bottom), (LARGURA_ATAQUE, ALTURA_ATAQUE))
                self.im_ataque = pygame.transform.rotate(Superficie.im_ataque, 270)
            elif self.olhando_direcao == 'cima':
                self.ataque_hitbox = pygame.Rect((self.hitbox.centerx - LARGURA_ATAQUE/2, self.hitbox.top - ALTURA_ATAQUE), (LARGURA_ATAQUE, ALTURA_ATAQUE))
                self.im_ataque = pygame.transform.rotate(Superficie.im_ataque, 90)
        else:
            Audios.audio_playing = False
    def morte(self):
        # Se o jogador chegar a 0 de Vida o jogo acaba
        if self.vida <= 0:
            self.morreu = True
    def atualizar(self, mapa):
        self.morte()
        if not self.morreu:
            # Isso vai atualizar o jogador, vendo se o ele fez algum input, sofreu dano, se movimentou ou atacou, e após isso tudo, coloca sua superficies na tela
            self.hitbox = self.imagem.get_rect(topleft=(self.x_jogador, self.y_jogador))
            if self.nivel_espada < 5:
                self.intervalo_ataque = 500 - self.nivel_espada * 50
            else:
                self.intervalo_ataque = 250
            # Efeito de piscar caso o personagem sofra dano
            if self.sofreu_dano and self.alfa == 255:
                self.alfa = 100
                self.imagem.set_alpha(self.alfa)
            elif self.alfa < 255:
                self.alfa = 255
                self.imagem.set_alpha(self.alfa)
            TELA.blit(self.imagem, self.hitbox)
            # Coloca o ataque na tela
            if not self.pode_atacar:
                if 0 < self.ataque_alfa:
                    TELA.blit(self.im_ataque, self.ataque_hitbox)
                    self.ataque_alfa -= 85
                    self.im_ataque.set_alpha(self.ataque_alfa)
                else:
                    self.ataque_hitbox = pygame.Rect((0,0), (0,0))
            if self.pode_atacar:
                self.ataque_alfa = 255
            self.input()
            self.movimento(self.velocidade, mapa)
        else:
            # Se o personagem morrer ele não aparece na tela porque ele morreu :(
            self.hitbox = pygame.Rect((0,0), (0,0))
        
        
