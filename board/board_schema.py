from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class NewPost(BaseModel):
    writer : str
    title : str
    content : Optional[str] = None

class Post(BaseModel):
    post_id : int
    writer : str
    title : str
    date : datetime
    content : Optional[str] = None

class UpdatePost(BaseModel):
    post_id : int
    title : str
    updater : str
    content : Optional[str] = None