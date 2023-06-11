from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.job_posts import JobCreate, JobShow
from db.session import get_db
from crud.job_posts import create_new_job_post


job_post_router = APIRouter(prefix='/jobs', tags=['job_posts'])

@job_post_router.post("/create-job/",response_model=JobShow)
def create_job_post(job_post: JobCreate, db: Session = Depends(get_db)):
    current_user = 1
    new_job_post = create_new_job_post(new_job_post=job_post, db=db, owner_id=current_user)
    return new_job_post