from settings import *
import pygame

pygame.init()
#classe deteminando a imagem do hud e seu tamanho na tela
class HUD:
    hud = pygame.image.load('projeto/assets/hud_pixel.png') 
    hud = pygame.transform.scale(hud, (280, 140))
    hud.set_alpha(150)