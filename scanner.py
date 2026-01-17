import socket

objetivo = "192.168.1.1"
puertos = [22, 80, 443]

print(f"--- Iniciando Escaneo Inteligente en {objetivo} ---")

for puerto in puertos:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    
    resultado = s.connect_ex((objetivo, puerto))
    
    if resultado == 0:
        print(f"[*] Puerto {puerto}: ABIERTO")
        try:
            # Intentamos recibir un mensaje de saludo del puerto
            banner = s.recv(1024).decode().strip()
            print(f"    [INFO] Software detectado: {banner}")
        except:
            print("    [INFO] No se pudo obtener información del software.")
    else:
        print(f"[ ] Puerto {puerto}: Cerrado")
    
    s.close()

print("--- Escaneo completado ---")