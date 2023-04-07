#FastAPI-microblog


###Клонировать репозиторий и перейти в него в командной строке:

```
bash
git clone https://github.com/taren4ik/Fastapi_microblog
cd Fastapi_microblog
```

###Cоздать и активировать виртуальное окружение:

```
bash
python -m venv venv
```

####Для *nix-систем:
```
bash
source venv/bin/activate
```

####Для windows-систем:
```
bash
source venv/Scripts/activate
```

###Установить зависимости из файла requirements.txt:

```
bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

###Выполнить миграции:

```
cd Fastapi_microblog
alembic revision --autogenerate -m "First"
alembic upgrade head 
```
###Запустить проект:

```
bash
uvicorn main:app --reload --зщке 8080   
```

###Сам проект  искать по адресу:
```
bash
http://127.0.0.1:8080
```

***Над проектом работали:***

*Dmitry P. Github:https://github.com/taren4ik |
