from settings import *
from audiovisual import Audios
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
        self.idx_animacao = 0
        self.contador_animacao = 0
        # sprites do jogador
        self.imagem = {
            'baixo': [pygame.transform.scale(pygame.image.load('projeto/assets\sprites_folder\sprites_player/playerfront-placeholder.png'), (LARGURA_JOGADOR, ALTURA_JOGADOR)).convert_alpha(), pygame.transform.scale(pygame.image.load('projeto/assets\sprites_folder\sprites_player\playerfront-placeholder2.png'), (LARGURA_JOGADOR, ALTURA_JOGADOR)).convert_alpha()],
            'cima': [pygame.transform.scale(pygame.image.load('projeto/assets\sprites_folder\sprites_player/playerback-placeholder.png'), (LARGURA_JOGADOR, ALTURA_JOGADOR)).convert_alpha(), pygame.transform.scale(pygame.image.load('projeto/assets\sprites_folder\sprites_player\playerback-placeholder2.png'), (LARGURA_JOGADOR, ALTURA_JOGADOR)).convert_alpha()],
            'direita': [pygame.transform.scale(pygame.image.load('projeto/assets\sprites_folder\sprites_player/playerright-placeholder.png'), (LARGURA_JOGADOR, ALTURA_JOGADOR)).convert_alpha(), pygame.transform.scale(pygame.image.load('projeto/assets\sprites_folder\sprites_player\playerright-placeholder2.png'), (LARGURA_JOGADOR, ALTURA_JOGADOR)).convert_alpha()],
            'esquerda': [pygame.transform.scale(pygame.image.load('projeto/assets\sprites_folder\sprites_player/playerleft-placeholder.png'), (LARGURA_JOGADOR, ALTURA_JOGADOR)).convert_alpha(), pygame.transform.scale(pygame.image.load('projeto/assets\sprites_folder\sprites_player\playerleft-placeholder2.png'), (LARGURA_JOGADOR, ALTURA_JOGADOR)).convert_alpha()]
        }
        self.sup_ataque = {
            'False': pygame.image.load('projeto/assets/sprites_folder\sprites_player/ataque-placeholder.png').convert_alpha(),
            'True': pygame.image.load('projeto/assets/sprites_folder\sprites_player/ataque-maior-placeholder.png').convert_alpha()
        }
        self.hitbox = self.imagem[self.olhando_direcao][self.idx_animacao].get_rect(topleft=(self.x_jogador, self.y_jogador))
        self.largura_ataque, self.altura_ataque = TAMANHO_TILE * 1.5, TAMANHO_TILE * 1.5
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
        self.andando_intervalo = 10
        self.espada = False
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
        # Caso o jogador pressione espaço ele ataca
        # Quando o jogador pressionar o espaço, agora tem o som :)
        if teclas[pygame.K_SPACE]:
            self.ataque()

    def movimento(self, velocidade, mapa):
        # Animações de andar
        if self.andando:
            self.contador_animacao += 1
        else:
            self.contador_animacao = 0
            self.idx_animacao = 0
        if self.contador_animacao > self.andando_intervalo:
            self.contador_animacao = 0
            self.idx_animacao += 1
            if self.idx_animacao >= 2:
                self.idx_animacao = 0
        # Impede que o vetor de direção fique com uma resultade maior que 1, senão o jogador conseguiria se mover mais rápido que o normal quando fosse na diagonal 
        if self.direcao.magnitude() != 0:
            self.direcao = self.direcao.normalize()
            self.andando = True
        else:
            self.andando = False
        # Move as coordenadas do jogador baseado na direção e velocidade
        self.x_jogador += self.direcao.x * velocidade
        self.hitbox = self.imagem[self.olhando_direcao][self.idx_animacao].get_rect(topleft=(self.x_jogador, self.y_jogador))
        if self.colisao_obstaculos(mapa):
            self.x_jogador -= self.direcao.x * velocidade 
        self.y_jogador += self.direcao.y * velocidade
        if self.colisao_obstaculos(mapa):
            self.y_jogador -= self.direcao.y * velocidade 
        # Vê se após esse movimento o jogador estaria dentro de um obstaculo, caso sim, ele volta. Isso impede que ele atravesse paredes
            
    def colisao_obstaculos(self, mapa):
        # Checa se, para todos os obstaculos da fase há ou não colisão com o jogador
        # Atualiza a caixa de colisão para as novas coordenadas
        self.hitbox = self.imagem[self.olhando_direcao][self.idx_animacao].get_rect(topleft=(self.x_jogador, self.y_jogador))
        colidiu = False
        for tile in mapa.tipo_tiles['Parede']:
            if self.hitbox.colliderect(tile.hitbox):
                colidiu = True
        return colidiu
    def ataque(self):
        # Checa se o jogador está no intervalo de tempo em que não pode atacar
        if self.pode_atacar:
            im_ataque = pygame.transform.scale(self.sup_ataque[str(self.espada)], (self.largura_ataque, self.altura_ataque))
            # Caso possa atacar ele ataca, mas entra em um intervalo de alguns milisegundos em que ele não pode atacar 
            self.pode_atacar = False
            if not Audios.audio_playing:
                if not self.espada:
                    Audios.ataque_sem_espada.play()
                else:
                    Audios.ataque_espada.play()
                Audios.audio_playing = True
            pygame.time.set_timer(EVENTO_INTERVALO_ATAQUE, INTERVALO_ATAQUE)
            # Checa a ultima direção em que o personagem se moveu para definir onde a caixa de colisão do ataque irá aparecer e rotaciona a imagem do ataque para ficar de acordo
            if self.olhando_direcao == 'direita':
                self.ataque_hitbox = pygame.Rect((self.hitbox.right, self.hitbox.centery - self.altura_ataque/2), (self.largura_ataque, self.altura_ataque))
                self.im_ataque = pygame.transform.flip(im_ataque, False, False)
            elif self.olhando_direcao == 'esquerda':
                self.ataque_hitbox = pygame.Rect((self.hitbox.left - self.largura_ataque, self.hitbox.centery - self.altura_ataque/2), (self.largura_ataque, self.altura_ataque))
                self.im_ataque = pygame.transform.flip(im_ataque, True, False)
            elif self.olhando_direcao == 'baixo':
                self.ataque_hitbox = pygame.Rect((self.hitbox.centerx - self.largura_ataque/2, self.hitbox.bottom), (self.largura_ataque, self.altura_ataque))
                self.im_ataque = pygame.transform.rotate(im_ataque, 270)
            elif self.olhando_direcao == 'cima':
                self.ataque_hitbox = pygame.Rect((self.hitbox.centerx - self.largura_ataque/2, self.hitbox.top - self.altura_ataque), (self.largura_ataque, self.altura_ataque))
                self.im_ataque = pygame.transform.rotate(im_ataque, 90)
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
            self.hitbox = self.imagem[self.olhando_direcao][self.idx_animacao].get_rect(topleft=(self.x_jogador, self.y_jogador))
            # Efeito de piscar caso o personagem sofra dano
            if self.sofreu_dano and self.alfa == 255:
                self.alfa = 55
            elif self.alfa < 255:
                self.alfa = 255
            self.imagem[self.olhando_direcao][self.idx_animacao].set_alpha(self.alfa)
            TELA.blit(self.imagem[self.olhando_direcao][self.idx_animacao], self.hitbox)
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
        
        
