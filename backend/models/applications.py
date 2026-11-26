import enum 
from sqlmodel import SQLModel, Field, UniqueConstraint
from datetime import datetime, timezone

class Status(str, enum.Enum):
    applied = "applied"
    assessment = "assessment"
    interview = "interview"
    offer = "offer"
    rejected = "rejected"


class ApplicationBase(SQLModel):
    job_id: int = Field(foreign_key="job.id")
    status: Status = Field(default=Status.applied)
    notes: str | None = Field(default=None, nullable=True)
    applied_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)


class Application(ApplicationBase, table=True):
    __table_args__ = (UniqueConstraint("user_id", "job_id", name="uq_user_job"), )

    id: int | None = Field(default=None, primary_key=True) 
    user_id: int = Field(foreign_key="users.id")