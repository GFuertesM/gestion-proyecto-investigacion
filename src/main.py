"""
Sistema de gestión de proyectos de investigación - Módulo principal.
"""

from datetime import datetime
from proyecto import Proyecto
import json
import os
import threading
import time
from pathlib import Path


# Lista en memoria para almacenar proyectos
proyectos = []

# Contador para generar IDs únicos
contador_id = 1

# Ruta del archivo de datos
ARCHIVO_DATOS = os.path.join(os.path.dirname(__file__), "proyectos.json")

# Control para autoguardado
autoguardado_activo = True
hilo_autoguardado = None


def guardar_proyectos():
    """
    Guarda todos los proyectos en un archivo JSON.
    """
    try:
        datos = {
            "contador_id": contador_id,
            "proyectos": []
        }
        
        for proyecto in proyectos:
            proyecto_dict = {
                "id": proyecto.id,
                "titulo": proyecto.titulo,
                "investigador_principal": proyecto.investigador_principal,
                "fecha_inicio": proyecto.fecha_inicio.isoformat() if isinstance(proyecto.fecha_inicio, datetime) else str(proyecto.fecha_inicio),
                "estado": proyecto.estado
            }
            datos["proyectos"].append(proyecto_dict)
        
        # Crear directorio si no existe
        Path(ARCHIVO_DATOS).parent.mkdir(parents=True, exist_ok=True)
        
        # Guardar con indentación para legibilidad
        with open(ARCHIVO_DATOS, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=2, ensure_ascii=False)
        
        print(f"✅ Proyectos guardados en {ARCHIVO_DATOS}")
        return True
    
    except Exception as e:
        print(f"❌ Error al guardar proyectos: {e}")
        return False


