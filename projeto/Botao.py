import pygame
from settings import *
from audios import *

class Button():
    def __init__(self, x, y, image, scale) : #recebe como parametro as coordenadas x y, a imagem do botao e a escala da imagem
        altura_botao = image.get_height()
        largura_botao =  image.get_width()
        self.image = pygame.transform.scale(image, (int(largura_botao *scale), int(altura_botao * scale)))
        self.rect = self.image.get_rect() #retangulo da img
        self.rect.topleft = (x,y)
        self.clicado = False
    
    def draw(self, surface): #desenha na tela o botao e verifica se o mouse clicou nele a partir da posição e do click do mouse, retorna true para clicado
        click = False
        #desenhar botao na tela
        surface.blit(self.image, (self.rect.x, self.rect.y))
        #posição do mouse
        pos = pygame.mouse.get_pos()
        
        #chegando se mouse está sobre os botoes
        if self.rect.collidepoint(pos):#collidepoint verifica se o 'rect' (retangulo da imagem do botao) colidiu com o ponto referente a posição do mouse
          if pygame.mouse.get_pressed()[0] == 1 and self.clicado == False:#checando se enquanto estiver em cima da imagem do botao, o mouse foi pressioando bot esq
            self.clicado = True
            click = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicado = False
        
        if click:
           Audios.click.play()
        return click