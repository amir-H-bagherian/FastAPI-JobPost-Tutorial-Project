from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request


templates = Jinja2Templates(directory='templates')
general_pages_router = APIRouter()


@general_pages_router.get('/')
async def home_page(req: Request):
    return templates.TemplateResponse('general_pages/homepage.html', {'request': req})