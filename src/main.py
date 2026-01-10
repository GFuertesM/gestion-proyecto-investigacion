"""
Sistema de gestión de proyectos de investigación - Módulo principal.
"""

from datetime import datetime
from proyecto import Proyecto


# Lista en memoria para almacenar proyectos
proyectos = []

# Contador para generar IDs únicos
contador_id = 1


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
    # Añadir algunos proyectos de ejemplo
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
    
    global contador_id
    contador_id = 3
    
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
                break
            else:
                print("\n❌ Opción inválida. Por favor, seleccione 1, 2 o 3.")
        
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego! Gracias por usar el sistema.")
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
