from .audio_engine import AudioEngine
from . import audio_filters as af

engine = AudioEngine()

def iniciar_player():
    return True

def reproducir_cancion(cancion):
    if cancion.ruta_audio == None:
        return False
    resultado = engine.reproducir_archivo(cancion.ruta_audio,esperar=False)

    return resultado

def detener_cancion():
    engine.detener()



def obtener_tiempo_actual():
    return engine.obtener_tiempo()

def obtener_duracion(cancion):
    if cancion.ruta_audio == None:
        return 0
    
    resultado = engine.obtener_info(cancion.ruta_audio)

    if resultado == None:
        return 0

    return  resultado["duracion"]



def esta_reproduciendo():
    return engine.esta_reproduciendo()

def pausar():
    return False

def reanudar():
    return False

def musica_activa():
    return engine.esta_reproduciendo()

def pausar_cancion():
    return pausar()

def reanudar_cancion():
    return reanudar()

def obtener_filtros():
    return af.obtener_filtros()

def obtener_filtros_disponibles():
    lista_filtros_disponibles = obtener_filtros()
    return lista_filtros_disponibles

def filtros_estan_activados():
    return engine.filtros_activados

def activar_filtros():
    resultado = engine.activar_filtros()
    return resultado

def desactivar_filtros():
    resultado = engine.desactivar_filtros()
    return resultado

def cambiar_filtro(nombre_filtro):
    return engine.cambiar_filtro(nombre_filtro)

def obtener_filtro_actual():
    return engine.filtro_actual





    