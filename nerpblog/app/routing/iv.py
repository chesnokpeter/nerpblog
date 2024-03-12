from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import FileResponse
from nerpblog.app.depends import uowdep
from nerpblog.app.services import PostServices
from datetime import datetime

ivRouter = APIRouter(tags=['instant view'])

templates = Jinja2Templates(directory="nerpblog/app/routing/iv")

@ivRouter.get('/{id}/iv')
async def iv(request: Request, id: int, uow: uowdep):
    print(request.headers)
    print(request.client)
    post = await PostServices(uow).one_post(id=id)
    if post:
        try:
            post.date = datetime.strptime(str(post.date), "%Y-%m-%d %H:%M:%S.%f").strftime("%H:%MD%d.%m")
        except ValueError:
            post.date = datetime.strptime(str(post.date), "%Y-%m-%d %H:%M:%S").strftime("%H:%MD%d.%m")
    return templates.TemplateResponse('post.html', {"request": request , "post":post})
