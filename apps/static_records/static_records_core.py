import time
import keyboard

from .biblioteca import Biblioteca
from .reproductor import Reproductor
from . import static_records_menu


def iniciar():
    biblioteca = Biblioteca("data/static_records") #VARIABLE/OBJETO: ES LA BIBLIOTECA DE CANCIONES DISPONIBLES DESDE LA CARPETA "SONGS".
    while True:
        seleccion = static_records_menu.seleccionar_elemento(biblioteca) 
    
        if seleccion == None:
            return
        elif hasattr(seleccion, "obtener_canciones"):
            reproducir_playlist(seleccion)
        else:
            reproducir_cancion(seleccion)
        
        

def reproducir_cancion(cancion):
    reproductor = Reproductor(cancion)
    reproductor.iniciar()
    print(str(cancion).upper()) #---LE DICE AL USUARIO LA CANCION_ESCOGIDA.
        
    while True:
        #---------PAUSA Y REANUDA LA CANCION---------#
        if keyboard.is_pressed("space"):
            reproductor.alternar_pausa()
            time.sleep(0.1)
                
        if not reproductor.actualizar():
            break
            
        time.sleep(0.03)

def reproducir_playlist(playlist):
    canciones_playlist = playlist.obtener_canciones()

    if not canciones_playlist: 
        print("Playlist vacia.")
        return False
    
    for cancion in canciones_playlist:
        reproducir_cancion(cancion)
    return True

    
