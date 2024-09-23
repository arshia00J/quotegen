from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

# Define the Quote model
class Quote(BaseModel):
    quote: str
    author: str

# In-memory quotes list
quotes = [
    {"id": 1, "quote": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"id": 2, "quote": "Life is 10% what happens to us and 90% how we react to it.", "author": "Charles R. Swindoll"},
    {"id": 3, "quote": "Success is not final, failure is not fatal: It is the courage to continue that counts.", "author": "Winston Churchill"},
    {"id": 4, "quote": "Believe you can and you’re halfway there.", "author": "Theodore Roosevelt"},
    {"id": 5, "quote": "You miss 100% of the shots you don’t take.", "author": "Wayne Gretzky"},
    {"id": 6, "quote": "Don’t watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
    {"id": 7, "quote": "Opportunities don't happen. You create them.", "author": "Chris Grosser"},
    {"id": 8, "quote": "Success usually comes to those who are too busy to be looking for it.", "author": "Henry David Thoreau"},
    {"id": 9, "quote": "It always seems impossible until it’s done.", "author": "Nelson Mandela"},
    {"id": 10, "quote": "Dream big and dare to fail.", "author": "Norman Vaughan"},
]

app = FastAPI()

@app.get("/quotes")
def get_all_quotes():
    return quotes

@app.get("/quotes/random")
def get_random_quote():
    return random.choice(quotes)

@app.post("/quotes")
def add_quote(quote: Quote):
    new_quote = {"id": len(quotes) + 1, "quote": quote.quote, "author": quote.author}
    quotes.append(new_quote)
    return {"message": "Quote added successfully!", "quote": new_quote}

@app.delete("/quotes/{id}")
def delete_quote(id: int):
    for i, quote in enumerate(quotes):
        if quote["id"] == id:
            deleted_quote = quotes.pop(i)
            return {"message": "Quote deleted successfully", "quote": deleted_quote}
    raise HTTPException(status_code=404, detail="Quote not found")
