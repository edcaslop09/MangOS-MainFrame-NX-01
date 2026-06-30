import os 
import random 
from .song import Cancion
from data import static_records


class Biblioteca:
    
    def __init__(self,ruta_data_static_records):
        
        self.ruta_biblioteca = ruta_data_static_records
        self.cargar_canciones()
        self.construir_indices()


    def construir_indices(self):
        self.indice_genero = self.construir_indices_genero()
        self.indice_artista = self.construir_indices_artista()
        self.indice_album = self.construir_indices_album()
        self.indice_titulo = self.construir_indices_titulo()
    

    def construir_indices_genero(self):
        indices_genero = {}
        for cancion in self.canciones:
            genero = cancion.genero.strip().lower()
            if not genero in indices_genero:
                indices_genero[genero] = []
            indices_genero[genero].append(cancion)
        return indices_genero
    
    def construir_indices_artista(self):
        indices_artista = {}
        for cancion in self.canciones:
            for artista in cancion.artistas:
                artista = artista.strip().lower()
                if not artista in indices_artista:
                    indices_artista[artista] = []
                indices_artista[artista].append(cancion)
        return indices_artista

    def construir_indices_album(self):
        indices_album = {}
        for cancion in self.canciones:
            album = cancion.album.strip().lower()
            if not album in indices_album:
                indices_album[album] = []
            indices_album[album].append(cancion)
        return indices_album
    
    def construir_indices_titulo(self):
        indices_titulo = {}
        for cancion in self.canciones:
            titulo = cancion.titulo.strip().lower()
            if not titulo in indices_titulo:
                indices_titulo[titulo] = []
            indices_titulo[titulo].append(cancion)
        return indices_titulo



    
    def cargar_canciones(self):
        
        self.canciones= []
        
        canciones = os.listdir(self.ruta_biblioteca)
        
        for cancion in canciones:
            ruta_cancion = os.path.join(self.ruta_biblioteca, cancion)
            if os.path.isdir(ruta_cancion):
                ruta_mp3 = os.path.join(ruta_cancion,"song.mp3")
                ruta_lrc = os.path.join(ruta_cancion,"lyrics.lrc")
                ruta_metadata = os.path.join(ruta_cancion,"metadata.json")
                ruta_colores = os.path.join(ruta_cancion,"colors.json")

                if not  os.path.exists(ruta_mp3):
                    continue 
                if not os.path.exists(ruta_lrc):
                    continue
                if not os.path.exists(ruta_metadata):
                    continue
                if not os.path.exists(ruta_colores):
                    continue 

                objeto_cancion = Cancion(ruta_cancion) 
                self.canciones.append(objeto_cancion)
        self.ordenar_canciones()
        
    def ordenar_canciones(self):
        self.canciones.sort(
            key=lambda x: x.titulo
            )
        
    
    def obtener_por_artista(self,usuario_busqueda):
        usuario_busqueda = (usuario_busqueda.strip()).lower()
        
        if usuario_busqueda in self.indice_artista:
            return self.indice_artista[usuario_busqueda]
        else:
            return []
            

    
    def obtener_por_titulo(self,usuario_busqueda):
        usuario_busqueda = (usuario_busqueda.strip()).lower()
        
        
        if usuario_busqueda in self.indice_titulo:
            return self.indice_titulo[usuario_busqueda]
        else:
            return []
    
    def obtener_por_album(self,usuario_busqueda):
        usuario_busqueda = (usuario_busqueda.strip()).lower()

        if usuario_busqueda in self.indice_album:
            return self.indice_album[usuario_busqueda]
        else:
            return []
    
    def obtener_por_genero(self,usuario_busqueda):
        usuario_busqueda = (usuario_busqueda.strip()).lower()

        if usuario_busqueda in self.indice_genero:
            return self.indice_genero[usuario_busqueda]
        else:
            return []
    
    def buscar(self,usuario_busqueda):
        usuario_busqueda = (usuario_busqueda.strip()).lower()
        resultados_busqueda = []
        
        
        resultados_artista = self.obtener_por_artista(usuario_busqueda)
        resultados_titulo = self.obtener_por_titulo(usuario_busqueda)
        resultados_album = self.obtener_por_album(usuario_busqueda)
        resultados_genero = self.obtener_por_genero(usuario_busqueda)
        
        resultados_busqueda = (resultados_artista + resultados_titulo + resultados_album + resultados_genero)
        resultados_busqueda = self.quita_duplicados(resultados_busqueda)
            
    
        return resultados_busqueda
    
    def obtener_favoritas(self):
        
        resultado_favoritas = []
        
        for cancion in self.canciones:
            if cancion.favorita:
                resultado_favoritas.append(cancion)
            
        resultado_favoritas.sort(key=lambda x: x.titulo)
        
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
    
    def quita_duplicados(self,resultados_busqueda):
        resultados_sin_duplicados = []
        for cancion in resultados_busqueda:
            if cancion not in resultados_sin_duplicados:
                resultados_sin_duplicados.append(cancion)

        return resultados_sin_duplicados 
    
    def obtener_todas(self,):
        return self.canciones
    
    def esta_vacia(self):
        return not self.canciones
        
    
    def cantidad(self):
            return len(self.canciones)
    
    def recargar(self):
        self.cargar_canciones()
        self.construir_indices()

    