import pygame
from settings import *

pygame.init()

class Superficie:
    # Fontes para as superficies
    fonte1 = pygame.font.Font('projeto/assets/fonts\Pixeltype.ttf', 75)
    fonte2 = pygame.font.Font('projeto/assets/fonts\Pixeltype.ttf', 50)
    fonte3 = pygame.font.Font('projeto/assets/fonts\Pixeltype.ttf', 150)
# Uma superficie é a forma de inserir uma imagem no display. Aqui estou criando uma superficie de teste e dando uma cor a ela para que ela aparece contra o fundo preto
    im_parede = pygame.image.load("projeto/assets\parede-placeholder.png").convert_alpha()
    im_chao = pygame.image.load("projeto/assets\chao-placeholder.jpg").convert_alpha()
    im_jogo = pygame.transform.scale(pygame.image.load('projeto/assets/background-placeholder.png').convert_alpha(), (LARGURA_TELA, ALTURA_TELA))
    titulo_jogo = fonte3.render(f'Dungeon Sword', False, 'white')
    sup_msg = fonte2.render(f'Aperte "M" para o Menu', False, 'white')
    sup_msg.set_alpha(120)
    #carregando imagens dos botoes
    start_img = pygame.image.load('projeto/assets/start_btn.png').convert_alpha()
    exit_img = pygame.image.load('projeto/assets/exit_btn.png').convert_alpha()
    restart_img = pygame.image.load('projeto/assets/restart_btn.png').convert_alpha()
    def __init__(self) -> None:
        pass


class Audios:
    ataque_sem_espada = pygame.mixer.Sound('projeto/assets/audio/sem-espada.mp3')
    ataque_espada = pygame.mixer.Sound('projeto/assets/audio/ataqueespada.mp3') 
    gameover = pygame.mixer.Sound('projeto/assets/audio/gameover.mp3') 
    coletar = pygame.mixer.Sound('projeto/assets/audio/coletar.mp3') 
    proximafase = pygame.mixer.Sound('projeto/assets/audio/proximafase.mp3')
    dano = pygame.mixer.Sound('projeto/assets/audio/dano.mp3')
    pause = pygame.mixer.Sound('projeto/assets/audio/pause.mp3')
    unpause = pygame.mixer.Sound('projeto/assets/audio/unpause.mp3')
    click = pygame.mixer.Sound('projeto/assets/audio/click_button.mp3')
    
    morte_inimigo = pygame.mixer.Sound('projeto/assets/audio/morte_inimigo.mp3')
    
    
    audio_playing = False
