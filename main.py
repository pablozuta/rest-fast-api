from fastapi import FastAPI
# http://127.0.0.1:8000 = API endpoint
# http://127.0.0.1:8000/docs# = esto nos da informacion sobre nuestras rutas

app = FastAPI()


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
    return{"books": []}
# /books-by-index/{index}
# /get-random-book
# /add-book
# /get-book?id=3hf...



