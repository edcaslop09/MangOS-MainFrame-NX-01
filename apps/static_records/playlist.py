
import random
import json
import os

class Playlist():
    def __init__(self,nombre):
        self.nombre = nombre 
        self.canciones = []
        self.ruta_playlist = os.path.join("playlists",f"{self.nombre}.json" )
    
    def agregar_cancion(self,cancion):
        if cancion not in self.canciones:
            self.canciones.append(cancion)
    
    def eliminar_cancion(self,cancion):
        if cancion in self.canciones:
            self.canciones.remove(cancion)
    
    def obtener_canciones(self):
        return self.canciones
    
    def cantidad(self):
        return len(self.canciones)
    
    def esta_vacia(self):
        return not self.canciones
    
    def vaciar(self):
        self.canciones = []
    
    
    def mezclar(self):
        random.shuffle(self.canciones)
    
    def __str__(self):
        return f"{self.nombre} - {self.cantidad()}"
    
    def guardar(self):
        playlist_actual = {}

        playlist_actual["nombre"] = self.nombre


        canciones = []
        for cancion in self.canciones:
            canciones.append(cancion.carpeta)
        
        playlist_actual["canciones"] = canciones
        
        

        with open (self.ruta_playlist,"w",encoding="utf-8") as archivo:
            if 
            json.dump(playlist_actual,archivo,indent=4)





