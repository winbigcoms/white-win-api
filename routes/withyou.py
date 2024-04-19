from fastapi import APIRouter
from model.withyou import Todo
from schema.promise import list_serial,indivisual_serial
from schema.user import indivisual_user_serial
from schema.event import event_list_serial
from config.db import promise_collection_name,user_collection_name,event_collection_name
from bson import ObjectId

router = APIRouter(prefix="/withyou", tags=["withyou"])

@router.get("/login")
async def login(
    email: str
):
    user = indivisual_user_serial(user_collection_name.find_one({
        "email":email
    }))

    return user

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
    print(event_id)
    promises = list_serial(promise_collection_name.find({
        "event_id":event_id
    }))
    return promises