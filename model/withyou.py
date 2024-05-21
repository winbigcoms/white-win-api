from pydantic import BaseModel

class EventData(BaseModel):
    event_title: str
    date: str
    opponent_name: str
    owner: str

class PromiseData(BaseModel):
    title: str
    memo: str
    imgs: list
    link:str
    isVisited: bool
    tag: str
    date: str

class PostImg(BaseModel):
    base64: str
    fileName: str
    imageType: str