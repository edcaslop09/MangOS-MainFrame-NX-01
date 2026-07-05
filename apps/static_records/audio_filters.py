
import numpy as np



def convertir_a_mono(audio):
    if audio.ndim == 1:
        return audio
    return np.mean(audio, axis=1)

def convertir_a_estereo(audio):
    if audio.ndim ==2:
        return audio
    return np.column_stack((audio,audio))

def normalizar(audio):
    volumen_maximo = np.max(np.abs(audio))

    if volumen_maximo == 0:
        return audio
    return audio / volumen_maximo * 0.8

def bitcrush(audio,niveles=24):
    return np.round(audio*niveles) / niveles

def downsample_fake(audio,factor=8):
    audio_reducido = audio[::factor]
    audio_expandido= np.repeat(audio_reducido,factor)

    return audio_expandido[:len(audio)]

def suavizar(audio, intensidad=4):
    if intensidad <= 1:
        return audio

    kernel = np.ones(intensidad) / intensidad
    return np.convolve(audio, kernel, mode="same")



def flat(audio,sample_rate):
    return audio

def old_radio(audio,sample_rate):
    audio_mono = convertir_a_mono(audio)

    audio_filtrado = np.tanh(audio_mono * 4.0)
    audio_filtrado = downsample_fake(audio_filtrado,factor=10)
    audio_filtrado = bitcrush(audio_filtrado,niveles=10)
    audio_filtrado = audio_filtrado *0.6

    return convertir_a_estereo(audio_filtrado)

def phone_speaker(audio,sample_rate):
    audio_mono = convertir_a_mono(audio)

    audio_filtrado = np.tanh(audio_mono * 3.5)
    audio_filtrado = bitcrush(audio_filtrado,niveles=14)
    audio_filtrado = audio_filtrado *0.5

    return convertir_a_estereo(audio_filtrado)

def vinyl_warm(audio, sample_rate):
    audio_mono = convertir_a_mono(audio)

    audio_filtrado = suavizar(audio_mono, intensidad=6)
    audio_filtrado = np.tanh(audio_filtrado * 1.0)
    audio_filtrado = audio_filtrado * 0.8

    return convertir_a_estereo(audio_filtrado)

def cassette_tape(audio,sample_rate):
    audio_mono = convertir_a_mono(audio)

    audio_filtrado = suavizar(audio_mono, intensidad=12)
    audio_filtrado = downsample_fake(audio_filtrado,factor= 3)
    audio_filtrado = np.tanh(audio_filtrado * 2.2)
    audio_filtrado = audio_filtrado *0.7

    return convertir_a_estereo(audio_filtrado)

def night_drive(audio,sample_rate):
    audio_mono = convertir_a_mono(audio)

    audio_filtrado = suavizar(audio_mono,intensidad=4)
    audio_filtrado = np.tanh(audio_filtrado*1.4)
    audio_filtrado = audio_filtrado *0.9

    return convertir_a_estereo(audio_filtrado)

def vinyl_black_classic(audio,sample_rate):
    audio_mono = convertir_a_mono(audio)

    audio_filtrado = suavizar(audio_mono,intensidad=10)
    audio_filtrado = np.tanh(audio_filtrado*2.5)
    audio_filtrado = bitcrush(audio_filtrado,niveles=20)
    audio_filtrado = audio_filtrado *0.75

    return convertir_a_estereo(audio_filtrado)


FILTROS ={
    "flat":flat,
    "old_radio":old_radio,
    "phone_speaker":phone_speaker,
    "vinyl_warm":vinyl_warm,
    "cassette_tape":cassette_tape,
    "night_drive":night_drive,
    "vinyl_black_classic":vinyl_black_classic,
}

def obtener_filtros():
    return list(FILTROS.keys())


def existe_filtro(nombre):
    return nombre in FILTROS
    
def aplicar_filtro(audio, sample_rate, nombre_filtro, filtros_activados=True):
    if not filtros_activados:
        return audio
    if not nombre_filtro in FILTROS:
        return audio
    
    funcion_filtro = FILTROS[nombre_filtro]
    audio_filtrado = funcion_filtro(audio,sample_rate)
    audio_filtrado = normalizar(audio_filtrado)
    
    return audio_filtrado