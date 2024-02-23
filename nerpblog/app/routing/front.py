
from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import FileResponse

frontRouter = APIRouter(tags=['front'])

templates = Jinja2Templates(directory="nerpblog/app/static/dist")
dist = 'nerpblog/app/static/dist'


@frontRouter.get('/')
def front(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})

@frontRouter.get('/prog')
def front(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})

@frontRouter.get('/about')
def front(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})


@frontRouter.get('/favicon.ico')
def front():
    return FileResponse(f'{dist}/favicon.ico')

@frontRouter.get('/apple-touch-icon.png')
def front():
    return FileResponse(f'{dist}/apple-touch-icon.png')

@frontRouter.get('/favicon.svg')
def front():
    return FileResponse(f'{dist}/favicon.svg')

@frontRouter.get('/sw.js')
def front():
    return FileResponse(f'{dist}/sw.js')

@frontRouter.get('/registerSW.js')
def front():
    return FileResponse(f'{dist}/registerSW.js')

@frontRouter.get('/manifest.webmanifest')
def front():
    return FileResponse(f'{dist}/manifest.webmanifest')

@frontRouter.get('/registerSW.js')
def front():
    return FileResponse(f'{dist}/registerSW.js')

@frontRouter.get('/pwa-192.png')
def front():
    return FileResponse(f'{dist}/pwa-192.png')

@frontRouter.get('/pwa-512.png')
def front():
    return FileResponse(f'{dist}/pwa-512.png')

@frontRouter.get('/mobile.jpg')
def front():
    return FileResponse(f'{dist}/mobile.jpg')


@frontRouter.get('/{id}')
def front(request: Request, id: int):
    return templates.TemplateResponse('index.html', {"request": request})