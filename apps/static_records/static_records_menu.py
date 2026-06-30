
def menu_principal():
    opciones_menu = ["Ver canciones","Buscar canción","Favoritas","Aleatoria","Salir"]
    
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
            
def elegir_cancion(biblioteca):
    while True:
        opcion = menu_principal()
        
        if opcion == 1:
            seleccion = seleccionar_cancion(biblioteca.canciones)
            if seleccion:
                return seleccion
            elif not seleccion:
                continue
        
        if opcion == 2:
            texto_busqueda = input("ingresa texto de busqueda: ")
            texto_busqueda = str(texto_busqueda)
            resultados = biblioteca.buscar(texto_busqueda)
            if resultados:
                return seleccionar_cancion(resultados)
            elif not resultados:
                print("No se han encontrado ningun resultados.")
                input("Presiona Enter para continuar...")
                continue 

        if opcion == 3:
            favoritas = biblioteca.obtener_favoritas()
            if favoritas:
                return seleccionar_cancion(favoritas)
            elif not favoritas:
                print("No se han encontrado ningun resultados.")
                input("Presiona Enter para continuar...")
                continue 
        
        if opcion == 4:
            aleatorio = biblioteca.obtener_aleatoria()

            if aleatorio:
                return seleccionar_cancion(aleatorio)
            elif not aleatorio:
                print("No se han encontrado ningun resultados.")
                input("Presiona Enter para continuar...")
                continue 
        
        
        if opcion == 5:
            return None

    