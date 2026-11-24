from fastapi import APIRouter, Depends, HTTPException, HTTPException
from sqlmodel import Session, select
from db.session import get_session
from models.jobs import Job
from schema.job import JobCreate, JobRead

router = APIRouter(prefix="/jobs", tags=["jobs"])

@router.post("/", response_model=JobRead)
def create_job(job: JobCreate, session: Session = Depends(get_session)):
    checker = select(Job).where(Job.url == job.url)
    existing_job = session.exec(checker).first()
    if existing_job:
        raise HTTPException(status_code=409, detail="Job with this URL already exists")
    new_job = Job.model_validate(job)
    session.add(new_job)
    session.commit()
    session.refresh(new_job)
    return new_job

@router.get('/', response_model=list[JobRead])
def read_jobs(session: Session = Depends(get_session)):
    select_jobs = select(Job)
    select_jobs_result = session.exec(select_jobs)
    return select_jobs_result.all()

## doesn't matter cause fastapi makes sure id is an int and gives an error
@router.get("/{job_id}", response_model=JobRead)
def singular_job(job_id: int, session: Session = Depends(get_session)):
    flag = False
    while flag == False:
        if type(job_id) != int:
            raise TypeError("Job ID must be an integer")
        else:
            job = session.get(Job, job_id)
            flag = True
            if not job:
                raise HTTPException(status_code=404, detail="Job not found")
            return job

@router.delete("/{job_id}")
def delete_job(job_id: int, session: Session = Depends(get_session)):
    job = session.get(Job, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    session.delete(job)
    session.commit()
    return {"message": f"Job deleted successfully: {job_id} | {job.title}" }