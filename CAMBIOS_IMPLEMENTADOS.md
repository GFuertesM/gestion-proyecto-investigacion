# Resumen de Implementación - Persistencia de Datos

## ✅ Cambios Implementados

### 1. **Guardado en Archivos JSON** ✓
- Función `guardar_proyectos()`: Serializa todos los proyectos a JSON
- Guarda en `src/proyectos.json` con formato legible (indentación de 2 espacios)
- Convierte fechas `datetime` al formato ISO 8601
- Crea el directorio automáticamente si no existe
- Se llama al añadir proyectos y antes de salir

### 2. **Carga de Proyectos al Iniciar** ✓
- Función `cargar_proyectos()`: Restaura proyectos desde JSON
- Se ejecuta automáticamente en `ejecutar_menu()`
- Deserializa fechas de formato ISO a objetos `datetime`
- Si no hay archivo, genera proyectos de ejemplo automáticamente
- Sincroniza el contador de IDs

### 3. **Autoguardado Periódico** ✓
- Función `autoguardar_periodico(intervalo=30)`: Thread independiente
- Función `iniciar_autoguardado(intervalo=30)`: Lanza el hilo
- Función `detener_autoguardado()`: Detiene correctamente antes de salir
- Se ejecuta en background sin bloquear la interfaz
- Guarda cada 30 segundos por defecto
- Realiza un guardado final al cerrar la aplicación

## 📝 Modificaciones al Archivo

### `src/main.py`

**Imports agregados:**
```python
import json
import os
import threading
import time
from pathlib import Path
```

**Variables globales agregadas:**
```python
ARCHIVO_DATOS = os.path.join(os.path.dirname(__file__), "proyectos.json")
autoguardado_activo = True
hilo_autoguardado = None
```

**Funciones nuevas:**
- `guardar_proyectos()` - 30 líneas
- `cargar_proyectos()` - 50 líneas
- `autoguardar_periodico()` - 20 líneas
- `iniciar_autoguardado()` - 18 líneas
- `detener_autoguardado()` - 10 líneas

**Funciones modificadas:**
- `añadir_proyecto()` - Agrega llamada a `guardar_proyectos()`
- `ejecutar_menu()` - Integra carga inicial y autoguardado

## 📁 Archivos Nuevos/Modificados

| Archivo | Acción | Descripción |
|---------|--------|-------------|
| `src/main.py` | Modificado | Agregadas todas las funciones de persistencia |
| `src/proyectos.json` | Creado | Archivo de almacenamiento (ejemplo con 2 proyectos) |
| `PERSISTENCIA.md` | Creado | Documentación completa de las nuevas funcionalidades |

## 🔄 Flujo de Ejecución

```
START
  ↓
Cargar proyectos desde JSON
  ├─ Si existen: Restaurar lista
  └─ Si no existen: Crear ejemplos y guardar
  ↓
Iniciar hilo de autoguardado (daemon, cada 30s)
  ↓
Mostrar menú y esperar entrada
  ├─ Opción 1: Listar proyectos
  ├─ Opción 2: Añadir proyecto → Guardar inmediatamente
  └─ Opción 3: Salir
       ↓
       Detener autoguardado
       ↓
       Guardar una última vez
       ↓
       EXIT
```

## 🧪 Prueba Recomendada

1. Ejecutar la aplicación: `python src/main.py`
2. Añadir un nuevo proyecto
3. Verificar que aparece en `src/proyectos.json`
4. Esperar 30 segundos para ver autoguardado
5. Cerrar la aplicación (Ctrl+C)
6. Ejecutar nuevamente y verificar que los proyectos persisten

## 🔧 Configuración

Para cambiar el intervalo de autoguardado (por defecto 30 segundos):
- Editar línea en `ejecutar_menu()`:
  ```python
  iniciar_autoguardado(intervalo=60)  # Cambiar a 60 segundos
  ```

## 🛡️ Características de Robustez

✓ Manejo de errores en lectura/escritura de JSON  
✓ Creación automática de directorios  
✓ Validación de formatos de fecha  
✓ Thread seguro para autoguardado  
✓ Guardado final garantizado al cerrar  
✓ Compatible con el modelo existente de `Proyecto`  
✓ No requiere dependencias externas

## 📊 Impacto en el Código

- Líneas añadidas: ~150
- Funciones nuevas: 5
- Funciones modificadas: 2
- Complejidad: O(n) para guardar/cargar (donde n = número de proyectos)
- Memoria: Mínima overhead del hilo (daemon)
