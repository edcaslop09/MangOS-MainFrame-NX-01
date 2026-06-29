
def cargar_lrc(cancion):
    texto_tiempo=[]         

    with open(cancion.ruta_lrc,"r",encoding="utf-8") as archivo:
        for linea in archivo:

            linea = linea.strip()

            if linea =="" or "]" not in linea:
                continue
 
            partes= linea.split("]",1)

            tiempo= partes[0].replace("[", "")
            texto=partes[1].strip()

            tiempo= convertir_tiempo(tiempo)
            

            texto_tiempo.append((tiempo, texto))



    return texto_tiempo
    

def convertir_tiempo(texto_tiempo):
    minutos, segundos= texto_tiempo.split(":")

    minutos =int(minutos)
    segundos = float(segundos)

    segundos_totales =(minutos*60) +segundos 

    return segundos_totales
    