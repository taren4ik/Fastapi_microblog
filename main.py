import shutil
from typing import List
from fastapi import FastAPI, Query, Path, Body, UploadFile, File
from schemas import Author, Book

app = FastAPI()


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
# @app.get('/user/{pk}/items/{item}')
# def get_user_item(pk: int, item: str):
#     return {'user': pk, 'item': item}


@app.get('/book')
def get_book(q: List[str] = Query(['test', 'test2'], description='Search '
                                                                 'book',
                                  deprecated=True)):
    return q


@app.post('/book/')
def create_book(item: Book, author: Author, qantity: int = Body(...)):
    return {"item": item, "author": author, "qantity": qantity}


@app.post('/author/')
def create_author(author: Author = Body(..., embed=True)):
    return {"author": author}


@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1, le=20), pages: int = Query(
    None, gt=10, le=500)):
    return {"pk": pk, "pages": pages}
