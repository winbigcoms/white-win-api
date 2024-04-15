from pydantic import BaseModel

class Todo(BaseModel):
    title: str
    memo: str
    imgs: list
    isVisited: bool
    tag: str