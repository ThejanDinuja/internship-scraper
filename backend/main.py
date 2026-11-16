from fastapi import FastAPI
from sqlmodel import create_engine

app = FastAPI()
engine = create_engine("postgresql+psycopg://postgres:dev@localhost:5432/postgres")

@app.get("/")
def health():
    return {"status": "ok"}

@app.get("/hello")
def hello():
    return {"message": "Hello, Thejan!"}

