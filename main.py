from uuid import uuid4
from fastapi import FastAPI, HTTPException
# este modulo se usa para generar una sugerencia de libro de forma aleatoria
import random
import os
import json
from pydantic import BaseModel
from typing import Optional, Literal
from fastapi.encoders import jsonable_encoder
# http://127.0.0.1:8000 = API endpoint
# http://127.0.0.1:8000/docs# = esto nos da informacion sobre nuestras rutas
# uvicorn main:app --reload

app = FastAPI()

# Book Model
class Book(BaseModel):
    name: str
    price: float
    genre: Literal["programming", "fiction", "history"]
    book_id: Optional[str] = uuid4().hex


BOOKS_FILE ="books.json"
BOOK_DATABASE = []

if os.path.exists(BOOKS_FILE):
    with open(BOOKS_FILE, "r") as f:
        BOOK_DATABASE = json.load(f)


# / root path
@app.get("/")
async def home():
    return{"message": "Welcome to Classy Bookstore" }

# /list-books
@app.get("/list-books")
async def list_books():
    return{"books": BOOK_DATABASE}

# /books-by-index/{index}
@app.get("/books-by-index/{index}")
async def books_by_index(index: int):
    if index < 0 or index >= len(BOOK_DATABASE):
        # Fail message
        raise HTTPException(404, f"Index {index} is out of range {len(BOOK_DATABASE)}")
    else:    
        return{"books": BOOK_DATABASE[index]}

# /get-random-book
@app.get("/get-random-book")
async def get_random_book():
    return random.choice(BOOK_DATABASE)

# /add-book
@app.post("/add-book")
async def add_book(book: Book):
    book.book_id = uuid4().hex
    json_book = jsonable_encoder(book)
    BOOK_DATABASE.append(json_book)
    with open(BOOKS_FILE, "w") as f:
        json.dump(BOOK_DATABASE, f)
    return {"message": f"Book {book} was added to database!", "book_id": book.book_id}

# /get-book?id=3hf...
@app.post("/get-book")
async def get_book(book_id: str):
    for book in BOOK_DATABASE:
        if book["book_id"] == book_id:
            return book

    raise HTTPException(404, f"Book not found: {book_id}")        




