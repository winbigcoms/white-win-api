from fastapi import APIRouter,UploadFile,File,HTTPException
from model.withyou import EventData
from schema.promise import list_serial,indivisual_serial
from schema.user import indivisual_user_serial
from schema.event import event_list_serial,indivisual_event_serial
from config.db import promise_collection_name,user_collection_name,event_collection_name
from bson import ObjectId
from utill.s3 import s3 
from typing import List

router = APIRouter(prefix="/withyou", tags=["withyou"])

@router.get("/login")
async def login(
    email: str
):
    user = indivisual_user_serial(user_collection_name.find_one({
        "email":email
    }))

    return user

@router.get("/event/{id}")
async def get_event(id:str):
    print(id)
    event = indivisual_event_serial(event_collection_name.find_one({
        "_id":ObjectId(id)
    }))
    return event

@router.get("/events")
async def get_events(owner:str):
    events = event_list_serial(event_collection_name.find({
        "owner":owner
    }))
    return events

@router.get("/promise")
async def get_promise(
    event_id:str
):
    promises = list_serial(promise_collection_name.find({
        "event_id":event_id
    }))
    return promises

@router.post("/event")
async def post_event(eventData:EventData):
    event_collection_name.insert_one(dict(eventData))
    return true

@router.post('/event-img')
async def upload_imgs(path,files: List[UploadFile]):
    for img in files:
        try:
            contents = img.file.read()
            img.file.seek(0)
            res = s3.upload_file(
                path,
                'with-you',
                img,
                ExtraArgs={'ContentType': 'image/jpeg'}
            )

