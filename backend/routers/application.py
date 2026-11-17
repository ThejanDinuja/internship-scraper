from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from db.session import get_session
from models.jobs import Job
from models.applications import Application
from schema.application import ApplicationCreate, ApplicationRead

router = APIRouter(prefix="/applications", tags=["applications"])

@router.post("/", response_model=ApplicationRead)
def create_application(application: ApplicationCreate, session: Session = Depends(get_session)):
    job = session.get(Job, application.job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    new_application = Application.model_validate(application)
    session.add(new_application)
    session.commit()
    session.refresh(new_application)
    return new_application