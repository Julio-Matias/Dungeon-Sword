from settings import *
from audiovisual import Superficie, Audios
import pygame

pygame.init()
#classe deteminando os elementos do hud e seu tamanho na tela
class HUD:
    imagem = pygame.image.load('projeto/assets/hud_pixel.png') 
    imagem = pygame.transform.scale(imagem, (280, 140))
    imagem.set_alpha(200)
    img_espada = pygame.image.load('projeto/assets/espada.png') 
    img_espada = pygame.transform.scale(img_espada, (20, 40))
    img_espada = pygame.transform.rotate(img_espada, 270)
    img_espada.set_alpha(175)
    img_nivel = pygame.image.load('projeto/assets/porta.png')
    img_nivel = pygame.transform.scale(img_nivel, (40, 40))
    img_nivel.set_alpha(175)
    fonte1 = pygame.font.Font('projeto/assets/fonts\Pixeltype.ttf', 75)
    fonte2 = pygame.font.Font('projeto/assets/fonts\Pixeltype.ttf', 50)

    def exibir_hud(self, jogador, Enemy):
        # Elementos da hud
        self.sup_vida= self.fonte1.render(f'{jogador.vida}', False, "Yellow")
        self.sup_pontuacao = self.fonte2.render(f'{jogador.pontuacao}', False, 'White')
        self.sup_nivel = self.fonte2.render(f': {Enemy.onda}', False, 'White')
        self.sup_espada = self.fonte2.render(f': {jogador.nivel_espada}', False, 'White')
        self.sup_msg = self.fonte2.render(f'Aperte "M" para o Menu', False, 'white')
        self.sup_msg.set_alpha(125)
        TELA.blit(self.sup_pontuacao, (190,103))
        TELA.blit(self.img_espada, (100,160))
        TELA.blit(self.img_nivel, (10, 145))
        TELA.blit(self.sup_nivel, (40, 155))
        TELA.blit(self.sup_espada, (140,155))
        TELA.blit(self.imagem, (2,2))
        TELA.blit(self.sup_vida, (225,43))
        TELA.blit(self.sup_msg,(400,20))


class Tela_morte:
    #classe deteminando a imagem da tela de morte e o que vai ser exibido nela
    tela_morte = pygame.image.load('projeto/assets/frase.png').convert_alpha()
    img_inimigo = pygame.image.load('projeto\sprites_folder\sprite_07.png').convert_alpha()
    img_inimigo = pygame.transform.scale(img_inimigo, (40, 40))
    def exibir_tela_morte(self, hud, jogador):
        sup_inimigos = hud.fonte2.render(f': {jogador.pontuacao}', False, 'White')
        TELA.blit(Superficie.im_jogo, (LARGURA_TELA/2 - Superficie.im_jogo.get_width()/2, ALTURA_TELA/2 - Superficie.im_jogo.get_height()/2))
        TELA.blit(Tela_morte.tela_morte, (1,1))
        TELA.blit(self.img_inimigo, (545, 385))
        TELA.blit(hud.img_nivel, (545, 440))
        TELA.blit(sup_inimigos, (580, 400))
        TELA.blit(hud.sup_nivel, (580, 450))


class Button():
    def __init__(self, image, scale) : #recebe como parametro as coordenadas x y, a imagem do botao e a escala da imagem
        altura_botao = image.get_height()
        largura_botao =  image.get_width()
        self.image = pygame.transform.scale(image, (int(largura_botao *scale), int(altura_botao * scale)))
        self.rect = self.image.get_rect() #retangulo da img
        self.clicado = False
    
    def draw(self, surface, x, y): #desenha na tela o botao e verifica se o mouse clicou nele a partir da posição e do click do mouse, retorna true para clicado
        self.rect.topleft = (x, y)
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