from models.job_posts import JobPost


def create_new_job_post(new_job_post, db, owner_id):
    new_job_post_model_obj = JobPost(**new_job_post.dict(), owner_id=owner_id)
    
    db.add(new_job_post_model_obj)
    db.commit()
    db.refresh(new_job_post_model_obj)
    
    return new_job_post_model_obj