from fastapi import APIRouter
from model.withyou import Todo
from schema.schemas import list_serial
from config.db import collection_name
from bson import ObjectId

router = APIRouter(prefix="/withyou", tags=["withyou"])

@router.get("/")
async def get_promise():
    promises = list_serial(collection_name.find())
    return promises