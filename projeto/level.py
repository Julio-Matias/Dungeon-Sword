from typing import Any
import pygame
from graphics import Superficie
from settings import *
# Aqui é onde seria a criação de mapa

pygame.init()

# Definição do mapa (cada caractere representa um tile)
class Tile:
    def __init__(self, superficie, x, y, tipo_do_tile):
        self.imagem = pygame.transform.scale(superficie, (TAMANHO_TILE, TAMANHO_TILE))
        self.hitbox = self.imagem.get_rect(topleft= (x * TAMANHO_TILE, y * TAMANHO_TILE))
        self.tipo = tipo_do_tile

class Mapa:
    def __init__(self):
        self.mapa_tiles = []
    def desenhar_mapa(self, TELA):
        for y, linha in enumerate(mapa):
            for x, tile in enumerate(linha):
                if tile == "P":
                    tile_parede = Tile(Superficie.im_parede, x, y, 'parede')
                    TELA.blit(tile_parede.imagem, (x * TAMANHO_TILE, y * TAMANHO_TILE))
                    self.mapa_tiles.append(tile_parede)
                elif tile == "0":
                    tile_chao = Tile(Superficie.im_chao, x, y, 'chao')
                    TELA.blit(tile_chao.imagem, (x * TAMANHO_TILE, y * TAMANHO_TILE))
                    self.mapa_tiles.append(tile_chao)