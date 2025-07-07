from playlist_manager import PlaylistManager, limpiar_pantalla

def mostrar_menu():
    print("1. Mostrar playlist")
    print("2. Añadir canción")
    print("3. Eliminar canción")
    print("4. Reproducir canción")
    print("5. Buscar canción")
    print("6. Salir")

def main():
    gestor = PlaylistManager()
    
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("\nElige una opción: ")
        print()

        if opcion == "1":
            limpiar_pantalla()
            gestor.mostrar_playlist()
            input("Presiona Enter para continuar...")  # Pausa para ver la playlist
        elif opcion == "2":
            limpiar_pantalla()
            gestor.añadir_cancion()
            input("Presiona Enter para continuar...")
        elif opcion == "3":
            limpiar_pantalla()
            gestor.eliminar_cancion()
            input("Presiona Enter para continuar...")
        elif opcion == "4":
            limpiar_pantalla()
            gestor.reproducir_cancion()
            input("Presiona Enter para continuar...")
        elif opcion == "5":
            limpiar_pantalla()
            gestor.buscar_cancion()
            input("Presiona Enter para continuar...")
        elif opcion == "6":
            print("Adiós 🎵")
            break
        else:
            print("Opción no válida.\n")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
