from sqlalchemy.orm import Session
from database import get_db

from fastapi import APIRouter, Depends

from board import board_crud, board_schema

app = APIRouter(
    prefix = "/board"
)

@app.post(path = "/create", description = "게시판 - 게시글 생성")
def create_new_post(new_post: board_schema.NewPost, db: Session = Depends(get_db)):
    return board_crud.insert_post(new_post, db)

@app.get(path = "/read/{post_id}", description = "게시판 - 게시글 조회", response_model = board_schema.Post)
def read_post(post_id : int, db: Session = Depends(get_db)):
    return board_crud.get_post(post_id, db)

@app.put(path = "/update/{post_id}", description = "게시판 - 게시글 업데이트")
def update_post(update_post : board_schema.UpdatePost, db: Session = Depends(get_db)):
    return board_crud.update_post(update_post, db)

@app.delete(path = "/delete/{post_id}", description = "게시판 - 게시글 삭제")
def delete_post(post_id : int, db : Session = Depends(get_db)):
    return board_crud.del_post(post_id, db)