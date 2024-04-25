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
    isVisited: str
    tag: str
    date: str
