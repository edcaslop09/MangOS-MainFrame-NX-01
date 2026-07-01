import os 
from .playlist import Playlist

class PlaylistManager:

    def __init__(self):
        self.ruta_playlists = os.path.join("data","static_records","playlists")
        os.makedirs(self.ruta_playlists, exist_ok=True)
        self.playlists = []
        self.cargar_todas()

    def cargar_todas(self):
        self.playlists = []

        playlists = os.listdir(self.ruta_playlists)
        
        for archivo_playlists in playlists:
                if not archivo_playlists.endswith(".json"):
                    continue 
                nombre = archivo_playlists.removesuffix(".json")
                objeto_playlist = Playlist(nombre)
                objeto_playlist.cargar()
                self.playlists.append(objeto_playlist)
        

    def existe(self,nombre):
        for playlist in self.playlists:
            if playlist.nombre == nombre:
                return True 
        return False
    
    def crear(self,nombre):
        if not nombre:
            return None
        
        elif self.existe(nombre):
            return None 
        
        objeto_playlist = Playlist(nombre)
        objeto_playlist.guardar()
        self.playlists.append(objeto_playlist)

        return objeto_playlist
    
    def obtener_playlists(self):
        return self.playlists
    
    def eliminar(self,nombre):
        playlist_encontrada = None

        for playlist in self.playlists:
            if playlist.nombre == nombre:
                playlist_encontrada = playlist

        if playlist_encontrada == None:
            return False
        
        else:
            ruta_archivo_json = os.path.join(self.ruta_playlists,f"{nombre}.json")
            if os.path.exists(ruta_archivo_json):
                os.remove(ruta_archivo_json)
                self.playlists.remove(playlist_encontrada) 
                return True 
            
            return False
        
        
