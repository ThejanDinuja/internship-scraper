from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine
from db.session import engine
from models.jobs import Job
from routers.jobs import router

app = FastAPI()
app.include_router(router)
engine = create_engine("postgresql+psycopg://postgres:dev@localhost:5432/postgres")

@app.get("/")
def health():
    return {"status": "ok"}

@app.get("/hello")
def hello():
    return {"message": "Hello, Thejan!"}

SQLModel.metadata.create_all(engine)