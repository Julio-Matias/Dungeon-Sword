from typing import Any
import pygame
from graphics import Superficie
from settings import *
# Aqui é onde seria a criação de mapa

pygame.init()

# Definição do mapa (cada caractere representa um tile)
class Tile:
    def __init__(self, superficie, x, y):
        self.imagem = pygame.transform.scale(superficie, (TAMANHO_TILE, TAMANHO_TILE))
        self.hitbox = self.imagem.get_rect(topleft= (x * TAMANHO_TILE, y * TAMANHO_TILE))

class Mapa:
    def __init__(self):
        self.mapa_tiles = []
        self.tipo_tiles = {'Parede': [], 'Chão': [], 'Spawner': []}
        self.montar_mapa()
    def montar_mapa(self):
        for y, linha in enumerate(MAPA):
            for x, tile in enumerate(linha):
                if tile == "P":
                    tile_parede = Tile(Superficie.im_parede, x, y)
                    self.mapa_tiles.append(tile_parede)
                    self.tipo_tiles['Parede'].append(tile_parede)
                elif tile == "0":
                    tile_chao = Tile(Superficie.im_chao, x, y)
                    self.mapa_tiles.append(tile_chao)
                    self.tipo_tiles['Chão'].append(tile_chao)
                elif tile == 'S':
                    tile_spawner = Tile(Superficie.im_chao, x, y)
                    self.mapa_tiles.append(tile_spawner)
                    self.tipo_tiles['Spawner'].append(tile_spawner)
    def desenhar_mapa(self):
        for tile in self.mapa_tiles:
            TELA.blit(tile.imagem, tile.hitbox)