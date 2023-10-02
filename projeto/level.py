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
        self.nivel = 0
        self.index_mapa_anterior = 0
    # Escolhe uma fase aleatóriamente, monta ela baseado na matriz e gera os inimigos nos lugares adequados aleatoriamente
    def proxima_fase(self, Coletaveis):
        self.nivel += 1
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
        if self.nivel < 5:
            for _ in range(self.nivel):
                inimigo = Enemy(self, 'slime')
                Enemy.lista_inimigos_presentes.append(inimigo)
        else:
            numero_ghost = self.nivel // 5
            for _ in range(numero_ghost):
                inimigo = Enemy(self, 'ghost')
                Enemy.lista_inimigos_presentes.append(inimigo)
            numero_slime = self.nivel - numero_ghost
            for _ in range(numero_slime):
                inimigo = Enemy(self, 'slime')
                Enemy.lista_inimigos_presentes.append(inimigo)
    def reiniciar_jogo(self, jogador, Coletaveis):
        jogador = Player()
        self.nivel =  0
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