import pygame
from graphics import Superficie
from settings import *
from sys import exit

# Inicializando o PyGame
pygame.init()
# Definindo o tamanho da tela
# O display (tela do jogo) é uma superficie onde tudo que está sendo mostrado ao jogador ficará
screen = pygame.display.set_mode((LARGURA,ALTURA)) 
# Definindo o titulo e o icon para a janela onde o jogo será executado
pygame.display.set_caption("Jogo maneirasso")
icon = pygame.image.load("projeto/assets\icone-placeholder.png")
pygame.display.set_icon(icon)
# Criando um objeto de relógio que ajudara a controlar o tempo percorrido no jogo
clock = pygame.time.Clock()



class Game:
    def __init__(self) -> None:
        pass
    def running(self):
        # Rodando o loop do jogo
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            # Inserindo uma superficie em cima do display. A os valores representam as cordenadas da superficie sobre o display. O ponto de origem é sempre no canto superior esquerdo
            screen.blit(Superficie.sup_fundo, (0,0))
            screen.blit(Superficie.sup_jogador,(300,200))
            screen.blit(Superficie.sup_texto, (300, 10))

            # Atualizando o que aparece na tela a cada "Tick" (Tick é uma única atualização que ocorre na simulação do jogo)
            pygame.display.update()
            # Limitando o número máximo de 'ticks'/'frames' por segundo a 60 para evitar que ocorra atualizações excessivas
            clock.tick(60)
Game().running()