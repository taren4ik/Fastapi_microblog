import shutil
from typing import List
from fastapi import FastAPI, Query, Path, Body, UploadFile, File
from routes import routes
from starlette.responses import Response
from starlette.requests import Request
from core.db import SessionLocal

app = FastAPI()


@app.middleware('http')   # при каждом запросе к API
# создается сессия с БД
async def db_session_middleware(request: Request, call_next):
    response = Response('Internal server error', status_code=500)
    try:
        request.state.db = SessionLocal()  # открытие сессии
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

app.include_router(routes)




# # загрузка
# @app.post('/')
# def load_file(file: UploadFile = File(..., description="Save file")):
#     with open(f'{file.filename}', 'wb') as buffer:
#         shutil.copyfileobj(file.file, buffer)
#     return {'file_name': file.filename}
#
#
# @app.post('/img')
# def load_file(file: List[UploadFile] = File(..., description="Save file")):
#     for img in file:
#         with open(f'{img.filename}', 'wb') as buffer:
#             shutil.copyfileobj(img.file, buffer)
#     return {'image_name': 'Image load'}


# @app.get('/{pk}')
# def get_item(pk: int, q: float = None):
#     return {'key': pk, 'q': q}
#
#
