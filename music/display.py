
from  colorama import Fore,Style

from . import color_manager 


def obtener_texto_parcial(texto, progreso):
    
    if progreso < 0:
        progreso= 0
    if progreso > 1:
        progreso=1
        

    longitud =len(texto)
    caracteres_a_mostrar =int(longitud*progreso)

    return texto[:caracteres_a_mostrar]

def mostrar_pantalla(i_anterior, i_actual, i_siguiente, cancion, progreso, tiempo_actual, duracion_total):
    
    i_actual = color_manager.colorear_linea_parcial(i_actual, cancion.reglas_colores, progreso)

    limpiar_pantalla()
    
    barra_progreso = crear_barra_progreso(tiempo_actual,duracion_total)
    
    print(barra_progreso)
    print()

    print(Fore.LIGHTBLACK_EX + i_anterior + Style.RESET_ALL)
    print()

    print(i_actual)

    print()
    print()

    print(Fore.LIGHTBLACK_EX + i_siguiente + Style.RESET_ALL)

def formatear_tiempo(segundos):
    minutos = int(segundos // 60)
    segundos_restantes = int(segundos % 60)
    return f"{minutos:02}:{segundos_restantes:02}"

def crear_barra_progreso(tiempo_actual,duracion_total):
    l_de_barra= 20

    bloques_llenos=int((tiempo_actual/duracion_total)*l_de_barra)
    bloques_vacios=l_de_barra-bloques_llenos

    barra = f"[{'█' * bloques_llenos}{'-' * bloques_vacios}][{formatear_tiempo(tiempo_actual)}/{formatear_tiempo(duracion_total)}]"

    return barra

def limpiar_pantalla():
    print("\033[H\033[J", end="")

