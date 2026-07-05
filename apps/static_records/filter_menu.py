from . import player

def mostrar_estado():
    filtro_actual = player.obtener_filtro_actual()
    filtros_activados = player.filtros_estan_activados()

    
    print(f"Filtro actual: {filtro_actual}\nFiltros activados: {filtros_activados}")


def menu_filtros():
    opciones = ["Activar filtros","Desactivar filtros", "Cambiar filtro", "Regresar"]

    print("---------- AUDIO FILTERS ----------")
    mostrar_estado()

    for (index,opcion) in enumerate(opciones,start=1):
        print(f"[{index}] {opcion}")
    while True:
        try:
            respuesta_usuario = int(input("Selecciona una opción del menú: "))
        except ValueError:
            print("Ingrese una opcion valida.")
            continue 
        if respuesta_usuario > len(opciones) or respuesta_usuario < 1:
            print("Ingrese una opcion valida.")
            continue 

        return respuesta_usuario

def seleccionar_filtro():
    lista_filtros = player.obtener_filtros_disponibles()

    for (index,filtro) in enumerate(lista_filtros,start=1):
        print(f"[{index}] {filtro}")
    while True:
        try:
            respuesta_usuario = int(input("Selecciona una opción del menú: "))
        except ValueError:
            print("Ingresa una opción valida.")
            continue 
        if respuesta_usuario > len(lista_filtros) or respuesta_usuario < 1:
            print("Ingresa una opción valida.")
            continue

        indice_real = respuesta_usuario - 1

        filtro_elegido = lista_filtros[indice_real]

        cambio = player.cambiar_filtro(filtro_elegido)

        if cambio == True:
            player.activar_filtros()
            print("Filtro cambiado y activado.")

            break
        print("No se pudo cambiar el filtro.")

def iniciar():

    while True:

        opcion = menu_filtros()

        if opcion == 1:
            player.activar_filtros()
            print("Filtros activados.")
            input("Presiona Enter para continuar...")
            continue

        if opcion == 2:
            player.desactivar_filtros()
            print("Filtros desactivados.")
            input("Presiona Enter para continuar...")
            continue

        if opcion == 3:
            seleccionar_filtro()
            input("Presiona Enter para continuar...")
            continue 

        if opcion == 4:
            return 


        

        