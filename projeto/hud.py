from settings import *
import pygame

pygame.init()
#classe deteminando a imagem do hud e seu tamanho na tela
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