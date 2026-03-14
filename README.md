# Task Manager Backend

![Python](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17.4-blue)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-87%25-yellowgreen)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![License](https://img.shields.io/badge/license-MIT-blue)
![CI](https://github.com/AliceLilae/task-manager-backend/actions/workflows/tests.yml/badge.svg)

Backend API for managing users and tasks built with **FastAPI**, **PostgreSQL 17.4**, and **SQLAlchemy 2.0**.

## Why this project

This project demonstrates backend engineering practices including:

- **REST API design** with FastAPI and proper HTTP status codes
- **Relational data modeling** with PostgreSQL and SQLAlchemy
- **Automated testing** with pytest and 87% coverage
- **Containerized deployment** with Docker and Docker Compose
- **Database migrations** with Alembic
- **CI/CD pipeline** with GitHub Actions

---

# Overview

The **Task Manager Backend** provides a REST API to manage users and tasks with PostgreSQL database and comprehensive testing.

---

# Features

* User CRUD API
* Task CRUD API
* Soft delete system
* Password hashing with **bcrypt**
* PostgreSQL database
* Database migrations with **Alembic**
* Automated tests with **pytest**
* Test coverage with **pytest-cov**
* Docker environment
* Continuous Integration with **GitHub Actions**
* OpenAPI documentation via FastAPI

---

# Tech Stack

| Technology       | Version | Purpose                   |
| ---------------- | ------- | ------------------------- |
| FastAPI          | 0.115.0 | Web API framework         |
| PostgreSQL       | 17.4    | Relational database       |
| SQLAlchemy       | 2.0+    | ORM                       |
| Alembic          | Latest  | Database migrations       |
| Pytest           | Latest  | Testing framework         |
| pytest-cov       | Latest  | Test coverage             |
| Docker           | Latest  | Containerized development |
| GitHub Actions   | Latest  | Continuous Integration    |
| Passlib / bcrypt | 4.0.1   | Password hashing          |
| Uvicorn          | Latest  | ASGI server               |
| Pydantic         | Latest  | Data validation           |

---

# Project Structure

```
task-manager-backend
│
├── app/
│   ├── models/           # SQLAlchemy models (User, Task)
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── task.py
│   ├── schemas/          # Pydantic schemas for API
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── task.py
│   ├── routers/          # API endpoints
│   │   ├── __init__.py
│   │   ├── users.py      # User CRUD operations
│   │   └── tasks.py      # Task CRUD operations
│   ├── utils/            # Utility functions
│   │   ├── __init__.py
│   │   └── security.py   # Password hashing
│   ├── database.py       # Database configuration
│   └── main.py           # FastAPI application entry
│
├── migrations/           # Alembic migration files
│   ├── versions/         # Individual migration scripts
│   ├── env.py           # Migration environment
│   └── script.py.mako   # Migration template
│
├── tests/               # Pytest test suite
│   ├── fixtures/        # Test data fixtures
│   ├── conftest.py      # Pytest configuration
│   ├── test_tasks.py    # Task API tests
│   ├── test_users.py    # User API tests
│   └── test_root.py     # Root endpoint tests
│
├── .github/             # GitHub workflows
│   └── workflows/
│       └── tests.yml    # CI/CD pipeline
│
├── docker-compose.yml   # Multi-container setup
├── Dockerfile           # Application container
├── requirements.txt     # Python dependencies
├── alembic.ini         # Alembic configuration
├── pytest.ini          # Pytest configuration
├── .env                # Environment variables (gitignored)
└── README.md
```

---

# API Documentation

Once the API is running, interactive documentation is available at:

```
http://localhost:8000/docs
```

FastAPI automatically generates OpenAPI documentation.

---

# Quick Start

## Prerequisites

- **Python 3.12+**
- **PostgreSQL 17.4** (or Docker)
- **Git**

## Option 1: Docker (Recommended)

The easiest way to run the entire project with database included:

```bash
# Clone the repository
git clone https://github.com/AliceLilae/task-manager-backend.git
cd task-manager-backend

# Create environment file
cp .env.example .env
# Edit .env with your database credentials

# Start all services
docker compose up --build
```

Services started:
- PostgreSQL database on port `5432`
- FastAPI application on port `8000`

Access points:
- **API**: `http://localhost:8000`
- **Documentation**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Option 2: Local Development

```bash
# Clone the repository
git clone https://github.com/AliceLilae/task-manager-backend.git
cd task-manager-backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup database (see Database Setup section)
# Run migrations
alembic upgrade head

# Start the server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

# Environment Variables

Create a `.env` file in the project root:

```bash
# Database Configuration
POSTGRES_DB=taskmanager
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/taskmanager

# Test Database (for CI/testing)
TEST_DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/taskmanager_test
```

**Note**: The `.env` file is already included in `.gitignore` for security.

## Database Setup

### Using Docker (Recommended)

```bash
# Start PostgreSQL container
docker compose up postgres -d

# Run migrations
alembic upgrade head
```

### Using Local PostgreSQL

1. Install PostgreSQL 17.4
2. Create database:
   ```sql
   CREATE DATABASE taskmanager;
   ```
3. Run migrations:
   ```bash
   alembic upgrade head
   ```

---

# Running Tests

Run the full test suite:

```
pytest
```

---

# Test Coverage

Generate coverage report:

```
pytest --cov=app
```

Example output:

```
TOTAL coverage: ~87%
```

Tests cover:

* user API
* task API
* error handling
* password hashing
* soft delete behavior

---

# Continuous Integration

Tests run automatically using **GitHub Actions**.

Pipeline includes:

* PostgreSQL service container
* Python environment setup
* dependency installation
* pytest execution

Workflow file:

```
.github/workflows/tests.yml
```

---

# API Endpoints

## Base URL
```
http://localhost:8000
```

## Users Endpoints

| Method | Endpoint | Description | Response |
| ------ | -------- | ----------- | -------- |
| POST | `/users/` | Create a new user | User object |
| GET | `/users/` | List all users (non-deleted) | List of users |
| GET | `/users/{user_id}` | Get user by ID | User object |
| PUT | `/users/{user_id}` | Update user | Updated user object |
| DELETE | `/users/{user_id}` | Soft delete user | Success message |

## Tasks Endpoints

| Method | Endpoint | Description | Response |
| ------ | -------- | ----------- | -------- |
| POST | `/tasks/` | Create a new task | Task object |
| GET | `/tasks/` | List all tasks (non-deleted) | List of tasks |
| GET | `/tasks/{task_id}` | Get task by ID | Task object |
| PUT | `/tasks/{task_id}` | Update task | Updated task object |
| DELETE | `/tasks/{task_id}` | Soft delete task | Success message |

## System Endpoint

| Method | Endpoint | Description | Response |
| ------ | -------- | ----------- | -------- |
| GET | `/` | Health check | API status message |

---

# API Usage Examples

## Create a User

```bash
curl -X POST "http://localhost:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice",
    "username": "alice",
    "email": "alice@example.com",
    "password_hash": "password123"
  }'
```

**Response:**
```json
{
  "id": 1,
  "name": "Alice",
  "username": "alice",
  "email": "alice@example.com",
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T10:30:00Z"
}
```

## Create a Task

```bash
curl -X POST "http://localhost:8000/tasks/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete project documentation",
    "description": "Write comprehensive README and API docs",
    "user_id": 1,
    "status": "pending"
  }'
