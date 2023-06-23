from mailbox import Message

from fastapi import UploadFile, File, APIRouter, Form, Request
import shutil
from typing import List
from schemas import UploadVideo, GetVideo
from models import Video, User


video_router = APIRouter()





@video_router.post('/')
async def root(tite: str = Form(...), description: str = Form(...), file: UploadFile = File(...)):
    with open(f"{file.filename}", "wb") as buffer:
        info = UploadVideo(title=tite, description=description)
        shutil.copyfileobj(file.file, buffer)
    user = await User.objects.first()
    return await Video.objects.create(file=file.filename, user=user, **info.dict())



@video_router.get('/video/{video_pk}/', response_model=GetVideo)
async def get_video(video_pk: int):
    return await Video.objects.select_related('user').get(pk=video_pk)


print('test')