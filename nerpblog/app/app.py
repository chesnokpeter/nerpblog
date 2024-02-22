from fastapi import FastAPI, Request, status, Response
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.wsgi import WSGIMiddleware

from nerpblog.app.routing.api import apiRouter
from nerpblog.app.routing.front import frontRouter
from nerpblog.app.routing.media import mediaRouter

from nerpblog.app.admin import admin

app = FastAPI(title='nerpblog api')

origins = [
    "http://localhost:9001",
    "http://localhost:9002",
    "http://localhost:9003"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/icons/like/', StaticFiles(directory='nerpblog/public/likes/'))
app.mount('/icons/ui/', StaticFiles(directory='nerpblog/public/icons/'))
app.mount('/admin', WSGIMiddleware(admin.app))

# app.mount("/assets", StaticFiles(directory="nerpblog/app/static/dist/assets"), name="assets")
app.include_router(apiRouter)
app.include_router(frontRouter)
app.include_router(mediaRouter)


# @app.middleware("https")
# async def log_request(request: Request, call_next):
#     request_log.info(f'{request.client.host} {request.method} {"/"+str(request.url).split(str(request.base_url))[1]}')
#     try:
#         return await call_next(request)
#     except Exception as e:
#         request_log.error(f'ERROR {request.client.host} {request.method} {"/"+str(request.url).split(str(request.base_url))[1]}')
#         error_log.error(e)
#         return Response("Internal server error", status_code=500)

