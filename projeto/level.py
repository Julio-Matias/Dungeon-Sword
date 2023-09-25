import pygame
from audiovisual import Superficie
from settings import *
from enemy import Enemy
from player import Player
import random
# Aqui é onde seria a criação de mapa

pygame.init()

# Definição do mapa (cada caractere representa um tile)
class Tile:
    def __init__(self, superficie, x, y):
        self.imagem = pygame.transform.scale(superficie, (TAMANHO_TILE, TAMANHO_TILE))
        self.hitbox = self.imagem.get_rect(topleft= (x * TAMANHO_TILE, y * TAMANHO_TILE))

class Mapa:
    def __init__(self):
        self.index_mapa_anterior = 0
        self.mapa_tiles = []
        self.tipo_tiles = {'Parede': [], 'Chão': [], 'Spawner': []}
    def proxima_fase(self, Coletaveis):
        Enemy.onda += 1
        if self.index_mapa_anterior == 0:
            mapa_atual = LISTA_MAPAS[random.randint(self.index_mapa_anterior + 1, len(LISTA_MAPAS) - 1)]
        elif self.index_mapa_anterior == len(LISTA_MAPAS) - 1:
            mapa_atual = LISTA_MAPAS[random.randint(0, len(LISTA_MAPAS) - 2)]
        else:
            mapa_atual = LISTA_MAPAS[random.choice([random.randint(0, self.index_mapa_anterior - 1),random.randint(self.index_mapa_anterior + 1, len(LISTA_MAPAS) - 1)])]
        self.index_mapa_anterior = LISTA_MAPAS.index(mapa_atual)
        self.mapa_tiles = []
        self.tipo_tiles = {'Parede': [], 'Chão': [], 'Spawner': []}
        self.montar_mapa(mapa_atual)
        Coletaveis.lista_coletaveis = []
        numero_inimigos = random.randint(Enemy.onda, 2 + Enemy.onda)
        for _ in range(numero_inimigos):
            inimigo = Enemy(self)
            Enemy.lista_inimigos_presentes.append(inimigo)
    def reiniciar_jogo(self, jogador, Coletaveis):
        jogador = Player()
        Enemy.onda =  0
        Enemy.lista_inimigos_presentes = []
        self.proxima_fase(Coletaveis)
        return jogador
    def montar_mapa(self, mapa):
        for y, linha in enumerate(mapa):
            for x, tile in enumerate(linha):
                if tile == "P":
                    tile_parede = Tile(Superficie.im_parede, x, y)
                    self.mapa_tiles.append(tile_parede)
                    self.tipo_tiles['Parede'].append(tile_parede)
                elif tile == "0":
                    tile_chao = Tile(Superficie.im_chao, x, y)
                    self.mapa_tiles.append(tile_chao)
                    self.tipo_tiles['Chão'].append(tile_chao)
                elif tile == 's':
                    tile_spawner = Tile(Superficie.im_chao, x, y)
                    self.mapa_tiles.append(tile_spawner)
                    self.tipo_tiles['Spawner'].append(tile_spawner)
    def desenhar_mapa(self):
        for tile in self.mapa_tiles:
            TELA.blit(tile.imagem, tile.hitbox)