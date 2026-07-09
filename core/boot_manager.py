import os 
import json 

from . import launcher

def cargar_configuracion():

    ruta_boot_config = os.path.join("data","system","boot_config.json")

    if not os.path.exists(ruta_boot_config):
        print("Archivo no encontrado.")
        return None 

    with open(ruta_boot_config,"r",encoding="utf-8")as archivo:
        configuracion = json.load(archivo)

    return configuracion

def mostrar_boot_sequence(configuracion):

    if configuracion == None:
        return None 

    show_boot_sequence = configuracion["show_boot_sequence"]

    if not show_boot_sequence:
        return None 

    system_name = configuracion["system_name"]
    system_version = configuracion["system_version"]
    boot_mode = configuracion["boot_mode"]

    print("---------- MangOS BOOT ----------")
    print(f"Boting {system_name}...")
    print(f"Version: {system_version}")
    print(f"Mode: {boot_mode}")
    print("Loading core system...")
    print("Checking startup services...")

    startup_services = configuracion["startup_services"]

    for service in startup_services:

        datos_servicio = startup_services[service]
        service_state = datos_servicio["enabled"]
    
        if service_state:
            print(f"{service}: enabled")
        else:
            print(f"{service}: disabled")
            

    print("System ready.")

def preparar_servicios(configuracion):
        
        if configuracion == None:
            return configuracion 

        startup_services = configuracion["startup_services"]

        servicios_preparados = [] 

        for servicio in startup_services:

            datos_servicio = startup_services[servicio]
            service_state = datos_servicio["enabled"]
            if service_state:
                print(f"Preparing service: {servicio}")
                servicios_preparados.append(servicio)
            else:
                print(f"Skipping service {servicio}")

        return servicios_preparados

def iniciar_mangos():
    configuracion = cargar_configuracion()

    if configuracion == None:
        print("Error. Configuracion vacia.")
        return False 

    mostrar_boot_sequence(configuracion)

    preparar_servicios(configuracion)

    print("Launching MangOS interface...")

    launcher.iniciar()
    return True 




# config = cargar_configuracion()
# mostrar_boot_sequence(config)
# servicios = preparar_servicios(config)
# print(servicios)