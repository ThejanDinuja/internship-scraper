from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from db.session import get_session
from models.jobs import Job
from models.applications import Application
from schema.application import ApplicationCreate, ApplicationRead, ApplicationUpdate

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

@router.get("/", response_model=list[ApplicationRead])
def read_applications(session: Session = Depends(get_session)):
    applications = session.exec(select(Application)).all()
    return applications

@router.get("/{application_id}", response_model=ApplicationRead)
def read_one_application(application_id: int, session: Session = Depends(get_session)):
    application = session.get(Application, application_id)
    if application is None:
        raise HTTPException(status_code=404, detail="Application not found")
    return application

@router.patch("/{application_id}", response_model=ApplicationRead)
def update_application(application_id: int, update_data: ApplicationUpdate, session: Session = Depends(get_session)):
    db_application = session.get(Application, application_id)
    if db_application is None:
        raise HTTPException(status_code=404, detail="Application not found")

    changes = update_data.model_dump(exclude_unset=True)

    for field in ("status", "applied_at"):
        if field in changes and changes[field] is None:
            raise HTTPException(status_code=422, detail=f"{field} cannot be set to None")

    db_application.sqlmodel_update(changes)
    session.add(db_application)
    session.commit()
    session.refresh(db_application)
    return db_application
