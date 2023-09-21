from settings import *
import pygame

pygame.init()
#classe deteminando a imagem do hud e seu tamanho na tela
class HUD:
    imagem = pygame.image.load('projeto/assets/hud_pixel.png') 
    imagem = pygame.transform.scale(imagem, (280, 140))
    imagem.set_alpha(150)
    fonte1 = pygame.font.Font('projeto/assets/fonts\Pixeltype.ttf', 75)
    fonte2 = pygame.font.Font('projeto/assets/fonts\Pixeltype.ttf', 50)

    def exibir_hud(self, jogador, Enemy):
        # Elementos da hud
        self.sup_vida= self.fonte1.render(f'{jogador.vida}', False, "Yellow")
        self.sup_pontuacao = self.fonte2.render(f'{jogador.pontuacao}', False, 'White')
        self.sup_nivel = self.fonte2.render(f'Nivel: {Enemy.onda}', False, 'White')
        self.sup_espada = self.fonte2.render(f'Espada: {jogador.nivel_espada}', False, 'White')
        self.sup_msg = self.fonte2.render(f'Aperte "M" para o Menu', False, 'white')
        TELA.blit(self.sup_pontuacao, (205,100))
        TELA.blit(self.sup_nivel, (80,150))
        TELA.blit(self.sup_espada, (50,200))
        TELA.blit(self.imagem, (2,2))
        TELA.blit(self.sup_vida, (225,43))
        TELA.blit(self.sup_msg,(400,20))