from fastapi import APIRouter

router = APIRouter(prefix="/default",tags=["default"])

@router.get('/')
def read_root():
    return {"Hello": "World"}
