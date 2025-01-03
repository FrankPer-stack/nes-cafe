#!/bin/bash
set -e

echo "Aplicando migraciones..."
python manage.py migrate

echo "Construyendo estilos de Tailwind..."
python manage.py tailwind build

echo "Iniciando servidor de desarrollo..."
python manage.py runserver localhost:8000
