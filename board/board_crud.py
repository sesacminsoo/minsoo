from sqlalchemy.orm import Session
from sqlalchemy import and_
from models import Board
from board.board_schema import NewPost, Post, UpdatePost

def insert_post(new_post: NewPost, db: Session):
    post = Board(
        writer = new_post.writer,
        title = new_post.title,
        content = new_post.content
    )
    db.add(post)
    db.commit()

    return post.post_id

def get_post(post_id : int, db: Session):
    try:
        post = db.query(Board).filter(and_(Board.post_id == post_id, Board.del_yn == 'Y')).first()
        return Post(post_id = post.post_id, writer = post.writer, title = post.title, date = post.date, content = post.content, updater = post.updater)
    except Exception as e:
        return {'error' : str(e), 'msg' : '존재하지 않는 게시글입니다.'}
    
def update_post(update_post : UpdatePost, db: Session):
    post = db.query(Board).filter(and_(Board.post_id == update_post.post_id, Board.del_yn == 'Y')).first()
    try:
        if not post:
            raise Exception("존재하지 않는 게시글입니다.")
        
        post.title = update_post.title
        post.updater = update_post.updater
        post.content = update_post.content
        db.commit()
        db.refresh(post)
        return get_post(post.post_id, db)
    
    except Exception as e:
        return str(e)

def del_post(post_id : int, db : Session):
    post = db.query(Board).filter(and_(Board.post_id == post_id, Board.del_yn == 'Y')).first()
    try:
        if not post:
            raise Exception("존재하지 않는 게시글입니다.")
        
        post.del_yn = 'N'
        db.delete(post)
        db.commit()
        return {'msg' : '삭제가 완료되었습니다.'}
    
    except Exception as e:
        return str(e)
