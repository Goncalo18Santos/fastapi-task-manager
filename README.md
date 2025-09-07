# FastAPI Task Manager

A simple Task Manager API built with FastAPI, PostgreSQL, and Docker.

## Features

1. CRUD operations on tasks (Create, Read, Update, Delete)  
2. Asynchronous database communication with PostgreSQL using SQLAlchemy and databases  
3. Dockerized app and database with Docker Compose  
4. Interactive API documentation with Swagger UI  

## Setup and Run Locally

### Prerequisites

- Docker and Docker Compose installed  
- Git installed  

### Steps

1. **Clone the repository**

```bash
git clone https://github.com/Goncalo18Santos/fastapi-task-manager.git
cd fastapi-task-manager
```
2. **Build and start the Docker containers**
```bash
docker-compose up --build
```
This will build the FastAPI app image and start both the app and PostgreSQL database containers.

3. **Access the API docs**  
Open your browser and go to: http://localhost:8000/docs  
Here you can explore and test all API endpoints interactively.

4. **Stop the containers**  
When done, stop the containers by pressing Ctrl+C in the terminal running Docker Compose, then run:
```bash
docker-compose down
```

**Project Structure**  
- **app/** - FastAPI application code
- **tests/** - Unit tests
- **Dockerfile** - Instructions to build the app container
- **docker-compose.yml** — Defines app and PostgreSQL services
- **requirements.txt** — Python dependencies
- **README.md** — This documentation

**Notes**  
- Database connection details are managed in the docker-compose.yml and app config.
- The app uses asynchronous SQLAlchemy for efficient database operations.
- Unit tests can be run locally inside the container or your dev environment.
