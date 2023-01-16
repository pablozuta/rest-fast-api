from fastapi import FastAPI, HTTPException
import random
# http://127.0.0.1:8000 = API endpoint
# http://127.0.0.1:8000/docs# = esto nos da informacion sobre nuestras rutas

app = FastAPI()

BOOKS_FILE ="books.json"
BOOK_DATABASE = [
    "Deep Work",
    "The Sun Also Rises",
    "Infinite Jest",
    "The Cambridge Handbook of Expertise and Expert Performance"
]


""" @app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/books")
async def books():
    return {"message": "Here are the Books"} """


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
async def add_book(book: str):
    BOOK_DATABASE.append(book)
    return {"message": f"Book {book} was added to database!"}

# /get-book?id=3hf...



