import pygame
from sys import exit

# Inicializando o PyGame
pygame.init()
# Definindo o tamanho da tela
# O display (tela do jogo) é uma superficie onde tudo que está sendo mostrado ao jogador ficará
screen = pygame.display.set_mode((800,600)) 
# Definindo o titulo e o icon para a janela onde o jogo será executado
pygame.display.set_caption("Jogo maneirasso")
icon = pygame.image.load("projeto/assets\icone-placeholder.png")
pygame.display.set_icon(icon)
# Criando um objeto de relógio que ajudara a controlar o tempo percorrido no jogo
clock = pygame.time.Clock()
# Decidindo uma fornte para colocar em uma superficie
fonte = pygame.font.Font('projeto/assets/fonts\Pixeltype.ttf', 50)


# Uma superficie é a forma de inserir uma imagem no display. Aqui estou criando uma superficie de teste e dando uma cor a ela para que ela aparece contra o fundo preto
superficie_jogador = pygame.Surface((200,200))
superficie_jogador.fill('Red')
superficie_fundo = pygame.image.load('projeto/assets/background-placeholder.jpg')
superficie_fundo = pygame.transform.scale(superficie_fundo, (800,800))
superficie_texto = fonte.render('JOGO MANEIRO', False, 'Black')


# Rodando o loop do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # Inserindo uma superficie em cima do display. A os valores representam as cordenadas da superficie sobre o display. O ponto de origem é sempre no canto superior esquerdo
    screen.blit(superficie_fundo, (0,0))
    screen.blit(superficie_jogador,(300,200))
    screen.blit(superficie_texto, (300, 10))

    # Atualizando o que aparece na tela a cada "Tick" (Tick é uma única atualização que ocorre na simulação do jogo)
    pygame.display.update()
    # Limitando o número máximo de 'ticks'/'frames' por segundo a 60 para evitar que ocorra atualizações excessivas
    clock.tick(60)