from typing import Any
import pygame
from graphics import Superficie
from settings import *
# Aqui é onde seria a criação de mapa

pygame.init()

# Definição do mapa (cada caractere representa uma imagem)
mapa = [
    "PPPPPPPPPPPPPPPPPPPPPPPP",
    "P000000000P000000000000P",
    "P000000000P000000000000P",
    "P0000000000000000000000P",
    "P0000000000000000000000P",
    "P0000000000000000000000P",
    "P0000000000000000000000P",
    "P0000000000000000000000P",
    "P0000000000000000000000P",
    "P0000000000000000000000P",
    "P0000000000000000000000P",
    "P0000000000000000000000P",
    "P000000000P000000000000P",
    "PPPPPPPPPPPPPPPPPPPPPPPP"
]
class Tile:
    def __init__(self, superficie):
        self.imagem = pygame.transform.scale(superficie, (TAMANHO_TILE, TAMANHO_TILE))
tile_parede = Tile(Superficie.im_parede)
tile_chao = Tile(Superficie.im_chao)
hitbox_tilemap = []
class Mapa:
    def __init__(self) -> None:
        pass
    def desenhar_mapa(TELA):
        for y, linha in enumerate(mapa):
            for x, tile in enumerate(linha):
                if tile == "P":
                    TELA.blit(tile_parede.imagem, (x * TAMANHO_TILE, y * TAMANHO_TILE))
                    hitbox_tilemap.append(pygame.Rect((x * TAMANHO_TILE, y * TAMANHO_TILE), (TAMANHO_TILE, TAMANHO_TILE)))
                elif tile == "0":
                    TELA.blit(tile_chao.imagem, (x * TAMANHO_TILE, y * TAMANHO_TILE))