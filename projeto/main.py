import pygame
from graphics import Superficie
from settings import *
from sys import exit
from player import Player
from level import Mapa
from enemy import Enemy
from debug import debug

# Inicializando o PyGame
pygame.init()
# Definindo o titulo e o icon para a janela onde o jogo será executado
pygame.display.set_caption("Jogo maneirasso")
icone = pygame.image.load("projeto/assets\icone-placeholder.png")
pygame.display.set_icon(icone)


class Game:
    def __init__(self):
        # Criando um objeto de relógio que ajudara a controlar o tempo percorrido no jogo
        self.relogio = pygame.time.Clock()
    def running(self):
        # Rodando o loop do jogo
        mapa = Mapa()
        inimigo = Enemy()
        jogador = Player()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            # A cada loop checamos a posição do personagem, e colocamos as imagens do personagem, texto, e inimigo 
            # Inserindo uma superficie em cima do display. A os valores representam as cordenadas da superficie sobre o display. O ponto de origem é sempre no canto superior esquerdo
            TELA.fill(Cor.PRETO)
            mapa.desenhar_mapa()
            TELA.blit(Superficie.sup_texto, (500, 10))
            TELA.blit(Superficie.vida, (900,10))
            TELA.blit(inimigo.imagem, inimigo.hitbox)
            jogador.atualizar(mapa)
            TELA.blit(inimigo.imagem, inimigo.hitbox)
            debug(jogador.olhando_direcao)
            # Atualizando o que aparece na tela a cada "Tick" (Tick é uma única atualização que ocorre na simulação do jogo)
            pygame.display.update()
            # Limitando o número máximo de 'ticks'/'frames' por segundo a 60 para evitar que ocorra atualizações excessivas
            self.relogio.tick(FPS)

# Certificando que o jogo só será rodado nesse arquivo, e não caso ele seja importado ou algo do tipo
if __name__ == '__main__':    
    Game().running()