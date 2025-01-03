# Imagen base oficial de Python 3.11 versión slim (más ligera)
FROM python:3.11-slim
FROM node:20

# Configuración de variables de entorno para Python
# Instala Python y pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Previene la generación de archivos .pyc y mejora el rendimiento
ENV PYTHONDONTWRITEBYTECODE 1
# Mantiene la salida de Python en tiempo real sin buffering
ENV PYTHONUNBUFFERED 1

# Establece el directorio de trabajo principal dentro del contenedor
WORKDIR /app

# Instalación de dependencias del sistema necesarias para el proyecto
# - postgresql-client: Para conexiones y gestión de base de datos
# - curl: Herramienta para descargas y transferencias
# - ca-certificates: Certificados para conexiones seguras
# - nodejs y npm: Para compilación de frontend (Tailwind CSS)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        python3-venv \
        curl \
        ca-certificates \
        nodejs \
        npm \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*  # Limpia la caché para reducir tamaño de imagen

    # Crea un entorno virtual y activa
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Actualiza npm a la última versión para garantizar compatibilidad
RUN npm install -g npm@latest

# Copia el archivo de requisitos e instala dependencias de Python
# --no-cache-dir evita almacenar paquetes en caché y reduce el tamaño de la imagen
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del proyecto al contenedor
COPY . .

# Cambia al directorio de Tailwind para instalar dependencias de frontend
# npm ci es más estricto y seguro que npm install para entornos de producción
WORKDIR /app/theme/static_src
RUN npm ci

# Construye los estilos de Tailwind CSS
# Compila los archivos de estilos según la configuración del proyecto
RUN npm run build

# Vuelve al directorio principal de la aplicación
WORKDIR /app

# Configura la ruta de npm para que Django Tailwind pueda encontrarlo
ENV NPM_BIN_PATH=/usr/bin/npm

# Añade permisos de ejecución al script de entrada
RUN chmod +x entrypoint.sh

# Expone el puerto 8000 para acceder a la aplicación web
EXPOSE 8000

# Comando para iniciar la aplicación Django
# 1. Aplica migraciones de base de datos
# 2. Construye estilos de Tailwind
# 3. Inicia el servidor de desarrollo
CMD ["./entrypoint.sh"]
