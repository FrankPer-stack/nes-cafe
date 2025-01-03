# Nes-Cafe ☕

![Django](https://img.shields.io/badge/Django-5.1.3-green.svg)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.8.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Nes-Cafe es una aplicación web moderna desarrollada con Django y Tailwind CSS, diseñada para ofrecer una experiencia de usuario excepcional en la gestión de una cafetería en línea.

## 🚀 Características

- 🔐 Sistema de autenticación robusto
- 🎨 Diseño moderno y responsivo con Tailwind CSS
- 📱 Interfaz adaptativa para dispositivos móviles
- 🔄 Gestión de usuarios y perfiles
- 🛡️ Seguridad integrada de Django
- 🌐 Soporte multilenguaje

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- Docker
- Docker Compose
- Git

## 🛠️ Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/nes-cafe.git
cd nes-cafe
```

2. Configurar variables de entorno:
- Copia `.env.example` a `.env`
- Modifica los valores según tu configuración

3. Construir y levantar los contenedores:
```bash
docker-compose up --build
```

4. Acceder a la aplicación:
- Web: http://localhost:8000
- Base de datos: localhost:5433

## 🎯 Uso

1. Accede a `http://localhost:8000` en tu navegador
2. Regístrate como nuevo usuario o inicia sesión
3. Explora las diferentes funcionalidades de la aplicación

## 🔧 Comandos Útiles

- Iniciar contenedores: `docker-compose up`
- Detener contenedores: `docker-compose down`
- Reconstruir: `docker-compose up --build`
- Ejecutar migraciones: `docker-compose exec web python manage.py migrate`

## 🔧 Solución de Problemas
- Asegúrate de tener Docker y Docker Compose instalados
- Verifica que los puertos 8000 y 5433 estén disponibles
- Revisa los logs con `docker-compose logs`

## 🔧 Estructura del Proyecto

```
Nes-Cafe/
├── apps/                   # Aplicaciones Django
│   ├── users/             # Gestión de usuarios
│   └── ...
├── config/                # Configuración del proyecto
├── static/                # Archivos estáticos
├── templates/             # Plantillas HTML
├── theme/                 # Configuración de Tailwind
└── manage.py             # Script de gestión de Django
```

## 🧪 Testing

Para ejecutar los tests:
```bash
docker-compose exec web python manage.py test
```

## 🚀 Deployment

Guía básica para despliegue en producción:

1. Configura las variables de entorno para producción
2. Recolecta los archivos estáticos
```bash
docker-compose exec web python manage.py collectstatic
```
3. Configura tu servidor web (nginx, Apache, etc.)
4. Configura tu servidor de aplicaciones (gunicorn, uwsgi, etc.)

## 🤝 Contribuir

1. Fork el proyecto
2. Crea tu rama de características (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## ✨ Agradecimientos

- Django Framework
- Tailwind CSS
- Todos los contribuidores que han participado en este proyecto

## 📞 Contacto

Francisco - [@user_peral] - fr4nkPeralt@outlook.com

Link del proyecto: [https://github.com/FrankPer-stack/](https://github.com/FrankPer-stack/)

---
⌨️ con ❤️ por [Francisco](https://github.com/FrankPer-stack/)
