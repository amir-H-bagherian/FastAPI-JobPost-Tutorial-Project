from fastapi import FastAPI
import uvicorn

from core.config import settings
from apis.general_pages.route_homepage import general_pages_router


app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
app.include_router(general_pages_router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)