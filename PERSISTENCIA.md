# Persistencia de Datos - Documentación

## 🎯 Nuevas Funcionalidades Implementadas

### 1. **Guardado en Archivos JSON**
- Los proyectos se guardan automáticamente en `src/proyectos.json`
- Formato JSON humanamente legible con indentación
- Conserva todos los atributos: ID, título, investigador, fecha y estado

**Ejemplo de estructura JSON:**
```json
{
  "contador_id": 3,
  "proyectos": [
    {
      "id": 1,
      "titulo": "Análisis de curvas de luz de supernovas",
      "investigador_principal": "Dr. Juan Pérez",
      "fecha_inicio": "2025-01-15T00:00:00",
      "estado": "En curso"
    }
  ]
}
```

### 2. **Carga de Proyectos al Iniciar**
- Al ejecutar la aplicación, se cargan automáticamente todos los proyectos guardados
- Si no existe archivo previo, se crean proyectos de ejemplo
- El contador de IDs se sincroniza automáticamente

**Función: `cargar_proyectos()`**
- Lee el archivo JSON
- Reconstruye los objetos `Proyecto` en memoria
- Actualiza el contador de IDs

### 3. **Autoguardado Periódico**
- Hilo independiente que guarda los cambios cada 30 segundos
- No bloquea la interfaz del usuario
- Se inicia automáticamente al abrir la aplicación
- Se detiene correctamente al salir

**Funciones principales:**
- `iniciar_autoguardado(intervalo=30)`: Inicia el hilo de autoguardado
- `autoguardar_periodico(intervalo=30)`: Ejecuta el guardado periódico
- `detener_autoguardado()`: Detiene el autoguardado antes de salir

## 📋 Funciones Disponibles

### `guardar_proyectos()`
Guarda inmediatamente todos los proyectos en el archivo JSON.
- Se llama automáticamente cuando se añade un nuevo proyecto
- Se llama cada 30 segundos por autoguardado
- Se llama una última vez al cerrar la aplicación

### `cargar_proyectos()`
Carga los proyectos desde el archivo JSON al iniciar.
- Retorna la cantidad de proyectos cargados
- Maneja automáticamente la conversión de fechas ISO a datetime

## 🔄 Flujo de la Aplicación

```
Inicio de la aplicación
    ↓
Cargar proyectos desde JSON
    ↓
Si no hay proyectos → Crear ejemplos
    ↓
Iniciar hilo de autoguardado (cada 30s)
    ↓
Menú principal
    ├─ Listar proyectos
    ├─ Añadir proyecto (guarda inmediatamente)
    └─ Salir (detiene autoguardado + guardado final)
```

## 💾 Archivos Generados

- `src/proyectos.json`: Archivo de almacenamiento de proyectos
- Creado automáticamente si no existe
- Se actualiza continuamente durante la sesión

## 🔧 Personalización

### Cambiar intervalo de autoguardado

En la función `ejecutar_menu()`, modificar:
```python
iniciar_autoguardado(intervalo=30)  # Cambiar 30 por los segundos deseados
```

### Intervalo recomendado
- **10 segundos**: Para desarrollo/testing
- **30 segundos**: Para uso normal (por defecto)
- **60 segundos o más**: Si hay muchos proyectos

## 🛡️ Manejo de Errores

- Validación de formato JSON
- Conversión segura de fechas
- Creación automática de directorios
- Mensajes informativos para cada operación
- Si hay error en un proyecto individual, se sigue cargando el resto

## ✅ Beneficios

✓ Persistencia automática de datos  
✓ No se pierden cambios incluso si falla la aplicación  
✓ Carga rápida de proyectos existentes  
✓ Compatible con cualquier versión de JSON  
✓ Fácil de respaldar y compartir (archivo JSON estándar)
