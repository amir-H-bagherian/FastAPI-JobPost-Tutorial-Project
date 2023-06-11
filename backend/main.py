from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
import uvicorn

from core.config import settings
from routes.homepage import general_pages_router
from routes.users import user_router
from routes.job_posts import job_post_router
from db.base import Base
from db.session import engine


app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
app.include_router(general_pages_router)
app.include_router(user_router)
app.include_router(job_post_router)

app.mount("/static", StaticFiles(directory="static"), name="static")
Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)