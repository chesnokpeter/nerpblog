
from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

frontRouter = APIRouter(tags=['front'])

templates = Jinja2Templates(directory="nerpblog/app/static/dist")


@frontRouter.get('/')
def front(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})

@frontRouter.get('/prog')
def front(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})

@frontRouter.get('/about')
def front(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})


@frontRouter.get('/{id}')
def front(request: Request, id: int):
    return templates.TemplateResponse('index.html', {"request": request})

