from fastapi import FastAPI
import uvicorn

from core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

@app.get('/')
def hello_api():
    return {'message': 'Hello world!'}



if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)