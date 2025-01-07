# Nes-Cafe ☕

![Django](https://img.shields.io/badge/Django-5.1.3-green.svg)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.8.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Nes-Cafe is a modern web application developed with Django and Tailwind CSS, designed to deliver an exceptional user experience for managing an online café.

## 🚀  Features

- 🔐 Robust authentication system
- 🎨 Modern and responsive design with Tailwind CSS
- 📱 Mobile-friendly interface
- 🔄 User and profile management
- 🛡️ Built-in Django security features
- 🌐 Multilanguage support


## 📋 Prerequisites

Before getting started, ensure you have installed:

- Docker
- Docker Compose
- Git

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/tu-usuario/nes-cafe.git
cd nes-cafe
```

2. Configure environment variables:
- Copy `.env.example` to `.env`
- Modify the values according to your setup

3. Build and start the containers:
```bash
docker-compose up --build
```

4. Access the application:
- Web: http://localhost:8000
- Database: localhost:5433

## 🎯 Usage

1. Open http://localhost:8000 in your browser
2. Register as a new user or log in
3. Explore the application's features

## 🔧 Useful Commands

- Start containers: `docker-compose up`
- Stop containers:  `docker-compose down`
- Rebuild containers: `docker-compose up --build`
- Run migrations: `docker-compose exec web python manage.py migrate`

## 🔧 Troubleshooting
- Ensure Docker and Docker Compose are installed
- Verify that ports 8000 and 5433 are available
- Check logs with `docker-compose logs`

## 🔧 Project Structure

```
Nes-Cafe/
├── apps/                  # Django apps
│   ├── users/             # User management
│   └── ...
├── config/                # Project configuration
├── static/                 # Static files
├── templates/            # HTML templates
├── theme/                 # Tailwind configuration
└── manage.py             # Django management script
```

## 🧪 Testing

To run tests:
```bash
docker-compose exec web python manage.py test
```

## 🚀 Deployment

Basic guide for production deployment:

1. Configure environment variables for production
2. Collect static files:
```bash
docker-compose exec web python manage.py collectstatic
```
3. Set up your web server (nginx, Apache, etc.)
4. Configure your application server (gunicorn, uwsgi, etc.)

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ✨ Acknowledgements

= Django Framework
- Tailwind CSS
- All contributors who participated in this

## 📞 Contact

Francisco - [@user_peral] - fr4nkPeralt@outlook.com

Project link: [https://github.com/FrankPer-stack/](https://github.com/FrankPer-stack/nes-cafe/)

---
⌨️ con ❤️ por [Francisco](https://github.com/FrankPer-stack/)
