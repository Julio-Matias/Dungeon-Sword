import pygame
import os
from settings import *


pygame.init()

# Decidindo uma fonte para colocar em uma superficie
fonte = pygame.font.Font('projeto/assets/fonts\Pixeltype.ttf', 50)

class Superficie:
# Uma superficie é a forma de inserir uma imagem no display. Aqui estou criando uma superficie de teste e dando uma cor a ela para que ela aparece contra o fundo preto
    im_jogador = pygame.Surface((LARGURA_JOGADOR, ALTURA_JOGADOR))
    im_jogador.fill('Red')
    im_fundo = pygame.image.load('projeto/assets/background-placeholder.png')
    im_fundo = pygame.transform.scale(im_fundo, (LARGURA_TELA, 1440))
    sup_texto = fonte.render('JOGO MANEIRO', False, Cor.BRANCO)
    im_inimigo = pygame.Surface((50, 50))
    im_inimigo.fill(Cor.BRANCO)
    im_parede = pygame.image.load("projeto/assets\parede-placeholder.png")
    im_chao = pygame.image.load("projeto/assets\chao-placeholder.jpg")
    def __init__(self) -> None:
        pass