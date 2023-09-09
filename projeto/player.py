from graphics import Superficie
import pygame
pygame.init()

x_jogador = 300
y_jogador = 200
class Player: 
    def __init__(self) -> None:
        pass
    def hitbox_jogador(posicao_jogador):
        player_rect = Superficie.sup_jogador.get_rect(topleft= posicao_jogador)
        return player_rect
    def movimento_jogador(evento):
        global x_jogador
        global y_jogador
        # Checa quais as teclas que estão sendo pressionadas e baseado nisso faz o personagem se mover
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:
            y_jogador -= 10
        if teclas[pygame.K_DOWN]:
            y_jogador += 10
        if teclas[pygame.K_LEFT]:
            x_jogador -= 10
        if teclas[pygame.K_RIGHT]:
            x_jogador += 10
        return (x_jogador, y_jogador)