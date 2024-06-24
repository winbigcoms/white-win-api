from fastapi import APIRouter,UploadFile,File,HTTPException,Form
from model.withyou import EventData,PostImg,PromiseData
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

@router.get("/promises")
async def get_promise(
    event_id:str
):
    promises = list_serial(promise_collection_name.find({
        "event_id":event_id
    }))
    return promises

@router.get("/promise/{id}")
async def get_promise(
    id:str
):
    promise = indivisual_serial(promise_collection_name.find_one({
        "_id":ObjectId(id)
    }))
    return promise

@router.post("/promise")
async def post_promise(promiseData:PromiseData):

    promise_collection_name.insert_one(dict(promiseData))
    return True

@router.patch("/promise/visit")
async def patch_promise_visit(promiseId:string):

    promise_collection_name.update_one({
        "_id":ObjectId(promiseId),
        "isVisited":True
    })
    return True

@router.post("/event")
async def post_event(eventData:EventData):
    event_collection_name.insert_one(dict(eventData))
    return True

@router.get("/event/img/pre-url")
async def get_presign_url(uploader:str):
    url = make_presign_url(uploader)
    return url

