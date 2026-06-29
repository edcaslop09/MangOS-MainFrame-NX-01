from . import player
from . import display


class Reproductor():
    def __init__(self, cancion):
        self.cancion_actual = cancion
        self.letras = self.cancion_actual.obtener_letras()
        self.duracion_total = player.obtener_duracion(self.cancion_actual)
        self.pause = False
    
    def iniciar(self):
        self.cancion_actual.iniciar_reproduccion()
        player.iniciar_player()
        player.reproducir_cancion(self.cancion_actual)
    
    def obtener_tiempo_actual(self):
        tiempo_actual = player.obtener_tiempo_actual()
        return tiempo_actual
    
    
    def verificar_reproduccion(self,tiempo_actual):
        tiempo_restante = self.duracion_total - tiempo_actual
        
        if tiempo_restante <= 15:
            self.cancion_actual.incrementar_reproduccion() 
        
    def obtener_indice_actual(self,tiempo_actual):
        indice_actual = -1
        for indice, (tiempo, _) in enumerate(self.letras):
            if tiempo <= tiempo_actual:
                indice_actual = indice
            
            if tiempo > tiempo_actual:
                break
            
        return indice_actual
    
    def preparar_lineas(self,indice_actual):
        i_anterior = ""
        i_actual = self.letras[indice_actual][1]
        i_siguiente = ""
        
        if indice_actual > 0:
            i_anterior = self.letras[indice_actual - 1][1]
        if indice_actual < len(self.letras) - 1:
            i_siguiente = self.letras[indice_actual + 1][1]
            
        return i_anterior,i_actual,i_siguiente
        
    def calcular_progreso_letra(self,indice_actual,tiempo_actual):
        tiempo_inicio_actual = self.letras[indice_actual][0]
        tiempo_inicio_siguiente = (
            self.letras[indice_actual + 1][0]
            if indice_actual < len(self.letras) - 1
            else tiempo_inicio_actual + 5
            )
        
        duracion_disponible = tiempo_inicio_siguiente - tiempo_inicio_actual
        duracion_efecto = min(duracion_disponible, 1.2)
        progreso = (tiempo_actual - tiempo_inicio_actual) / duracion_efecto 
        progreso = min(progreso, 1)
        
        return progreso
    
    def mostrar(self,tiempo_actual):
        
        indice_actual = self.obtener_indice_actual(tiempo_actual)
        
        if indice_actual == -1:
            
            return 
        
        i_anterior, i_actual, i_siguiente = self.preparar_lineas(indice_actual)
        
        progreso = self.calcular_progreso_letra(indice_actual, tiempo_actual)
        
        display.mostrar_pantalla(
            i_anterior,
            i_actual,
            i_siguiente,
            self.cancion_actual,
            progreso,
            tiempo_actual,
            self.duracion_total
        )
    def actualizar(self):
        
        tiempo_actual = self.obtener_tiempo_actual()
        
        self.verificar_reproduccion(tiempo_actual)
        
        self.mostrar(tiempo_actual)
        
        if not player.musica_activa() and not self.pause:
            return False  
        
        return True
    
    def alternar_pausa(self):
        
        if self.pause == False :
            player.pausar_cancion()
            self.pause = True

        else:
            player.reanudar_cancion()
            self.pause = False 


