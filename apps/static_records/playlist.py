
import random
import json
import os
from .song import Cancion 

class Playlist():
    def __init__(self,nombre):
        self.nombre = nombre 
        self.canciones = []
        self.ruta_playlist = os.path.join("data/static_records/playlists",f"{self.nombre}.json" )
    
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
        
        os.makedirs("data/static_records/playlists", exist_ok=True)
        
        with open (self.ruta_playlist,"w",encoding="utf-8") as archivo:
            
            json.dump(playlist_actual,archivo,indent=4)
    
    def cargar(self):
        if not os.path.exists(self.ruta_playlist):
            return  
        
        with open(self.ruta_playlist,"r",encoding="utf-8") as archivo:
            playlist_actual = json.load(archivo)

        self.nombre = playlist_actual["nombre"]
        ruta_canciones = playlist_actual["canciones"]
        
        self.canciones = []

        for ruta in ruta_canciones:
            if os.path.exists(ruta):
                cancion = Cancion(ruta)
                self.canciones.append(cancion)
            





