from .audio_engine import AudioEngine


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
    pausar()

def reanudar_cancion():
    reanudar()


    