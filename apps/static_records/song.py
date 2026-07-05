import os 
import json 
from . import color_manager
from . import lrc_parser

def cargar_metadata(ruta_metadata):
    try: 
        with open(ruta_metadata,"r",encoding="utf-8")as archivo:
            metadata = json.load(archivo)
            return metadata
    except FileNotFoundError:
        
        
        metadata_por_defecto = {
            "titulo": "Desconocido",
            "artistas": ["Desconocido"],
            "album": "",
            "genero": "",
            "favorita": False,
            "veces_reproducida": 0
            } 
        
        return metadata_por_defecto
    
    except json.JSONDecodeError:
        
        metadata_por_defecto = {
            "titulo": "Desconocido",
            "artistas": ["Desconocido"],
            "album": "",
            "genero": "",
            "favorita": False,
            "veces_reproducida": 0
            } 
        
        return metadata_por_defecto



class Cancion:
    def __init__(self,carpeta):
        self.carpeta = carpeta 
        
        self.ruta_audio = self.buscar_audio()
        self.ruta_lrc = os.path.join(carpeta, "lyrics.lrc")
        self.ruta_colores = os.path.join(carpeta, "colors.json") 
        self.ruta_metadata = os.path.join(carpeta, "metadata.json")
        
        self.reglas_colores = color_manager.cargar_json(self.ruta_colores)
        self.metadata = cargar_metadata(self.ruta_metadata) 
        
        self.titulo = self.metadata.get("titulo", "Desconocido")
        
        self.artistas = self.metadata.get("artistas", ["Desconocido"])
        self.nombre_artistas = " ft ".join(self.artistas)
        
        self.album = self.metadata.get("album", "")
        self.genero = self.metadata.get("genero", "")
        self.favorita = self.metadata.get("favorita", False)
        self.veces_reproducida = self.metadata.get("veces_reproducida", 0)
        
        self.reproduccion_contada = False

    def buscar_audio(self):
        archivos_audio = [
            "original.flac",
            "song.flac",
            "song.wav",
            "song.mp3"
        ]

        for archivo_audio in archivos_audio:
            ruta = os.path.join(self.carpeta, archivo_audio)

            if os.path.exists(ruta):
                return ruta
        return None

    def tiene_audio(self):
        return self.ruta_audio is not None
    
    def __str__(self):
    
        return f"{self.titulo} - {self.nombre_artistas}"
    
    def obtener_letras(self):
        return lrc_parser.cargar_lrc(self)
            
    def guardar_metadata(self):
        metadata_actual = {
            "titulo":self.titulo,
            "artistas":self.artistas,
            "album":self.album,
            "genero":self.genero,
            "favorita":self.favorita,
            "veces_reproducida":self.veces_reproducida
        }
        
        with open(self.ruta_metadata,"w",encoding="utf-8") as archivo:
            json.dump(metadata_actual,archivo,sort_keys=True,indent=4)
    
    def iniciar_reproduccion(self):
        self.reproduccion_contada = False 
    
    def incrementar_reproduccion(self):
        
        if self.reproduccion_contada == False:
            self.veces_reproducida = self.veces_reproducida+1
            self.reproduccion_contada = True 
            self.guardar_metadata()

    def marcar_favorita(self):
        self.favorita = True
        self.guardar_metadata()
        
    def desmarcar_favorita(self):
        self.favorita = False
        self.guardar_metadata()

        
