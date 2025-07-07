import json
import os

# 👇 Función limpiar_pantalla definida FUERA de la clase
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

class PlaylistManager:
    def __init__(self, archivo="playlist.json"):
        self.archivo = archivo
        self.playlist = []
        self.cargar_playlist()

    def cargar_playlist(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r", encoding="utf-8") as f:
                try:
                    self.playlist = json.load(f)
                    print("Playlist cargada desde archivo.\n")
                except json.JSONDecodeError:
                    self.playlist = []
                    print("Archivo corrupto o vacío. Se inicia playlist vacía.\n")
        else:
            self.playlist = []
            print("No existe playlist guardada. Se crea una nueva.\n")

    def guardar_playlist(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(self.playlist, f, indent=4, ensure_ascii=False)
        print("Playlist guardada.\n")

    def mostrar_playlist(self):
        if not self.playlist:
            print("La playlist está vacía.\n")
        else:
            print("\n--- Playlist ---")
            for i, cancion in enumerate(self.playlist):
                print(f"{i}: {cancion['titulo']} - {cancion['artista']}", end="")
                if cancion['album']:
                    print(f" | Álbum: {cancion['album']}")
                else:
                    print(" | Sencillo")
            print("----------------\n")

    def añadir_cancion(self):
        titulo = input("Ingresa el nombre de la canción: ").strip()
        artista = input("Ingresa el nombre del artista: ").strip()
        es_sencillo = input("¿Es un sencillo? (s/n): ").strip().lower()
        album = ""
        if es_sencillo == 'n':
            album = input("Ingresa el nombre del álbum: ").strip()

        cancion = {
            "titulo": titulo,
            "artista": artista,
            "album": album
        }
        self.playlist.append(cancion)
        self.guardar_playlist()
        print(f'"{titulo}" fue añadida a la playlist.\n')

    def eliminar_cancion(self):
        self.mostrar_playlist()
        if not self.playlist:
            return
        try:
            numero = int(input("Número de la canción a eliminar: "))
            if 0 <= numero < len(self.playlist):
                eliminada = self.playlist.pop(numero)
                self.guardar_playlist()
                print(f'"{eliminada["titulo"]}" fue eliminada de la playlist.\n')
            else:
                print("Número inválido.\n")
        except ValueError:
            print("Ingresa un número válido.\n")

    def reproducir_cancion(self):
        self.mostrar_playlist()
        if not self.playlist:
            return
        try:
            numero = int(input("Número de la canción a reproducir: "))
            if 0 <= numero < len(self.playlist):
                cancion = self.playlist[numero]
                print(f'🎵 "{cancion["titulo"]}" de {cancion["artista"]} se está reproduciendo... 🎵\n')
            else:
                print("Número inválido.\n")
        except ValueError:
            print("Ingresa un número válido.\n")

    def buscar_cancion(self):
        objetivo = input("Nombre de la canción a buscar: ").strip().lower()
        for i, cancion in enumerate(self.playlist):
            if cancion['titulo'].lower() == objetivo:
                print(f'"{cancion["titulo"]}" de {cancion["artista"]} encontrada en la posición {i}.\n')
                return
        print(f'"{objetivo}" no está en la playlist.\n')
