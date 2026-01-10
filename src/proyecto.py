"""
Módulo para la gestión de proyectos de investigación.
"""

from datetime import datetime


class Proyecto:
    """
    Clase que representa un proyecto de investigación.
    
    Atributos:
        id (int): Identificador único del proyecto
        titulo (str): Título del proyecto
        investigador_principal (str): Nombre del investigador principal
        fecha_inicio (datetime): Fecha de inicio del proyecto
        estado (str): Estado actual del proyecto (ej: "En planificación", "En curso", "Completado")
    """
    
    def __init__(self, id, titulo, investigador_principal, fecha_inicio, estado="En planificación"):
        """
        Inicializa un nuevo proyecto de investigación.
        
        Args:
            id (int): Identificador único del proyecto
            titulo (str): Título del proyecto
            investigador_principal (str): Nombre del investigador principal
            fecha_inicio (datetime): Fecha de inicio del proyecto
            estado (str): Estado del proyecto (por defecto "En planificación")
        """
        self.id = id
        self.titulo = titulo
        self.investigador_principal = investigador_principal
        self.fecha_inicio = fecha_inicio
        self.estado = estado
    
    def __str__(self):
        """
        Retorna una representación en cadena del proyecto.
        """
        fecha_str = self.fecha_inicio.strftime("%d/%m/%Y") if isinstance(self.fecha_inicio, datetime) else str(self.fecha_inicio)
        return f"[{self.id}] {self.titulo} - IP: {self.investigador_principal} - Inicio: {fecha_str} - Estado: {self.estado}"
    
    def __repr__(self):
        """
        Retorna una representación detallada del proyecto.
        """
        return f"Proyecto(id={self.id}, titulo='{self.titulo}', investigador_principal='{self.investigador_principal}', fecha_inicio={self.fecha_inicio}, estado='{self.estado}')"
