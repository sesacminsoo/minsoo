from sqlalchemy import Column, Text, Integer, ForeignKey, DateTime, VARCHAR
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Board(Base):
    __tablename__ = "Board"

    post_id = Column(Integer, primary_key = True, autoincrement = True)
    writer = Column(Text, nullable = False)
    title = Column(Text, nullable = False)
    content = Column(Text, nullable = True)
    date = Column(DateTime, nullable = False, default = datetime.now)
    del_yn = Column(VARCHAR(1), nullable = False, default = 'Y')
    updater = Column(Text, nullable = True)



"""class Post(Base):
    __tablename__ = "post"

    post_id = Column(Integer, primary_key = True, autoincrement = True)  # primary_key를 통해 고유성을 지켜주기 위함
    title = Column(Text, nullable = False)
    content = Column(Text, nullable = True)
    writer = Column(Text, nullable = False)

    comment = relationship("Comment", backref = "user_comment")


class Comment(Base):
    __tablename__ = "comment"

    post_id = Column(Integer, ForeignKey("post.post_id"), nullable = False)
    comment_id = Column(Integer, primary_key = True, autoincrement = True)
    writer = Column(Text, nullable = False)
    content = Column(Text, nullable = True)

    user_comment = relationship("Post", backref = "comment")"""