def cargar_proyectos():
    """
    Carga todos los proyectos desde el archivo JSON.
    Retorna el número de proyectos cargados.
    """
    global contador_id
    
    try:
        if not os.path.exists(ARCHIVO_DATOS):
            print(f"ℹ️  Archivo de datos no encontrado en {ARCHIVO_DATOS}")
            return 0
        
        with open(ARCHIVO_DATOS, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
        
        proyectos.clear()
        
        # Restaurar contador_id
        contador_id = datos.get("contador_id", 1)
        
        # Cargar proyectos
        for proyecto_dict in datos.get("proyectos", []):
            try:
                # Convertir fecha ISO a datetime
                fecha_str = proyecto_dict["fecha_inicio"]
                if fecha_str:
                    fecha_inicio = datetime.fromisoformat(fecha_str)
                else:
                    fecha_inicio = datetime.now()
                
                proyecto = Proyecto(
                    id=proyecto_dict["id"],
                    titulo=proyecto_dict["titulo"],
                    investigador_principal=proyecto_dict["investigador_principal"],
                    fecha_inicio=fecha_inicio,
                    estado=proyecto_dict.get("estado", "En planificación")
                )
                proyectos.append(proyecto)
            
            except Exception as e:
                print(f"⚠️  Error al cargar proyecto: {e}")
                continue
        
        cantidad = len(proyectos)
        if cantidad > 0:
            print(f"✅ {cantidad} proyecto(s) cargado(s) exitosamente")
        return cantidad
    
    except Exception as e:
        print(f"❌ Error al cargar proyectos: {e}")
        return 0


def autoguardar_periodico(intervalo=30):
    """
    Thread que guarda los proyectos automáticamente cada X segundos.
    
    Args:
        intervalo (int): Segundos entre autoguardos (por defecto 30)
    """
    global autoguardado_activo
    
    print(f"\n🔄 Autoguardado activado (cada {intervalo} segundos)")
    
    while autoguardado_activo:
        try:
            time.sleep(intervalo)
            if autoguardado_activo:
                guardar_proyectos()
        
        except Exception as e:
            print(f"❌ Error en autoguardado: {e}")


def iniciar_autoguardado(intervalo=30):
    """
    Inicia el hilo de autoguardado.
    
    Args:
        intervalo (int): Segundos entre autoguardos (por defecto 30)
    """
    global hilo_autoguardado, autoguardado_activo
    
    if hilo_autoguardado is None or not hilo_autoguardado.is_alive():
        autoguardado_activo = True
        hilo_autoguardado = threading.Thread(
            target=autoguardar_periodico,
            args=(intervalo,),
            daemon=True
        )
        hilo_autoguardado.start()


def detener_autoguardado():
    """
    Detiene el hilo de autoguardado.
    """
    global autoguardado_activo
    
    autoguardado_activo = False
    
    # Guardar una última vez antes de salir
    print("\n💾 Guardando cambios finales...")
    guardar_proyectos()


def listar_proyectos():
    """
    Lista todos los proyectos almacenados en memoria.
    """
    if not proyectos:
        print("\n📋 No hay proyectos registrados.")
        return
    
    print("\n" + "="*80)
    print("📋 LISTA DE PROYECTOS DE INVESTIGACIÓN")
    print("="*80)
    
    for proyecto in proyectos:
        print(f"\n{proyecto}")
    
    print("\n" + "="*80)
    print(f"Total de proyectos: {len(proyectos)}")
    print("="*80)


def añadir_proyecto():
    """
    Añade un nuevo proyecto a la lista en memoria.
    """
    global contador_id
    
    print("\n" + "="*80)
    print("➕ AÑADIR NUEVO PROYECTO")
    print("="*80)
    
    try:
        titulo = input("\nTítulo del proyecto: ").strip()
        if not titulo:
            print("❌ Error: El título no puede estar vacío.")
            return
        
        investigador_principal = input("Investigador principal: ").strip()
        if not investigador_principal:
            print("❌ Error: El investigador principal no puede estar vacío.")
            return
        
        fecha_str = input("Fecha de inicio (dd/mm/aaaa) [Enter para hoy]: ").strip()
        if fecha_str:
            try:
                fecha_inicio = datetime.strptime(fecha_str, "%d/%m/%Y")
            except ValueError:
                print("❌ Error: Formato de fecha incorrecto. Use dd/mm/aaaa")
                return
        else:
            fecha_inicio = datetime.now()
        
        print("\nEstados disponibles:")
        print("1. En planificación")
        print("2. En curso")
        print("3. Completado")
        print("4. Cancelado")
        
        estado_opcion = input("Seleccione estado [1-4, Enter para 'En planificación']: ").strip()
        estados = {
            "1": "En planificación",
            "2": "En curso",
            "3": "Completado",
            "4": "Cancelado",
            "": "En planificación"
        }
        
        estado = estados.get(estado_opcion, "En planificación")
        
        # Crear el nuevo proyecto
        nuevo_proyecto = Proyecto(
            id=contador_id,
            titulo=titulo,
            investigador_principal=investigador_principal,
            fecha_inicio=fecha_inicio,
            estado=estado
        )
        
        proyectos.append(nuevo_proyecto)
        contador_id += 1
        
        print(f"\n✅ Proyecto añadido exitosamente con ID: {nuevo_proyecto.id}")
        print(f"   {nuevo_proyecto}")
        
        # Guardar inmediatamente
        guardar_proyectos()
        
    except KeyboardInterrupt:
        print("\n\n❌ Operación cancelada.")
    except Exception as e:
        print(f"\n❌ Error al añadir proyecto: {e}")


def mostrar_menu():
    """
    Muestra el menú principal del sistema.
    """
    print("\n" + "="*80)
    print("🔬 SISTEMA DE GESTIÓN DE PROYECTOS DE INVESTIGACIÓN ASTROINFORMÁTICA")
    print("="*80)
    print("\n1. 📋 Listar proyectos")
    print("2. ➕ Añadir nuevo proyecto")
    print("3. 🚪 Salir")
    print("\n" + "-"*80)


def ejecutar_menu():
    """
    Ejecuta el bucle principal del menú.
    """
    global contador_id
    
    print("\n" + "="*80)
    print("🔬 INICIANDO SISTEMA DE GESTIÓN DE PROYECTOS")
    print("="*80)
    
    # Cargar proyectos desde archivo
    proyectos_cargados = cargar_proyectos()
    
    # Si no hay proyectos cargados, crear algunos de ejemplo
    if proyectos_cargados == 0:
        print("\n📝 Creando proyectos de ejemplo...")
        proyectos.append(Proyecto(
            id=1,
            titulo="Análisis de curvas de luz de supernovas",
            investigador_principal="Dr. Juan Pérez",
            fecha_inicio=datetime(2025, 1, 15),
            estado="En curso"
        ))
        
        proyectos.append(Proyecto(
            id=2,
            titulo="Clasificación automática de galaxias con ML",
            investigador_principal="Dra. María González",
            fecha_inicio=datetime(2025, 3, 1),
            estado="En planificación"
        ))
        
        # Guardar proyectos de ejemplo
        guardar_proyectos()
    
    # Actualizar contador_id basado en los proyectos existentes
    contador_id = max(p.id for p in proyectos) + 1 if proyectos else 1
    
    # Iniciar autoguardado cada 30 segundos
    iniciar_autoguardado(intervalo=30)
    
    while True:
        try:
            mostrar_menu()
            opcion = input("Seleccione una opción [1-3]: ").strip()
            
            if opcion == "1":
                listar_proyectos()
            elif opcion == "2":
                añadir_proyecto()
            elif opcion == "3":
                print("\n👋 ¡Hasta luego! Gracias por usar el sistema.")
                detener_autoguardado()
                break
            else:
                print("\n❌ Opción inválida. Por favor, seleccione 1, 2 o 3.")
        
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego! Gracias por usar el sistema.")
            detener_autoguardado()
            break
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")


def main():
    """
    Función principal del programa.
    """
    ejecutar_menu()


if __name__ == "__main__":
    main()
