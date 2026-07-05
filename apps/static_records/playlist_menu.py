from .playlist_manager import PlaylistManager

def menu_playlists():
    titulo = "---------- PLAYLISTS ----------"
    opciones_menu = ["Crear playlist","Ver playlists","Eliminar playlist","Regresar"]

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
    
def iniciar():
    manager = PlaylistManager()
    
    
    while True:
        opcion =menu_playlists()

        if opcion == 1:
            nombre_playlist = str(input("Ingresa nombre de la playlist: "))
            nombre_playlist = nombre_playlist.strip()

            objeto_playlist = manager.crear(nombre_playlist)

            if not objeto_playlist:
                print(f"No se pudo crear la playlist.")
            elif objeto_playlist:
                print(f"Se ha creado con exito la playlist {nombre_playlist}.")
            
            input("Presione Enter para continuar...")
            continue
        
        elif opcion == 2:
            playlists = manager.obtener_playlists()

            if not playlists:
                print("No hay playlists creadas.")
            else:
                for (index,playlist) in enumerate(playlists,start=1):
                    print(f"[{index}] {playlist.nombre} - {playlist.cantidad()} canciones.")
            input("Presione Enter para continuar...")
            continue

        elif opcion == 3:
            playlists = manager.obtener_playlists()

            if not playlists:
                print("No hay playlists.")
                input("Presione Enter para continuar...")
                continue
            
            print("---------- TUS PLAYLISTS ----------")
            for (index,playlist) in enumerate(playlists,start=1):
                print(f"[{index}] {playlist}")
            
            while True:
                try:
                    respuesta_usuario = int(input("Selecciona alguna de las opciones: "))
                except ValueError:
                    print("Ingrese una opcion valida.")
                    continue
                if respuesta_usuario < 1 or respuesta_usuario > len(playlists):
                    print("Ingrese una opcion valida.")
                    continue
                
                indice_real = respuesta_usuario-1

                playlist_escogida = playlists[indice_real]

                eliminacion = manager.eliminar(playlist_escogida.nombre)
                if eliminacion:
                    print("Playlist eliminada con exito.")
                    input("Presione Enter para continuar...")
                    break
                else:
                    print("No se pudo eliminar")
                    input("Presione Enter para continuar...")
                    break


        elif opcion == 4:
            return 

def agregar_cancion_a_playlist(cancion):

    manager = PlaylistManager()

    playlists = manager.obtener_playlists()

    if not playlists:
        print("No hay playlists creadas.")
        return False
    print("---------- PLAYLISTS ----------")
    for (index,playlist) in enumerate(playlists, start=1):
        print(f"[{index}] {playlist.nombre} - {playlist.cantidad()}")

    while True:

        try:
            respuesta_usuario = int(input("Selecciona alguna de las opciones del menú: "))
        except ValueError:
            print("Ingrese una opción valida.")
            continue 

        if respuesta_usuario < 1 or respuesta_usuario > len(playlists):
            print("Ingrese una opción valida.")
            continue 

        indice_real = respuesta_usuario - 1
        playlist_elegida = playlists[indice_real]

        playlist_elegida.agregar_cancion(cancion)
        playlist_elegida.guardar()

        print(f"Canción agregada a {playlist_elegida.nombre}.")
        return True

def seleccionar_playlist():
    manager = PlaylistManager()

    playlists = manager.obtener_playlists()

    if not playlists:
        print("No se ha encontrado ninguna playlist.")
        return None
    print("---------- PLAYLISTS ----------")

    for (index,playlist) in enumerate(playlists,start=1):
        print(f"[{index}] {playlist.nombre}")

    while True:
        try:
            respuesta_usuario = input("Selecciona una de las opciones del menu: ")
            opcion = int(respuesta_usuario)
        except ValueError:
            print("Ingrese una opción valida.")
            continue
        if opcion < 1 or opcion > len(playlists):
            print("Ingrese una opción valida.")
            continue

        indice_real = opcion -1 
        playlist_elegida = playlists[indice_real]

        return playlist_elegida

    



