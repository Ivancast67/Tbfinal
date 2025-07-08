import random
from datetime import datetime, timedelta

def agregar_tareas_aleatorias(lista, cantidad):
    for i in range(cantidad):
        titulo = f"Tarea Aleatoria {i+1}"
        prioridad = random.randint(1, 10)  # Prioridad aleatoria entre 1 y 5
        dias_extra = random.randint(0, 365)  # Fechas dentro de los próximos 30 días
        fecha_limite = (datetime.today() + timedelta(days=dias_extra)).strftime("%Y-%m-%d")
        lista.agregar_tarea(titulo, prioridad, fecha_limite)
