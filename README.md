# Cargo/Delivery Website

This is a personal project aimed at developing a cargo/delivery website backend using Django, Django REST Framework (DRF), PostgreSQL, Docker, Redis, and Celery.

## Technologies Used
- Django: Python web framework for backend development
- Django REST Framework (DRF): Toolkit for building RESTful APIs in Django
- PostgreSQL: Relational database management system
- Docker: Containerization platform for easy deployment
- Redis: In-memory data structure store for caching and message broker
- Celery: Distributed task queue for asynchronous processing

## Description
The cargo/delivery website backend is being developed to handle various functionalities, such as user management, cargo tracking, and payment integration. It utilizes Django's powerful features and integrates with DRF for building the API endpoints. The project also incorporates Docker for containerization, PostgreSQL for data persistence, Redis for caching and message queuing, and Celery for asynchronous task processing.

## Development Setup
1. Clone the repository: `git clone https://github.com/NuraySh/CargoProject.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Configure the PostgreSQL database settings in `settings.py`
4. Start the PostgreSQL and Redis services using Docker Compose: `docker-compose up -d`
5. Apply database migrations: `python manage.py migrate`
6. Start the Celery worker: `celery -A cargoproject worker --loglevel=info`
7. Start the Django development server: `python manage.py runserver`

## Roadmap
This project is still in active development. Planned features and improvements include:
- Integrating third-party payment gateways
- Enhancing cargo tracking functionality
- Adding unit and integration tests
- Optimizing database queries and performance
- Documenting the API endpoints

## Contact
For any questions or suggestions regarding this project, feel free to reach out to me at [nshahvaladli@gmail.com](mailto:nshahvaladli@gmail.com)
