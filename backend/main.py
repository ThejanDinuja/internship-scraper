from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine
from db.session import engine
from models.jobs import Job
from routers.jobs import router as job_router
from models.applications import Application
from routers.application import router as application_router
from models.user import User


app = FastAPI()
app.include_router(job_router)
app.include_router(application_router)
engine = create_engine("postgresql+psycopg://postgres:dev@localhost:5432/postgres")

@app.get("/")
def health():
    return {"status": "ok"}

@app.get("/hello")
def hello():
    return {"message": "Hello, Thejan!"}

SQLModel.metadata.create_all(engine)