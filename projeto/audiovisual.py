import pygame
from settings import *

pygame.init()

class Superficie:
    # Fontes para as superficiess
    fonte1 = pygame.font.Font('projeto/assets/fonts\Pixeltype.ttf', 75)
    fonte2 = pygame.font.Font('projeto/assets/fonts\Pixeltype.ttf', 50)
# Uma superficie é a forma de inserir uma imagem no display. Aqui estou criando uma superficie de teste e dando uma cor a ela para que ela aparece contra o fundo preto
    im_titulo = pygame.transform.scale(pygame.image.load("projeto/assets/title.png").convert_alpha(), (LARGURA_TELA/2 + 500, ALTURA_TELA + 400))
    im_parede = pygame.image.load("projeto/assets\parede-placeholder.png").convert_alpha()
    im_chao = pygame.image.load("projeto/assets\chao-placeholder.jpg").convert_alpha()
    im_jogo = pygame.transform.scale(pygame.image.load('projeto/assets/background-placeholder.png').convert_alpha(), (LARGURA_TELA, ALTURA_TELA))
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
    ataque_sem_espada.set_volume(0.2)
    ataque_espada = pygame.mixer.Sound('projeto/assets/audio/ataqueespada.mp3') 
    ataque_espada.set_volume(0.2)
    gameover = pygame.mixer.Sound('projeto/assets/audio/gameover.mp3') 
    coletar = pygame.mixer.Sound('projeto/assets/audio/coletar.mp3')
    coletar.set_volume(0.5) 
    proximafase = pygame.mixer.Sound('projeto/assets/audio/proximafase.mp3')
    proximafase.set_volume(0.2)
    dano = pygame.mixer.Sound('projeto/assets/audio/dano.mp3')
    dano.set_volume(0.4)
    pause = pygame.mixer.Sound('projeto/assets/audio/pause.mp3')
    pause.set_volume(0.5)
    unpause = pygame.mixer.Sound('projeto/assets/audio/unpause.mp3')
    unpause.set_volume(0.5)
    click = pygame.mixer.Sound('projeto/assets/audio/click_button.mp3')
    click.set_volume(0.5)
    morte_inimigo = pygame.mixer.Sound('projeto/assets/audio/morte_inimigo.mp3')
    morte_inimigo.set_volume(0.5)
    
    audio_playing = False
