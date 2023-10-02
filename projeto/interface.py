from settings import *
from audiovisual import Superficie, Audios
import pygame

pygame.init()
#classe deteminando os elementos do hud e seu tamanho na tela
class HUD:
    imagem = {
        'False': pygame.image.load('projeto/assets/hud_sem_espada.png').convert_alpha(),
        'True': pygame.image.load('projeto/assets/hud_com_espada.png').convert_alpha()
    }
    
    def exibir_hud(self, jogador, Mapa):
        pygame.transform.scale(self.imagem[str(jogador.espada)], (280, 200))
        self.imagem[str(jogador.espada)].set_alpha(180)
        # Elementos da hud
        self.sup_vida= Superficie.fonte1.render(f'{jogador.vida}', False, "Yellow")
        self.sup_pontuacao = Superficie.fonte2.render(f'{jogador.pontuacao}', False, 'White')
        self.sup_nivel = Superficie.fonte2.render(f'{Mapa.nivel}', False, 'White')
        self.sup_espada = Superficie.fonte2.render(f'{jogador.nivel_espada}', False, 'White')
        TELA.blit(self.sup_pontuacao, (190,105))
        TELA.blit(self.sup_nivel, (90, 148))
        TELA.blit(self.sup_espada, (207,148))
        TELA.blit(self.imagem[str(jogador.espada)], (2,2))
        TELA.blit(self.sup_vida, (225,43))
        TELA.blit(Superficie.sup_msg,(400,20))


class Tela_morte:
    #classe deteminando a imagem da tela de morte e o que vai ser exibido nela
    tela_morte = pygame.image.load('projeto/assets/frase.png').convert_alpha()
    inimigos_derrotados = pygame.image.load('projeto/assets\inimigos_derrotados.png').convert_alpha()
    inimigos_derrotados = pygame.transform.scale(inimigos_derrotados, (50, 37))
    nivel = pygame.image.load('projeto/assets/nivel.png').convert_alpha()
    nivel = pygame.transform.scale(nivel, (56, 24))
    espadas_coletadas = pygame.image.load('projeto/assets\espadas_coletadas.png').convert_alpha()
    espadas_coletadas = pygame.transform.scale(espadas_coletadas, (50, 21))
    def exibir_tela_morte(self, hud):
        TELA.blit(Superficie.im_jogo, (LARGURA_TELA/2 - Superficie.im_jogo.get_width()/2, ALTURA_TELA/2 - Superficie.im_jogo.get_height()/2))
        TELA.blit(Tela_morte.tela_morte, (1,1))
        TELA.blit(self.inimigos_derrotados, (455, 385))
        TELA.blit(self.espadas_coletadas, (620, 393))
        TELA.blit(self.nivel, (545, 440))
        TELA.blit(hud.sup_espada, (675, 392))
        TELA.blit(hud.sup_pontuacao, (510, 392))
        TELA.blit(hud.sup_nivel, (610, 440))


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