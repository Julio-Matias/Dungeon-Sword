from typing import Any
import pygame
from graphics import Superficie

pygame.init()
# Aqui é onde seria a criação de mapa
TAMANHO_TILE = 50
# Definição do mapa (cada caractere representa uma imagem)
mapa = [
    "PPPPPPPPPPPPPPPPPPPPP",
    "P000000000P000000000P",
    "P000000000P000000000P",
    "P0000000000000000000P",
    "P0000000000000000000P",
    "P0000000000000000000P",
    "P000000000P000000000P",
    "PPPPPPPPPPPPPPPPPPPPP",
]

tile_parede = pygame.transform.scale(Superficie.im_parede, (TAMANHO_TILE, TAMANHO_TILE))
tile_chao = pygame.transform.scale(Superficie.im_chao, (TAMANHO_TILE, TAMANHO_TILE))
class Mapa:
    def __init__(self) -> None:
        pass
    def desenhar_mapa(TELA):
        for y, linha in enumerate(mapa):
            for x, tile in enumerate(linha):
                if tile == "P":
                    TELA.blit(tile_parede, (x * TAMANHO_TILE, y * TAMANHO_TILE))
                elif tile == "0":
                    TELA.blit(tile_chao, (x * TAMANHO_TILE, y * TAMANHO_TILE))