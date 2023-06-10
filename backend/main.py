from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
import uvicorn

from core.config import settings
from apis.general_pages.route_homepage import general_pages_router
from db.base_class import Base
from db.session import engine


app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
app.include_router(general_pages_router)
app.mount("/static", StaticFiles(directory="static"), name="static")
Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)