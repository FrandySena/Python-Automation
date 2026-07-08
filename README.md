# Local File System Automations (Python)

Este repositorio contiene scripts sencillos en Python diseñados para automatizar tareas rutinarias de ordenamiento y limpieza en directorios del sistema de manera local.

## Scripts Incluidos

### 1. Organizador de Descargas (`Go2PDFs.py`)
* **Función:** Escanea la carpeta predeterminada de descargas del usuario (`Downloads`).
* **Acción:** Detecta los archivos con extensión `.pdf` y los mueve automáticamente a una carpeta centralizada (`Documents/PDFs`). Si el directorio de destino no existe, el script lo crea de forma dinámica.
* **Módulos utilizados:** `os`, `shutil`, `pathlib`.

### 2. Limpiador de Capturas de Pantalla (`ScreenshotCleaner.py`)
* **Función:** Revisa el directorio de capturas de pantalla (`Pictures/Screenshots`).
* **Acción:** Identifica los archivos `.png` y los envía a la papelera de reciclaje del sistema operativo, permitiendo una depuración segura sin eliminar los archivos de forma permanente e irreversible.
* **Módulos utilizados:** `pathlib`, `send2trash`.

## Requisitos e Instalación

Los scripts utilizan principalmente la biblioteca estándar de Python, a excepción de la gestión segura de la papelera de reciclaje.

1. Clonar el repositorio.
2. Instalar la dependencia externa necesaria para el script de limpieza:
   ```bash
   pip install send2trash
