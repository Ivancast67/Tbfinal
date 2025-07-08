import time
from clases import ListaDobleEnlazada
from bubble_sort import bubble_sort
import random
from datetime import datetime, timedelta

def generar_lista_caso(n, tipo):
    lista = ListaDobleEnlazada()
    hoy = datetime.today()

    if tipo == "mejor":
        for i in range(n, 0, -1):
            titulo = f"Tarea {i}"
            prioridad = i
            fecha = (hoy + timedelta(days=i)).strftime("%Y-%m-%d")
            lista.agregar_tarea(titulo, prioridad, fecha)

    elif tipo == "peor":
        for i in range(1, n + 1):
            titulo = f"Tarea {i}"
            prioridad = i
            fecha = (hoy + timedelta(days=n - i)).strftime("%Y-%m-%d")
            lista.agregar_tarea(titulo, prioridad, fecha)

    elif tipo == "promedio":
        for i in range(n):
            titulo = f"Tarea {i}"
            prioridad = random.randint(1, 5)
            fecha = (hoy + timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")
            lista.agregar_tarea(titulo, prioridad, fecha)

    return lista

def medir_tiempo(lista):
    inicio = time.perf_counter()
    bubble_sort(lista)
    fin = time.perf_counter()
    return (fin - inicio) * 1_000_000  # microsegundos

def formatear_tiempo(us):
    return f"{us/1000:.2f} ms" if us >= 1000 else f"{us:.2f} µs"

def imprimir_tabla(resultados):
    ancho = 74
    print("╔" + "═" * (ancho - 2) + "╗")
    print("║ {:^8} │ {:^18} │ {:^18} │ {:^18} ║".format(
        "Tamaño", "Mejor Caso", "Promedio", "Peor Caso"))
    print("╠" + "═" * 8 + "╪" + "═" * 20 + "╪" + "═" * 20 + "╪" + "═" * 20 + "╣")
    for fila in resultados:
        print("║ {:>8} │ {:>18} │ {:>18} │ {:>18} ║".format(*fila))
    print("╚" + "═" * (ancho - 2) + "╝")

# Tamaños a probar
tamanios = [10, 100, 500, 1000, 2000]
resultados = []

for n in tamanios:
    lista_mejor = generar_lista_caso(n, "mejor")
    lista_prom = generar_lista_caso(n, "promedio")
    lista_peor = generar_lista_caso(n, "peor")

    t_mejor = medir_tiempo(lista_mejor)
    t_prom = medir_tiempo(lista_prom)
    t_peor = medir_tiempo(lista_peor)

    resultados.append([
        n,
        formatear_tiempo(t_mejor),
        formatear_tiempo(t_prom),
        formatear_tiempo(t_peor)
    ])

imprimir_tabla(resultados)
