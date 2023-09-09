import pygame
from graphics import Superficie
from settings import *
from sys import exit
from player import Player
from enemy import Inimigo

# Inicializando o PyGame
pygame.init()
# O display (tela do jogo) é uma superficie onde tudo que está sendo mostrado ao jogador ficará
TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA)) 
# Definindo o titulo e o icon para a janela onde o jogo será executado
pygame.display.set_caption("Jogo maneirasso")
icone = pygame.image.load("projeto/assets\icone-placeholder.png")
pygame.display.set_icon(icone)
# Criando um objeto de relógio que ajudara a controlar o tempo percorrido no jogo
relogio = pygame.time.Clock()


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
            # A cada loop checamos a posição do personagem, e colocamos as imagens do personagem, texto, inimigo e 
            posicao_jogador = Player.movimento_jogador(event)
            jogador_rect = Player.hitbox_jogador(posicao_jogador) 
            inimigo_rect = Inimigo.hitbox_inimigo()
            # Inserindo uma superficie em cima do display. A os valores representam as cordenadas da superficie sobre o display. O ponto de origem é sempre no canto superior esquerdo
            TELA.fill(COR_FUNDO)
            TELA.blit(Superficie.sup_fundo, (0,0))
            TELA.blit(Superficie.sup_jogador, posicao_jogador)
            TELA.blit(Superficie.sup_texto, (300, 10))
            TELA.blit(Superficie.sup_inimigo, (20, 40))
            print(jogador_rect.colliderect(inimigo_rect))
            # Atualizando o que aparece na tela a cada "Tick" (Tick é uma única atualização que ocorre na simulação do jogo)
            pygame.display.update()
            # Limitando o número máximo de 'ticks'/'frames' por segundo a 60 para evitar que ocorra atualizações excessivas
            relogio.tick(FPS)

if __name__ == '__main__':    
    Game().running()