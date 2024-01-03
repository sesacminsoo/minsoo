#get매서드는 URL에 데이터를 심어서 전송하는 것
#post매서드는 전송하는 body에 데이터를 심어서 전송하는 것의 차이가 존재

from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
"""import models
from database import engine
models.Base.metadata.create_all(bind=engine)"""

from board import board_router

app = FastAPI()  # fastapi 앱으로 동작할 수 있도록 만드는 기본 구성
app.include_router(board_router.app, tags=["board"])

templates = Jinja2Templates(directory = "templates")

@app.get("/")  # @ : 함수에 추가적인 기능을 부여하는 데코레이터, get 안에 있는 url이 우리가 서버에 처음 들어가면 보이게 되는것
def index(request:Request):
    return templates.TemplateResponse(
        "main_board.html", {
            "request" : request
        }
    )

@app.get("/")
def index(request:Request):
    return templates.TemplateResponse(
        "Board_detail.html", {
            "request" : request
        }
    )

@app.get("/")
def index(request:Request):
    return templates.TemplateResponse(
        "editingBoard.html", {
            "request" : request
        }
    )

@app.get("/")
def index(request:Request):
    return templates.TemplateResponse(
        "writingBoard.html", {
            "request" : request
        }
    )
    

# 아래부턴 post 매서드로 서버 열어봄
