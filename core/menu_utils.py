
def pedir_opcion(titulo, opciones):
    print(f"---------- {titulo.upper()} ----------")

    for (index, opcion) in enumerate(opciones, start=1):
        print(f"[{index}] {opcion}")

    while True:
        try:
            respuesta_usuario = input("Ingresa una de las opciones del menú: ")
            opcion = int(respuesta_usuario)
        except ValueError:
            print("Ingrese una opción válida.")
            continue 
        if opcion < 1 or opcion > len(opciones):
            print("Ingrese una opción válida.")
            continue

        return opcion 

def seleccionar_elemento(titulo, elementos, texto_vacio="No hay elementos."):

    if not elementos:
        print(texto_vacio)
        return None
    
    indice =pedir_opcion(titulo, elementos)
    indice_real = indice - 1
    elemento_elegido = elementos[indice_real]

    return elemento_elegido

def esperar_enter():
    while True:

        respuesta = input("Presiona Enter para continuar...")

        if not respuesta:
            return 

        print("Solo presiona Enter.")

