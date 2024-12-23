# FastAPI Project Setup and Workflow Guide

## 1. What is FastAPI?
FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. It is known for:
- **Speed** – One of the fastest Python frameworks.
- **Ease of Use** – Automatic generation of interactive API documentation.
- **Automatic Validation** – Request data validation using Pydantic.
- **Asynchronous Support** – Native support for async and await, enabling non-blocking code.
- **Built-in Documentation** – Swagger UI and ReDoc.

---

## 2. Environment Setup

### 1. Prerequisites
- **Python** – Version 3.8 or higher
- **Pip** – Latest version installed

### 2. Create Virtual Environment
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install Requirements
```bash
# Install dependencies from requirements.txt
pip install -r requirements.txt
```

### 4. Run FastAPI Application
```bash
# Run the FastAPI app using Uvicorn
uvicorn app.main:app --reload
```
- `app.main` – Path to the main FastAPI app instance
- `--reload` – Enables automatic reload on code changes (use in development)

## 3. Project Structure

```
bookshelf_manager/
│
├── app/                  # Main FastAPI application directory
│   │
│   ├── main.py           # Entry point for FastAPI app
│   ├── models.py         # Database models (Pydantic/SQLAlchemy)
│   ├── database.py       # Database connection setup
│   │
│   ├── routers/          # API endpoints (organized by feature)
│   │   ├── __init__.py   # Initialize router
│   │   ├── authors.py    # Author-related endpoints
│   │   ├── books.py      # Book-related endpoints
│   │   ├── categories.py # Category-related endpoints
│   │   ├── reviews.py    # Review-related endpoints
│   │   └── users.py      # User-related endpoints
│   │
│   ├── schemas/          # Pydantic schemas for data validation
│   │   ├── __init__.py
│   │   ├── authors.py
│   │   ├── books.py
│   │   ├── categories.py
│   │   ├── reviews.py
│   │   └── users.py
│   │
│   ├── services/         # Business logic layer
│   │   ├── __init__.py
│   │   ├── authors.py
│   │   ├── books.py
│   │   ├── categories.py
│   │   ├── reviews.py
│   │   └── users.py
│
├── task/                 # Task documentation and workflow
│   ├── stage1.md         # Task details for stage 1
│   └── stage2.md         # Task details for stage 2
│
├── env/                  # Virtual environment (not tracked in Git)
│
└── requirements.txt      # Project dependencies
```

## 4. View API Documentation
- Once the server is running, access the interactive documentation at:
		- Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
		- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 5. Book Router (/books)

Handles all operations related to books.

### Endpoints:
- `GET /books` – Retrieve all books
- `POST /books` – Add a new book
- `GET /books/{book_id}` – Retrieve a specific book
- `PUT /books/{book_id}` – Update book details
- `DELETE /books/{book_id}` – Delete a book

## 6. Docs Router (/docs)
- Provides custom API documentation or handles file uploads.

## 7. Tasks (Workflow for New Developers)

### 1. Stage 1 – Initial Setup
- Read through `tasks/stage1.md`
- Implement and test API endpoints for others.
- Ensure `/books` and `/docs` routes are properly configured.
- Use `GET /docs` to verify API documentation.

### 2. Stage 2 – Advanced Implementation
- Follow the instructions in `tasks/stage2.md` to implement:
- User authentication and registration.
- Secure API routes with JWT tokens.
- Pagination and filtering on the `/books` route.
- Ensure tests are written and endpoints are fully documented.

## 8. Notes for New Developers
- Always follow the task instructions in the `tasks/` directory.
- Refer to `/docs` for endpoint verification during development.
- Use the virtual environment to avoid dependency conflicts.
- Commit changes frequently and document API endpoints clearly.
