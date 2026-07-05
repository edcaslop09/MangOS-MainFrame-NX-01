import soundfile as sf
from . import audio_filters as af 

import sounddevice as sd
import os 
import time 

class AudioEngine:
    def __init__(self):
        self.filtro_actual = "flat"
        self.filtros_activados = False 

        self.audio_actual = None
        self.sample_rate_actual = None
        self.ruta_actual = None
        self.duracion_actual = 0.0
        self.tiempo_inicio = None
        self.reproduciendo =  False


    def activar_filtros(self):
        self.filtros_activados = True 
        return self.filtros_activados
    
    def desactivar_filtros(self):
        self.filtros_activados = False
        return self.filtros_activados

    def cambiar_filtro(self, nombre_filtro):
        
        if af.existe_filtro(nombre_filtro): 
            self.filtro_actual = nombre_filtro
            return True 

        return False 

    def obtener_info(self,ruta_audio):
        if os.path.exists(ruta_audio):
            info = sf.info(ruta_audio)
            informacion_tecnica = {
                "archivo": ruta_audio,
                "formato": info.format,
                "subformato": info.subtype,
                "sample_rate": info.samplerate,
                "canales": info.channels,
                "frames" : info.frames,
                "duracion": info.duration
            }
            return informacion_tecnica
        return None 

    def cargar_audio(self,ruta_audio):
        if os.path.exists(ruta_audio):
            audio, sample_rate = sf.read(ruta_audio)

            return audio, sample_rate
        return None,None

    def reproducir_archivo(self,ruta_audio, esperar=False):

        audio, sample_rate = self.cargar_audio(ruta_audio)

        if audio is None or sample_rate is None:
            return False
        
        audio_procesado = af.aplicar_filtro(
            audio,
            sample_rate,
            self.filtro_actual,
            self.filtros_activados
        )

        
        calcular_duracion = len(audio_procesado) / sample_rate

        sd.stop()
        sd.play(audio_procesado,sample_rate)


        self.audio_actual = audio_procesado
        self.sample_rate_actual = sample_rate
        self.ruta_actual = ruta_audio
        self.duracion_actual = calcular_duracion
        self.tiempo_inicio =time.time()
        self.reproduciendo = True

        if esperar:
            sd.wait()
            self.reproduciendo = False

        return True 
        
    def detener(self):
        sd.stop()

        
        self.audio_actual = None
        self.sample_rate_actual = None
        self.ruta_actual = None
        self.duracion_actual = 0.0
        self.tiempo_inicio = None
        self.reproduciendo =  False

    def obtener_tiempo(self):
        if self.reproduciendo == False or self.tiempo_inicio == None:
            return 0

        tiempo_actual = time.time() -self.tiempo_inicio

        if tiempo_actual >= self.duracion_actual:
            self.reproduciendo = False
            return self.duracion_actual

        return tiempo_actual

    def esta_reproduciendo(self):
        if self.reproduciendo == False or self.tiempo_inicio == None:
            return False

        tiempo_actual = time.time()-self.tiempo_inicio

        if tiempo_actual >= self.duracion_actual:
            self.reproduciendo = False
            return False

        return True 


