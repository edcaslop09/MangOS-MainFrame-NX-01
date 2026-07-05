from . import playlist_menu 
from . import filter_menu
def menu_principal():
    titulo = "---------- STATIC RECORDS----------"
    opciones_menu = ["Ver canciones","Buscar canción","Playlists","Reproducir playlist","Audio Filters","Favoritas","Aleatoria","Salir"]
    
    print(titulo)
    for (index,opcion) in enumerate(opciones_menu, start=1):
        print(f"[{index}] {opcion}")
        
    while True:
        try:
            respuesta_usuario = int(input("Seleccione una de las opciones del menú: "))
        except ValueError:
            print("Ingrese una opcion valida.")
            continue
        
        if respuesta_usuario < 1 or respuesta_usuario > len(opciones_menu):
            print("Ingrese una opcion valida.")
            continue
        
        return respuesta_usuario

def seleccionar_cancion(lista_canciones):
    if not lista_canciones:
        print("No se encontro ningun elemento.")
        return None
    
    if lista_canciones:
        for (index,cancion) in enumerate(lista_canciones,start=1):
            print(f"[{index}] {cancion}")
        while True:
            try:
                respuesta_usuario = int(input("Seleccione una de las canciones: "))
            except ValueError:
                print("Ingrese una opcion valida.")
                continue
                
            if respuesta_usuario < 1 or respuesta_usuario > len(lista_canciones):
                print("Ingrese una opcion valida.")
                continue
                
            indice_real = respuesta_usuario-1
                
            return lista_canciones[indice_real]

def acciones_cancion(cancion):
    opciones = ["Reproducir","Agregar a playlist","Regresar"]
    

    print("---------- CANCIÓN ----------")

    for (index,opcion) in enumerate(opciones,start=1):
        print(f"[{index}] {opcion}")

    while True:
        try:
            respuesta_usuario = (input("Seleccione una opción del menú: "))
            opcion =int(respuesta_usuario)
        except ValueError:
            print("Ingrese una opción valida.")
            continue
        if opcion < 1 or opcion > len(opciones):
            print("Ingrese una opción valida.")
            continue
    
        if opcion == 1:
            return cancion

        if opcion == 2:
            playlist_menu.agregar_cancion_a_playlist(cancion)
            input("Presiona Enter para continuar...")
            return None

        if opcion == 3:
            return None



def seleccionar_elemento(biblioteca):
    while True:
        opcion = menu_principal()
        
        if opcion == 1:
            seleccion = seleccionar_cancion(biblioteca.canciones)

            if seleccion:
                resultado = acciones_cancion(seleccion)
                if resultado:
                    return resultado
                
            elif not seleccion:
                continue
        
        if opcion == 2:
            texto_busqueda = input("ingresa texto de busqueda: ")
            texto_busqueda = str(texto_busqueda)
            resultados = biblioteca.buscar(texto_busqueda)

            if resultados:
                seleccion = seleccionar_cancion(resultados)

                if seleccion:
                    resultado = acciones_cancion(seleccion)
                    if resultado:
                        return resultado
                    
            elif not resultados:
                print("No se han encontrado ningun resultados.")
                input("Presiona Enter para continuar...")
                continue 
        
        if opcion == 3:
            playlist_menu.iniciar()
            continue

        if opcion == 4:
            playlist = playlist_menu.seleccionar_playlist()

            if playlist:
                return playlist
            continue

        if opcion == 5:
            filter_menu.iniciar()
            continue 

        if opcion == 6:
            favoritas = biblioteca.obtener_favoritas()

            if favoritas:
                favoritas = seleccionar_cancion(resultados)
                
                if favoritas:
                    seleccion = acciones_cancion(seleccion)
                    if seleccion:
                        return seleccion
                    
            elif not favoritas:
                print("No se han encontrado ningun resultados.")
                input("Presiona Enter para continuar...")
                continue 
        
        if opcion == 7:
            aleatorio = biblioteca.obtener_aleatoria()

            if aleatorio:
                resultado = acciones_cancion(aleatorio)

                if resultado:
                    return resultado

                else:
                    continue

            elif not aleatorio:
                print("No se han encontrado ningun resultados.")
                input("Presiona Enter para continuar...")
                continue 
        
        
        if opcion == 8:
            return None

