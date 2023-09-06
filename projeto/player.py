from graphics import Superficie
import pygame
pygame.init()

x_jogador = 300
y_jogador = 200
class Player: 
    def __init__(self) -> None:
        pass
    def movimento_jogador(evento):
        global x_jogador
        global y_jogador
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                y_jogador -= 10
            elif evento.key == pygame.K_DOWN:
                y_jogador += 10
            elif evento.key == pygame.K_LEFT:
                x_jogador -= 10
            elif evento.key == pygame.K_RIGHT:
                x_jogador += 10
        return (x_jogador, y_jogador)
