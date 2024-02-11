from fastapi import FastAPI, Request, status, Response
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from nerpblog.app.routing.api import apiRouter
from nerpblog.app.routing.front import frontRouter

app = FastAPI(title='nerpblog api')

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/icons/like/', StaticFiles(directory='nerpblog/public/likes/'))
# app.mount("/assets", StaticFiles(directory="nerpblog/app/static/dist/assets"), name="assets")
app.include_router(apiRouter)
app.include_router(frontRouter)



# @app.middleware("https")
# async def log_request(request: Request, call_next):
#     request_log.info(f'{request.client.host} {request.method} {"/"+str(request.url).split(str(request.base_url))[1]}')
#     try:
#         return await call_next(request)
#     except Exception as e:
#         request_log.error(f'ERROR {request.client.host} {request.method} {"/"+str(request.url).split(str(request.base_url))[1]}')
#         error_log.error(e)
#         return Response("Internal server error", status_code=500)

