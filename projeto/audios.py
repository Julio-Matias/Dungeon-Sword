import pygame
pygame.init()

class Audios:
    ataque_sem_espada = pygame.mixer.Sound('projeto/assets/audio/sem-espada.mp3')
    ataque_espada = pygame.mixer.Sound('projeto/assets/audio/ataqueespada.mp3') 
    gameover = pygame.mixer.Sound('projeto/assets/audio/gameover.mp3') 
    coletar = pygame.mixer.Sound('projeto/assets/audio/coletar.mp3') 
    proximafase = pygame.mixer.Sound('projeto/assets/audio/proximafase.mp3')
    dano = pygame.mixer.Sound('projeto/assets/audio/damage.mp3')
    pause = pygame.mixer.Sound('projeto/assets/audio/pause.mp3')
    unpause = pygame.mixer.Sound('projeto/assets/audio/unpause.mp3')
    audio_playing = False
