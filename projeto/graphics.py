import pygame
import os
from settings import *

pygame.init()

class Superficie:
# Uma superficie é a forma de inserir uma imagem no display. Aqui estou criando uma superficie de teste e dando uma cor a ela para que ela aparece contra o fundo preto
    im_ataque = pygame.transform.scale(pygame.image.load('projeto/assets/ataque-placeholder.png'), (LARGURA_ATAQUE, ALTURA_ATAQUE))
    im_fundo = pygame.transform.scale(pygame.image.load('projeto/assets/background-placeholder.png'), (LARGURA_TELA, 1440))
    im_parede = pygame.image.load("projeto/assets\parede-placeholder.png")
    im_chao = pygame.image.load("projeto/assets\chao-placeholder.jpg")
    im_jogo = pygame.image.load('projeto/assets/imagem_jogo.jpg').convert_alpha()
    def __init__(self) -> None:
        pass