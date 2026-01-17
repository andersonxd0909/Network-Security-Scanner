# 🔍 Python Network Scanner & Banner Grabber

Este es un escáner de puertos ligero y eficiente desarrollado en **Python**. Está diseñado para realizar auditorías básicas de seguridad, permitiendo identificar puertos abiertos y detectar las versiones de software que se ejecutan en ellos mediante la técnica de **Banner Grabbing**.

---

## 🛠️ ¿Qué es y qué hace?

Este software es una herramienta de **Reconocimiento (Footprinting)**. 
* **Escaneo de Puertos:** Revisa si un servicio (como una web o una base de datos) está escuchando en un puerto específico.
* **Banner Grabbing:** "Escucha" la presentación del servidor para saber qué software usa (ej. Apache, OpenSSH, etc.).



---

## 🚀 Instalación y Uso

### 1. Requisitos
Necesitas tener instalado **Python 3.x**. Si no lo tienes, descárgalo aquí: [python.org](https://www.python.org/downloads/).

### 2. Configuración
Clona este repositorio o descarga el archivo `scanner.py`. Abre el archivo y edita las siguientes líneas con tu objetivo:

Abre tu terminal o CMD y escribe:
python scanner.py

```python
objetivo = "192.168.1.1"  # La IP que quieres escanear
puertos = [22, 80, 443]   # Los puertos que quieres revisar
