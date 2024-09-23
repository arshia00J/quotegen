
# FastAPI Quote Manager

A simple quote management application built with FastAPI and a basic HTML/JavaScript frontend. The app allows users to:
- Get all quotes
- Fetch a random quote
- Add a new quote
- Delete a quote by ID

## Features
- **FastAPI Backend**: Provides APIs to manage quotes (GET, POST, DELETE).
- **In-memory Storage**: Quotes are stored in memory for simplicity.
- **Frontend UI**: Simple HTML/JavaScript-based user interface to interact with the API.

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/fastapi-quote-manager.git
cd fastapi-quote-manager
```

### 2. Install Python Dependencies
Make sure you have Python installed. Then, create a virtual environment and install the dependencies.

```bash
# Create virtual environment
python3 -m venv venv

# Activate the virtual environment (MacOS/Linux)
source venv/bin/activate

# Activate the virtual environment (Windows)
venv\Scripts\activate

# Install FastAPI and Uvicorn
pip install fastapi uvicorn

# Install optional dependencies (including CORS middleware)
pip install 'fastapi[all]'
```

### 3. Running the FastAPI Server
Start the FastAPI server by running:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

### 4. Enabling CORS
CORS is enabled to allow requests from the frontend. The CORS middleware is set to allow requests from any origin (`*`). If you'd like to restrict this, modify the `allow_origins` parameter in the FastAPI setup.

## API Endpoints

| Method | Endpoint                | Description                      |
|--------|-------------------------|----------------------------------|
| GET    | `/quotes`               | Get all quotes                   |
| GET    | `/quotes/random`        | Get a random quote               |
| POST   | `/quotes`               | Add a new quote                  |
| DELETE | `/quotes/{id}`          | Delete a quote by ID             |

### Example API Usage

- **Get a random quote:**

```bash
GET http://127.0.0.1:8000/quotes/random
```

Response:
```json
{
    "id": 1,
    "quote": "The only way to do great work is to love what you do.",
    "author": "Steve Jobs"
}
```

- **Add a new quote:**

```bash
POST http://127.0.0.1:8000/quotes
Content-Type: application/json

{
    "quote": "Innovation distinguishes between a leader and a follower.",
    "author": "Steve Jobs"
}
```

- **Delete a quote by ID:**

```bash
DELETE http://127.0.0.1:8000/quotes/1
```

## Frontend UI

The frontend interface allows users to:
- Fetch a random quote
- Add a new quote via a simple form
- Delete a quote by entering the quote ID

### How to Use the Frontend

1. Open `index.html` in a browser.
2. Interact with the buttons:
   - **Random Quote**: Displays a random quote.
   - **Add Quote**: Allows you to add a new quote (inputs required: quote and author).
   - **Delete Quote**: Deletes a quote by entering its ID.

### Frontend Setup

The HTML file is a simple static page that interacts with the FastAPI backend via JavaScript `fetch()` calls. You don't need any extra setup to run the UI locally — just open the `index.html` file in your browser after starting the FastAPI server.

### Troubleshooting

- **CORS Issues**: If you get CORS errors when running the app, make sure the FastAPI app has CORS enabled. This is handled via the `CORSMiddleware` in `main.py`.
- **Port Conflicts**: Ensure that no other applications are running on port `8000` before starting the FastAPI server.
- **Cross-Origin Block in Browser**: Make sure you have CORS configured correctly in FastAPI if you're testing the frontend by opening `index.html` locally in your browser.

## Acknowledgments
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
```

### Key Sections:
- **Installation and Setup**: Describes how to set up the Python environment and run the FastAPI app.
- **API Endpoints**: Lists the available API routes with sample requests.
- **Frontend UI**: Explains the basic functionality of the frontend and how to interact with it.
- **Troubleshooting**: Provides guidance on common issues like CORS and port conflicts.

This README will help users understand how to install, run, and interact with your project both via the API and the UI.