import time
import keyboard
import sys 
from music.biblioteca import Biblioteca
from music.reproductor import Reproductor
from music import music_menu


def iniciar():
    biblioteca = Biblioteca("songs") #VARIABLE/OBJETO: ES LA BIBLIOTECA DE CANCIONES DISPONIBLES DESDE LA CARPETA "SONGS".
    cancion_escogida = music_menu.elegir_cancion(biblioteca) #---VARIABLE: ESTA ES CANCION_ESCOGIDA POR EL USUARIO.
    
    if cancion_escogida == None:
        return
        
    
    reproductor = Reproductor(cancion_escogida)
    reproductor.iniciar()
    
    print(str(cancion_escogida).upper()) #---LE DICE AL USUARIO LA CANCION_ESCOGIDA.
    
    while True:
        #---------PAUSA Y REANUDA LA CANCION---------#
        if keyboard.is_pressed("space"):
            reproductor.alternar_pausa()
            time.sleep(0.1)
            
        if not reproductor.actualizar():
            break
        
        time.sleep(0.03)
