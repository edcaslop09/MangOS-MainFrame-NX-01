
from apps.static_records import static_records_core
import sys


def menu_launcher():
    titulo = "---------- MangOS Main Menú----------"
    opciones_menu = ["STATIC RECORDS","NOTAS","FILES","AI","SETTINGS","SALIR"]
    
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
    
def elegir_modulo():
        opcion = menu_launcher()
        if opcion == 1:
            static_records_core.iniciar()
        if opcion == 2:
            print("Modulo en Desarollo")
            input("Presiona Enter para continuar...")
            return  
        if opcion == 3:
            print("Modulo en Desarollo")
            input("Presiona Enter para continuar...")
            return 
        if opcion == 4:
            print("Modulo en Desarollo")
            input("Presiona Enter para continuar...")
            return
        if opcion == 5:
            print("Modulo en Desarollo")
            input("Presiona Enter para continuar...")
            return 
        if opcion == 6:
            sys.exit()

def iniciar():
    while True:
        elegir_modulo()