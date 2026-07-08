import time
import msvcrt

from core.menu_utils import esperar_enter
from . import playlist_menu
from . import player
from .reproductor import Reproductor


FILTRO_RADIO = "vinyl_black_classic"


def leer_tecla_radio():
    if msvcrt.kbhit():
        tecla = msvcrt.getch().decode("utf-8", errors="ignore").lower()
        return tecla

    return None


def limpiar_buffer_teclas():
    while msvcrt.kbhit():
        msvcrt.getch()


def mostrar_controles():
    print("---------- VINYL BLACK.FM ----------")
    print("[F] Activar/desactivar filtro")
    print("[N] Siguiente canción")
    print("[S] Estado")
    print("[Q] Salir de la estación")


def mostrar_panel_radio(cancion, indice, total, mensaje=""):
    print()
    print("---------- VINYL BLACK.FM ----------")
    print(f"Transmitiendo: {cancion.titulo}")
    print(f"Progreso de playlist: {indice + 1}/{total}")
    print(f"Filtro actual: {player.obtener_filtro_actual()}")

    if player.filtros_estan_activados():
        print("Filtros: activados")
    else:
        print("Filtros: desactivados")

    print("[F] Activar/desactivar filtro | [N] Siguiente | [S] Estado | [Q] Salir")

    if mensaje:
        print(mensaje)


def configurar_sonido_radio():
    player.cambiar_filtro(FILTRO_RADIO)
    player.activar_filtros()


def alternar_filtro_radio():
    if player.filtros_estan_activados():
        player.desactivar_filtros()
        return "Filtro Vinyl Black desactivado. El cambio se aplicará en la siguiente canción."

    player.cambiar_filtro(FILTRO_RADIO)
    player.activar_filtros()
    return "Filtro Vinyl Black activado. El cambio se aplicará en la siguiente canción."


def generar_estado_radio(indice, total, cancion):
    if player.filtros_estan_activados():
        estado_filtros = "activados"
    else:
        estado_filtros = "desactivados"

    return (
        "---------- ESTADO VINYL BLACK.FM ----------\n"
        f"Canción: {cancion.titulo}\n"
        f"Progreso de playlist: {indice + 1}/{total}\n"
        f"Filtro actual: {player.obtener_filtro_actual()}\n"
        f"Filtros: {estado_filtros}"
    )


def transmitir_playlist(playlist):
    canciones = playlist.obtener_canciones()

    if not canciones:
        print("Esta playlist está vacía.")
        return False

    indice = 0
    estacion_activa = True
    mensaje_radio = ""
    mensaje_hasta = 0

    limpiar_buffer_teclas()

    while estacion_activa:
        cancion = canciones[indice]

        reproductor = Reproductor(cancion)
        reproductor.iniciar()

        while True:
            if not reproductor.actualizar():
                break

            if mensaje_radio and time.time() > mensaje_hasta:
                mensaje_radio = ""

            mostrar_panel_radio(cancion, indice, len(canciones), mensaje_radio)

            tecla = leer_tecla_radio()

            if tecla == "f":
                mensaje_radio = alternar_filtro_radio()
                mensaje_hasta = time.time() + 4

            elif tecla == "s":
                mensaje_radio = generar_estado_radio(indice, len(canciones), cancion)
                mensaje_hasta = time.time() + 4

            elif tecla == "n":
                mensaje_radio = "Saltando a la siguiente canción..."
                mensaje_hasta = time.time() + 2
                player.detener_cancion()
                break

            elif tecla == "q":
                mensaje_radio = "Apagando Vinyl Black.FM..."
                mensaje_hasta = time.time() + 2
                player.detener_cancion()
                estacion_activa = False
                break

            time.sleep(0.03)

        if estacion_activa:
            indice = (indice + 1) % len(canciones)

    player.detener_cancion()
    limpiar_buffer_teclas()
    print("Estación apagada...")
    return True


def iniciar():
    print("---------- VINYL BLACK.FM ----------")
    print("VIRTUAL RADIO STATION BY STATIC RECORDS")

    playlist = playlist_menu.seleccionar_playlist()

    if playlist is None:
        return None

    canciones = playlist.obtener_canciones()

    if not canciones:
        print("La playlist está vacía.")
        esperar_enter()
        return None

    configurar_sonido_radio()

    print(f"Iniciando con... {playlist.nombre}")
    print(f"La transmisión cuenta con: {len(canciones)} canciones cargadas.")
    mostrar_controles()
    esperar_enter("Presiona Enter para iniciar transmisión...")

    transmitir_playlist(playlist)

    return None