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