from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from html import escape
from typing import List

from schemas.job_posts import JobCreate, JobShow
from db.session import get_db
from crud.job_posts import create_new_job_post, read_job_post, read_all_job_posts


job_post_router = APIRouter(prefix='/jobs', tags=['job_posts'])

@job_post_router.post("/create-job/",response_model=JobShow)
def create_job_post(job_post: JobCreate, db: Session = Depends(get_db)):
    current_user = 1
    new_job_post = create_new_job_post(new_job_post=job_post, db=db, owner_id=current_user)
    return new_job_post

@job_post_router.get('/get/{id}', response_model=JobShow)
def get_single_job_post(id: int, db: Session = Depends(get_db)):
    requested_job_post = read_job_post(id=id, db=db)
    if not requested_job_post:
        raise HTTPException(status_code=404,
                            detail=f"Requested job post with id {escape(id)} is not found!")
    return requested_job_post

@job_post_router.get('/all/', response_model=List[JobShow])
def read_all_job_posts(db: Session = Depends(get_db)):
    list_of_all_posts = read_all_job_posts(db=db)
    return list_of_all_posts