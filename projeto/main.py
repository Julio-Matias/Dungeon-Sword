import pygame

#initialising pygame
pygame.init()

#defining size of game window
tela = pygame.display.set_mode((800,600)) 

#Titulo e icon
pygame.display.set_caption("Jogo maneirasso")
icon = pygame.image.load("pochitinha.webp")
pygame.display.set_icon(icon)

rodando = True
while rodando:
    for event in pygame.event.get():
        print('OLA marcus')
        if event.type == pygame.QUIT:
            rodando = False