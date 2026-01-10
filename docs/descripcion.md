# 📖 Descripción del Proyecto

## 🎯 Objetivo

El sistema de gestión de proyectos de investigación tiene como objetivo proporcionar una herramienta simple y efectiva para administrar proyectos científicos en el ámbito de la Astroinformática. Permite a los investigadores y administradores:

- Registrar nuevos proyectos de investigación
- Mantener un seguimiento del estado de cada proyecto
- Visualizar información consolidada de todos los proyectos
- Gestionar información clave como investigadores principales y fechas de inicio

El sistema está diseñado para ser intuitivo y fácil de usar, con una interfaz de consola interactiva que no requiere conocimientos técnicos avanzados.

## 📋 Requisitos Mínimos

### Requisitos Técnicos

- **Python**: Versión 3.6 o superior
- **Sistema Operativo**: Compatible con Windows, Linux y macOS
- **Memoria**: Mínimo 50 MB de RAM disponible
- **Disco**: 10 MB de espacio libre

### Requisitos Funcionales

El sistema debe cumplir con las siguientes funcionalidades básicas:

1. **Gestión de Proyectos**:
   - Cada proyecto debe tener un ID único
   - Título descriptivo del proyecto
   - Investigador principal asignado
   - Fecha de inicio
   - Estado actual del proyecto

2. **Operaciones Básicas**:
   - Listar todos los proyectos registrados
   - Añadir nuevos proyectos al sistema
   - Interfaz de menú interactivo por consola

3. **Almacenamiento**:
   - Datos almacenados en memoria durante la ejecución
   - Proyectos de ejemplo precargados para demostración

### Arquitectura Actual

```
┌─────────────────────────────────────┐
│          Interfaz Usuario           │
│         (Console Menu)              │
└─────────────────┬───────────────────┘
                  │
┌─────────────────▼───────────────────┐
│         Lógica de Negocio           │
│    (main.py - funciones CRUD)       │
└─────────────────┬───────────────────┘
                  │
┌─────────────────▼───────────────────┐
│         Modelo de Datos             │
│      (proyecto.py - Clase)          │
└─────────────────┬───────────────────┘
                  │
┌─────────────────▼───────────────────┐
│      Almacenamiento en Memoria      │
│         (Lista Python)              │
└─────────────────────────────────────┘
```

## 🚀 Mejoras Futuras

### Corto Plazo

1. **Persistencia de Datos**:
   - Implementar guardado en archivos JSON
   - Cargar proyectos al iniciar la aplicación
   - Autoguardado periódico

2. **Operaciones CRUD Completas**:
   - Editar proyectos existentes
   - Eliminar proyectos
   - Cambiar estado de proyectos

3. **Validaciones Mejoradas**:
   - Validación de formatos de entrada
   - Verificación de datos duplicados
   - Manejo de errores más robusto

4. **Búsqueda y Filtrado**:
   - Buscar proyectos por título
   - Filtrar por investigador principal
   - Filtrar por estado o fecha

### Mediano Plazo

1. **Gestión Avanzada**:
   - Múltiples investigadores por proyecto
   - Gestión de recursos y presupuesto
   - Hitos y fechas importantes
   - Documentos y archivos adjuntos

2. **Reportes y Estadísticas**:
   - Resumen de proyectos por estado
   - Gráficos y visualizaciones
   - Exportar a PDF o Excel
   - Dashboard con métricas clave

3. **Base de Datos**:
   - Migrar a SQLite o PostgreSQL
   - Mejor rendimiento con grandes volúmenes
   - Consultas complejas optimizadas

4. **Testing**:
   - Pruebas unitarias (unittest/pytest)
   - Pruebas de integración
   - Cobertura de código > 80%

### Largo Plazo

1. **Interfaz Gráfica**:
   - GUI con Tkinter, PyQt o web (Flask/Django)
   - Experiencia de usuario mejorada
   - Visualizaciones interactivas

2. **Sistema Multiusuario**:
   - Autenticación y autorización
   - Roles (administrador, investigador, colaborador)
   - Permisos por proyecto

3. **Colaboración**:
   - Comentarios y notas en proyectos
   - Notificaciones y alertas
   - Historial de cambios
   - Control de versiones de documentos

4. **Integración**:
   - API REST para integraciones
   - Sincronización con calendarios
   - Exportación a formatos científicos
   - Integración con sistemas de gestión institucional

5. **Análisis Avanzado**:
   - Machine Learning para predicción de plazos
   - Análisis de tendencias
   - Recomendaciones automáticas
   - Detección de riesgos en proyectos

## 🔧 Consideraciones Técnicas

### Buenas Prácticas Implementadas

- ✅ Código modular y organizado
- ✅ Docstrings en funciones y clases
- ✅ Separación de responsabilidades (modelo-vista-controlador simplificado)
- ✅ Manejo de excepciones
- ✅ Interfaz de usuario clara e intuitiva

### Próximas Mejoras Técnicas

- 📝 Agregar type hints (PEP 484)
- 📝 Implementar logging
- 📝 Configuración mediante archivos .env
- 📝 Documentación con Sphinx
- 📝 CI/CD con GitHub Actions
- 📝 Containerización con Docker

## 📞 Contribuciones

Este proyecto está abierto a mejoras y contribuciones. Para contribuir:

1. Fork del repositorio
2. Crear una rama para tu feature
3. Commit de cambios con mensajes descriptivos
4. Push a la rama
5. Crear Pull Request

---

**Versión**: 1.0.0  
**Última actualización**: Enero 2026  
**Estado**: En desarrollo activo