# 🔬 Gestión de Proyectos de Investigación

Sistema de gestión de proyectos de investigación en Astroinformática desarrollado en Python.

## 📋 Descripción

Esta aplicación permite gestionar proyectos de investigación científica, facilitando el registro y seguimiento de proyectos, investigadores principales, fechas de inicio y estados de cada proyecto. El sistema funciona con un almacenamiento en memoria y proporciona una interfaz de consola interactiva.

## 📂 Estructura del Proyecto

```
gestion-proyecto-investigacion/
│
├── src/                          # Código fuente
│   ├── proyecto.py              # Clase Proyecto con atributos del proyecto
│   └── main.py                  # Aplicación principal con menú interactivo
│
├── docs/                         # Documentación
│   └── descripcion.md           # Descripción detallada del proyecto
│
└── README.md                     # Este archivo
```

## 🚀 Cómo Ejecutar

### Requisitos Previos

- Python 3.6 o superior

### Ejecución

Desde la raíz del proyecto, ejecuta:

```bash
python src/main.py
```

O también puedes ejecutar desde el directorio `src`:

```bash
cd src
python main.py
```

## 💡 Ejemplo de Uso

Al ejecutar la aplicación, se mostrará un menú interactivo:

```
🔬 SISTEMA DE GESTIÓN DE PROYECTOS DE INVESTIGACIÓN ASTROINFORMÁTICA
================================================================================

1. 📋 Listar proyectos
2. ➕ Añadir nuevo proyecto
3. 🚪 Salir

Seleccione una opción [1-3]:
```

### Operaciones disponibles:

1. **Listar proyectos**: Muestra todos los proyectos registrados con sus detalles
2. **Añadir proyecto**: Permite registrar un nuevo proyecto proporcionando:
   - Título del proyecto
   - Investigador principal
   - Fecha de inicio (formato dd/mm/aaaa)
   - Estado (En planificación, En curso, Completado, Cancelado)
3. **Salir**: Cierra la aplicación

### Ejemplo de interacción:

```
Seleccione una opción [1-3]: 2

➕ AÑADIR NUEVO PROYECTO
================================================================================

Título del proyecto: Detección de exoplanetas con ML
Investigador principal: Dr. Carlos Martínez
Fecha de inicio (dd/mm/aaaa) [Enter para hoy]: 01/06/2026
Seleccione estado [1-4, Enter para 'En planificación']: 2

✅ Proyecto añadido exitosamente con ID: 3
   [3] Detección de exoplanetas con ML - IP: Dr. Carlos Martínez - Inicio: 01/06/2026 - Estado: En curso
```

## 🎯 Próximos Pasos

- [ ] Implementar persistencia de datos (JSON, CSV o base de datos)
- [ ] Añadir funcionalidad para editar proyectos existentes
- [ ] Implementar búsqueda y filtrado de proyectos
- [ ] Agregar validaciones más robustas
- [ ] Añadir gestión de colaboradores y recursos
- [ ] Implementar reportes y estadísticas
- [ ] Desarrollar interfaz gráfica (GUI)
- [ ] Añadir pruebas unitarias
- [ ] Implementar sistema de autenticación de usuarios

## 📚 Documentación Adicional

Para más detalles sobre los objetivos, requisitos y mejoras futuras, consulta el archivo [docs/descripcion.md](docs/descripcion.md).

## 👨‍💻 Desarrollo

Este proyecto está en fase inicial de desarrollo y utiliza Python estándar sin dependencias externas.

## :godmode: Autor: Gabriel Fuertes Muñoz - EUPT - Unizar.
