from fastapi import APIRouter, Depends
from common.schemas import UserCreate, UserRead
from .interfaces import IUserService
from .dependencies import get_user_service

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserRead)
def create_user(
    data: UserCreate,
    user_service: IUserService = Depends(get_user_service)
):
    return user_service.create_user(data)

@router.get("/", response_model=list[UserRead])
def list_users(
    user_service: IUserService = Depends(get_user_service)
):
    return user_service.list_users()
