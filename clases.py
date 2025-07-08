from datetime import datetime

class Nodo:
    def __init__(self, titulo, prioridad, fecha_limite):
        self.titulo = titulo
        self.prioridad = prioridad
        self.fecha_limite = datetime.strptime(fecha_limite, "%Y-%m-%d")
        self.anterior = None
        self.siguiente = None

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_tarea(self, titulo, prioridad, fecha_limite):
        nuevo = Nodo(titulo, prioridad, fecha_limite)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            temp = self.cabeza
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nuevo
            nuevo.anterior = temp

    def mostrar_tareas(self):
        temp = self.cabeza
        if not temp:
            print("\nNo hay tareas registradas...")
            return
        print("\nLista de Tareas:")
        while temp:
            print(f"Título: {temp.titulo} | Prioridad: {temp.prioridad} | Fecha límite: {temp.fecha_limite.date()}")
            temp = temp.siguiente

    def buscar_tarea(self, titulo_busqueda):
        temp = self.cabeza
        while temp:
            if temp.titulo.lower() == titulo_busqueda.lower():
                return temp
            temp = temp.siguiente
        return None

    def modificar_tarea(self, titulo_busqueda, nuevo_titulo, nueva_prioridad, nueva_fecha):
        tarea = self.buscar_tarea(titulo_busqueda)
        if tarea:
            tarea.titulo = nuevo_titulo
            tarea.prioridad = nueva_prioridad
            tarea.fecha_limite = datetime.strptime(nueva_fecha, "%Y-%m-%d")
            return True
        else:
            return False
