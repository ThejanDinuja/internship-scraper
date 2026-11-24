from fastapi import APIRouter, Depends
from models.user import User
from core.security import get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/me")
def read_me(user: User = Depends(get_current_user)):
    return user