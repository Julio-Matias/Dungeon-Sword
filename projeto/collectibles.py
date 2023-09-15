from settings import *
import pygame

pygame.init()

class Coletaveis:
    sword = pygame.image.load('projeto/assets/espada.png') 
    sword = pygame.transform.scale(sword, (40, 80))
    shield = pygame.image.load('projeto/assets/escudo.png')
    shield = pygame.transform.scale(shield, (130,100))
