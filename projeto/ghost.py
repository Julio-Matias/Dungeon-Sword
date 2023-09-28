# Caracteristicas da programação dos inimigos
from settings import *
import pygame
import random
from collectibles import Coletaveis
from audiovisual import Audios
pygame.init()

class Enemy:
    onda = 50
    lista_inimigos_presentes = []
    lista_slime = {"animation": {
    "00": pygame.transform.scale(pygame.image.load("projeto/sprites_folder/ghost_00.png"),(LARGURA_INIMIGO,ALTURA_INIMIGO)).convert_alpha(),
    "01": pygame.transform.scale(pygame.image.load("projeto/sprites_folder/ghost_01.png"),(LARGURA_INIMIGO,ALTURA_INIMIGO)).convert_alpha(),
    "02": pygame.transform.scale(pygame.image.load("projeto/sprites_folder/ghost_02.png"),(LARGURA_INIMIGO,ALTURA_INIMIGO)).convert_alpha(),
    "03": pygame.transform.scale(pygame.image.load("projeto/sprites_folder/ghost_03.png"),(LARGURA_INIMIGO,ALTURA_INIMIGO)).convert_alpha(),
    "04": pygame.transform.scale(pygame.image.load("projeto/sprites_folder/ghost_04.png"),(LARGURA_INIMIGO,ALTURA_INIMIGO)).convert_alpha(),
    "05": pygame.transform.scale(pygame.image.load("projeto/sprites_folder/ghost_05.png"),(LARGURA_INIMIGO,ALTURA_INIMIGO)).convert_alpha(),
    "06": pygame.transform.scale(pygame.image.load("projeto/sprites_folder/ghost_06.png"),(LARGURA_INIMIGO,ALTURA_INIMIGO)).convert_alpha(),
    "07": pygame.transform.scale(pygame.image.load("projeto/sprites_folder/ghost_07.png"),(LARGURA_INIMIGO,ALTURA_INIMIGO)).convert_alpha(),
    "08": pygame.transform.scale(pygame.image.load("projeto/sprites_folder/ghost_08.png"),(LARGURA_INIMIGO,ALTURA_INIMIGO)).convert_alpha(),
    "09": pygame.transform.scale(pygame.image.load("projeto/sprites_folder/ghost_09.png"),(LARGURA_INIMIGO,ALTURA_INIMIGO)).convert_alpha(),
    "10": pygame.transform.scale(pygame.image.load("projeto/sprites_folder/ghost_10.png"),(LARGURA_INIMIGO,ALTURA_INIMIGO)).convert_alpha(),
    "11": pygame.transform.scale(pygame.image.load("projeto/sprites_folder/ghost_11.png"),(LARGURA_INIMIGO,ALTURA_INIMIGO)).convert_alpha(),
    "12": pygame.transform.scale(pygame.image.load("projeto/sprites_folder/ghost_12.png"),(LARGURA_INIMIGO,ALTURA_INIMIGO)).convert_alpha(),
    "13": pygame.transform.scale(pygame.image.load("projeto/sprites_folder/ghost_13.png"),(LARGURA_INIMIGO,ALTURA_INIMIGO)).convert_alpha(),
    "14": pygame.transform.scale(pygame.image.load("projeto/sprites_folder/ghost_14.png"),(LARGURA_INIMIGO,ALTURA_INIMIGO)).convert_alpha()
    }}
    def __init__(self, mapa):
        # Caracteristicas do inimigo
        self.vida = VIDA_INIMIGO 
        self.alfa = 255
        self.animation_frames = Enemy.lista_slime["animation"]
        self.current_frame = "00"  # Comece com o primeiro quadro
        self.frame_delay = FPS  # Ajuste a taxa de quadros da animação
        self.image = self.animation_frames[self.current_frame]
        # Já nasce em um lugar aleatorio que não seja um obstaculo
        local_spawn = mapa.tipo_tiles['Spawner'][random.randint(0, len(mapa.tipo_tiles['Spawner']) - 1)].hitbox
        self.y, self.x = local_spawn.top, local_spawn.left
        self.velocidade = 10
        self.hitbox = self.image.get_rect(topleft=(self.x, self.y)) 
        self.sofreu_dano = False
    def acertado_por_ataque(self, jogador):
        # Checa se a caixa de colisão do ataque do jogador encostou nele e faz o inimgo sofrer dano. 
        if jogador.ataque_hitbox.colliderect(self.hitbox) and not self.sofreu_dano:
            self.vida -= 1
            self.alfa = 0
            self.sofreu_dano = True
        elif not jogador.ataque_hitbox.colliderect(self.hitbox):
            self.sofreu_dano = False
    def causou_dano(self, jogador):
        # Checa se o inimigo encostou no jogador e faz o jogador sofrer dano
        if self.hitbox.colliderect(jogador.hitbox) and not jogador.sofreu_dano:
            jogador.sofreu_dano = True
            Audios.dano.play()
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
        if self.colisao_obstaculos(mapa):
            self.x -= direcao_x * self.velocidade
        self.y += direcao_y * self.velocidade 
        if self.colisao_obstaculos(mapa):
            self.y -= direcao_y * self.velocidade
        # Vê se após esse movimento o inimigo estaria dentro de um obstaculo, caso sim, ele volta. Isso impede que ele atravesse paredes
    def morte(self): 
        posicao = self.x, self.y
        n_aleatorio = random.randint(0, 20)
        if 15 <= n_aleatorio < 18:
            espada = Coletaveis(posicao, 'espada')
        elif 18 < n_aleatorio <= 20:
            escudo = Coletaveis(posicao, 'escudo')
        Enemy.lista_inimigos_presentes.remove(self)
        Audios.morte_inimigo.play()
    def colisao_obstaculos(self, mapa):
        # Muda a posição do hitbox pra ficar onde o inimigo vai estar 
        self.hitbox = self.image.get_rect(topleft=(self.x, self.y))
        # Checa se, para todos os obstaculos da fase há ou não colisão com o jogador
        colidiu = False
        return colidiu
    def atualizar(self, jogador, mapa): 
        # Isso vai atualizar o inimigo, checando se ele sofreu um ataque do jogador ou causou dano no mesmo, e após isso coloca sua superficie na tela
        self.causou_dano(jogador)
        self.hitbox = self.image.get_rect(topleft=(self.x, self.y))
        if self.frame_delay <= 0:
            # Avance para o próximo quadro
            current_index = int(self.current_frame)
            current_index = (current_index + 1) % 15  # 15 é o número total de quadros
            self.current_frame = f"{current_index:02d}"
            self.image = self.animation_frames[self.current_frame]
            self.frame_delay = 10  # Reinicie o contador de atraso
        else:
            self.frame_delay -= 1
        self.acertado_por_ataque(jogador)

        if self.vida <= 0:
            self.morte()
            jogador.pontuacao += 2
        else:
            self.seguir_jogador(jogador, mapa)
        self.image.set_alpha(self.alfa)
        TELA.blit(self.image, self.hitbox)
        if self.alfa < 255:
            self.alfa += 25.5