```

**Response:**
```json
{
  "id": 1,
  "title": "Complete project documentation",
  "description": "Write comprehensive README and API docs",
  "user_id": 1,
  "status": "pending",
  "created_at": "2024-01-15T10:35:00Z",
  "updated_at": "2024-01-15T10:35:00Z"
}
```

## Get All Users

```bash
curl -X GET "http://localhost:8000/users/" \
  -H "Content-Type: application/json"
```

## Get User Tasks

```bash
curl -X GET "http://localhost:8000/tasks/?user_id=1" \
  -H "Content-Type: application/json"
```

---

# Database Migrations

## Alembic Commands

```bash
# Create new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

---

# Security

- **Password Hashing**: bcrypt with salt
- **Soft Delete**: Data preservation with `deleted_at` timestamp
- **Input Validation**: Pydantic schemas for all API inputs
- **SQL Injection Protection**: SQLAlchemy ORM parameterized queries

---

# Performance

- **Database Indexing**: Primary keys and foreign keys
- **Connection Pooling**: SQLAlchemy default pooling
- **FastAPI**: Async support for high concurrency

---

# Future Improvements

- **JWT Authentication**: Secure token-based auth
- **API Pagination**: Efficient large dataset handling
- **Rate Limiting**: API abuse prevention
- **Caching Layer**: Redis for performance

---

# License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **FastAPI Team** - Excellent web framework
- **SQLAlchemy Team** - Powerful ORM
- **PostgreSQL Team** - Reliable database
- **Python Community** - Great ecosystem

---

## Contact

For questions, suggestions, or issues:

- **GitHub Issues**: [Create an issue](https://github.com/AliceLilae/task-manager-backend/issues)
- **Email**: al.clarenn@gmail.com
- **LinkedIn**: [Your Profile](https://linkedin.com/in/alexis-clarenn)

---
