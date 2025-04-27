## Project Overview

This is a simple FastAPI application that implements a basic items API. The API allows you to create, list, and retrieve items.

## Project Structure

```
fastAPI/
├── app/                  # Application directory (create this)
│   └── main.py           # Main application file
├── dockerfile            # Docker configuration
├── requirements.txt      # Python dependencies
└── README.md             # This documentation
```

## Installation Instructions

### Local Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate the virtual environment:

   ```bash
   # On Windows
   .venv\Scripts\activate

   # On macOS/Linux
   source .venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Create the app directory and move main.py into it:
   ```bash
   mkdir app
   move main.py app/
   ```
6. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

### Docker Setup

1. Make sure Docker is installed on your system
2. Create the app directory and move main.py into it:
   ```bash
   mkdir app
   move main.py app/
   ```
3. Build the Docker image:
   ```bash
   docker build -t fastapi-app .
   ```
4. Run the container:
   ```bash
   docker run -p 8000:8000 fastapi-app
   ```

## API Endpoints

- `GET /`: Root endpoint, returns a "Hello World" message
- `POST /items`: Create a new item
- `GET /items`: List all items (with optional limit parameter)
- `GET /items/{item_id}`: Retrieve a specific item by ID

## Access the API

After running the application, access the API documentation at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
