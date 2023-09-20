from typing import Any
import pygame
from graphics import Superficie
from settings import *
from enemy import Enemy
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
        self.mapa_tiles = []
        self.tipo_tiles = {'Parede': [], 'Chão': [], 'Spawner': []}
    def proxima_fase(self):
        Enemy.onda += 1
        mapa_atual = LISTA_MAPAS[random.randint(0, len(LISTA_MAPAS) - 1)]
        self.mapa_tiles = []
        self.tipo_tiles = {'Parede': [], 'Chão': [], 'Spawner': []}
        self.montar_mapa(mapa_atual)
        numero_inimigos = random.randint(Enemy.onda, 2 + Enemy.onda)
        for _ in range(numero_inimigos):
            inimigo = Enemy(self)
            Enemy.lista_inimigos_presentes.append(inimigo)
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