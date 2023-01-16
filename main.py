from fastapi import FastAPI
# http://127.0.0.1:8000 = API endpoint

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

