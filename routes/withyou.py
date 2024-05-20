from fastapi import APIRouter,UploadFile,File,HTTPException,Form
from model.withyou import EventData,PostImg
from schema.promise import list_serial,indivisual_serial
from schema.user import indivisual_user_serial
from schema.event import event_list_serial,indivisual_event_serial
from config.db import promise_collection_name,user_collection_name,event_collection_name
from bson import ObjectId
from utill.s3 import s3,upload_to_s3,make_presign_url
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

@router.get("/event/img/pre-url")
async def get_presign_url(uploader:str):
    url = make_presign_url(uploader)
    return url

@router.post('/event-imgs')
async def upload_imgs(files: List[PostImg] = File(...), uploader:str = Form(...)):
    s3_urls = []
    for file in files:
        s3_url = upload_to_s3(file,uploader)
        s3_urls.append(s3_url)
    return {"s3_urls": s3_urls}


