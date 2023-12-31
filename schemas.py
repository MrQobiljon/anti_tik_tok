from pydantic import BaseModel
from typing import List



class User(BaseModel):
    id: int
    username: str


class UploadVideo(BaseModel):
    title: str
    description: str


class GetVideo(BaseModel):
    user: User
    title: str
    description: str
