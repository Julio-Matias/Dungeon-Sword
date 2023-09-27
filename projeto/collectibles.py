from settings import *
from audiovisual import Audios
import pygame

pygame.init()

class Coletaveis:
    lista_coletaveis = []
    def __init__(self, posicao, tipo):
        if tipo == 'espada':
            self.tipo = 'espada'
            self.imagem = pygame.image.load('projeto/assets/espada.png') 
            self.imagem = pygame.transform.scale(self.imagem, (21, 50))
        elif tipo == 'escudo':
            self.tipo = 'escudo'
            self.imagem = pygame.image.load('projeto/assets/escudo.png')
            self.imagem = pygame.transform.scale(self.imagem, (40,40))
        self.lista_coletaveis.append(self)
        self.hitbox = self.imagem.get_rect(topleft=(posicao))
        self.coletado = False

    def coletar(self, jogador):
        if self.hitbox.colliderect(jogador.hitbox):
            self.hitbox = pygame.Rect((0,0), (0,0))
            self.coletado = True
            Coletaveis.lista_coletaveis.remove(self)
            if self.tipo == 'espada':
                jogador.nivel_espada += 1
                jogador.espada = True
                jogador.largura_ataque, jogador.altura_ataque = TAMANHO_TILE * 2.5, TAMANHO_TILE * 2.5
                pygame.time.set_timer(EVENTO_ESPADA, TEMPO_ESPADA)
            elif self.tipo == 'escudo':
                jogador.vida += 1
            
            #som quando coletar espada ou escudo
            if not Audios.audio_playing:
                Audios.coletar.play()
                Audios.audio_playing = True
        else:
            Audios.audio_playing = False
            
class Portal:
    altura_porta = TAMANHO_TILE * 1.5
    largura_porta = TAMANHO_TILE * 0.93
    def __init__(self):
        self.colisao = True
        self.imagem = pygame.image.load('projeto/assets/porta.png')
        self.imagem = pygame.transform.scale(self.imagem, (self.largura_porta, self.altura_porta))
        self.hitbox = self.imagem.get_rect(topleft=((LARGURA_TELA- self.largura_porta)/2, (ALTURA_TELA - self.altura_porta)/2))