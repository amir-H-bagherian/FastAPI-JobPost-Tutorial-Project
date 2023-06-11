from models.job_posts import JobPost
from sqlalchemy.orm import Session


def create_new_job_post(new_job_post, db, owner_id):
    new_job_post_model_obj = JobPost(**new_job_post.dict(), owner_id=owner_id)
    
    db.add(new_job_post_model_obj)
    db.commit()
    db.refresh(new_job_post_model_obj)
    
    return new_job_post_model_obj

def read_job_post(id, db: Session):
    queried_job_post = db.query(JobPost).filter(JobPost.id==id).first()
    return queried_job_post

def read_all_job_posts(db: Session):
    list_of_posts = db.query(JobPost).filter(JobPost.is_active).all()
    return list_of_posts