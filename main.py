import os
from datetime import datetime
from clases import ListaDobleEnlazada
from bubble_sort import bubble_sort
from tareas_random import agregar_tareas_aleatorias


tareas = ListaDobleEnlazada()

while True:
    os.system('cls')  # Cambia a 'clear' si estás en Linux o Mac
    print("---------- Gestión de Tareas ----------")
    print("1. Agregar Tarea")
    print("2. Buscar Tarea")
    print("3. Modificar Tarea")
    print("4. Mostrar Todas las Tareas")
    print("5. Ordenar Lista de Tareas")
    print("6. Salir...")
    print("7. Agregar tareas aleatorias")
    opcion = str(input("\nIngrese una opción: "))

    match opcion:
        case "1":
            os.system('cls')
            print("---- Agregar Tarea ----")
            titulo = input("Título de la tarea: ")
            try:
                prioridad = int(input("Prioridad (número entero, mayor es más prioridad): "))
                fecha = input("Fecha límite (YYYY-MM-DD): ")
                datetime.strptime(fecha, "%Y-%m-%d")
                tareas.agregar_tarea(titulo, prioridad, fecha)
                print("Tarea agregada exitosamente.")
            except ValueError:
                print("Error: Prioridad o fecha inválida. Intenta de nuevo.")
            input("\nPresiona Enter para continuar...")

        case "2":
            os.system('cls')
            print("---- Buscar Tarea ----")
            buscar = input("Ingrese el título de la tarea a buscar: ")
            resultado = tareas.buscar_tarea(buscar)
            if resultado:
                print(f"Título: {resultado.titulo} | Prioridad: {resultado.prioridad} | Fecha límite: {resultado.fecha_limite.date()}")
            else:
                print("Tarea no encontrada.")
            input("\nPresiona Enter para continuar...")

        case "3":
            os.system('cls')
            print("---- Modificar Tarea ----")
            buscar = input("Ingrese el título de la tarea a modificar: ")
            resultado = tareas.buscar_tarea(buscar)
            if resultado:
                nuevo_titulo = input("Nuevo título: ")
                try:
                    nueva_prioridad = int(input("Nueva prioridad: "))
                    nueva_fecha = input("Nueva fecha límite (YYYY-MM-DD): ")
                    datetime.strptime(nueva_fecha, "%Y-%m-%d")
                    if tareas.modificar_tarea(buscar, nuevo_titulo, nueva_prioridad, nueva_fecha):
                        print("Tarea modificada exitosamente.")
                except ValueError:
                    print("Error: Prioridad o fecha inválida.")
            else:
                print("Tarea no encontrada.")
            input("\nPresiona Enter para continuar...")

        case "4":
            os.system('cls')
            tareas.mostrar_tareas()
            input("\nPresiona Enter para continuar...")

        case "5":
            import time
            os.system('cls')
            print("Ordenando tareas por prioridad y fecha límite...")

            tiempo_inicio = time.perf_counter()
            cantidad_ordenada = bubble_sort(tareas)
            tiempo_fin = time.perf_counter()
            tiempo_total = tiempo_fin - tiempo_inicio

            print("Tareas ordenadas exitosamente.")
            print(f"Total de tareas ordenadas: {cantidad_ordenada}")
            print(f"Tiempo de ejecución: {tiempo_total:.6f} segundos")
            input("\nPresiona Enter para continuar...")

        case "6":
            print("Saliendo del programa...")
            break
        
        case "7":
            os.system('cls')
            print("---- Agregar Tareas Aleatorias ----")
            try:
                cantidad = int(input("¿Cuántas tareas aleatorias desea agregar?: "))
                if cantidad > 0:
                    agregar_tareas_aleatorias(tareas, cantidad)
                    print(f"{cantidad} tareas aleatorias agregadas exitosamente.")
                else:
                    print("Debe ingresar un número positivo.")
            except ValueError:
                print("Error: Debe ingresar un número entero válido.")
            input("\nPresiona Enter para continuar...")

        case _:
            print("Opción no válida. Intenta de nuevo.")
            input("\nPresiona Enter para continuar...")
