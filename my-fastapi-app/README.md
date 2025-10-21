# My FastAPI App

This is a FastAPI application that provides several JSON test endpoints. The application is structured to support versioning of the API and includes a variety of features for easy development and testing.

## Project Structure

```
my-fastapi-app
├── src
│   ├── main.py                # Entry point of the FastAPI application
│   ├── app
│   │   ├── __init__.py        # Marks the app directory as a Python package
│   │   ├── api
│   │   │   ├── __init__.py    # Marks the api directory as a Python package
│   │   │   └── v1
│   │   │       ├── __init__.py # Marks the v1 directory as a Python package
│   │   │       └── test_endpoints.py # Defines JSON test endpoints
│   │   ├── models
│   │   │   └── schemas.py      # Defines Pydantic models for validation
│   │   └── core
│   │       └── config.py       # Configuration settings for the application
├── tests
│   └── test_endpoints.py       # Unit tests for the JSON test endpoints
├── requirements.txt             # Lists dependencies required for the project
├── Dockerfile                   # Instructions for building a Docker image
├── .devcontainer
│   └── devcontainer.json        # Configuration for the development container
└── README.md                    # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd my-fastapi-app
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```
   uvicorn src.main:app --reload
   ```

4. **Access the API documentation:**
   Open your browser and navigate to `http://localhost:8000/docs` to view the interactive API documentation.

## Usage

The application provides several JSON endpoints that can be tested using tools like Postman or directly through the Swagger UI available at `/docs`. 

## Testing

To run the tests, use the following command:
```
pytest tests/test_endpoints.py
```

## License

This project is licensed under the MIT License.