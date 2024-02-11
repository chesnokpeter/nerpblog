
from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

frontRouter = APIRouter(tags=['front'])

templates = Jinja2Templates(directory="app/static/dist")


# @frontRouter.get('/')
# def front(request: Request):
#     return templates.TemplateResponse('index.html', {"request": request})
