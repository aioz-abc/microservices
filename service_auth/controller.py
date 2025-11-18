from fastapi import APIRouter, Depends
from .interfaces import LoginSchema, RegisterSchema, AuthResponse, IAuthService
from .dependencies import get_auth_service

router = APIRouter(prefix="/auth")


@router.post("/login", response_model=AuthResponse)
def login(data: LoginSchema, service: IAuthService = Depends(get_auth_service)):
    return service.login(data)


@router.post("/register", response_model=AuthResponse)
def register(data: RegisterSchema, service: IAuthService = Depends(get_auth_service)):
    return service.register(data)
