from colorama import Fore, Style 
import json 


def cargar_json(ruta_json):
    try:
        with open(ruta_json,"r",encoding="utf-8") as archivo:
            reglas= json.load(archivo)

    except FileNotFoundError:
        reglas= {
            "base": "BLANCO",
            "palabras": {},
            "speakers": {}
            }
    return reglas 
    
def obtener_codigo_color(nombre_color):
    colores = {
    "BLANCO": Fore.WHITE,
    "GRIS": Fore.LIGHTBLACK_EX,
    "NEGRO": Fore.BLACK,

    "AMARILLO": Fore.YELLOW,
    "AMARILLO_CLARO": Fore.LIGHTYELLOW_EX,

    "AZUL": Fore.BLUE,
    "AZUL_CLARO": Fore.LIGHTBLUE_EX,

    "CELESTE": Fore.CYAN,
    "AQUA": Fore.LIGHTCYAN_EX,

    "VERDE": Fore.GREEN,
    "VERDE_CLARO": Fore.LIGHTGREEN_EX,

    "ROSA": Fore.LIGHTMAGENTA_EX,
    "MORADO": Fore.MAGENTA,
    
    "ROJO": Fore.RED,
    "ROJO_CLARO": Fore.LIGHTRED_EX,
    
    "NARANJA": "\033[38;2;255;140;0m"
    ,
    "NARANJA_CLARO": "\033[38;2;255;165;0m",
    "DORADO": "\033[38;2;255;215;0m",
    "TURQUESA": "\033[38;2;64;224;208m",
    "LIMA": "\033[38;2;50;205;50m",
    "VIOLETA": "\033[38;2;148;0;211m",
    "FUCSIA": "\033[38;2;255;20;147m",
    "CORAL": "\033[38;2;255;127;80m",
    }


    if nombre_color in colores:
        return colores[nombre_color]
    else:
        return Fore.WHITE


def colorear_linea(texto, reglas):

    nombre_color = reglas["base"]

    palabras_destacadas = reglas["palabras"]

    speakers = reglas["speakers"]
    

    for speaker in speakers:
        marcador = "["+speaker+"]"

        if texto.startswith(marcador):
           color_real = obtener_codigo_color(speakers.get(speaker))
           texto_sin_marcador = texto.replace(marcador,"")    
           return (color_real + texto_sin_marcador + Style.RESET_ALL)
    
    blanco_base = obtener_codigo_color(nombre_color)
    texto_base = (blanco_base+texto)
        
        
    for color in palabras_destacadas:
        palabras = palabras_destacadas.get(color)
            
        for palabra in palabras:
            if palabra in texto:
                color_real = obtener_codigo_color(color)
                texto_base = texto_base.replace(palabra,color_real + palabra + Style.RESET_ALL + blanco_base)
        
    return texto_base

        

def colorear_linea_parcial(texto, reglas, progreso):
    if progreso < 0:
        progreso = 0
    if progreso > 1:
        progreso = 1

    cantidad = int(len(texto) * progreso)
    texto_visible = texto[:cantidad]

    # Primero: revisar si es diálogo
    speakers = reglas["speakers"]

    for speaker in speakers:
        marcador = "[" + speaker + "]"
        
        if texto.startswith(marcador):
            texto_sin_marcador = texto.replace(marcador, "", 1)
            color_real = obtener_codigo_color(speakers.get(speaker))
            
            cantidad = int(len(texto_sin_marcador) * progreso)
            
            texto_visible = texto_sin_marcador[:cantidad]
            
            return color_real + texto_visible + Style.RESET_ALL

    # Si no es diálogo, usar color base
    nombre_color = reglas["base"]
    blanco_base = obtener_codigo_color(nombre_color)

    palabras_destacadas = reglas["palabras"]

    resultado = blanco_base

    i = 0

    while i < len(texto_visible):
        coloreado = False

        for color in palabras_destacadas:
            palabras = palabras_destacadas.get(color)

            for palabra in palabras:
                if texto.startswith(palabra, i):
                    color_real = obtener_codigo_color(color)

                    parte_visible = texto_visible[i:i + len(palabra)]

                    resultado += color_real + parte_visible + Style.RESET_ALL + blanco_base

                    i += len(parte_visible)
                    coloreado = True
                    break

            if coloreado:
                break

        if not coloreado:
            resultado += texto_visible[i]
            i += 1

    return resultado + Style.RESET_ALL


    

    
  


