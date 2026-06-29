import os 
import music.song as song
import random 

class Biblioteca:
    
    def __init__(self,songs):
        
        self.ruta_biblioteca = songs
        self.cargar_canciones()
    
    def cargar_canciones(self):
        
        self.canciones= []
        
        canciones = os.listdir(self.ruta_biblioteca)
        
        for cancion in canciones:
            ruta_cancion = os.path.join(self.ruta_biblioteca, cancion)
            if os.path.isdir(ruta_cancion):
                objeto_cancion = song.Cancion(ruta_cancion) 
                self.canciones.append(objeto_cancion)
        self.ordenar_canciones()
        
    def ordenar_canciones(self):
        self.canciones.sort(
            key=lambda x: x.titulo
            )
        
    
    def obtener_por_artista(self,usuario_busqueda):
        usuario_busqueda = (usuario_busqueda.strip()).lower()
        resultados_busqueda_por_artista = []
        
        for cancion in self.canciones:
            if usuario_busqueda in cancion.nombre_artistas.lower():
                resultados_busqueda_por_artista.append(cancion)
                
        return resultados_busqueda_por_artista
    
    def obtener_por_titulo(self,usuario_busqueda):
        usuario_busqueda = (usuario_busqueda.strip()).lower()
        resultados_busqueda_por_titulo = []
        
        for cancion in self.canciones:
            if usuario_busqueda in cancion.titulo.lower():
                resultados_busqueda_por_titulo.append(cancion)
                
        return resultados_busqueda_por_titulo
    
    def obtener_por_album(self,usuario_busqueda):
        usuario_busqueda = (usuario_busqueda.strip()).lower()
        resultados_busqueda_por_album = []
        
        for cancion in self.canciones:
            if usuario_busqueda in cancion.album.lower(): 
                resultados_busqueda_por_album.append(cancion)
                
        return resultados_busqueda_por_album
    
    def obtener_por_genero(self,usuario_busqueda):
        usuario_busqueda = (usuario_busqueda.strip()).lower()
        resultados_busqueda_por_genero = []
        
        for cancion in self.canciones:
            if usuario_busqueda in cancion.genero.lower():
                resultados_busqueda_por_genero.append(cancion)
        
        return resultados_busqueda_por_genero
    
    def buscar(self,usuario_busqueda):
        usuario_busqueda = (usuario_busqueda.strip()).lower()
        resultados_busqueda = []
        
        
        resultados_artista = self.obtener_por_artista(usuario_busqueda)
        resultados_titulo = self.obtener_por_titulo(usuario_busqueda)
        resultados_album = self.obtener_por_album(usuario_busqueda)
        resultados_genero = self.obtener_por_genero(usuario_busqueda)
        
        resultados_busqueda = (resultados_artista + resultados_titulo + resultados_album + resultados_genero)
        resultados_busqueda = list(set(resultados_busqueda))
            
    
        return resultados_busqueda
    
    def obtener_favoritas(self):
        
        resultado_favoritas = []
        
        for cancion in self.canciones:
            if cancion.favorita:
                resultado_favoritas.append(cancion)
                
        
        return resultado_favoritas
    
    
    def marcar_favorita(self, cancion):
        cancion.marcar_favorita()
    
    def desmarcar_favorita(self, cancion):
        cancion.desmarcar_favorita()
        
    def alternar_favorita(self, cancion):
        if cancion.favorita:
            cancion.desmarcar_favorita()
        else:
            cancion.marcar_favorita()
    
    def obtener_aleatoria(self):
        if self.canciones:
            return (random.choice(self.canciones))
        else:
            return None 
    
    

    