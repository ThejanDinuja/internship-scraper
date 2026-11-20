from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    __tablename__ = "users"
    id: int | None = Field(default=None, primary_key=True)
    username: str | None = None
    auth0id: str = Field(unique=True)
    email: str | None = Field(default=None, unique=True)
