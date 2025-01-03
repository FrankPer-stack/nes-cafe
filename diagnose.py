import socket
import os

def check_port_availability(host, port):
    """Verificar si un puerto está disponible."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except Exception as e:
        print(f"Error al verificar el puerto {port}: {e}")
        return False

def diagnose_docker_network():
    """Diagnóstico de la configuración de red de Docker."""
    print("🔍 Diagnóstico de red de Docker")
    
    # Verificar puertos
    ports_to_check = [
        ('localhost', 8000),
        ('0.0.0.0', 8000),
        ('127.0.0.1', 8000)
    ]
    
    for host, port in ports_to_check:
        status = "🟢 Disponible" if check_port_availability(host, port) else "🔴 No disponible"
        print(f"Puerto {port} en {host}: {status}")
    
    # Verificar variables de entorno
    print("\n🔍 Variables de entorno relevantes:")
    env_vars = [
        'DJANGO_SETTINGS_MODULE',
        'DEBUG',
        'ALLOWED_HOSTS',
        'DATABASE_URL'
    ]
    
    for var in env_vars:
        value = os.getenv(var, 'No establecida')
        print(f"{var}: {value}")

if __name__ == "__main__":
    diagnose_docker_network()
