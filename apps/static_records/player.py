import pygame
from mutagen.mp3 import MP3


def iniciar_player():
    pygame.mixer.init()

def reproducir_cancion(cancion):
    pygame.mixer.music.load(cancion.ruta_mp3)
    pygame.mixer.music.play()

def detener_cancion():
    pygame.mixer.music.stop()


def obtener_tiempo_actual():
    return pygame.mixer.music.get_pos() / 1000.0

def obtener_duracion(cancion):
    audio = MP3(cancion.ruta_mp3)
    return audio.info.length

def musica_activa():
    return pygame.mixer.music.get_busy()

def pausar_cancion():
    pygame.mixer.music.pause()

def reanudar_cancion():
    pygame.mixer.music.unpause()





    