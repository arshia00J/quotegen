Here's a sample `README.md` for your Quote Generator project:

# Quote Generator API

## Overview
The Quote Generator API is a simple RESTful API built using FastAPI that allows users to manage a collection of motivational quotes. Users can retrieve all quotes, get a random quote, add new quotes, and delete existing ones.

## Features
- **Get All Quotes**: Retrieve a list of all quotes.
- **Get Random Quote**: Fetch a random quote from the collection.
- **Add New Quote**: Add a new quote to the collection.
- **Delete Quote**: Remove a quote from the collection by its ID.

## Technologies Used
- [FastAPI](https://fastapi.tiangolo.com/) - A modern web framework for building APIs with Python 3.6+.
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation and settings management using Python type annotations.
- [Uvicorn](https://www.uvicorn.org/) - ASGI server for running FastAPI applications.

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Clone the Repository
```bash
git clone https://github.com/yourusername/quote-generator.git
cd quote-generator
```

### Install Dependencies
```bash
pip install fastapi uvicorn
```

## Usage

### Run the API
Start the server with the following command:
```bash
uvicorn main:app --reload
```

### Endpoints

- **GET /quotes**
  - Retrieves a list of all quotes.
  
- **GET /quotes/random**
  - Returns a random quote.
  
- **POST /quotes**
  - Adds a new quote.
  - Request Body:
    ```json
    {
      "quote": "Your quote here.",
      "author": "Author Name"
    }
    ```
  
- **DELETE /quotes/{id}**
  - Deletes a quote by ID.

### Example Requests

#### Get All Quotes
```bash
curl -X GET http://127.0.0.1:8000/quotes
```

#### Get Random Quote
```bash
curl -X GET http://127.0.0.1:8000/quotes/random
```

#### Add New Quote
```bash
curl -X POST http://127.0.0.1:8000/quotes -H "Content-Type: application/json" -d '{"quote": "Life is beautiful.", "author": "Unknown"}'
```

#### Delete Quote
```bash
curl -X DELETE http://127.0.0.1:8000/quotes/1
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request.
