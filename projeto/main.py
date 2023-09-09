import pygame
from graphics import Superficie
from settings import *
from sys import exit
from player import Player
from level import Mapa, hitbox_tilemap
from enemy import Enemy

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
            # A cada loop checamos a posição do personagem, e colocamos as imagens do personagem, texto, e inimigo 
            # Inserindo uma superficie em cima do display. A os valores representam as cordenadas da superficie sobre o display. O ponto de origem é sempre no canto superior esquerdo
            inimigo = Enemy()
            jogador = Player()
            TELA.fill(Cor.PRETO)
            colisao = jogador.checando_colisao()
            posicao_jogador = Player.movimento_jogador(colisao)
            Mapa.desenhar_mapa(TELA)
            if colisao:
                print(colisao)
            """TELA.blit(Superficie.im_fundo, (0,0))"""
            TELA.blit(jogador.imagem, posicao_jogador)
            TELA.blit(Superficie.sup_texto, (300, 10))
            TELA.blit(inimigo.imagem, (20, 40))
            # Atualizando o que aparece na tela a cada "Tick" (Tick é uma única atualização que ocorre na simulação do jogo)
            pygame.display.update()
            # Limitando o número máximo de 'ticks'/'frames' por segundo a 60 para evitar que ocorra atualizações excessivas
            relogio.tick(FPS)

# Certificando que o jogo só será rodado nesse arquivo, e não caso ele seja importado ou algo do tipo
if __name__ == '__main__':    
    Game().running()