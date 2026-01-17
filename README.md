# 🔍 Network Scanner & Banner Grabber - Python

Este es un proyecto de **software** de red desarrollado para el aprendizaje de protocolos de comunicación y **ciberseguridad**. La herramienta permite identificar dispositivos activos y servicios expuestos en una red local mediante el análisis de puertos.

> [!CAUTION]
> **AVISO LEGAL:** Este script es exclusivamente para fines educativos y auditorías de red autorizadas. Realizar escaneos en redes ajenas sin permiso es ilegal. El autor no se hace responsable del uso indebido de esta herramienta.

## ✨ Características
- **Escaneo TCP:** Detecta si los puertos están abiertos o cerrados mediante el saludo de tres vías (3-way handshake).
- **Banner Grabbing:** Intenta capturar la información del software que se ejecuta en el puerto (versión, nombre del servicio).
- **Timeouts personalizables:** Configurado para evitar bloqueos si el objetivo no responde.

## 🛠️ Tecnologías y Conceptos
- **Lenguaje:** Python 3.
- **Librería principal:** `socket` (vínculo esencial para comunicaciones en red).
- **Programación de Redes:** Uso de sockets de flujo (`SOCK_STREAM`) para conexiones TCP confiables.

## 🛡️ ¿Por qué es importante el escaneo de puertos?
Desde la perspectiva de la ciberseguridad, es fundamental porque:
1. **Visibilidad:** Permite saber qué servicios están expuestos a internet o a la red interna.
2. **Hardening:** Ayuda a los administradores a cerrar puertos innecesarios que podrían ser vectores de ataque.
3. **Gestión de Parches:** El *Banner Grabbing* ayuda a identificar versiones de software antiguas que necesitan actualización.

## 🛠️ Instalación y Requisitos

Para ejecutar este escáner, solo necesitas tener **Python 3** instalado (no requiere librerías externas adicionales).

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/python-network-scanner.git](https://github.com/tu-usuario/python-network-scanner.git)
   cd python-network-scanner
