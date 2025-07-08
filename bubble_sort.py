def bubble_sort(lista):
    if not lista.cabeza:
        print("No hay tareas para ordenar.")
        return 0  # Devuelve 0 si no hay tareas

    # Contar nodos antes de ordenar
    contador = 0
    temp = lista.cabeza
    while temp:
        contador += 1
        temp = temp.siguiente

    cambio = True
    while cambio:
        cambio = False
        actual = lista.cabeza
        while actual.siguiente:
            siguiente = actual.siguiente
            if (actual.prioridad < siguiente.prioridad) or \
               (actual.prioridad == siguiente.prioridad and actual.fecha_limite > siguiente.fecha_limite):
                # Intercambio de datos entre nodos
                actual.titulo, siguiente.titulo = siguiente.titulo, actual.titulo
                actual.prioridad, siguiente.prioridad = siguiente.prioridad, actual.prioridad
                actual.fecha_limite, siguiente.fecha_limite = siguiente.fecha_limite, actual.fecha_limite
                cambio = True
            actual = actual.siguiente

    return contador  # Devuelve la cantidad de tareas ordenadas
