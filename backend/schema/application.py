from models.applications import ApplicationBase, Status
from datetime import datetime
from sqlmodel import SQLModel

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationRead(ApplicationBase):
    id: int

class ApplicationUpdate(SQLModel):
    status: Status | None = None
    notes: str | None = None
    applied_at: datetime | None = None