from sqlmodel import create_engine
from core.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
# print(f" here is the engine: {engine}")