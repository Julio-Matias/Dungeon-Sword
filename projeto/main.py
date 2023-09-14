import pygame
from graphics import Superficie
from settings import *
from sys import exit
from player import Player
from level import Mapa
from enemy import Enemy
from debug import debug
from collectibles import Coletaveis

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
        # Decidindo uma fonte para a UI, e criando a instancia de mapa, inimigo e jogador
        fonte = pygame.font.Font('projeto/assets/fonts\Pixeltype.ttf', 50)
        mapa = Mapa()
        inimigo = Enemy(mapa)
        jogador = Player()
        # Rodando o loop do jogo
        while True:  
            # Isso vai 'limpar' a tela de fundo, para que as imagens que aparecem na tela não fiquem permanentemente nela 
            TELA.fill('Black')
            # Cria o mapa do jogo
            mapa.desenhar_mapa()
            # Vai checar quais eventos estão ocorrendo por dentro
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # Ver função ataque do Player
                elif event.type == EVENTO_INTERVALO_ATAQUE:
                    jogador.pode_atacar = True
                # Ver função causou_dano do Enemy
                elif event.type == EVENTO_INTERVALO_DANO:
                    jogador.sofreu_dano = False
            # Inserindo uma superficie em cima do display. A os valores representam as cordenadas da superficie sobre o display. O ponto de origem é sempre no canto superior esquerdo
            sup_pontuacao = fonte.render(f'{jogador.pontuacao}', False, 'White')
            TELA.blit(sup_pontuacao, (500, 10))
            TELA.blit(Coletaveis.sword, (900,100))
            # Isso vai atualizar o jogador e o inimigo, vendo se o jogador fez algum input, se o jogador ou o inimigo sofreu dano, e movimentando ambos, e após isso tudo, coloca suas superficies na tela
            inimigo.atualizar(jogador, mapa)
            jogador.atualizar(mapa)
            # Debug
            debug(jogador.olhando_direcao, 'Direção:')         
            debug((inimigo.vida), 'Vida inimigo:', 30)
            debug((jogador.vida), 'Vida jogador:', 60)
            # Atualizando o que aparece na tela a cada "Tick" (Tick é uma única atualização que ocorre na simulação do jogo)
            pygame.display.update()
            # Limitando o número máximo de 'ticks'/'frames' por segundo a 60 para evitar que ocorra atualizações excessivas
            self.relogio.tick(FPS)
# Certificando que o jogo só será rodado nesse arquivo, e não caso ele seja importado ou algo do tipo
if __name__ == '__main__':    
    Game().running()