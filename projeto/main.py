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
            TELA.fill(Cor.PRETO)
            mapa.desenhar_mapa()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == jogador.evento_intervalo_ataque:
                    jogador.pode_atacar = True
                elif event.type == inimigo.evento_intervalo_dano:
                    jogador.sofreu_dano = False
            # A cada loop checamos a posição do personagem, e colocamos as imagens do personagem, texto, e inimigo 
            # Inserindo uma superficie em cima do display. A os valores representam as cordenadas da superficie sobre o display. O ponto de origem é sempre no canto superior esquerdo
            sup_pontuacao = fonte.render(f'{jogador.pontuacao}', False, Cor.BRANCO)
            TELA.blit(sup_pontuacao, (500, 10))
            TELA.blit(Coletaveis.sword, (900,100))
            inimigo.atualizar(jogador, mapa)
            jogador.atualizar(mapa)
            debug(jogador.olhando_direcao, 'Direção')         
            debug((inimigo.vida), 'Vida inimigo', 30)
            debug((jogador.pontuacao), 'Pontos do jogador', 60)
            debug((jogador.vida), 'Vida jogador', 90)
            # Atualizando o que aparece na tela a cada "Tick" (Tick é uma única atualização que ocorre na simulação do jogo)
            pygame.display.update()
            # Limitando o número máximo de 'ticks'/'frames' por segundo a 60 para evitar que ocorra atualizações excessivas
            self.relogio.tick(FPS)

# Certificando que o jogo só será rodado nesse arquivo, e não caso ele seja importado ou algo do tipo
if __name__ == '__main__':    
    Game().running()