import os
import json
from datetime import datetime


class NotesManager:
    def __init__(self, ruta_archivo=os.path.join("data", "notes", "notes.json")):
        self.ruta_archivo = ruta_archivo
        self.crear_estructura()

    def crear_estructura(self):
        carpeta = os.path.dirname(self.ruta_archivo)

        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
                json.dump([], archivo, indent=4)

    def cargar_notas(self):
        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                notas = json.load(archivo)

            if type(notas) is not list:
                return []

            return notas

        except json.JSONDecodeError:
            return []

    def guardar_notas(self, notas):
        with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(notas, archivo, indent=4, ensure_ascii=False)

    def crear_nota(self, titulo, contenido):
        notas = self.cargar_notas()

        nueva_nota = {
            "id": self.generar_id(),
            "titulo": titulo,
            "contenido": contenido,
            "fecha_creacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        notas.append(nueva_nota)
        self.guardar_notas(notas)

        return nueva_nota

    def eliminar_nota(self, id_nota):
        notas = self.cargar_notas()

        notas_actualizadas = []

        for nota in notas:
            if nota["id"] != id_nota:
                notas_actualizadas.append(nota)

        self.guardar_notas(notas_actualizadas)

    def generar_id(self):
        notas = self.cargar_notas()

        if not notas:
            return 1

        ids = []

        for nota in notas:
            ids.append(nota["id"])

        return max(ids) + 1

    
        
        